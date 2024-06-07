import click
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import json
import os
from datetime import datetime


def get_dynamodb_client(profile, region):
    session = boto3.Session(profile_name=profile) if profile else boto3.Session()
    return session.client('dynamodb', region_name=region)


@click.group()
@click.option('--aws-profile', default=None, help='AWS profile name to use for accessing DynamoDB.')
@click.pass_context
def ddb_exporter(ctx, aws_profile):
    """DynamoDB operations utility tool."""
    ctx.ensure_object(dict)
    ctx.obj['AWS_PROFILE'] = aws_profile


@ddb_exporter.command()
@click.option('--region', default='us-east-1', help='AWS region to use.')
@click.option('--detail', is_flag=True, help='Include schema information of tables.')
@click.pass_context
def list_tables(ctx, region, detail):
    """List DynamoDB tables in the specified region."""
    try:
        client = get_dynamodb_client(ctx.obj['AWS_PROFILE'], region)
        response = client.list_tables()
        tables = response.get('TableNames', [])
        if detail:
            for table in tables:
                table_info = client.describe_table(TableName=table)
                click.echo(json.dumps(table_info, indent=2))
        else:
            click.echo(json.dumps(tables, indent=2))
    except (NoCredentialsError, PartialCredentialsError):
        click.echo("AWS credentials not found. Please configure your credentials or specify a profile.")
    except ClientError as e:
        click.echo(f"Failed to list tables: {str(e)}")


@ddb_exporter.command()
@click.option('--region', default='us-east-1', help='AWS region to use.')
@click.option('--table', required=True, help='DynamoDB table name to export.')
@click.option('--output', default=None, help='Output JSON file path.')
@click.option('--overwrite', is_flag=True, help='Overwrite output file if it exists.')
@click.option('--partition-key', default=None, help='Partition key to filter the data.')
@click.option('--sort-key', default=None, help='Sort key to filter the data.')
@click.option('--sort-key-range', default=None, help='Sort key range to filter the data (format: start,end).')
@click.option('--index-name', default=None, help='Secondary index name to query.')
@click.option('--index-partition-key', default=None, help='Partition key for the secondary index.')
@click.option('--index-sort-key', default=None, help='Sort key for the secondary index.')
@click.pass_context
def export_table(ctx, region, table, output, overwrite, partition_key, sort_key, sort_key_range, index_name,
                 index_partition_key, index_sort_key):
    """Export data from DynamoDB table."""
    try:
        client = get_dynamodb_client(ctx.obj['AWS_PROFILE'], region)

        if not output:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output = f"{table}_{timestamp}.json"

        if os.path.exists(output) and not overwrite:
            click.confirm(f"{output} already exists. Do you want to overwrite?", abort=True)

        scan_kwargs = {}

        if partition_key:
            scan_kwargs['FilterExpression'] = f"partition_key = :pk"
            scan_kwargs['ExpressionAttributeValues'] = {":pk": {"S": partition_key}}

        if sort_key:
            if sort_key_range:
                start, end = sort_key_range.split(',')
                scan_kwargs['FilterExpression'] += f" AND sort_key BETWEEN :start AND :end"
                scan_kwargs['ExpressionAttributeValues'].update({":start": {"S": start}, ":end": {"S": end}})
            else:
                scan_kwargs['FilterExpression'] += f" AND sort_key = :sk"
                scan_kwargs['ExpressionAttributeValues'].update({":sk": {"S": sort_key}})

        if index_name:
            scan_kwargs['IndexName'] = index_name
            if index_partition_key:
                scan_kwargs['FilterExpression'] = f"index_partition_key = :ipk"
                scan_kwargs['ExpressionAttributeValues'] = {":ipk": {"S": index_partition_key}}
            if index_sort_key:
                scan_kwargs['FilterExpression'] += f" AND index_sort_key = :isk"
                scan_kwargs['ExpressionAttributeValues'].update({":isk": {"S": index_sort_key}})

        paginator = client.get_paginator('scan')
        items = []
        for page in paginator.paginate(TableName=table, **scan_kwargs):
            items.extend(page.get('Items', []))

        with open(output, 'w') as f:
            json.dump(items, f, indent=2)

        click.echo(f"Data exported to {output}")

    except (NoCredentialsError, PartialCredentialsError):
        click.echo("AWS credentials not found. Please configure your credentials or specify a profile.")
    except ClientError as e:
        click.echo(f"Failed to export table: {str(e)}")


if __name__ == '__main__':
    ddb_exporter()

# ddb_exporter

`ddb_exporter` は、AWS DynamoDBのテーブル操作およびデータエクスポートを簡単に行うためのコマンドラインツールです。

## インストール

`ddb_exporter` をインストールするには、以下のコマンドを実行してください:

```bash
pip install click boto3
```

次に、スクリプトファイルを実行可能にして、適切なディレクトリに配置します。

## 使い方

`ddb_exporter` コマンドは、AWSのDynamoDBサービスにアクセスして操作を行うためのサブコマンドを提供します。以下に各サブコマンドの詳細を示します。

### 共通オプション

- `--aws-profile` (オプション): 使用するAWSプロファイル名。指定がない場合、デフォルトプロファイルまたは環境変数で設定された認証情報が使用されます。

### サブコマンド

#### `list-tables`

指定したリージョンのDynamoDBテーブルを一覧表示します。

```bash
ddb_exporter list-tables --region <region> [--detail]
```

- `--region` (オプション): AWSリージョン。デフォルトは `us-east-1` です。
- `--detail` (オプション): テーブルのスキーマ情報も含めて表示します。

#### `export-table`

指定したDynamoDBテーブルのデータをJSONファイルにエクスポートします。

```bash
ddb_exporter export-table --region <region> --table <table_name> [--output <output_file>] [--overwrite] [--partition-key <key>] [--sort-key <key>] [--sort-key-range <start,end>] [--index-name <index_name>] [--index-partition-key <key>] [--index-sort-key <key>]
```

- `--region` (オプション): AWSリージョン。デフォルトは `us-east-1` です。
- `--table` (必須): エクスポートするDynamoDBテーブル名。
- `--output` (オプション): 出力先のJSONファイルパス。指定がない場合は `テーブル名_タイムスタンプ.json` 形式で生成されます。
- `--overwrite` (オプション): 出力ファイルが既に存在する場合に上書きします。
- `--partition-key` (オプション): パーティションキーでデータをフィルタリングします。
- `--sort-key` (オプション): ソートキーでデータをフィルタリングします。
- `--sort-key-range` (オプション): ソートキーの範囲条件でデータをフィルタリングします（フォーマット: `start,end`）。
- `--index-name` (オプション): セカンダリインデックス名。
- `--index-partition-key` (オプション): セカンダリインデックスのパーティションキーでデータをフィルタリングします。
- `--index-sort-key` (オプション): セカンダリインデックスのソートキーでデータをフィルタリングします。

## 認証情報の設定

AWSの認証情報は、以下の方法で設定できます:

1. AWS CLIでプロファイルを設定する。
    ```bash
    aws configure --profile <profile_name>
    ```
2. 環境変数を設定する。
    ```bash
    export AWS_ACCESS_KEY_ID=<your_access_key_id>
    export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
    export AWS_SESSION_TOKEN=<your_session_token>  # 必要な場合
    ```

## エラー処理

認証情報が見つからない場合や認証に失敗した場合、以下のエラーメッセージが表示されます:

```
AWS credentials not found. Please configure your credentials or specify a profile.
```

また、DynamoDB操作に失敗した場合、適切なエラーメッセージが表示されます。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については `LICENSE` ファイルを参照してください。


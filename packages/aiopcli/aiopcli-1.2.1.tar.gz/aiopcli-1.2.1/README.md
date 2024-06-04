# aiopcli

## Installation

```
pip install aiopcli
```

## Examples

```
# 単体コンテナイメージを登録
# デフォルトapi serverポートが8080
docker save my-image | gzip > my-image.tgz
aiopcli add server --name=my-image --api-server=my-image.tgz \
  --api-port=80 --liveness-endpoint=/health --readiness-endpoint=/health
# "servableId"が出力されます。例えば、 `s-z15uerp3mehdxg33`

aiopcli create --tag=test --servable=s-z15uerp3mehdxg33 --server-plan=basic
# env id 321が返却されれば、
aiopcli status test
aiopcli status 321
# が同じ結果を返却

# default endpointがmultipart/form-dataを受け取る場合
aiopcli predict test -Fimage=@invoice.png
# servableがapplication/jsonを受け取る場合
aiopcli predict 321 -d'{"inputs": {"array": [0, 4, 8]}}'
# 別のendpointを叩く
aiopcli predict 321 --endpoint=receipt/read -Fimage=@receipt.jpg

# この端末で登録されたenvを全て確認
aiopcli status

# envを削除
aiopcli delete test

# 推論サーバ（tritonserver, TF Servingなど）こみのコンテナイメージ登録
docker save api-server | gzip > api-server.tgz
docker save inference-server | gzip > inference-server.tgz
aiopcli add server --name=my-image \
  --api-server=api-server.tgz \
  --inference-server=inference-server.tgz \
  --api-port=8000 \
  --metrics-port=8002 \  # tritonの場合のみ
  --liveness-endpoint=/health \
  --readiness-endpoint=/health/ready
```

## Usage guide

基本設定で作成
```
aiopcli create --servable=<servable-id> --server-plan=<basic,standard,gpu_basic>
```

tagを付けて作成
```
aiopcli create --tag=<tag> --servable=<servable-id> --server-plan=<basic,standard,gpu_basic>
```

環境を削除
```
aiopcli delete <tagまたはenv_id>
```

単体envのステータスを確認
```
aiopcli status <tagまたはenv_id>
```

cliで作成したenvのステータスを確認
```
aiopcli status
```

プロフィール（ホスト・APIキー）を設定してコマンドを実行
```
aiopcli --profile=<profile> <command> <arg> ...
# または
aiopcli -p<profile> <command> <arg> ...
```

host・apikeyをoverrideして実行
```
aiopcli --host=<host> --apikey=<apikey> <command> <arg> ...
# または
aiopcli --host=<host> -k<apikey> <command> <arg> ...
```

custom docker imageを登録
```
# apiserver
aiopcli add server \
    --name=single-custom \
    --api-server=container.tgz \
    --api-port=8000 \
    --liveness-endpoint=/health \
    --readiness-endpoint=/health

# apiserver & inferenceserver
aiopcli add server --name=double-custom --api-server=apiserver.tgz --inference-server=tritonserver.tgz
```

## Configuration

利用可能な環境変数
```
AIOP_CONFIG=~/.aiop
AIOP_LOG_LEVEL=INFO
AIOP_PROFILE=stg
AIOP_HOST=https://aiops.inside.ai
AIOP_APIKEY=ICMxJ0Z4PTtvbHE/ITd8Njk4RCgjcy5TL0E3b0YwRj83R2hXKTl8WFAiaGdpSU55fH0kd0IsOCJSZ1AwaUJuPVhWdFJvO1B0O09OQDtsOkVtPydKOnRaIUcqIm8ibFghWitiKTlxUVsqQWkkPG9lJFNbNyNrJzRoNTZzaTF7P2djMy9zKTg4JHZNMVEpQlBIayYkQTtRR2luOEIsXj1iO0JzRyJAdzBaVn1HbWNcc0k5X0JUO0tLeC1vdnRnNTVxLEJfbEEmR1lZNl97ZSZALl9FNnxDYSh+Q09WYHxDPEBqeWYhM1BUbDR5YEw0aCh3UlM6TnAxPmMhXzNnZ3YoYQ==
```

設定ファイルフォーマットはtoml。
デフォルト保存先： `~/.aiop`、`AIOP_CONFIG`環境変数で設定可。
```toml
# プロフィールのデフォルト
default = "stg"

# apikeyのデフォルト
apikey = "ICMxJ0Z4PTtvbHE/ITd8Njk4RCgjcy5TL0E3b0YwRj83R2hXKTl8WFAiaGdpSU55fH0kd0IsOCJSZ1AwaUJuPVhWdFJvO1B0O09OQDtsOkVtPydKOnRaIUcqIm8ibFghWitiKTlxUVsqQWkkPG9lJFNbNyNrJzRoNTZzaTF7P2djMy9zKTg4JHZNMVEpQlBIayYkQTtRR2luOEIsXj1iO0JzRyJAdzBaVn1HbWNcc0k5X0JUO0tLeC1vdnRnNTVxLEJfbEEmR1lZNl97ZSZALl9FNnxDYSh+Q09WYHxDPEBqeWYhM1BUbDR5YEw0aCh3UlM6TnAxPmMhXzNnZ3YoYQ=="

# profiles
[profiles.stg]
log_level = "INFO"

[profiles.prod]
apikey = "QDd+VC55cy1tLV4rQXo2bSZ1OXsgOnx0UzUwbDpEUEQ/UXc3cihvPmtBWHBTWj1LT1w+RXY/aCksbCthVUZGdFUzd2d6e1IrRi5zUycxKlp9YFxEdjE0PXNAXEtGVyZhOC14WWtcXXcoWls6OScxJmlkTSwrTDttc0ouIzhFLEZGJ3xFJWhpI3lpeV1iJ24nSjsyICcgRzxEIi95cGF0eU96TmheaWcobEk+RVxGX01ZYz9jfk9cbThIRyUpaXpLdDklJCR5eTVjYzwyb3F6J2pqJEZbckViNG16PHQkK3xqdUtBSjpRY1UoYiQ1MHBHLitYazUzKD52aVddXzYsbA=="
```

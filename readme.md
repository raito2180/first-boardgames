Tailwind CSS ファイルをコンパイルし、変更を監視する。
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch

azureにログインする
az login --use-device-code
azの指定のコンテナレジストリにログインする
az acr login --name testflaskregi.azurecr.io
azの指定のコンテナレジストリにコンテナを作成
docker build -t testflaskregi.azurecr.io/testflask:v1.1.0 .
azの指定のコンテナレジストリにpushする
docker push testflaskregi.azurecr.io/testflask:v1.1.0
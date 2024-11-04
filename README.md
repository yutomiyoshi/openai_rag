## 目的

RAG システムの構築のチュートリアルを実行し、RAG のコツを掴む。

参照：[RAG をゼロから解説](https://qiita.com/yk__/items/d466698be59a16d75a49#rag%E3%81%8C%E6%9C%89%E5%8A%B9%E3%81%AA%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3)

## 手順

1. 本ディレクトリに.env ファイルを新規作成し、API キーを記述する

```
OPENAI_API_KEY=(ここにAPIキーを入れる)
```

参照：[API キーの生成](https://openai.com/ja-JP/api/)

2. このディレクトリでターミナルを開いて以下のコマンドを実行して、コンテナを作成・起動する

```
sudo docker compose up --build
```

3. さらに、以下のコマンドを実行して、コンテナの sh を開く

```
sudo docker compose exec container /bin/sh
```

4. sh で以下を実行して、sample_data.json を生成する

```
python3 embedder.py
```

5. sh で以下を実行して、回答を生成する

```
python3 main.py
```

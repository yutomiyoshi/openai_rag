from abc import ABC, abstractmethod
import json
import openai


# データをベクトル化するモジュールのインターフェース
class Embedder(ABC):

    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError

    @abstractmethod
    def save(self, texts: list[str], filename: str) -> bool:
        raise NotImplementedError


# Embedderインターフェースの実装
class OpenAIEmbedder(Embedder):
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def embed(self, texts: list[str]) -> list[list[float]]:
        # openai 1.10.0 で動作確認
        response = openai.embeddings.create(input=texts, model="text-embedding-3-small")
        # レスポンスからベクトルを抽出
        return [data.embedding for data in response.data]

    def save(self, texts: list[str], filename: str) -> bool:
        vectors = self.embed(texts)
        data_to_save = [
            {"id": idx, "text": text, "vector": vector}
            for idx, (text, vector) in enumerate(zip(texts, vectors))
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        print(f"{filename} に保存されました。")
        return True


if __name__ == "__main__":
    import os

    texts = [
        "うんめいのとうは、ゲーム「ポケモン　不思議のダンジョン　空の探検隊」の最難関ダンジョンです。",
        "うんめいのとうに挑戦するときポケモンのレベルが1になるので、レベルが低い状態でも能力値の高い、もしくはレベルが低い状態でも能力がよく伸びるポケモンがクリアに有利です。",
        "壁の中を移動できるゴーストポケモンは敵ポケモンとの接触を減らすことができるので、クリアに有利です。",
        "テレポートを覚えるポケモンは、接敵したときに他の場所にワープできるので、クリアに有利です。",
        "ユレイドルはいわ・くさタイプのポケモンです。レベルが低いときの能力値が低く、能力の伸びも悪いです。",
        "フーディンはエスパータイプのポケモンです。レベルが低いときの能力値は普通です。レベル1でテレポートを覚えています。",
        "カクレオンはノーマルタイプのポケモンです。レベルが低いときの能力値は低く能力の伸びも悪いです。しかし、レベルが高くなると急激に強くなります。",
        "ディアルガははがね・ドラゴンタイプのポケモンです。伝説のポケモンですが、必ずしも能力値は高くありません。",
        "ロトムはでんき・ゴーストタイプのポケモンです。レベル1時点での能力値は低いものの、レベルが低いうちから能力がよく伸びます。",
    ]

    # OpenAI APIキーを事前に環境変数にセットしてください。
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        raise ValueError("APIキーがセットされていません。")

    embedder = OpenAIEmbedder(api_key)
    embedder.save(texts, "sample_data.json")

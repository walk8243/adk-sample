# adk-sample

Agent Development Kitを使ってみる

## Ollamaのインストールと実行

まず、Ollamaをお使いのPCにインストールします。

1.  Ollamaの公式サイトにアクセスします。
      * [https://ollama.com/](https://ollama.com/)
2.  お使いのOS（macOS, Windows, Linux）用のインストーラーをダウンロードし、画面の指示に従ってインストールを完了させます。

インストールが完了したら、以下のコマンドを実行します。

```bash
ollama run gemma3:270m
```

  * **初回実行時**: Ollamaが自動的に `gemma3:270m` モデルのダウンロードを開始します。
  * **ダウンロード後**: モデルの読み込みが完了すると、プロンプト（入力待機状態）が表示され、チャットが可能になります。

詳しくは[こちら](ollama.md)をご覧ください。

## ADKのインストール

このプロジェクトでは、 [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) を使用します。

### 前提条件

- Python 3.13以上
- uv（Pythonパッケージマネージャー）

### インストール手順

プロジェクトのルートディレクトリで以下のコマンドを実行します。

```bash
uv sync
```

これにより、`pyproject.toml`に記載されている依存関係（`google-adk>=1.18.0`など）がインストールされます。

## ADKの実行方法

### 基本的な実行

プロジェクトのルートディレクトリで以下のコマンドを実行します。

```bash
uv run adk web
```

その後、以下をブラウザで表示し、モデルを選択してチャットしてください。

http://127.0.0.1:8000

### トラブルシューティング

#### DEBUGログの出力

以下のコマンドを使って起動することでLLMへのリクエストなど詳細なログが確認できます。

```
uv run adk web --log_level DEBUG
```

#### Windowsでのエラー

Windowsで実行すると以下のエラーが発生する可能性があります。

```
OSError: [WinError 1314] クライアントは要求された特権を保有していません
```

このエラーが発生した場合は、以下の手順で開発者モードを有効にしてください。

1. Windowsの設定を開きます。
2. 「システム」を選択します。
3. 「詳細設定」を選択します。
4. 開発者モードを有効にします。

### エージェントの使用

`sample_agent/agent.py`には、Gemini 2.5 Flashモデルを使用するサンプルエージェントが定義されています。

エージェントを使用するには、Pythonコード内で以下のようにインポートします。

```python
from sample_agent.agent import root_agent
```

詳しい使用方法については、`sample_agent/agent.py`を参照してください。

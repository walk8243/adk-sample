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

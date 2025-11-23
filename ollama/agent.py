from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # 👈 これをインポート

# ▼▼▼ ここがOllama設定のポイント ▼▼▼
ollama_model = LiteLlm(
    # (1) モデル名を "ollama_chat/<model_name>" または "ollama/<model_name>" に設定
    model="ollama_chat/gemma3:270m", 
    
    # (2) OllamaサーバーのURLを指定
    api_base="http://localhost:11434", 
    
    # (3) ストリーミングを有効にする（推奨）
    stream=True
)
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

# エージェントの定義
root_agent = Agent(
    name="my_ollama_agent",
    model=ollama_model, # 👈 設定したOllamaモデルを渡す
    description="OllamaとLiteLLMで動作するローカルエージェント",
    instruction="あなたはユーザーの質問に答えるAIアシスタントです。ユーザーの入力を無視せず、的確に回答してください。"
)

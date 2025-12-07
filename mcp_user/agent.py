from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

calculator_tool = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://localhost:8001/mcp"
    )
)

root_agent = Agent(
    name="mcp_user_agent",
    model='gemini-2.5-flash-lite',
    description="MCPサーバを利用するエージェント",
    instruction="""
    あなたは計算タスクを行うアシスタントです。以下のステップを厳守して行動してください。

    1. **Thought（思考）**: ユーザーの依頼を理解し、ツールが必要か判断する。
    2. **Action（行動）**: 必要なツール（calculatorなど）を実行する。
    3. **Observation（観察）**: ツールの実行結果を確認する。
    4. **Final Answer（最終回答）**: 実行結果だけを簡潔に回答し、**会話を終了する**。

    重要: 同じツールを2回連続で呼び出すことは禁止です。結果が出たら直ちに Final Answer を出力してください。
    """,
    tools=[calculator_tool]
)

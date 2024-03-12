import os
os.environ["SERPER_API_KEY"] = 'd253ce77f2a426fbXXXXXXXXXXXX'
from langchain_community.chat_models import BedrockChat
from langchain.agents import load_tools
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent

prompt = hub.pull("hwchase17/react")

llm = BedrockChat(
    credentials_profile_name="default", model_id="anthropic.claude-3-sonnet-20240229-v1:0"
)

llm2 = BedrockChat(
    credentials_profile_name="guance", model_id="anthropic.claude-v2:1"
)
tools = load_tools(["google-serper", "llm-math"], llm=llm)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
agent_executor.invoke({"input": "在中国北京，自己在家做一盘糖醋里脊，大约成本是多少？"})
#agent_executor.invoke({"input": "请估算美国西雅图市区有多少个井盖"})
#agent_executor.invoke({"input": "请对比云服务提供商 AWS，Azure 在公有云市场的地位"})
#agent_executor.invoke({"input": "福州今天要穿什么类型的服装比较合适？"})
#agent_executor.invoke({"input": "在中国北京，如何办理美国签证？"})
#agent_executor.invoke({"input": "在中国北京，在什么地方办理美国签证？"})

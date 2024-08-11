# https://github.com/run-llama/python-agents-tutorial/blob/main/2_local_agent.py
import os
# prun python local_agent_llama_index.py 可以识别 $LANGFUSE_PUBLIC_KEY 在xonshrc定义变量

# os.environ["LANGFUSE_PUBLIC_KEY"] = "sk-lf-eb90153a-e53f-4997-9d99-4afc840b01ef"
# os.environ["LANGFUSE_SECRET_KEY"] = "pk-lf-63de746a-efed-49ea-af26-d9208853b652"
# os.environ["LANGFUSE_HOST"] = "http://localhost:3000"
# => 本地LANGFUSE key 无效！
#received error response: {'error': 'UnauthorizedError', 'message': "Invalid public key. Confirm that you've configured the correct host."}
#Received 401 error by Langfuse server, not retrying: {'error': 'UnauthorizedError', 'message': "Invalid public key. Confirm that you've configured the correct host."}

# langfuse_us_key() 是有效的 , ！！US的变量是有效的。!!!
# os.environ["LANGFUSE_PUBLIC_KEY"] = 。。。

from dotenv import load_dotenv
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool

# https://langfuse.com/docs/integrations/llama-index/get-started
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager
from langfuse.llama_index import LlamaIndexCallbackHandler
langfuse_callback_handler = LlamaIndexCallbackHandler()
Settings.callback_manager = CallbackManager([langfuse_callback_handler])

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)

#llm = Ollama(model="mixtral:8x7b", request_timeout=120.0) => 26GB太大了
llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)

response = agent.chat("What is 20+(2*4)? Calculate step by step.")

print(response) #=> Answer: The result of 20+(2*4) is 28.

# In [1]: from dotenv import load_dotenv
# from dotenv import load_dotenvIn [1]: from dotenv import load_dotenv
#
# In [2]: load_dotenv()
# In [2]: load_dotenv()
# Out[2]: False
#
# In [3]: from llama_index.core.agent import ReActAgent
# from llama_index.core.agent import ReActAgentIn [3]: from llama_index.core.agent import ReActAgent
#
# In [4]: from llama_index.llms.ollama import Ollama
# In [4]: from llama_index.llms.ollama import Ollama
#
# In [5]: from llama_index.core.tools import FunctionTool
# from llama_index.core.tools import FunctionToolIn [5]: from llama_index.core.tools import FunctionTool
#
# In [6]:
# def multiply(a: float, b: float) -> float:
# """Multiply two numbers and returns the product"""
# return a * b
#
#
#
# In [6]: In [6]:
#
# In [6]: def multiply(a: float, b: float) -> float:
#    ...:     """Multiply two numbers and returns the product"""
#    ...:     return a * b
#    ...: In [6]: def multiply(a: float, b: float) -> float:
#    ...:     """Multiply two numbers and returns the product"""
#    ...:     return a * b
#    ...:
#
# In [7]: In [7]:
#
# In [7]: In [7]:
#
# In [7]: In [7]: In [7]:
# multiply_tool = FunctionTool.from_defaults(fn=multiply)
#
#
#
# In [7]: In [7]:
#
# In [7]: multiply_tool = FunctionTool.from_defaults(fn=multiply)In [7]: multiply_tool = FunctionTool.from_defaults(fn=multiply)
#
# In [8]: In [8]:
#
# In [8]: In [8]:
#
# In [8]: In [8]:
#
# In [8]: In [8]: In [8]:
# def add(a: float, b: float) -> float:
# """Add two numbers and returns the sum"""
# return a + b
#
#
#
# In [8]: In [8]:
#
# In [8]: def add(a: float, b: float) -> float:
#    ...:     """Add two numbers and returns the sum"""
#    ...:     return a + b
#    ...: In [8]: def add(a: float, b: float) -> float:
#    ...:     """Add two numbers and returns the sum"""
#    ...:     return a + b
#    ...:
#
# In [9]: In [9]:
#
# In [9]: In [9]:
#
# In [9]: In [9]: In [9]:
# In [9]:
#
# In [9]: add
# In [9]: add
# Out[9]: <function __main__.add(a: float, b: float) -> float>
#
# In [10]: multiply
# In [10]: multiply
# Out[10]: <function __main__.multiply(a: float, b: float) -> float>
#
# In [11]: add_tool = FunctionTool.from_defaults(fn=add)
# In [11]: add_tool = FunctionTool.from_defaults(fn=add)
#
# In [12]: llm = Ollama(model="llama3.1:latest", request_timeout=120.0)
# llm = Ollama(model="llama3.1:latest", request_timeout=120.0)In [12]: llm = Ollama(model="llama3.1:latest", request_timeout=120.0)
#
# In [13]: agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
# )
# )
#     ...:
#
# In [14]: response = agent.chat("What is 20+(2*4)? Calculate step by step.")
# response = agent.chat("What is 20+(2*4)? Calculate step by step.")In [14]: response = agent.chat("What is 20+(2*4)? Calculate step by step.")
# > Running step b87b02fe-c498-44a4-9781-47f817b4ebf0. Step input: What is 20+(2*4)? Calculate step by step.
# Thought: The current language of the user is: English. I need to use a tool to help me answer the question.
# Action: add
# Action Input: {'a': 20, 'b': AttributedDict([('input', 8), ('type', 'number')])}
# Observation: Error: unsupported operand type(s) for +: 'int' and 'AttributedDict'
# > Running step 359de45a-775e-43e3-8f68-1a0e756ea2b0. Step input: None
# Thought: It seems like the tool I used earlier didn't work as expected. Let me try again.
# Action: multiply
# Action Input: {'a': 2, 'b': 4}
# Observation: 8
# > Running step ece4f5fe-8036-41bb-9c84-6d39c5d3a2cd. Step input: None
# Thought: Now that I have the result of 2*4, I can continue with the original question. Time to use another tool!
# Action: add
# Action Input: {'a': 20, 'b': 8}
# Observation: 28
# > Running step 905a5e8e-3bd4-4c94-8a2b-301143e4d195. Step input: None
# Thought: The calculation is complete! Now I can provide the final answer.
# Answer: The result of 20+(2*4) is 28.
# In [15]:
#
#

## 调用llm的tracing: https://us.cloud.langfuse.com/project/clxfdeck6000fl5tkkzg8ut7r/traces/bc05dc1b-d0e1-41ae-95c7-713a29b2da08
# 坚持去λ化(中-易) jim-emacs-fun-py  master @  prun python local_agent_llama_index.py
# > Running step e1420a7c-c762-45b5-9b00-fb604dbf93ab. Step input: What is 20+(2*4)? Calculate step by step.
# Thought: The current language of the user is English. I need to use a tool to help me answer the question.
# Action: add
# Action Input: {'a': 20, 'b': 8}
# Observation: 28
# > Running step 84e74b95-6aad-460b-8d15-d95a0f3ffa81. Step input: None
# Thought: Now that we know the result of 20+(2*4), let's analyze this step by step. We can use another tool to multiply 2 and 4 first.
# Action: multiply
# Action Input: {'a': 2, 'b': 4}
# Observation: 8
# > Running step 25901cb7-6e1a-4430-8257-801343919c34. Step input: None
# Thought: Now that we know the result of 2*4 is 8. We can substitute this value back into the original equation to get 20+8.
# Action: add
# Action Input: {'a': 20, 'b': 8}
# Observation: 28
# > Running step 6b4201c2-93a9-4df3-a3dd-cc281915cba2. Step input: None
# Thought: I can answer without using any more tools. I'll use the user's language to answer
# Answer: The final result is indeed 28!
# The final result is indeed 28!
# 坚持去λ化(中-易) jim-emacs-fun-py  master @
#

# https://us.cloud.langfuse.com/project/clxfdeck6000fl5tkkzg8ut7r/traces/bc05dc1b-d0e1-41ae-95c7-713a29b2da08?observation=7652a1dc-8392-42e5-83a1-d6f7af9f7dea

# 输入 [ "What is 20+(2*4)? Calculate step by step."] => The final result is indeed 28! 输出。
agent_step_Metadata =
{
    "sources": [
        {
            "content": "28",
            "raw_input": {
                "args": [],
                "kwargs": {
                    "a": 20,
                    "b": 8
                }
            },
            "tool_name": "add",
            "raw_output": 28
        },
        {
            "content": "8",
            "raw_input": {
                "args": [],
                "kwargs": {
                    "a": 2,
                    "b": 4
                }
            },
            "tool_name": "multiply",
            "raw_output": 8
        },
        {
            "content": "28",
            "raw_input": {
                "args": [],
                "kwargs": {
                    "a": 20,
                    "b": 8
                }
            },
            "tool_name": "add",
            "raw_output": 28
        }
    ],
    "metadata": null,
    "source_nodes": [],
    "is_dummy_stream": false
}
## 第一次llm请求：
# cp llama_index/llama-index-core/llama_index/core/agent/react_multimodal/prompts.py  llama-index-react-prompts.py
# => TODO 把这些ReAct实例化的提示词再次提交给LLM都测试一下
system_role ="""
You are designed to help with a variety of tasks, from answering questions to providing summaries to other types of analyses.

## Tools 工具列表声明1

You have access to a wide variety of tools. You are responsible for using the tools in any sequence you deem appropriate to complete the task at hand.
This may require breaking the task into subtasks and using different tools to complete each subtask.

You have access to the following tools: ## 下面的是生成填充的工具列表{tool_desc}, 包含参数和注释使用。
> Tool Name: multiply
Tool Description: multiply(a: float, b: float) -> float
Multiply two numbers and returns the product
Tool Args: {"type": "object", "properties": {"a": {"title": "A", "type": "number"}, "b": {"title": "B", "type": "number"}}, "required": ["a", "b"]}

> Tool Name: add
Tool Description: add(a: float, b: float) -> float
Add two numbers and returns the sum
Tool Args: {"type": "object", "properties": {"a": {"title": "A", "type": "number"}, "b": {"title": "B", "type": "number"}}, "required": ["a", "b"]}



## Output Format 输出格式声明2: Thought Loop & Action Loop

Please answer in the same language as the question and use the following format:

```
Thought: The current language of the user is: (user's language). I need to use a tool to help me answer the question.
Action: tool name (one of multiply, add) if using a tool. ## 工具列表再次声明变量填充：(one of {tool_names})
Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {"input": "hello world", "num_beams": 5})
```

Please ALWAYS start with a Thought.

NEVER surround your response with markdown code markers. You may use code markers within your response if you need to.

Please use a valid JSON format for the Action Input. Do NOT do this {'input': 'hello world', 'num_beams': 5}.

If this format is used, the user will respond in the following format:

```
Observation: tool response
```

You should keep repeating the above format till you have enough information to answer the question without using any more tools. At that point, you MUST respond in the one of the following two formats:

```
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: [your answer here (In the same language as the user's question)]
```

```
Thought: I cannot answer the question with the provided tools.
Answer: [your answer here (In the same language as the user's question)]
```

## Current Conversation

Below is the current conversation consisting of interleaving human and assistant messages.

"""
user_role="""
"What is 20+(2*4)? Calculate step by step."
"""
assistant_role="""
Thought: The current language of the user is English. I need to use a tool to help me answer the question.

Action: add
Action Input: {"a": 20, "b": 8}

Thought: Now that we have calculated 20+8=28, let's proceed with the rest of the calculation.

Action: multiply
Action Input: {"a": 2, "b": 4}

Thought: Now that we have calculated 2*4=8, let's add this to the previous result.

Answer: 28+8=36
"""
## 第一次function_call
function_call1 =
{
    "tool": {
        "name": "add",
        "fn_schema": {},
        "description": "add(a: float, b: float) -> float\nAdd two numbers and returns the sum",
        "return_direct": false
    },
    "function_call": {
        "a": 20,
        "b": 8
    }
}

## 第二次LLM请求: UA对话。
#system_role 和上一个一样
#user: What is 20+(2*4)? Calculate step by step.
assistant_role = """
Thought: The current language of the user is English. I need to use a tool to help me answer the question.
Action: add
Action Input: {'a': 20, 'b': 8}
"""
# 11111 Observation 是用户输入输出的repl，+ x
user_role = """
"Observation: 28"
"""
assistant_role = """
Thought: Now that we know the result of 20+(2*4), let's analyze this step by step. We can use another tool to multiply 2 and 4 first.
Action: multiply
Action Input: {'a': 2, 'b': 4}
"""

## 第二次function_call
function_call2 =
{
    "tool": {
        "name": "multiply",
        "fn_schema": {},
        "description": "multiply(a: float, b: float) -> float\nMultiply two numbers and returns the product",
        "return_direct": false
    },
    "function_call": {
        "a": 2,
        "b": 4
    }
}
#=> {    "function_call_response": "8"}

## 第三次llm请求
#user
"What is 20+(2*4)? Calculate step by step."
#assistant
"Thought: The current language of the user is English. I need to use a tool to help me answer the question.
Action: add
Action Input: {'a': 20, 'b': 8}"
#user
"Observation: 28"
#assistant
"Thought: Now that we know the result of 20+(2*4), let's analyze this step by step. We can use another tool to multiply 2 and 4 first.
Action: multiply
Action Input: {'a': 2, 'b': 4}"
#user
"Observation: 8"
#assistant
"Thought: Now that we know the result of 2*4 is 8. We can substitute this value back into the original equation to get 20+8.
Action: add
Action Input: {'a': 20, 'b': 8}"

## 第四次llm请求
#user
"What is 20+(2*4)? Calculate step by step."
#assistant
"Thought: The current language of the user is English. I need to use a tool to help me answer the question.
Action: add
Action Input: {'a': 20, 'b': 8}"
#user
"Observation: 28"
#assistant
"Thought: Now that we know the result of 20+(2*4), let's analyze this step by step. We can use another tool to multiply 2 and 4 first.
Action: multiply
Action Input: {'a': 2, 'b': 4}"
#user
"Observation: 8"
#assistant
"Thought: Now that we know the result of 2*4 is 8. We can substitute this value back into the original equation to get 20+8.
Action: add
Action Input: {'a': 20, 'b': 8}"
#user
"Observation: 28"
#assistant
"Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: The final result is indeed 28!"

# 最后一次function_call:
function_call3 =
{
    "tool": {
        "name": "add",
        "fn_schema": {},
        "description": "add(a: float, b: float) -> float\nAdd two numbers and returns the sum",
        "return_direct": false
    },
    "function_call": {
        "a": 20,
        "b": 8
    }
}
#=> {   "function_call_response": "28"}

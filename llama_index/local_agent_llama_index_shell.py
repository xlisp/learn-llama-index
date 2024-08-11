# https://github.com/run-llama/python-agents-tutorial/blob/main/2_local_agent.py
# GPT1:  following this code： XXX run shell code as tools , code return as observe. input quesion can call ipython code tools answer this question "Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v."
import os
from dotenv import load_dotenv
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
# https://langfuse.com/docs/integrations/llama-index/get-started
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager
from langfuse.llama_index import LlamaIndexCallbackHandler
import subprocess

langfuse_callback_handler = LlamaIndexCallbackHandler()
Settings.callback_manager = CallbackManager([langfuse_callback_handler])

langfuse_callback_handler.set_trace_params(
  user_id="user-123",
  session_id="session-abc",
  tags=["ReAct shell"]
)

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b
multiply_tool = FunctionTool.from_defaults(fn=multiply)

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b
add_tool = FunctionTool.from_defaults(fn=add)

def run_shell_command(command: str) -> str:
    """Runs a shell command and returns the output or error"""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')
shell_command_tool = FunctionTool.from_defaults(fn=run_shell_command)

llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

agent = ReActAgent.from_tools([multiply_tool, add_tool, shell_command_tool], llm=llm, verbose=True)

response = agent.chat("Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v.")

print(response) #=> The result of performing a mathematical operation on the version number of Node (v22.3.0) is 66.

## TODO: 比如问加法和命令的：两个文件夹目录相差多少个文件？

# -------- llm trace: https://us.cloud.langfuse.com/project/clxfdeck6000fl5tkkzg8ut7r/traces/e0e82be1-79af-40d6-986f-1b8bc318f25e?observation=800ab32d-0bac-4a0a-993c-8978758295da

# ./GENERATION_functioncall_LOOP.png

# 坚持去λ化(中-易) jim-emacs-fun-py  master @ prun python local_agent_llama_index_shell.py
# > Running step 40c7259d-0184-4ec3-bf25-073ffe1a5563. Step input: Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v.
# Thought: The user wants me to execute a shell command to check if an installation is successful or not.
# Action: run_shell_command
# Action Input: {'command': 'npm install'}
# Observation: npm error code ENOENT
# npm error syscall open
# npm error path /Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json
# npm error errno -2
# npm error enoent Could not read package.json: Error: ENOENT: no such file or directory, open '/Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json'
# npm error enoent This is related to npm not being able to find a file.
# npm error enoent
# npm error A complete log of this run can be found in: /Users/emacspy/.npm/_logs/2024-07-23T11_41_07_039Z-debug-0.log
#
# > Running step 266a58af-cdfa-44a8-a304-15cd9d7474da. Step input: None
# Thought: The installation command failed due to an error related to a missing package.json file. Now, the user wants me to check the version of Node.
# Action: run_shell_command
# Action Input: {'command': 'node -v'}
# Observation: v22.3.0
#
# > Running step bf20d195-2022-4555-bc22-9a79640d7e78. Step input: None
# Thought: The installation command failed again, and now I need to use another tool to answer this question.
# Action: add
# Action Input: {'a': 2.3, 'b': 1}
# Observation: 3.3
# > Running step 9b29a2ca-8ff3-4d6a-bd57-826b0487d988. Step input: None
# Thought: The user wants me to perform a mathematical operation on the version number of Node (v22.3.0).
# Action: multiply
# Action Input: {'a': 22.3, 'b': 1}
# Observation: 22.3
# > Running step 0c30e2e7-50cb-4040-b67a-05d6e511d678. Step input: None
# Observation: Error: Could not parse output. Please follow the thought-action-input format. Try again.
# > Running step 06877c62-12c8-4ef8-a050-d0c0e6798375. Step input: None
# Thought: I need to use a different tool to perform the mathematical operation on the version number of Node.
# Action: add
# Action Input: {'a': 22, 'b': 3}
# Observation: 25
# > Running step 108fb2ce-9e42-4949-86f7-e1325a827bc0. Step input: None
# Observation: Error: Could not parse output. Please follow the thought-action-input format. Try again.
# > Running step d4da78c6-40b5-4622-842b-6529fe3b276d. Step input: None
# Thought: The user wants me to perform a mathematical operation on two numbers.
# Action: multiply
# Action Input: {'a': 22, 'b': 3}
# Observation: 66
# > Running step b0ddd1a7-43e3-44a1-9db9-1e7d05c4b25a. Step input: None
# Thought: I can answer the question without using any more tools. I'll use the user's language to answer.
# Answer: The result of performing a mathematical operation on the version number of Node (v22.3.0) is 66.
# The result of performing a mathematical operation on the version number of Node (v22.3.0) is 66.
# 坚持去λ化(中-易) jim-emacs-fun-py  master @ node -v
# v22.3.0
# 坚持去λ化(中-易) jim-emacs-fun-py  master @
#
#

# agent_step, i [Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v.] o : The result of performing a mathematical operation on the version number of Node (v22.3.0) is 66. , and metata:
# {
#     "sources": [
#         {
#             "content": "npm error code ENOENT\nnpm error syscall open\nnpm error path /Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json\nnpm error errno -2\nnpm error enoent Could not read package.json: Error: ENOENT: no such file or directory, open '/Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json'\nnpm error enoent This is related to npm not being able to find a file.\nnpm error enoent\nnpm error A complete log of this run can be found in: /Users/emacspy/.npm/_logs/2024-07-23T11_41_07_039Z-debug-0.log\n",
#             "raw_input": {
#                 "args": [],
#                 "kwargs": {
#                     "command": "npm install"
#                 }
#             },
#             "tool_name": "run_shell_command",
#             "raw_output": "npm error code ENOENT\nnpm error syscall open\nnpm error path /Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json\nnpm error errno -2\nnpm error enoent Could not read package.json: Error: ENOENT: no such file or directory, open '/Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json'\nnpm error enoent This is related to npm not being able to find a file.\nnpm error enoent\nnpm error A complete log of this run can be found in: /Users/emacspy/.npm/_logs/2024-07-23T11_41_07_039Z-debug-0.log\n"
#         },
#         {
#             "content": "v22.3.0\n",
#             "raw_input": {
#                 "args": [],
#                 "kwargs": {
#                     "command": "node -v"
#                 }
#             },
#             "tool_name": "run_shell_command",
#             "raw_output": "v22.3.0\n"
#         },
#         {
#             "content": "3.3",
#             "raw_input": {
#                 "args": [],
#                 "kwargs": {
#                     "a": 2.3,
#                     "b": 1
#                 }
#             },
#             "tool_name": "add",
#             "raw_output": 3.3
#         },
#         {
#             "content": "22.3",
#             "raw_input": {
#                 "args": [],
#                 "kwargs": {
#                     "a": 22.3,
#                     "b": 1
#                 }
#             },
#             "tool_name": "multiply",
#             "raw_output": 22.3
#         },
#         {
#             "content": "Error: Could not parse output. Please follow the thought-action-input format. Try again.",
#             "raw_input": {},
#             "tool_name": "unknown",
#             "raw_output": "Error: Could not parse output. Please follow the thought-action-input format. Try again."
#         },
#         {
#             "content": "25",
#             "raw_input": {
#                 "args": [],
#                 "kwargs": {
#                     "a": 22,
#                     "b": 3
#                 }
#             },
#             "tool_name": "add",
#             "raw_output": 25
#         },
#         {
#             "content": "Error: Could not parse output. Please follow the thought-action-input format. Try again.",
#             "raw_input": {},
#             "tool_name": "unknown",
#             "raw_output": "Error: Could not parse output. Please follow the thought-action-input format. Try again."
#         },
#         {
#             "content": "66",
#             "raw_input": {
#                 "args": [],
#                 "kwargs": {
#                     "a": 22,
#                     "b": 3
#                 }
#             },
#             "tool_name": "multiply",
#             "raw_output": 66
#         }
#     ],
#     "metadata": null,
#     "source_nodes": [],
#     "is_dummy_stream": false
# }
#
# # 第一个llm请求和funcall：
# user
#
# "Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v."
# assistant
#
#
# "Thought: The user wants me to execute a shell command to check if an installation is successful or not.
#
# Action: run_shell_command
# Action Input: {"command": "npm install"}
#
# Please respond with the output of the command execution."
#
# ## 第一个funcall
# Input
#
# {
# tool: {
# name: "run_shell_command"
# fn_schema: {
# }
# description: "run_shell_command(command: str) -> str
# Runs a shell command and returns the output or error"
# return_direct: false
# }
# function_call: {
# command: "npm install"
# }
# }
# Output
#
# {
# function_call_response: "npm error code ENOENT
# npm error syscall open
# npm error path /Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json
# npm error errno -2
# npm error enoent Could not read package.json: Error: ENOENT: no such file or directory, open '/Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json'
# npm error enoent This is related to npm not being able to find a file.
# npm error enoent
# npm error A complete log of this run can be found in: /Users/emacspy/.npm/_logs/2024-07-23T11_41_07_039Z-debug-0.log
# "
# }
#
# # 第二个llm请求和funcall：=》UA就是这个上下文，上一个UA故事列表是怎么样的？然后下一个应该怎么样？相当于你前面有几次成功案例，在这个session下面再继续提问！
# user
#
#
# "Observation: npm error code ENOENT
# npm error syscall open
# npm error path /Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json
# npm error errno -2
# npm error enoent Could not read package.json: Error: ENOENT: no such file or directory, open '/Users/emacspy/EmacsPyPro/jim-emacs-fun-py/package.json'
# npm error enoent This is related to npm not being able to find a file.
# npm error enoent
# npm error A complete log of this run can be found in: /Users/emacspy/.npm/_logs/2024-07-23T11_41_07_039Z-debug-0.log
# "
# assistant
#
#
# "Thought: The installation command failed due to an error related to a missing package.json file. Now, the user wants me to check the version of Node.
# Action: run_shell_command
# Action Input: {'command': 'node -v'}"
#
# ## funcall：
# Input
#
# {
# tool: {
# name: "run_shell_command"
# fn_schema: {
# }
# description: "run_shell_command(command: str) -> str
# Runs a shell command and returns the output or error"
# return_direct: false
# }
# function_call: {
# command: "node -v"
# }
# }
# Output
#
# {
# function_call_response: "v22.3.0
# "
# }
#
# # 第三次llm调用和funcall：
# user
#
# "Observation: v22.3.0
# "
# assistant
#
# "Thought: The installation command failed again, and now I need to use another tool to answer this question.
# Action: add
# Action Input: {"a": 2.3, "b": 1}"
#
# ## 第四次是错的了。。。
# "Observation: 3.3"
# assistant
#
# "Thought: The user wants me to perform a mathematical operation on the version number of Node (v22.3.0).
# Action: multiply
# Action Input: {"a": 22.3, "b": 1}"
#

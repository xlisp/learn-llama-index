## USE: prunp llama_index/local_agent_llama_index_shell2.py "Execute the installation command npm install. If successful, it will return to npm list. If it fails, it will return to node -v."

import os
import sys
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
import subprocess

def run_shell_command(command: str) -> str:
    """Runs a shell command and returns the output or error"""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')
shell_command_tool = FunctionTool.from_defaults(fn=run_shell_command)

llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

agent = ReActAgent.from_tools([shell_command_tool], llm=llm, verbose=True)

question = sys.argv[1]
response = agent.chat(question)

print(response)


from dotenv import load_dotenv
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core import Settings
from llama_index.tools.yahoo_finance import YahooFinanceToolSpec

# settings
Settings.llm = OpenAI(model="gpt-4o",temperature=0)

# function tools
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)

finance_tools = YahooFinanceToolSpec().to_tool_list()
finance_tools.extend([multiply_tool, add_tool])

agent = ReActAgent.from_tools(finance_tools, verbose=True)

response = agent.chat("What is the current price of NVDA?")

print(response)

#========>>>
# In [1]: from llama_index.tools.yahoo_finance import YahooFinanceToolSpec
#    ...:
# 
# In [2]: finance_tools = YahooFinanceToolSpec().to_tool_list()
#    ...:
# 
# In [3]: finance_tools
# Out[3]:
# [<llama_index.core.tools.function_tool.FunctionTool at 0x144b35990>,
#  <llama_index.core.tools.function_tool.FunctionTool at 0x143cb9250>,
#  <llama_index.core.tools.function_tool.FunctionTool at 0x107262a10>,
#  <llama_index.core.tools.function_tool.FunctionTool at 0x143ac83d0>,
#  <llama_index.core.tools.function_tool.FunctionTool at 0x144a8a7d0>,
#  <llama_index.core.tools.function_tool.FunctionTool at 0x143c93990>]
# 
# In [4]: finance_tools("NVDA")
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[4], line 1
# ----> 1 finance_tools("NVDA")
# 
# TypeError: 'list' object is not callable
# 
# In [5]: finance_tools[0]("NVDA")
# Out[5]: ToolOutput(content='Balance Sheet: \n                                                        2024-01-31     2023-01-31     2022-01-31     2021-01-31     2020-01-31\nTreasury Shares Number                                         NaN            NaN            NaN  13800000000.0  13700576960.0\nOrdinary Shares Number                               24640000000.0  24661365720.0  25060000000.0  24800000000.0            NaN\nShare Issued                                         24640000000.0  24661365720.0  25060000000.0  38600000000.0            NaN\nNet Debt                                              2429000000.0   7564000000.0   8956000000.0   6116000000.0            NaN\nTotal Debt                                           11056000000.0  12031000000.0  11831000000.0   7597000000.0            NaN\nTangible Book Value                                  37436000000.0  16053000000.0  19924000000.0   9963000000.0            NaN\nInvested Capital                                     52687000000.0  33054000000.0  37558000000.0  23856000000.0            NaN\nWorking Capital                                      33714000000.0  16510000000.0  24494000000.0  12130000000.0            NaN\nNet Tangible Assets                                  37436000000.0  16053000000.0  19924000000.0   9963000000.0            NaN\nCapital Lease Obligations                             1347000000.0   1078000000.0    885000000.0    634000000.0            NaN\nCommon Stock Equity                                  42978000000.0  22101000000.0  26612000000.0  16893000000.0            NaN\nTotal Capitalization                                 51437000000.0  31804000000.0  37558000000.0  22857000000.0            NaN\nTotal Equity Gross Minority Interest                 42978000000.0  22101000000.0  26612000000.0  16893000000.0            NaN\nStockholders Equity                                  42978000000.0  22101000000.0  26612000000.0  16893000000.0            NaN\nGains Losses Not Affecting Retained Earnings            27000000.0    -43000000.0    -11000000.0     19000000.0            NaN\nOther Equity Adjustments                                27
# 

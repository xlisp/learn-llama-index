from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_parse import LlamaParse

documents2 = LlamaParse(result_type="markdown").load_data("./data/2023_canadian_budget.pdf")


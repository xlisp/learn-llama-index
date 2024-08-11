# https://colab.research.google.com/drive/1l3OLQ0p3CPWonoFmC9SgPzE2XkZI5sWm#scrollTo=LHkVWR8vH7SO
import os
from google.colab import userdata
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

os.environ["OPENAI_API_KEY"] = userdata.get('openai-key')

# settings
Settings.llm = OpenAI(model="gpt-3.5-turbo",temperature=0)

result = Settings.llm.complete("What is the capital of south dakota?")
print(result)

#=> The capital of South Dakota is Pierre.


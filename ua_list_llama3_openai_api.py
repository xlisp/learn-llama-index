## llama_index 如何使用ua例子学习？https://ollama.com/blog/openai-compatibility

from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

response = client.chat.completions.create(
  model="llama3.1",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
## 给UA例子知识
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The LA Dodgers won in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content)

# =>  prunp ua_list_llama3_openai_api.py ------------
# The 2020 World Series was actually played between the Los Angeles Dodgers and the Tampa Bay Rays, but not at a traditional ballpark.
# Due to the COVID-19 pandemic, the World Series was held with limited fans in attendance and featured an unique format. Game 6 of the series was played at Globe Life Field in Arlington, Texas (home of the Texas Rangers), as it was already set up for a potential game there instead of Los Angeles due to restrictions. The Dodgers then won the last two games on the road to take the series.
# It's worth noting that this was an unusual World Series setup as well, and not a traditional home-and-home format at either the Dodgers' or Rays' ballparks.


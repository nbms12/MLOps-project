import streamlit as st
from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

st.title("💬 Deepseek r1 model Chatbot")
st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
 

completion = client.chat.completions.create(
  model="deepseek-ai/deepseek-r1",
  messages=[{"role":"user","content":"explain me about electric cars in 5 lines only"}],
  temperature=0.6,
  top_p=0.7,
  max_tokens=4096,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    #print(chunk.choices[0].delta.content, end="")
    st.text(chunk.choices[0].delta.content)

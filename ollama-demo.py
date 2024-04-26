import ollama
import streamlit as st
import json


def call_llm(modelsList, text):
  response = ollama.chat(model=modelsList, messages=[
    {
      'role': 'user',
      'content': text,
    },
  ])
  return response['message']['content']


@st.cache_resource(ttl=3600)
def get_models():
  mymodels = ollama.list()['models']
  names = []
  for model in mymodels:
    names.append(model['name'].split(":")[0])
  return names

def main():
  st.title("Chat locally")
  st.write("Ask me anything!")

  with st.form("my-form"):
    modelsList = st.selectbox("Select a model", get_models())
    text = st.text_input("Enter your question")
    submitted = st.form_submit_button("Submit")

    if submitted:
      #modelsList = 'llama2'
      st.write(call_llm(modelsList, text))

if __name__ == "__main__":
    main()

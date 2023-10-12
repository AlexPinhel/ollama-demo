from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler                                  

llm = Ollama(model="llama2", 
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

ask = input("Que voulez-vous demander au chatbot?")

#import sys
#ask = sys.argv[1]

llm(ask)
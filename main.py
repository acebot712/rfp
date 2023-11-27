from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
import os

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.environ.get("AZURE_ENDPOINT"),
    deployment_name=os.environ.get("DEPLOYMENT_NAME"),
    openai_api_version=os.environ.get("OPENAI_API_VERSION"),
    openai_api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    model_name=os.environ.get("MODEL_NAME"),
)

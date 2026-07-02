from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    CHAT_MODEL = os.getenv("CHAT_MODEL", "gemma3:12b")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
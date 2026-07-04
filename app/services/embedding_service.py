from app.services.ai_client import AIClient


class EmbeddingService:

    def __init__(self):

        self.ai = AIClient()

    def generate(self, text: str):

        return self.ai.embed(text)
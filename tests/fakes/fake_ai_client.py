import hashlib


class FakeAIClient:

    def __init__(self):

        self.called = False
        self.last_text = None

    def embed(self, text: str):

        self.called = True
        self.last_text = text

        #
        # Deterministic embedding.
        # Same text -> same vector.
        #

        digest = hashlib.sha256(
            text.encode("utf-8")
        ).digest()

        vector = []

        #
        # Build a 768-dimensional vector
        #
        for i in range(768):

            value = digest[i % len(digest)]

            #
            # Normalize between 0 and 1
            #

            vector.append(value / 255.0)

        return vector

    def chat(self, prompt: str):

        return "Fake AI response."
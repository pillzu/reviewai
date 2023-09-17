import cohere
import numpy as np

COMMON_WORDS = [
    "the", "and", "of", "to", "in", "a", "for", "on", "with", "as",
    "by", "at", "an", "is", "it", "or", "be", "from", "that", "which",
    "want", "this", "but", "you", "your", "we", "are", "not", "can", "all",
    "have", "has", "has", "was", "if", "when", "here", "there", "now", "then" "I"
]


# Helper class
class Review:
    def __init__(self, review_1, review_2) -> None:
        self.first = review_1
        self.second = review_2

    def cleanNoise(self, raw_text: str):
        tokens = raw_text.split()
        filtered_tokens = [token for token in tokens if token.lower()
                           not in COMMON_WORDS]
        filtered_text = " ".join(filtered_tokens)
        return filtered_text

    def cleanReviews(self):
        self.first = self.cleanNoise(self.first)
        self.second = self.cleanNoise(self.second)


class AI:
    def __init__(self, api_key: str):
        self.AIClient = cohere.Client(api_key)

    def generate_ratings(self, input: str, review_1: str, review_2):

        review = Review(review_1, review_2)
        review.cleanReviews()

        # Embed the user input
        user_embedding = self.AIClient.embed(texts=[input]).embeddings[0]

        # Embed the computer reviews
        review_1_embedding = self.AIClient.embed(
            texts=[review.first]).embeddings[0]
        review_2_embedding = self.AIClient.embed(
            texts=[review.second]).embeddings[0]

        # Calculate cosine similarity between user input and reviews
        similarity_1 = np.dot(user_embedding, review_1_embedding) / \
            (np.linalg.norm(user_embedding) * np.linalg.norm(review_1_embedding))
        similarity_2 = np.dot(user_embedding, review_2_embedding) / \
            (np.linalg.norm(user_embedding) * np.linalg.norm(review_2_embedding))

        # Determine which computer review is a better fit
        if similarity_1 > similarity_2:
            return True
        else:
            return False

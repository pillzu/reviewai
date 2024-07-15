import cohere
import numpy as np

COMMON_WORDS = [
    "the", "and", "of", "to", "in", "a", "for", "on", "with", "as",
    "by", "at", "an", "is", "it", "or", "be", "from", "that", "which",
    "want", "this", "but", "you", "your", "we", "are", "not", "can", "all",
    "have", "has", "has", "was", "if", "when", "here", "there", "now", "then" "I"
]
COMPREHENSIVE_PROMPT = "Based on the user story, understand the two laptops reviews and come up with a detailed feature-wise breakdown of each laptop's suitability for the user's needs. Highlight the key aspects such as performance, portability, battery life, display quality, and any other relevant factors. Finally, make a recommendation on which laptop would be the best choice for the user based on this analysis in exactly 1000 words."

SUMMARIZE_PROMPT = "You are a tech reviewer who wrote about the %s. Talk about all aspects, including the laptop's pros and cons, key features, performance evaluations, design elements, and any distinctive attributes that distinguish it in the market in exactly 500 words."


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

    def process_raw_reviews(self, model, reviews):
        summaries = []
        for review in reviews:
            prompt = """context:
%s
<end>

%s
""" % (review, SUMMARIZE_PROMPT % model)
            response = self.AIClient.generate(
                prompt=prompt,
                max_tokens=1200,  # Adjust this value as needed
                num_generations=1,  # You can specify stop words or phrases to end the response
                truncate="END"
            )[0]  # Assuming [0] accesses the first generation

            # Convert the response to a string and then append it to the 'summaries' list
            summaries.append(response.text)

        # Join the summaries into a single string
        summary_string = "\n".join(summaries)
        return summary_string

    def generate_basic_ratings(self, input: str, review_1: str, review_2):

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

    def generate_comprehensive_rating(self, input: str, review_1: str, review_2: str):
        review = Review(review_1, review_2)

        prompt = f"""user-story: 
{input}
<end>

first review:
{review.first}
<end>

second review:
{review.second}
<end>

{COMPREHENSIVE_PROMPT}
"""
        response = self.AIClient.generate(
            prompt=prompt, num_generations=1, truncate="START", max_tokens=1500)[0]

        return response.text

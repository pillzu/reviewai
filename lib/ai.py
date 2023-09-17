import cohere
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Define the two computer reviews
non_filterd_1 = """The Dell Inspiron 15z is a laptop that can be used for many purposes, such as word processing, browsing the Internet, watching movies, or playing games. It has a large 15.4-inch display, a fast processor, and a long battery life. The Inspiron 15z is a great choice for anyone looking for a versatile laptop that can handle a variety of tasks.

The Dell Inspiron 15z is a laptop that is designed for everyday use. It is perfect for students, families, and anyone who needs a reliable laptop for browsing the internet, checking email, watching videos, or playing light games. The Inspiron 15z is powered by an Intel Core i5-8250U processor, 8GB of RAM, and a 256GB SSD. It also has a 1366 x 768 resolution display, a webcam, and a microphone. The Inspiron 15z is a great laptop for anyone who needs a basic laptop for everyday use.

The Dell Inspiron 15z is a great laptop for anyone who is looking for a laptop that is both stylish and functional. It has a sleek design that is perfect for anyone who wants a laptop that looks good, while also being very easy to use. The Inspiron 15z is also very lightweight, making it perfect for anyone who wants a laptop that is easy to carry around with them. The Inspiron 15z is also very affordable, making it a great option for anyone who is looking for a laptop that is both stylish and affordable."""


# Tokenize the input string
tokens = non_filterd_1.split()

# List of common words to remove
common_words = [
    "the", "and", "of", "to", "in", "a", "for", "on", "with", "as",
    "by", "at", "an", "is", "it", "or", "be", "from", "that", "which",
    "want", "this", "but", "you", "your", "we", "are", "not", "can", "all",
    "have", "has", "has", "was", "if", "when", "here", "there", "now", "then" "I"
]

# Remove common words
filtered_tokens = [token for token in tokens if token.lower()
                   not in common_words]

# Reconstruct the string without common words
computer_review_1 = " ".join(filtered_tokens)

non_filterd_2 = """It’s a great machine for most day to day activities, though it’s worth pointing out that the M2 is technically last year’s chip. It’s an open question whether Apple will return to an annual refresh cadence (with new Max/Pro models dropping precisely in the middle). Apple silicon is only a few years old, mind, and it seems perfectly reasonably to suspect continued supply chain concerns threw off the company’s rhythm. As with the 13-inch, Apple opted not to include a fan here. The assumption is that most casual users won’t be pushing the machine to a point where this is an issue too often. That’s probably right. If say, you’re doing 3D rending or editing 8K video, just buy a Pro. . Steam, for instance, really lives up to its name on the MacBook. It’s a little too easy to heat things up. I would say that if gaming is important in general, take a good long look at the Pro. Though honestly, the Windows ecosystem has such a massive head start on that front, that the Mac remains a tough sell for gamers. Apple is obviously working on that, with improved APIs for porting over existing titles. For a more casual approach to laptop gaming that doesn’t involving hours-long stretches, the Air is reasonably capable. Apple believes two is more than enough for most people – especially with the MagSafe onboard – perhaps that true, but I don’t know anyone who would say “no thank you” to another one.  There are four colors (to the Pro’s two). Apple sent a Starlight for review, but that would have been my last choice, honestly. I really dig the Midnight, along with the more classic Space Gray and Silver. But the Starlight’s yellow tint is subtle enough that the machine looks silver in most lights. It’s hardly ostentatious. Its starting price of $1,299 is quite reasonable for a Mac. That’s $200 more expensive than the 13-inch M2 (and $300 more than the more classic design M1 model that’s still kicking) and a full $700 less than the 14-inch Pro."""

# Tokenize the input string
tokens = non_filterd_2.split()

# Remove common words
filtered_tokens = [token for token in tokens if token.lower()
                   not in common_words]

# Reconstruct the string without common words
computer_review_2 = " ".join(filtered_tokens)

# Paste your Cohere API key here
api_key = '_'

# Initialize the Cohere client
co = cohere.Client(api_key)


def compare_computers(user_input):
    # Embed the user input
    user_embedding = co.embed(texts=[user_input]).embeddings[0]

    # Embed the computer reviews
    review_1_embedding = co.embed(texts=[computer_review_1]).embeddings[0]
    review_2_embedding = co.embed(texts=[computer_review_2]).embeddings[0]

    # Calculate cosine similarity between user input and reviews
    similarity_1 = np.dot(user_embedding, review_1_embedding) / \
        (np.linalg.norm(user_embedding) * np.linalg.norm(review_1_embedding))
    similarity_2 = np.dot(user_embedding, review_2_embedding) / \
        (np.linalg.norm(user_embedding) * np.linalg.norm(review_2_embedding))

    print(similarity_1)
    print(similarity_2)
    # Determine which computer review is a better fit
    if similarity_1 > similarity_2:
        return "Computer Review 1 is a better fit for you."
    else:
        return "Computer Review 2 is a better fit for you."


# Capture user input
user_input = input("Enter your requirements and preferences for a computer: ")

# Compare the user input against the computer reviews
result = compare_computers(user_input)

# Display the result
print(result)

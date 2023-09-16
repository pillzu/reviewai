import certifi
import ssl
from googlesearch import search
from bs4 import BeautifulSoup
import requests

#no f-ing idea
ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context().load_verify_locations(certifi.where())

# Get the search query from the user

# class DataScraper:
#     def __init__(self, url):
#         self.url = url

def scrape(user_query):

# List of target websites
    target_websites = ["theverge.com", "cnet.com", "techcrunch.com"]

# Initialize a variable to store the review content
    review_content_string = ""

# Loop through the target websites
    for website in target_websites:
        print(f"Searching for '{user_query}' reviews on {website}...")

        # Append "reviews" to the user's query and include the site restriction
        query = f"{user_query} reviews site:{website}"

        # Perform the Google search and get the first 4 results
        search_results = list(search(query, num=4, stop=4, pause=2))

        # Loop through the search results
        for idx, result_url in enumerate(search_results, start=1):
            print(f"Result {idx}: {result_url}")

            # Check if both the target website and "review" are in the URL
            if website in result_url and 'review' in result_url:
                try:
                    # Send an HTTP GET request to the website
                    response = requests.get(result_url)
                    response.raise_for_status()

                    # Parse the HTML content of the page using Beautiful Soup
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Extract and append the review content to the string
                    review_content = ' '.join(soup.stripped_strings)
                    review_content_string += review_content + "\n"

                    print("=" * 50)  

                    
                    break
                except requests.exceptions.RequestException as e:
                    print(f"Failed to retrieve the web page: {str(e)}")


    print("\nReview Content (Text Only):")
    print(review_content_string)

scrape("macbook air m2 2023")

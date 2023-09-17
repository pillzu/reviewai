import certifi
import ssl
from googlesearch import search
from bs4 import BeautifulSoup
import requests

ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context().load_verify_locations(certifi.where())


class DataScraper:
    def __init__(self, model):
        self.model = model
        pass

    def cnet(self):
        website = "cnet.com"
        print(f"Searching for '{self.model}' reviews on {website}..")
        # Append "reviews" to the user's query and include the site restriction
        query = f"{self.model} reviews site:{website}"

        # Perform the Google search and get the first 4 results
        search_results = list(search(query, num=4, stop=4, pause=2,
                              user_agent='your bot 1.0'))

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
                    info = soup.find("div", class_="c-pageArticle_content")

                    stripped_info = ' '.join(info.stripped_strings)

                    return stripped_info
                except requests.exceptions.RequestException as e:
                    print(f"Failed to retrieve the web page: {str(e)}")

    def pcmag(self):
        website = "pcmag.com"
        print(f"Searching for '{self.model}' reviews on {website}..")

        # Append "reviews" to the user's query and include the site restriction
        query = f"{self.model} reviews site:{website}"

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
                    info = soup.find("article", {"id": "article"})

                    stripped_info = ' '.join(info.stripped_strings)

                    return stripped_info

                except requests.exceptions.RequestException as e:
                    print(f"Failed to retrieve the web page: {str(e)}")

    def scrape(self):
        reviews = []

        # Call the verge function and append its stripped content to the reviews list
        # verge_info = verge(user_query)
        # if verge_info:
        #     reviews.append(verge_info)

        # Call the cnet function and append its stripped content to the reviews list
        cnet_info = self.cnet()
        if cnet_info:
            reviews.append(cnet_info)

        # Call the pcmag function and append its stripped content to the reviews list
        pcmag_info = self.pcmag()
        if pcmag_info:
            reviews.append(pcmag_info)

        return reviews

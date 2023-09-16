import requests
from bs4 import BeautifulSoup


class DataScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        try:
            # Send an HTTP GET request to the specified URL
            response = requests.get(self.url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract and return the scraped data
                # You can modify this part to extract specific data you need
                scraped_data = soup.get_text()
                return scraped_data

            else:
                return f"Failed to fetch data. Status code: {response.status_code}"

        except Exception as e:
            return f"An error occurred: {str(e)}"

# indexer.py

import requests
from bs4 import BeautifulSoup

def sitemap(website_url: str) -> list:
    """
    Extracts all the URLs from a website's XML sitemap.

    Args:
        website_url: str
            The URL of the website's sitemap.

    Returns:
        list
            A list of all the URLs in the sitemap.
    """
    try:
        response = requests.get(website_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        soup = BeautifulSoup(response.content, "html.parser")  # Specify the parser as "xml"
        urls = [loc.get_text() for loc in soup.find_all("loc")]
        
        print(f"Extracted {len(urls)} URLs from the sitemap:")
        return urls
        
        
    except requests.RequestException as e:
        raise Exception(f"Error fetching sitemap: {e}")
    except Exception as e:  # Added to catch potential parsing errors
        raise Exception(f"Error parsing sitemap: {e}")


if __name__ == "__main__":
    # website_url = input("Enter the URL of the website's sitemap: ")
    website_url = "https://creately.com/en/sitemap.xml"
    all_urls = sitemap(website_url)
    for url in all_urls:
        print(url)

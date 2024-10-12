import requests
import re
import time

# Set of URLs we've already visited
visited_urls = set()
# Base URL for Power BI documentation
base_url = "https://matplotlib.org/stable/users/explain"

def scrape_website(url: str):
    if url in visited_urls:
        return
    visited_urls.add(url)

    api_url = f"https://r.jina.ai/{url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            markdown_content = response.text
            print(f"Fetched content from {url}")

            # Process the Markdown content as needed, such as saving it to a database
            
            # Extract links for further crawling
            links = extract_links(markdown_content)
            for link in links:
                if link.startswith(base_url):
                    scrape_website(link)

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

def extract_links(markdown_content: str):
    # Regex to find all markdown links in the content
    link_pattern = re.compile(r'\[(.*?)\]\((https:\/\/matplotlib\.org\/stable\/users\/explain\/[^\s\)]+)\)')
    links = link_pattern.findall(markdown_content)
    # Return only the URLs from the matches
    return [link[1] for link in links]

# Start scraping from the initial documentation URL
initial_url = "https://matplotlib.org/stable/users/explain"
scrape_website(initial_url)

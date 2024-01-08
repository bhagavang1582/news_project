import requests
from bs4 import BeautifulSoup
from news_app.models import NewsArticle

def extract_urls():
    # URL of the website you want to extract data from
    website_url = 'https://moneycontrol.com/news/'  # Replace with the desired website URL

    # Send a GET request to the website and get its HTML content
    response = requests.get(website_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.content

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all anchor tags
        all_links = soup.find_all('a')

        # Extract URLs and their titles that match the criteria
        urls_and_titles = {}
        for link in all_links:
            url = link.get('href')
            title = link.text.strip() if link.text else "No title provided"
            if url.startswith('https:') and url.endswith('.html'):
                urls_and_titles[url] = title

        # Delete existing articles from the NewsArticle model
        NewsArticle.objects.all().delete()

        # Save URLs and titles into the NewsArticle model
        for url, title in urls_and_titles.items():
            NewsArticle.objects.create(url=url, title=title)

    #     print("URLs and titles saved into the database.")
    # else:
    #     print(f"Failed to fetch the website. Status code: {response.status_code}")

if __name__ == "__main__":
    extract_urls()

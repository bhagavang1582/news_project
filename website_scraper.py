import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting heading
    heading = soup.find('h1').get_text().strip() if soup.find('h1') else "Heading not found"

    # Extracting main textual content
    content_paragraphs = soup.find_all('p')
    text_content = '\n'.join([p.get_text().strip() for p in content_paragraphs])

    # Extracting images
    images = [img['src'] for img in soup.find_all('img', src=True)]

    return {
        "heading": heading,
        "text_content": text_content,
        "images": images
    }

def scrape_and_save(urls, output_file):
    # Scraping each URL and storing the data
    output_data = []
    for url in urls:
        scraped_data = scrape_website(url)
        output_data.append(scraped_data)

    # Save the scraped data to a JSON file
    with open(output_file, 'w') as file:
        json.dump(output_data, file, indent=4)

    print(f"Scraped data saved to '{output_file}'.")
import bs4 as bs
import urllib.request

# List of Wikipedia URLs
links = [
    "https://es.wikipedia.org/wiki/Canis_familiaris",
    "https://es.wikipedia.org/wiki/Canis_lupus",
    "https://es.wikipedia.org/wiki/Delphinidae",
    "https://es.wikipedia.org/wiki/Oryctolagus_cuniculus",
    "https://es.wikipedia.org/wiki/Psittacoidea",
    "https://es.wikipedia.org/wiki/Struthio_camelus",
    "https://es.wikipedia.org/wiki/Elephantidae",
    "https://es.wikipedia.org/wiki/Gorilla",
    "https://es.wikipedia.org/wiki/Panthera_pardus",
    "https://es.wikipedia.org/wiki/Giraffa_camelopardalis"
]

def fetch_and_parse(url):
    """Fetch and parse a webpage, returning a BeautifulSoup object."""
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request) as webpage:
            source = webpage.read()
        soup = bs.BeautifulSoup(source, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_info(soup):
    """Extracts and prints the title and first paragraph of the Wikipedia page."""
    if soup:
        title = soup.find('h1').get_text()
        paragraph = soup.find('p').get_text()
        print(f"Title: {title}")
        print(f"First paragraph: {paragraph}\n")

def main():
    for link in links:
        print(f"Processing {link}...")
        soup = fetch_and_parse(link)
        extract_info(soup)

# Run the script
main()

    






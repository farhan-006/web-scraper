import argparse
import requests
from bs4 import BeautifulSoup


def scrape_website(url, options):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
      
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        
        soup = BeautifulSoup(response.content, "lxml")

        # Find specific sections of the page to extract data from
        content_div = soup.find("div", {"id": "content"})
        if content_div:
            elements = content_div.find_all()
        else:
            elements = soup.find_all()

        
        for i, element in enumerate(elements):
            # Extract the tag name
            tag_name = element.name
            if tag_name:
                # Extract the attributes
                attributes = element.attrs
                # Extract the text content
                text_content = element.text
                # Extract the HTML content
                html_content = str(element)

               
                if 'all' in options or 'name' in options:
                    print(f"Tag name: {tag_name}")
                if 'all' in options or 'attrs' in options:
                    print(f"Attributes: {attributes}")
                if 'all' in options or 'text' in options:
                    print(f"Text content: {text_content}")
                if 'all' in options or 'html' in options:
                    print(f"HTML content: {html_content}\n")

    except requests.exceptions.RequestException as e:
        # Handle errors with the request or response
        print(f"Error scraping {url}: {e}")


def main():
    
    parser = argparse.ArgumentParser(description='Scrape websites for specific data')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+',
                        help='URLs of the websites to scrape')
    parser.add_argument('--tags', dest='options', action='append_const', const='name',
                        help='Include tag names in output')
    parser.add_argument('--attrs', dest='options', action='append_const', const='attrs',
                        help='Include attributes in output')
    parser.add_argument('--text', dest='options', action='append_const', const='text',
                        help='Include text content in output')
    parser.add_argument('--html', dest='options', action='append_const', const='html',
                        help='Include HTML content in output')

    
    parser.add_argument('--all', dest='options', action='store_const', const='all',
                        help='Include all data in output')

    
    args = parser.parse_args()

    
    options_mapping = {
        'tags': 'name',
        'attrs': 'attrs',
        'text': 'text',
        'html': 'html',
        'all': 'all'
    }
    options = [options_mapping[option] for option in args.options] if args.options else []

  
    for url in args.urls:
        scrape_website(url, options)


if __name__ == '__main__':
    main()

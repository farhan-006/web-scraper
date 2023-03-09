# Website Scraper

This is a Python script for scraping data from websites. It allows the user to specify which types of data to extract from the website (tag names, attributes, text content, HTML content) or to scrape all available data.

## Dependencies

This script requires the following dependencies:
- `argparse`
- `requests`
- `beautifulsoup4`

You can install them using `pip`:
pip install argparse requests beautifulsoup4


## Usage

python website_scraper.py [-h] [--tags] [--attrs] [--text] [--html] [--all] URL [URL ...]


### Positional arguments:
- `URL`: URLs of the websites to scrape

### Optional arguments:
- `-h, --help`: show help message and exit
- `--tags`: Include tag names in output
- `--attrs`: Include attributes in output
- `--text`: Include text content in output
- `--html`: Include HTML content in output
- `--all`: Include all data in output

## Examples

Extract tag names and text content from a single website:
python website_scraper.py --tags --text https://www.example.com


Extract all available data from multiple websites:
python website_scraper.py --all https://www.example.com https://www.example2.com





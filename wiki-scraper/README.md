
# Wiki-scraper

A Scrapy tool that gathers useless information from wikipedia pages, current main purpose of comparing amount of links to words, only handles paragraphs for now.

## Usage

#### Option 1

Run 'scrapy parse `WIKILINK` --spider=wiki_spider' into command line inside current directory where wikistats is located.

#### Option 2

1. Open wikistats/spiders/wiki_spider.py

2. Add all links inside urls list variable at start_requests method

3. Run 'scrapy crawl wiki_spider' into command line inside current directory where wikistats is located.

## Output

Outputs a dictionary of different items

**num_paragraphs**: number of paragraphs scrapy found

**total_words**: number of words inside paragraphs

**num_links**: number of links inside paragraphs

**percent_as_links**: percentage between links and words ((num_links / total_words) * 100)

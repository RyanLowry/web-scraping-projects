# -*- coding: utf-8 -*-
import scrapy
from wikiscraper.items import WikiScraperItem


class WikiSpider(scrapy.Spider):
    name = 'wiki_spider'
    allowed_domains = ['wikipedia.com']
    
    def start_requests(self, *args, **kwargs):
        urls = ['https://en.wikipedia.org/wiki/Hello','https://en.wikipedia.org/wiki/MediaWiki']
        for url in urls:
            yield scrapy.Request(url = url,callback = self.parse)

    def parse(self,res):
        wikiContent = res.css('div.mw-parser-output *')

        wikiItem = WikiScraperItem()
        totalWords = 0
        numLinks = 0
        numParagraphs = 0
        
        #TODO:use all content inside mw-parser-output, ignoring self-referenced links
        for ele in wikiContent:
            #Finds only paragraphs inside main content
            #ignore tables and divs currently
            if ele.css('p'):
                numParagraphs += 1
                numLinks += len(ele.css('a::text'))
                totalWordsInParagraph = "".join(ele.css('p *::text').getall()).split(" ")
                totalWords += len(totalWordsInParagraph)

        percentAsLinks = (numLinks / totalWords) * 100

        wikiItem['total_words'] = totalWords
        wikiItem['num_links'] = numLinks
        wikiItem['num_paragraphs'] = numParagraphs
        wikiItem['percent_as_links'] = '{0:.2f}'.format(percentAsLinks)

        yield wikiItem

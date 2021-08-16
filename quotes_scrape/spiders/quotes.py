import scrapy
from ..items import QuotesScrapeItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        items=QuotesScrapeItem()
        list_of_quotes = response.xpath('//div[@class="quote"]')
        for quote in list_of_quotes:
            text = quote.xpath('span[@class="text"]/text()').extract()
            author = quote.xpath('span/small[@class="author"]/text()').extract()
            items['text']=text
            items['author']=author
            yield items        
            # print(items)
    

        

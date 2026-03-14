import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('span a::attr("href")').get()
                # 'tags': quote.css('div.tags::text').get()
            }

            next_page = response.css('li.next a::attr("href")').get()
            next_page_url = 'https://quotes.toscrape.com/' + next_page

            yield response.follow(next_page_url, self.parse)

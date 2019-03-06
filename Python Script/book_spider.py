import scrapy


class BooksSpider(scrapy.Spider):
    # identify each spider
    name = 'books'
    # set the url
    start_urls = ['http://books.toscrape.com/']

    def parse(self, respone):
        # retrieve data
        # the information of each book are under the <article class='product_pod]'
        # we are using css() to lookup all the article elements
        for book in response.cass('article.product_pod'):
            # books' names are under 'article>h3>a>title'
            name = book.xpath('.h3/a/@title').extract_first()

            # the price is under <p class='price_color'>
            price = book.css('p.price_color::text').extract_first()
            yield{
                'name': name,
                'price': price,
            }
            # retrieve the url
            # the 'Next Page's url is under the ul.paper > li.next >a
            next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            # if find the next ulr, get the absolute path, establish the new request target
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

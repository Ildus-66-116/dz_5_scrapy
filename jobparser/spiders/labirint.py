import scrapy
from sbor_and_razmetka_data.dz.dz_5_scrapy.jobparser.items import JobparserItem


class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["labirint.ru"]
    start_urls = [
        "https://www.labirint.ru/search/%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B0/?stype=0"]

    def parse(self, response):
        """Получаем начальные ссылки на страницу"""
        next_page = response.xpath("//div[@class='pagination-next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class='product-card__img']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.books_parse)

    def books_parse(self, response):
        url = response.url
        _id = response.xpath('//div[@class="articul"]//text()').get()
        author = response.xpath("//a[@data-event-label='author']//text()").get()
        name = response.xpath('//div[@id="product-title"]/h1//text()').get()
        price = response.xpath('//span[@class="buying-pricenew-val-number"]//text()').get()
        description = response.xpath('//div[@id="product-about"]//p//text()').get()
        number_of_pages = response.xpath('//div[contains(text(),"Страниц:")]//text()').get()
        yield JobparserItem(_id=_id, name=name, author=author, url=url, price=price, description=description,
                            number_of_pages=number_of_pages)

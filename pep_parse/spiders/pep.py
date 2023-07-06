import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = [f"https://{url}/" for url in allowed_domains]

    def parse(self, response):
        links = set(
            response.css('table.pep-zero-table a::attr(href)').getall()
        )
        for pep_url in list(links)[:3]:
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('.page-title::text').get().split(' – ')
        yield PepParseItem(dict(
            name=name,
            number=number[4:],
            status=response.css('abbr::text').get(),
        ))

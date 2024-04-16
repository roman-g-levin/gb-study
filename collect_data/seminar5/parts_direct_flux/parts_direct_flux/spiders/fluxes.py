import scrapy
import csv


class FluxesSpider(scrapy.Spider):
    name = "fluxes"
    allowed_domains = ["www.partsdirect.ru"]
    start_urls = ["https://www.partsdirect.ru/for_soldering/flux_and_rosin"]

    def parse(self, response):
        fluxes = response.xpath("//table[@class='cl']/tr")
        
        for flux in fluxes:
            name = flux.xpath(".//td/a/text()").get().strip()
            link = flux.xpath(".//td/a/@href").get()
            #name = flux.xpath(".//tr/a/text()").get().strip()
            #link = flux.xpath(".//tr/a/@href").get()
            
            with open('./fluxes_finded.csv', 'a', newline='', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow([name, link])

            #absolute_url = response.urljoin(link)
            #yield response.follow(url=link, callback=self.parse_flux)
            yield response.follow(url=link, callback=self.parse_flux, meta={'flux_name' : name})

    def parse_flux(self, response):
        name = response.request.meta['flux_name']
        #rows = response.xpath("//tr[contains(@class, 'datatable')]")
        description = response.xpath("//div[contains(@class, 'title')]/h1").get()
        price = response.xpath("//div[contains(@class, 'roz_price')]/strong/text()").get().strip()
        description = description.replace("</h1>","").strip()
        description = description.replace('<h1 itemprop="name">',"").strip()
        description = description.replace("<strong>","").strip()
        description = description.replace("</strong>","").strip()
        description = description.replace("\n","").strip()
    #     for row in rows:
    #         related = row.xpath(".//td/a/text()").get().strip()
    #         last = float(row.xpath(".//td[2]/text()").get())
    #         previous = float(row.xpath(".//td[3]/text()").get())
        
    #         yield {
    #             'country_name' : name,
    #             'related' : related,
    #             'last' : last,
    #             'previous' : previous
    #         }
        with open('./fluxes_crawled.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow([name, description, price])

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector
from biancospider.items import BiancospiderItem

class BiancoSpider(CrawlSpider):
    name = 'BiancoSpider'
    allowed_domains = ["biancogres.com.br"]
    start_urls = ['https://www.biancogres.com.br/produtos/']
    base_url = 'https://www.biancogres.com.br/produtos/'
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['nome', 'url', 'imagem', 'formato', 'categoria', 'acabamento', 'relevo', 'classe_ad', 'variacao_tonalidade', 'n_faces', 'espessura', 'junta', 'm2_caixa', 'pecas_caixa'],
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='next page-numbers']"), follow=True),
        Rule(LinkExtractor(allow=r"/produto/[-a-zA-Z]"), callback='parse_details', follow=True),
    )

    def parse_details(self, response):
        exists = response.xpath('//table[@id="variacoes"]').extract_first()

        if exists:
            item = BiancospiderItem()
            item['nome'] = response.xpath('//h1/text()').extract_first()
            item['url'] = response.url

            imgList = []
            testImg = response.xpath('//div[@class="ae-swiper-slide-wrapper"]/a/img/@src').extract()
            for imgs in testImg:
                if imgs.find("AMBIENTE") == -1:
                    imgList.append(imgs)

            item['imagem'] = imgList[0]
            item['formato'] = response.xpath('//table[@id="variacoes"]//tr/td[1]/text()').extract_first()
            item['categoria'] = response.xpath('//table[@id="variacoes"]//tr/td[2]/text()').extract_first()
            item['acabamento'] = response.xpath('//table[@id="variacoes"]//tr/td[3]/text()').extract_first()
            item['relevo'] = response.xpath('//table[@id="variacoes"]//tr/td[4]/text()').extract_first()
            item['classe_ad'] = response.xpath('//table[@id="variacoes"]//tr/td[5]/text()').extract_first()
            item['variacao_tonalidade'] = response.xpath('//table[@id="variacoes"]//tr/td[6]/text()').extract_first()
            item['n_faces'] = response.xpath('//table[@id="variacoes"]//tr/td[7]/text()').extract_first()
            item['espessura'] = response.xpath('//table[@id="variacoes"]//tr/td[8]/text()').extract_first()
            item['junta'] = response.xpath('//table[@id="variacoes"]//tr/td[9]/text()').extract_first()
            item['m2_caixa'] = response.xpath('//table[@id="variacoes"]//tr/td[10]/text()').extract_first()
            item['pecas_caixa'] = response.xpath('//table[@id="variacoes"]//tr/td[11]/text()').extract_first()


            yield item

        else:
            print (response.url)

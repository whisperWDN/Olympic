import scrapy
from OlympicModel.items import OlympicmodelItem


class BaiduSpider(scrapy.Spider):
    name = 'baidutiyu'
    allowed_domains = ['tiyu.baidu.com/']
    start_urls = ['https://tiyu.baidu.com/tokyoly/home/tab/%E5%A5%96%E7%89%8C%E6%A6%9C/from/pc']

    def parse(self, response):
        models = response.xpath('//*[@id="sfr-app"]/div/div[2]/div/div/div/main/section/div[1]/b-grouplist-sticky/div/div[3]/div/div/div[2]/div/div/a')
        for model in models:
            item = OlympicmodelItem()
            item['rank'] = model.xpath('div[1]/div[1]/p/text()').extract_first()
            item['nation'] = model.xpath('div[1]/div[2]/span[2]/text()').extract_first()
            item['gold'] = model.xpath('div[2]/div[1]/text()').extract_first()
            item['silver'] = model.xpath('div[2]/div[2]/text()').extract_first()
            item['bronze'] = model.xpath('div[2]/div[3]/text()').extract_first()
            item['total'] = model.xpath('div[2]/div[4]/text()').extract_first()
            yield item

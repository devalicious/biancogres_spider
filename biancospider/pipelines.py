# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporter import CsvItemExporter

class BiancospiderPipeline(object):
    def __init__(self):
        self.myCsv = csv.writer(open('Item.csv', 'w', encoding='utf-8'))
        self.myCsv.writerow(['nome', 'url', 'imagem', 'formato', 'categoria', 'acabamento', 'relevo', 'classe_ad', 'variacao_tonalidade', 'n_faces', 'espessura', 'junta', 'm2_caixa', 'pecas_caixa'])

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

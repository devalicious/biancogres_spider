# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiancospiderItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    imagem = scrapy.Field()
    nome = scrapy.Field()
    formato = scrapy.Field()
    categoria = scrapy.Field()
    acabamento = scrapy.Field()
    relevo = scrapy.Field()
    classe_ad = scrapy.Field()
    variacao_tonalidade = scrapy.Field()
    n_faces = scrapy.Field()
    espessura = scrapy.Field()
    junta = scrapy.Field()
    m2_caixa = scrapy.Field()
    pecas_caixa = scrapy.Field()

    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YummlySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    recipeUrl = scrapy.Field()
    recipeName = scrapy.Field()
    recipePhoto = scrapy.Field()
    ingredients = scrapy.Field()
    ratings = scrapy.Field()
    cookTime = scrapy.Field()
    serve = scrapy.Field()
    tags = scrapy.Field()
    recipeType = scrapy.Field()
    

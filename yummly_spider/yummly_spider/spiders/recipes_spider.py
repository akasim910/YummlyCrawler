# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from yummly_spider.items import YummlySpiderItem
import json
from bs4 import BeautifulSoup
import requests


class RecipesSpider(CrawlSpider):
    name = 'recipes'
    allowed_domains = ['yummly.com']
    start_urls = ['https://yummly.com/recipes/']

    rules = [
        Rule(
            LinkExtractor(allow=[r'recipe/\w+']),
            callback='parse_recipes',
            follow=True
        )
    ]

    def parse_recipes(self, response):
        #fetch the content from the url, using the requests library
        try:
            page_response = requests.get(response.url, timeout=30)
        except requests.exceptions.Timeout:
            print("Timeout occurred")

        
        soup = BeautifulSoup(page_response.content, features="lxml")

        #finds all div tags with appropriate class
        #this class contains a JSON object of all the necessary information
        mydivs = soup.find_all("div", class_="structured-data-info")


        #loads converts JSON string into python object
        data = json.loads(mydivs[0].text)

        #store values in YummlySpiderItem object
        item = YummlySpiderItem()
        item['recipeUrl'] = response.url
        item['recipeName'] = data['name']
        item['recipePhoto'] = data['image']
        item['ingredients'] = data['recipeIngredient']
        try:
            item['ratings'] = float(data['aggregateRating']['ratingValue'])
        except:
            item['ratings'] = 0.0

        try:
            item['cookTime'] = data['totalTime']
        except:
            item['cookTime'] = ''

        try:    
            item['serve'] = int(data['recipeYield'].split()[0])
        except:
            item['serve'] = ''

        try:
            item['tags'] = [x.strip() for x in data['keywords'].split(',')]
        except:
            item['tags'] = []

        try:
            item['recipeType'] = data['recipeCategory'][0]
        except:
            item['recipeType'] = ''


        #append items to file one by one
        with open('output.txt', 'a') as f:
            f.write('{{recipeUrl: \'{0}\',\n recipeName: \'{1}\',\n recipePhoto: \'{2}\',\n ingredients: {3},\n ratings: {4},\n cookTime: \'{5}\',\n serve: {6},\n tags: {7}, \n recipeType: \'{8}\'\n}},\n'
                .format(item['recipeUrl'], item['recipeName'], item['recipePhoto'], item['ingredients'], item['ratings'], item['cookTime'], item['serve'], item['tags'], item['recipeType']))
        yield item
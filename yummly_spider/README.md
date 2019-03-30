# Yummly Web Crawler
> Web crawler to download recipes from Yummly in JSON format

This is a web crawler and web scraper designed to download recipes from Yummly in the following format:
```shell
[
{
recipeUrl: string,
recipeName: string,
recipePhoto: string,
ingredients: string[],
ratings: float,
cookTime: string,
serve: number
tags: string[]
recipeType: enum ( main course, drink, breakfast, desert, salad)
}
…
]
```
# Getting started


## Install Python 3.7 and Virtualenv

* Python 3.7 using ```pip```

* Virtualenv using ```pip install virtualenv```

## Create virtual environment and activate it

Create a virtual environment using Python 3.7
```shell
python3.7 -m virtualenv venv 
```
Activate the virtual environment
```shell
source venv/bin/activate
```


## Install dependencies

Download all the dependencies to run the program using the given requirements.txt file. 

```shell
pip install -r /path/to/requirements.txt
```

# How to use
Navigate to the top level directory with the scrapy.cfg file
```shell
yummly
   venv
   yummly_spider
       README.md
       scrapy.cfg
       yummly_spider
```

Run using the following command:
```shell
scrapy crawl recipes
```

> **Press Ctrl-C to stop the crawler anytime** 


## Check ```output.txt``` to see the crawled data

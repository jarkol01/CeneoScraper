import requests
import json
from bs4 import BeautifulSoup

selected_product_id = input("Enter selected product ID: ")
#test product_id: 101052360

url = f'https://www.ceneo.pl/{selected_product_id}/opinie-1'

all_opinions = []

while url:
    response = requests.get(url)
    page = BeautifulSoup(response.text, "html.parser")

    opinions = page.select('div.js_product-review')

    for opinion in opinions:
        opinion_id = opinion['data-entry-id']
        author = opinion.select_one('span.user-post__author-name').get_text().strip()
        try:
            recommendation = opinion.select_one('span.user-post__author-recomendation > em').get_text()
        except AttributeError:
            recommendation = None
        stars = opinion.select_one('span.user-post__score-count').get_text()
        content = opinion.select_one('div.user-post__text').get_text()
        useful = opinion.select_one('button.vote-yes > span').get_text()
        useless = opinion.select_one('button.vote-no > span').get_text()
        published = opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]
        purchased = opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]
        pros = opinion.select('div.review-feature__title--positives ~ div.review-feature__item')
        pros = [item.get_text().strip() for item in pros]
        cons = opinion.select('div.review-feature__title--negatives ~ div.review-feature__item')
        cons = [item.get_text().strip() for item in cons]

        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "recommendation": recommendation,
            "stars": stars,
            "content": content,
            "useful": useful,
            "useless": useless,
            "published": published,
            "purchased": purchased,
            "pros": pros,
            "cons": cons
        }
        all_opinions.append(single_opinion)
    try:
        url = 'https://www.ceneo.pl'+page.select_one('a.pagination__next')['href']
    except TypeError:
        url = None

with open(f"opinions/{selected_product_id}.json", 'w', encoding='UTF-8') as file:
    json.dump(all_opinions, file, indent=4, ensure_ascii=False)


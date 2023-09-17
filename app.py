from flask import Flask, jsonify, request, abort
import os
from dotenv import load_dotenv
from lib.scraper import DataScraper
from lib.ai import AI

app = Flask(__name__)


ai = None


@app.route('/', methods=['POST'])
def home():
    if not request.json:
        abort(400, 'missing params')

    # get story, product #1, product #2, payment tier
    try:
        story = request.json['story']
        product_1 = request.json['product_1']
        product_2 = request.json['product_2']
        isPremium = request.json['is_premium']
    except:
        abort(500, "Missing parameters")

    # for each product
    # 1. scrape data
    # 2. Generate summarized text
    scraped_p1 = DataScraper(product_1)
    scraped_p1_reviews = scraped_p1.scrape()
    summarized_p1 = ai.process_raw_reviews(product_1, scraped_p1_reviews)

    scraped_p2 = DataScraper(product_2)
    scraped_p2_reviews = scraped_p2.scrape()
    summarized_p2 = ai.process_raw_reviews(product_2, scraped_p2_reviews)

    ret = {
        "is_premium": isPremium,
    }

    # based on payment tier
    #   run generate_basic...
    #   run generate_premium...
    if isPremium:
        text = ai.generate_comprehensive_rating(
            story, summarized_p1, summarized_p2)
        ret['text'] = text
    else:
        isFirstBetter = ai.generate_basic_ratings(
            story, summarized_p1, summarized_p2)
        ret['suggested_product'] = product_1

        if not isFirstBetter:
            ret['suggested_product'] = product_2

    return jsonify(ret)


if __name__ == '__main__':
    load_dotenv()
    port = int(os.environ.get('PORT', 5000))
    api_key = str(os.environ.get('COHERE_KEY'))
    ai = AI(api_key)
    app.run(host='0.0.0.0', port=port)

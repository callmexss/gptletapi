import os

import dotenv
from apify_client import ApifyClient

dotenv.load_dotenv()


APIFY_TOKEN = os.getenv('APIFY_KEY')


client = ApifyClient(APIFY_TOKEN)
dataset_collection_client = client.datasets()
gpts_dataset = dataset_collection_client.get_or_create(name='gpts')


def convert_item_to_entry_obj(item):
    return {
        'name': item['title'],
        'description': item['description'],
        'image_url': item['logoUrl'],
        'link_url': item['url'],
        'author': item['author'],
        'welcome_message': item['welcomeMessage'],
    }


def build_gpts_link_dict(url):
    return {
        'url': url
    }


def fetch_urls(urls: list[dict[str, str]]):
    run_input = {
        "proxyConfiguration": {
            "useApifyProxy": True,
            "apifyProxyCountry": "US",
        },
        "gptsUrls": urls,
    }

    return client.actor("ouOMaUFUM39WV6xKP").call(run_input=run_input)


def extract_items(run):
    return client.dataset(run["defaultDatasetId"]).list_items().items


if __name__ == "__main__":
    url = 'https://chat.openai.com/g/g-TYnHP4RG0'
    urls = [build_gpts_link_dict(url)]
    run = fetch_urls(urls)
    item = extract_items(run)
    convert_item_to_entry_obj(item)
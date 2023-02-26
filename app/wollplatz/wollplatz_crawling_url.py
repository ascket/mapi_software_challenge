import requests
from bs4 import BeautifulSoup
from typing import NamedTuple, List, Dict
import re
import json

# URL = f"https://dynamic.sooqr.com/suggest/script/"
# ACCOUNT_NUMBER = "SQ-119572-1"

# products_to_crawling = [
#     {"brand_name": "DMC", "product_name": "Natura XL"},
#     {"brand_name": "Drops", "product_name": "Safran"},
#     {"brand_name": "Drops", "product_name": "Baby Merino Mix"},
#     {"brand_name": "Hahn", "product_name": "Alpacca Speciale"},
#     {"brand_name": "Stylecraft", "product_name": "Special double knit"}
# ]


def get_search_url(start_url: str, brand_name: str, product_name: str) -> str:
    """
    This method converts the start search URL to the desired format. The result is a URL that can be used further to get search results.

    Args:
        start_url: Start search url
        brand_name: Brand name from the search list of products
        product_name: Product name from the search list of products

    Returns:
        Converted url without account number.
    """
    raw_brand_name = brand_name.strip().lower().replace(" ", "%20")
    raw_product_name = product_name.strip().lower().replace(" ", "%20")
    brand_product = "%20".join([raw_brand_name, raw_product_name])
    url = f"{start_url}?type=suggest&searchQuery={brand_product}"
    return url


def wollplatz_product_url(products: List[Dict[str, str]], start_url: str,
                          account: str) -> List[Dict[str, str]]:
    json_regex = re.compile((r'{.*}'))
    results = []
    params = {
        "account": account
    }
    for product in products:
        url = get_search_url(start_url, product["brand_name"], product["product_name"])
        res = requests.get(url, params=params)
        res.raise_for_status()
        mo = json_regex.search(res.text)
        js = json.loads(mo.group())
        if int(js["numberOfResults"]) > 0:
            res = js["resultsPanel"]["html"]
            soup = BeautifulSoup(res, "html.parser")
            #result = soup.select_one(".productlist-title").select_one("a").attrs
            result = soup.select(".productlist-title")
            results.append(result[0].select_one("a").attrs)
            for r in result[1:]:
                prod = r.select_one("a").attrs
                if " ".join([product["brand_name"], product["product_name"]]) in prod["title"]:
                    results.append(prod)
            #results.append(result)
        else:
            results.append({"href": None, "title": " ".join([product["brand_name"], product["product_name"]])})
    return results

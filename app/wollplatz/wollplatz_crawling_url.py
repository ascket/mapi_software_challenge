"""wollplatz.de search functions. Store search is organized using sooqr.com"""

import requests
from bs4 import BeautifulSoup
from typing import NamedTuple, List, Dict
import re
import json


def get_search_url(start_url: str, brand_name: str, product_name: str) -> str:
    """
    This function converts the start search URL to the desired format. The result is a URL that can be used further to get search results

    Args:
        start_url: Start search url
        brand_name: Brand name from the search list of products
        product_name: Product name from the search list of products

    Returns:
        Converted url without account number
    """
    raw_brand_name = brand_name.strip().lower().replace(" ", "%20")
    raw_product_name = product_name.strip().lower().replace(" ", "%20")
    brand_product = "%20".join([raw_brand_name, raw_product_name])
    url = f"{start_url}?type=suggest&searchQuery={brand_product}"
    return url


def wollplatz_product_url(products_to_crawling: List[Dict[str, str]], start_url: str,
                          account: str) -> List[Dict[str, str]]:
    """
    This function is used to get the urls of products from the store search results. It gets crawling products information, joints it with the search query url, gets a page with search results for each product, strips the desired products information from this page and converts it to json format. Next, it finds the required URL addresses and adds them to the list

    Args:
        products_to_crawling: List of dictionaries with products for crawling
        start_url: URL of sooqr.com
        account: Account number of dynamic.sooqr

    Returns:
        List of URLs of products that were found as a result of a store search
    """
    json_regex = re.compile((r'{.*}'))
    results = []
    params = {
        "account": account
    }
    for product in products_to_crawling:
        url = get_search_url(start_url, product["brand_name"], product["product_name"])
        res = requests.get(url, params=params)
        res.raise_for_status()
        mo = json_regex.search(res.text)
        js = json.loads(mo.group())
        if int(js["numberOfResults"]) > 0:
            res = js["resultsPanel"]["html"]
            soup = BeautifulSoup(res, "html.parser")
            result = soup.select(".productlist-title")
            # If results are found, then we are guaranteed to take the first result
            results.append(result[0].select_one("a").attrs)

            # If more than one result is found, then we try to take the results that best match the search query. For example 'Rico Essentials Super' has more than one search result
            for r in result[1:]:
                prod = r.select_one("a").attrs
                if " ".join([product["brand_name"], product["product_name"]]) in prod["title"]:
                    results.append(prod)
        else:
            results.append({"href": None, "title": " ".join([product["brand_name"], product["product_name"]])})
    return results

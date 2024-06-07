import requests
from requests import Response
import json
from pythed.app.api import *

def search(cookies:list=[], **kwargs):
    check_cookies(cookies=cookies)
            
    endpoint: str = endpoints["search"]["value"]
    params: list = endpoints["search"]["params"]
    
    url: str = build_url(endpoint=endpoint, params=params, **kwargs)
        
    try:
        res: Response = requests.get(url=url, headers=headers, cookies=cookies)
        res.raise_for_status()

        data = res.json()
        
        return data
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
        
def similar_items(cookies:list=[], item_id: str=""):
    check_cookies(cookies=cookies)
    if item_id == "" or item_id == None:
        raise Exception("Error: item id was not given. ❌")
    
    endpoint: str = endpoints["similar_items"]["value"].replace("{id}", item_id)
    url: str = build_url(endpoint=endpoint)
        
    try:
        res: Response = requests.get(url=url, headers=headers, cookies=cookies)
        res.raise_for_status()

        data = res.json()
        
        return data
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")

def get_item_details(cookies: list=[], item_id: str=""):
    check_cookies(cookies=cookies)
    if item_id == "" or item_id == None:
        raise Exception("Error: item id was not given. ❌")
    
    try:
        if item_id:
            endpoint = endpoints["item_details"]["value"].replace("{id}", item_id)    
            url = build_url(endpoint=endpoint)
            
            res: Response = requests.get(url=url, headers=headers, cookies=cookies)
            res.raise_for_status()

            data = res.json()
            
            return data["item"]
        else:
            raise Exception("No item id was given. ❌")
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
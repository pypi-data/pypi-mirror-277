import requests
from requests import Response
import json
from pythed.app.api import *

def get_shipping_details(cookies:list=[], **kwargs):
    check_cookies(cookies=cookies)
    
    item_id = kwargs.get("item_id")
            
    try:
        if item_id:
            endpoint = endpoints["shipping_details"]["value"].replace("{id}", item_id)    
            url = build_url(endpoint=endpoint)
            
            res: Response = requests.get(url=url, headers=headers, cookies=cookies)
            res.raise_for_status()

            data = res.json()
            
            return data
        else:
            raise Exception("No item id was given. ❌")
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
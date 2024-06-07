import requests
from requests import Response
import json
from pythed.app.api import *

def get_user_info(cookies:list=[], **kwargs):
    check_cookies(cookies=cookies)
        
    try:
        user_id = kwargs.get("user_id")
    
        endpoint: str = endpoints["user_info"]["value"].replace("{user_id}", user_id)
    
        if user_id:
            url: str = build_url(endpoint=endpoint)
            
            res: Response = requests.get(url=url, headers=headers, cookies=cookies)
            res.raise_for_status()

            data = res.json()
            
            return data
        else:
            raise Exception("No user id was given. ❌")
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
    
def get_user_reviews(cookies:list = [], **kwargs):
    check_cookies(cookies=cookies)
    args = check_params(**kwargs)
        
    try:
        user_id = kwargs.get("user_id")
    
        endpoint: str = endpoints["user_reviews"]["value"]
        params: list = endpoints["user_reviews"]["params"]
    
        if user_id:
            url: str = build_url(endpoint=endpoint, params=params, **args)
            
            res: Response = requests.get(url=url, headers=headers, cookies=cookies)
            res.raise_for_status()

            data = res.json()
            
            return data
        else:
            raise Exception("No user id was given. ❌")
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
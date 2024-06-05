from src.app.utils import config_functions

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}

endpoints = config_functions.read_json("src/app/config/endpoints.json")
BASE_URL = endpoints["BASE_URL"]
endpoints = endpoints["endpoints"]

def build_url(endpoint: str, params: list = [], **kwargs) -> str:
    url = f"{BASE_URL}{endpoint}?"
    for param in params:
        if param in kwargs:
            url += f"{param}={kwargs[param]}&"
    return url.rstrip('&')

def check_cookies(cookies:list=[]):
    if len(cookies) == 0 or cookies == None:
        raise Exception("Error: cookies were not given. ❌")
    
def check_params(**kwargs):
    newArgs = {}
    
    for key, value in kwargs.items():
        if value != None:
            newArgs[key] = value
            
    return newArgs
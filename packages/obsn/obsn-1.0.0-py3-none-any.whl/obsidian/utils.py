import requests, json
from plyer import notification

def gd(endpoint, **data):
    defaults = {
        'gameVersion': 22,
        'binaryVersion': 36,
        'secret': 'Wmfd2893gb7'
    }

    for key, value in defaults.items():
        data.setdefault(key, value)
    response = requests.post(f"https://www.boomlings.com/database/{endpoint}.php", headers={'User-Agent':''}, data=data)
    return response.text

def gd2json(response):
    parts = response.split('#')
    main_data = parts[0]
    extra_info = parts[1] if len(parts) > 1 else None
    
    results = main_data.split('|')
    
    parsed_results = []
    for result in results:
        items = result.split(':')
        parsed_result = {items[i]: items[i+1] for i in range(0, len(items), 2)}
        parsed_results.append(parsed_result)

    if extra_info:
        parsed_results[-1]['extraInfo'] = extra_info
    
    return parsed_results

def gdbrowser(endpoint, value, **kwargs):
    base = f"https://gdbrowser.com/api/{endpoint}/{value}"
    if kwargs:
        args = "&".join([f"{key}={value}" for key, value in kwargs.items()])
        url = f"{base}?{args}"
    else:
        url = base_url
    response = requests.get(url)
    return response.json()

def toast(title, content, timeout=3):
    notification.notify(title=title, message=content, timeout=timeout)
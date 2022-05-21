from typing import Set
import re

import requests

proxies = {
    'http': 'socks5://127.0.0.1:10808',
    'https': 'socks5://127.0.0.1:10808'
}

def extract_follow(url: str) -> Set[str]:
    results: Set[str] = set()
    follows_pattern = re.compile(r'''<span class="Link--secondary.*?">(.*?)</span>''')
    next_button_pattern = re.compile(r'''Previous</\w*?><a rel="nofollow" href="(https://github.com/.*?)">Next</a>''')
    res = requests.get(url, proxies=proxies)
    results.update(re.findall(follows_pattern, res.text))
    while (r := re.search(next_button_pattern, res.text)):
        res = requests.get(r.group(1), proxies=proxies)
        results.update(re.findall(follows_pattern, res.text))
    return results

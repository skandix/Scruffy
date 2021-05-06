import requests

domain="kongsberg.com"

_unique_domains = []
_alive_domains = []
url = f"https://crt.sh/json?q={domain}"
for domain in requests.get(url).json():
    for u_domain in domain["name_value"].rsplit():
        if u_domain not in _unique_domains and not(u_domain.startswith('*')):
            _unique_domains.append(u_domain)

for _domain in _unique_domains:
    _alive_domains.append(_domain)


count = 0
for k in _alive_domains:
    for j in k:
        count += 1

# print (count)


print ([x for x in _alive_domains])

import requests

sample_url="https://tfas.ir"
def check_headers(url):
    response=requests.get(url)
    headers=response.headers
    print(headers)

check_headers(sample_url)
import requests

response = requests.get("https://gist.githubusercontent.com/kimkitae/e85de2ee375ed44948c11e2e6d573234/raw/4990e9c81cd00cce1545ad5b0c57f01be2d6dc59/Monster.lib")
print(response.text)

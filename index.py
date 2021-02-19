from requests import get
x = get('https://api.github.com/repos/rishit-khandelwal/snippets/contents').json()
for file in filter(lambda _: True if _[-3:] == '.py' and _ != "index.py" else False, map(lambda _: _["download_url"], x)):
    print(file)

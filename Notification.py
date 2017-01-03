import requests, bs4
res = requests.get('https://www.reddit.com/r/buildapcsales/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
type(noStarchSoup)
newVariable = noStarchSoup.select('.title')
print (newVariable)

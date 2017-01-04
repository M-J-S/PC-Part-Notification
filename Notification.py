import requests, bs4 # import requests (allows HTTP requests) and import bs4 (beautifulsoup4, used for parsing HTML and XML files)

res = requests.get('https://www.reddit.com/r/buildapcsales/')           # returns a response object in a varaible named res
res.raise_for_status()                                                  # allows a bad request to be raised 
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")               # Python's html.parser
type(noStarchSoup)                                                      # next two lines will sort by p tag with class="title" in the original HTML document
newVariable = noStarchSoup.find_all("a", "title")
#newVariable.split(',')
for each in newVariable:
    if each.findNext("a", "title"):
        #print (newVariable.text)
        #print (location + 'test')
        print (newVariable)                                                 # prints all the title tags that are stored from the HTML document in the strinf newVariable
        print ('<br>')
        newVariable = each.findNext("a", "title")
    else:
        print ("done")


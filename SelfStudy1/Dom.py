from xml.dom import minidom
import datetime

dateNow = datetime.datetime.now()
doc = minidom.parse("dblp.xml")

def getNodeText(node):
    nodeList = []
    try:
        nodeList = node[0].childNodes
    except:
        pass
    result = []
    for node in nodeList:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

articles = doc.getElementsByTagName("article")

articleCount = len(articles)
print(articleCount)

articleInJournalCount = 0
for a in articles:
    if len(a.getElementsByTagName("journal")) > 0:
        articleInJournalCount += 1

print(articleInJournalCount)


articleInJournalInYear1990Count = 0

for a in articles:
    if len(a.getElementsByTagName("journal")) > 0:
        if getNodeText(a.getElementsByTagName("year")) == "1990":
            articleInJournalInYear1990Count += 1

print(articleInJournalInYear1990Count)

articleInWith7OrMoreAuthorsCount = 0

for a in articles:
    if len(a.getElementsByTagName("author")) > 7:
        articleInWith7OrMoreAuthorsCount += 1

print(articleInWith7OrMoreAuthorsCount)
print(datetime.datetime.now() - dateNow)
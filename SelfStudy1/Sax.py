import xml.sax
import datetime

class ArticleCounter(xml.sax.ContentHandler):
    count = 0
    def startElement(self, name, attrs):     
        if name == "article":
            self.count = self.count + 1
        
    def startDocument(self):
        self.count = 0

    def endDocument(self):
        print(self.count)

class ArticleInJournalCounter(xml.sax.ContentHandler):
    count = 0
    inArticle = False
    journalFound = False
    def startElement(self, name, attrs):     
        if name == "journal":
            if self.inArticle == True:
                self.journalFound = True
        if name == "article":
            self.inArticle = True  
    
    def startDocument(self):
        self.count = 0

    def endDocument(self):
        print(self.count)
    
    def endElement(self, name):
        if name == "article":
            if self.journalFound == True:
                self.count = self.count + 1
                self.journalFound = False


class ArticleInJournalDuring1990Counter(xml.sax.ContentHandler):
    count = 0
    inArticle = False
    journalFound = False
    yearFound = False
    yearText = ""
    def startElement(self, name, attrs):     
        if name == "journal":
            if self.inArticle == True:
                self.journalFound = True
        if name == "article":
            self.inArticle = True

        if name == "year":
            self.yearFound = True

    def characters(self, content):
        if self.yearFound == True:
            self.yearText += content
            
    def endElement(self, name):
        if name == "article":
            if self.yearText == "1990":
                self.count += 1
            self.yearText = ""
            self.inArticle = False
        if name == "year":
            self.yearFound = False
        if name == "journal":
            self.journalFound = False
    def startDocument(self):
        self.count = 0

    def endDocument(self):
        print(self.count)
    
class ArticleWithAuthorsCounter(xml.sax.ContentHandler):
    count = 0
    inArticle = False
    authorCounter = 0
    def startElement(self, name, attrs):     
        if name == "article":
            self.inArticle = True
        if name == "author":
            if self.inArticle == True:
                self.authorCounter = self.authorCounter + 1

    def endElement(self, name):
        if name == "article":
            self.inArticle = False
            if self.authorCounter > 7:
                self.count += 1
            self.authorCounter = 0
    def startDocument(self):
        self.count = 0

    def endDocument(self):
        print(self.count)

dateNow = datetime.datetime.now()
parser = xml.sax.make_parser()
parser.setContentHandler(ArticleCounter())
parser.parse(open("dblp.xml","r"))
parser.setContentHandler(ArticleInJournalCounter())
parser.parse(open("dblp.xml","r"))
parser.setContentHandler(ArticleInJournalDuring1990Counter())
parser.parse(open("dblp.xml","r"))
parser.setContentHandler(ArticleWithAuthorsCounter())
parser.parse(open("dblp.xml","r"))
print(datetime.datetime.now() - dateNow)
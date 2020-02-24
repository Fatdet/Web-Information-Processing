import xml.sax

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


class Article(xml.sax.ContentHandler):
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

parser = xml.sax.make_parser()
parser.setContentHandler(ArticleInJournalCounter())
parser.parse(open("dblp.xml","r"))


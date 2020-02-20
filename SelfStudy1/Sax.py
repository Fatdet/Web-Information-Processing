import xml.sax

class Parser(xml.sax.ContentHandler):
    hashTable = {}
    def startElement(self, name, attrs):      
        key = name
        if key in self.hashTable.keys():
            count = self.hashTable[key]
            self.hashTable[key] = count + 1
        else:
            self.hashTable[key] = 1
        

    
    def startDocument(self):
        self.hashTable = {}

    def endDocument(self):
        for k, v in self.hashTable.items():
            print(k, v)

parser = xml.sax.make_parser()
parser.setContentHandler(Parser())
parser.parse(open("dblp.xml","r"))


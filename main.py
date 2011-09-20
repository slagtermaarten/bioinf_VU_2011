import urllib2
import xml.sax
import xml.sax.handler

class PfamHandler(xml.sax.handler.ContentHandler):
  def __init__(self):
    self.inSeq = 0
    self.buffer = ''
    self.sequence = ''
 
  def startElement(self, name, attributes):
    if name == "sequence":
      self.inSeq = 1
 
  def characters(self, data):
    if self.inSeq:
      self.buffer += data
 
  def endElement(self, name):
    if name == "sequence":
      self.inSeq = 0
      self.sequence = self.buffer


protid = { 'EGR1' : 'P13653', 
           'Calmodulin' : 818,
       	   'ompF' : 945554,
           'secD' : 957363,
           'sopII' : 5953098
	   }

# http://www.ebi.ac.uk/QuickGO/GAnnotation?protein=P12345&format=tsv
# http://www.ebi.ac.uk/QuickGO/GAnnotation?protein=945554&format=tsv
def GO(id): 
    baseUrl = 'http://www.ebi.ac.uk/QuickGO/GAnnotation?protein='
    appendix = '&format=tsv'
    url = baseUrl + str(id) + appendix
    fh = urllib2.urlopen(url)
    result = fh.readlines()
    for x in result:
        array = x.split()
	print array[6], array[7], array[11]
    fh.close()

def Pfam(id):
    baseUrl = 'http://pfam.sanger.ac.uk/protein?output=xml&acc='
    url = baseUrl + str(id)
    fh = urllib2.urlopen(url)
    parser = xml.sax.make_parser()
    handler = PfamHandler()
    parser.setContentHandler(handler)
    parser.parse(fh)
    fh.close()
    return handler


def BLAST(sequence):
    baseUrl = 'http://'
    appendix = ''
    url = baseUrl + appendix
    fh = urllib2.urlopen(url)
    result = fh.readlines()
    for x in result:
        print x
    fh.close()

for id in protid.values():
    #print "======" +  + "======"  
    #GO(id)
    pfamEntry = Pfam(id)
    sequence = pfamEntry.sequence
    print sequence
    #SCOP(id)
    #BLAST(sequence)


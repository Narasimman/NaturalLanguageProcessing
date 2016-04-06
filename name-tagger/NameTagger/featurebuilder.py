from parseinput import *

class FeatureBuilder:
  def __init__(self, sentences):
    self.sentences = sentences
    self.readNameFile()
    self.locations = self.readLocationFile()


  def buildFeatureVector(self, outfilename):
    outfile = open(outfilename, "w+")
    for sentence in self.sentences:
      sentence = [('<s>', '<s>', '<s>', '<s>')] + sentence + [('</s>', '</s>', '</s>', '</s>')]
      if len(sentence) > 2:
        for i in range(1, len(sentence) - 1):
          prev = sentence[i - 1]
          curr = sentence[i]
          next = sentence[i + 1]
          feature = self.computeFeature(prev, curr, next)
          outfile.write(feature.strip() + "\n")
        outfile.write("\n")
    outfile.close()
  
  def readNameFile(self):
    namefile = open("names.txt", 'r')
    self.names = []
    for line in namefile:
      name = line.strip('\n').split()
      self.names.append(name[0].capitalize())

  def readLocationFile(self):
    locationfile = open("cities.txt", 'r')
    locations = []
    for line in locationfile:
      location = line.strip("\n").replace("'",'').replace("\r","").split(" ")
      locations.extend(location)
    return list(set(locations))

  def isCapitalWord(self, word):
    if word[0].isupper():
      return "true"
    else:
      return "false"

  def isHyphenated(self, word):
    if word.find("-"):
      return "true"
    else:
      return "false"

  def isUpperWord(self, word):
    if word.isupper():
      return "true"
    else:
      return "false"
  
  def isPrevComma(self, prevWord):
    if prevWord == ",":
      return "true"
    else:
      return "false"  

  def isPerson(self, curr):
    if curr in self.names:
      return "true"
    else:
      return "false"

  def isLocation(self, curr):
    if curr in self.locations:
      return "true"
    else:
      return "false"  

  def getFeatureValue(self, word):
    if len(word) == 0 or word == '<s>' or word == '</s>':
      return '@@'
    else:
      return word

  def computeFeature(self, prev, curr, next):
    tab = "\t"
    feature = curr[0] + tab

    if curr[0] == "-DOCSTART-":
      feature = "-DOCSTART-" + tab + "-X-" + tab + "O" + tab +"O"
      return feature

    if prev[0] == '<s>':
      feature += "firstword=true" + tab
    else:
      feature += "firstword=false" + tab

    #feature += "prevNP=" + self.getFeatureValue(prev[2]) + tab
    feature += "prevTag=" + self.getFeatureValue(prev[1]) + tab
    feature += "currTag=" + curr[1] + tab
    feature += "nextTag=" + self.getFeatureValue(next[1]) + tab
    feature += "prevWord=" + self.getFeatureValue(prev[0]) + tab
    feature += "currWord=" + curr[0] + tab
    feature += "nextWord=" + self.getFeatureValue(next[0]) + tab
    feature += "isCapitalized=" + self.isCapitalWord(curr[0]) + tab
    feature += "isHyphenated=" + self.isHyphenated(curr[0]) + tab
    feature += "isUpperWord=" + self.isUpperWord(curr[0]) + tab

    feature += "isPrevComma=" + self.isUpperWord(prev[0]) + tab
    feature += "isPerson=" + self.isUpperWord(curr[0]) + tab
    feature += "isLocation=" + self.isUpperWord(curr[0]) + tab

    if len(curr[3]) > 0:
      feature += curr[3]

    return feature


from parseinput import *

class FeatureBuilder:
  def __init__(self, sentences):
    self.sentences = sentences

  def buildFeatureVector(self, outfilename):
    outfile = open(outfilename, "w+")
    for sentence in self.sentences:
      sentence = [('<s>', '<s>', '<s>')] + sentence + [('</s>', '</s>', '</s>')]
      if len(sentence) > 2:
        for i in range(1, len(sentence) - 1):
          prev = sentence[i - 1]
          curr = sentence[i]
          next = sentence[i + 1]
          feature = self.computeFeature(prev, curr, next)
          outfile.write(feature + "\n")
        outfile.write("\n")

    outfile.close()

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

  def getFeatureValue(self, word):
    if len(word) == 0 or word == '<s>' or word == '</s>':
      return '@@'
    else:
      return word

  def computeFeature(self, prev, curr, next):
    tab = "\t"
    feature = curr[0] + tab

    if prev[0] == '<s>':
      feature += "firstword=true" + tab
    else:
      feature += "firstword=false" + tab

    feature += "prevNP=" + self.getFeatureValue(prev[2]) + tab
    feature += "prevTag=" + self.getFeatureValue(prev[1]) + tab
    feature += "currTag=" + curr[1] + tab
    feature += "nextTag=" + self.getFeatureValue(next[1]) + tab
    feature += "prevWord=" + self.getFeatureValue(prev[0]) + tab
    feature += "currWord=" + curr[0] + tab
    feature += "nextWord=" + self.getFeatureValue(next[0]) + tab
    feature += "isCapitalized=" + self.isCapitalWord(curr[0]) + tab
    feature += "isHyphenated=" + self.isHyphenated(curr[0]) + tab
    feature += "isUpperWord=" + self.isUpperWord(curr[0]) + tab

    if len(curr[2]) > 0:
      feature += curr[2]

    return feature


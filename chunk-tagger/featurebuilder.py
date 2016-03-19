from parseinput import *

class FeatureBuilder:
  def __init__(self, sentences):
    self.sentences = sentences

  def buildFeatureVector(self):
    outfile = open("test", "w+")
    for sentence in self.sentences:
      sentence = [('<s>', '<s>', '<s>')] + sentence + [('</s>', '</s>', '</s>')]
      if len(sentence) > 2:
        for i in range(1, len(sentence) - 1):
          prev = sentence[i - 1]
          curr = sentence[i]
          next = sentence[i + 1]
          feature = self.computeFeature(prev, curr, next)
          outfile.write(feature + "\n")

    outfile.close()

  def isCapitalWord(self, word):
    if word[0].isupper():
      return "true"
    else:
      return "false"

  def getFeatureValue(self, word):
    if word == '<s>' or word == '</s>':
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
    feature += "nextNP=" + self.getFeatureValue(next[2]) + tab    
    feature += "prevTag=" + self.getFeatureValue(prev[1]) + tab
    feature += "currTag=" + curr[1] + tab
    feature += "nextTag=" + self.getFeatureValue(next[1]) + tab
    feature += "prevWord=" + prev[0] + tab
    feature += "currWord=" + curr[0] + tab
    feature += "nextWord=" + next[0] + tab
    feature += "isCapitalized=" + self.isCapitalWord(curr[0]) + tab
    feature += curr[2]
    return feature

if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("WSJ_CHUNK_CORPUS_FOR_STUDENTS/WSJ_02-21.pos-chunk")

  fb = FeatureBuilder(sentences)
  fb.buildFeatureVector()

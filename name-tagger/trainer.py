from parseinput import *
from featurebuilder import *

def readTestCorpus(filepath):
  sentences = []
  sentence  = []
  tData = open(filepath, 'r')
  
  for line in tData:
    line = line.strip()
    if len(line) == 0:
      if len(sentence) > 0:
        sentences.append(sentence)
        sentence = []
    else:
      pair = line.split("\t")
      word = pair[0]
      tag = pair[1]
      nptag = pair[2]
      if len(word) > 0 and len(tag) > 0 and len(nptag):
        sentence.append((word,tag,nptag))
  if len(sentence) > 0:
    sentences.append(sentence)
  tData.close()
  return sentences


if __name__ == "__main__":
  sentences = readTrainingData("CONLL_NAME_CORPUS_FOR_STUDENTS/CONLL_train.pos-chunk-name")

  fb = FeatureBuilder(sentences)
  fb.buildFeatureVector("CONLL_train.feature")

  sentences = readTestCorpus("CONLL_NAME_CORPUS_FOR_STUDENTS/CONLL_dev.pos-chunk")
  
  fb = FeatureBuilder(sentences)
  fb.buildFeatureVector("CONLL_dev.feature")

  

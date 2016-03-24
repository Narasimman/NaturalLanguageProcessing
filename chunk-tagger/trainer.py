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
      if len(word) > 0 and len(tag) > 0:
        sentence.append((word,tag,""))
  if len(sentence) > 0:
    sentences.append(sentence)
  tData.close()
  return sentences


if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("WSJ_CHUNK_CORPUS_FOR_STUDENTS/WSJ_02-21.pos-chunk")

  fb = FeatureBuilder(sentences)
  fb.buildFeatureVector("WSJ_02-21.feature")

  sentences = readTestCorpus("WSJ_CHUNK_CORPUS_FOR_STUDENTS/WSJ_23.pos")
  
  fb = FeatureBuilder(sentences)
  fb.buildFeatureVector("WSJ_23.feature")

  

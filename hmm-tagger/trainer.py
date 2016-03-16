from parseinput import *
from viterbi import *


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
      word = line
      if len(word) > 0:
        sentence.append(word)
  if len(sentence) > 0:
    sentences.append(sentence)
  tData.close()
  return sentences


if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_02-21.pos")
  model = Viterbi(lexicon, tags)
  model.getCounts(sentences)
  model.calculateProb()

  sentences = readTestCorpus("WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_23.words")
  
  outfile = open("WSJ_23.pos", 'w+')

  for sentence in sentences:
    result = model.decode(sentence)
    for pair in result:
      outfile.write(pair[0] + "\t" + pair[1] + "\n")
    outfile.write("\n")  

  outfile.close()    
  

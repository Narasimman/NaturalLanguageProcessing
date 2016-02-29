from parseinput import *
from viterbi import *

#_re_nonAlpha = re.compile("[^A-Za-z0-9_/ \t]")

def readTestCorpus(filepath):
  sentences = []
  sentence  = []
  tData = open(filepath, 'r')
  
  for line in tData:
    line.strip()
    line.lower()
    if len(line.strip()) == 0:
      if len(sentence) > 0:
        sentences.append(sentence)
        sentence = []
    else:
      #line = _re_nonAlpha.sub("", line)
      word = line.strip()
      if len(word) > 0:
        sentence.append(word)
  if len(sentence) > 0:
    sentences.append(sentence)
  tData.close()
  return sentences


if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("data/WSJ_02-21.pos")
  model = Viterbi(lexicon, tags)
  model.getCounts(sentences)
  model.calculateProb()

  sentences = readTestCorpus("data/WSJ_24.words")
  
  outfile = open("WSJ_24.pos", 'rw')

  for sentence in sentences:
    result = model.decode(sentence)
    for pair in result:
      outfile.write(pair[0] + "\t" + pair[1] + "\n")
    outfile.write("\n")  

  outfile.close()    
  

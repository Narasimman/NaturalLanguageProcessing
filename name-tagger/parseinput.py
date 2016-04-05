import re

def readTrainingData(filepath):
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
      if len(pair) == 4:
        word = pair[0].strip()
        pos  = pair[1].strip()
        nptag = pair[2].strip()
        name = pair[3].strip()
        
        if(len(word) > 0 and len(pos) > 0 and len(nptag) > 0 and len(name)):
          sentence.append((word,pos,nptag,name))
  if len(sentence) > 0:
    sentences.append(sentence)

  tData.close()
  return sentences


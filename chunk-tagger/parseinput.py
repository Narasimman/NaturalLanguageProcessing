import re

def readTrainingData(filepath):
  sentences = []
  lexicon   = {}
  tags      = {}
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
      if len(pair) == 3:
        word = pair[0].strip()
        pos  = pair[1].strip()
        nptag = pair[2].strip()
        
        if(len(word) > 0 and len(pos) > 0 and len(nptag) > 0):
          lexicon[word] = 0
          tags[pos] = 0
          sentence.append((word,pos,nptag))
  if len(sentence) > 0:
    sentences.append(sentence)

  tData.close()
  return sentences, lexicon.keys(),tags.keys()

if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("WSJ_CHUNK_CORPUS_FOR_STUDENTS/WSJ_02-21.pos-chunk")
  print sentences[0]

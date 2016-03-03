import re

#_re_nonAlpha = re.compile("[^A-Za-z0-9_/ \t]")

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
      #line = _re_nonAlpha.sub("", line)
      pair = line.split("\t")
      if len(pair) == 2:
        word = pair[0].strip()
        pos  = pair[1].strip()
        
        if(len(word) > 0 and len(pos) > 0):
          lexicon[word] = 0
          tags[pos] = 0
          sentence.append((word,pos))
  if len(sentence) > 0:
    sentences.append(sentence)

  tData.close()
  return sentences, lexicon.keys(),tags.keys()

if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("data/WSJ_02-21.pos")
  print tags

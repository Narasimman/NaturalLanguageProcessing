import re

_re_nonAlpha = re.compile("[^A-Za-z0-9_/ \t]")

def readTrainingData(filepath):
  sentences = []
  lexicon   = {}
  tags      = {}
  sentence  = []
  tData = open(filepath)
  for line in tData:

    line = _re_nonAlpha.sub("", line)
    
    line.strip()
    line.lower()
    if len(line.strip()) == 0:
      if len(sentence) > 0:
        sentences.append(sentence)
      sentence = []   
    else:
      pair = line.split("\t")
      if len(pair) == 2:
        word = pair[0].strip()
        pos  = pair[1].strip()

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

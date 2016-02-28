from parseinput import *
from collections import defaultdict

class Viterbi:
  def __init__(self, lexicon, tags):
    self.tags = ['<START>', '</START>'] + tags
    self.trans_count = []
    self.emit_count  = {}
    self.tag_index = {}

    i = 0
    for tag in self.tags:
      self.tag_index[tag] = i
      i = i + 1
    for tag in self.tags:
      self.trans_count.append([0] * len(self.tags))
      self.emit_count[self.tag_index[tag]] = dict()

  def calc_p(self, sentences):
    for sentence in sentences:
      prev = self.tag_index['<START>']
      for pair in sentence:
        word = pair[0]
        state  = self.tag_index[pair[1]]
        self.trans_count[prev][state] += 1
        
        counter = 0
        
        d = self.emit_count[state];
        d[word] = d.get(word, 0) + 1

        prev = state

if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("data/WSJ_02-21.pos")
  model = Viterbi(lexicon, tags)
  model.calc_p(sentences)
  print len(model.trans_count)

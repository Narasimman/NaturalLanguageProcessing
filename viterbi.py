from parseinput import *
from collections import defaultdict
import numpy as np

class Viterbi:
  def __init__(self, lexicon, tags):
    self.tags = ['<START>', '</START>'] + tags #adding start and end tags
    self.trans_count = [] #count of arcs from s0 to s1
    self.emit_count  = {} #count of emission of words in state s1
    self.state_count = [0]*len(self.tags) #count of words in state s
    self.tag_index = {}

    self.tp = []
    self.ep = {}

    i = 0
    for tag in self.tags:
      self.tag_index[tag] = i
      i = i + 1
    
    #initialize the transition matrix
    for tag in self.tags:
      self.trans_count.append([0] * len(self.tags))
      self.emit_count[self.tag_index[tag]] = dict()

      self.tp.append([0] * len(self.tags))
      self.ep[self.tag_index[tag]] = dict()

  #calculate the counts for all states and words(useful to calculate tp and ep)
  def getCounts(self, sentences):
    for sentence in sentences:
      prev = self.tag_index['<START>']
      self.state_count[prev] += 1
      for pair in sentence:
        word = pair[0]
        state  = self.tag_index[pair[1]]
        self.trans_count[prev][state] += 1
        
        d = self.emit_count[state];
        self.emit_count[state][word] = d.get(word, 0) + 1
        self.state_count[state] += 1
        prev = state

  def calculateProb(self):
    for i in range(len(self.trans_count)):
      for j in range(len(self.trans_count[i])):
        try:
          self.tp[i][j] = float(self.trans_count[i][j])/float(self.state_count[i])
        except:
          self.tp[i][j] = 0.0001

    for i in range(len(self.emit_count)):
      for word in self.emit_count[i].keys():
        try:
          self.ep[i][word] = float(self.emit_count[i][word])/float(self.state_count[i])
        except:
          self.ep[i][word] = 0.0001

  def decode(self, sentence):
    N = len(sentence)
    T = len(self.tags)

    #viterbi table
    vt = np.zeros((N,T))

    start = self.tag_index['<START>']
    for tag in self.tags:
      ti = self.tag_index[tag]
      try:
        vt[0][ti] = self.tp[start][ti] * self.ep[ti][sentence[0]]
      except:
        vt[0][ti] = 0.0001

    for i in xrange(1, N):
      for tag in self.tags:
        tag_id  = self.tag_index[tag]
        prev_vt = {}
        for prev in self.tags:
          prev_id = self.tag_index[prev]
          prev_vt[(i-1, prev)] = vt[i-1][prev_id] * self.tp[prev_id][tag_id]
        try:
          vt[i][tag_id] = max(prev_vt.values()) * self.ep[tag_id][sentence[i]]
        except:
          vt[i][tag_id] = 0.0001

    print vt

if __name__ == "__main__":
  sentences, lexicon, tags = readTrainingData("data/WSJ_02-21.pos")
  model = Viterbi(lexicon, tags)
  model.getCounts(sentences)
  model.calculateProb()
  model.decode(['the','most','troublesome','report','may','be','','the','August','merchandise','trade','deficit','due','out','tomorrow'])

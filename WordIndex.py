#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineNum = 0
  words = {} #create an empty dictionary
  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w.replace("," "")
      w.replace("." "")
      w.replace("!" "")

      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w] = [lineNum]
  for word in words:
    print(word, words[word])
if __name__ == '__main__':
  main()

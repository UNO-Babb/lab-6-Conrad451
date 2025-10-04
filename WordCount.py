#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  while True:
    filename = input("Enter a File Name: ")
    try:
      textFile = open(filename, 'r')
      break
    except FileNotFoundError:
      print(f"File {filename} not found.")


  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount = lineCount +1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      letters = len(w)
      letterCount += letters
    #print(line)
  print()
  print("Lines: " + str(lineCount))
  print("Words: " + str(wordCount))
  print("Characters: " + str(letterCount))

if __name__ == '__main__':
  main()

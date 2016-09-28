word = open('words.txt')

def words(word):
    wordCount = 0
    lineCount = 0
    for line in word:
        if line.find('e') == -1:
            print line
            wordCount += 1
        lineCount += 1
    percent  = (float(wordCount) / float(lineCount)) * 100.0
    print percent, '%'

words(word)

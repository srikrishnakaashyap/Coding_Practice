# from ctypes import BigEndianStructure
from collections import deque


class WordLadder:
    def wordLadder(self, beginWord, endWord, wordList):

        wordMap = {}

        for word in wordList:
            wordMap[word] = 0

        if endWord not in wordMap:
            return False

        characterArray = [set() for i in range(len(beginWord))]

        for word in wordList:
            for index, character in enumerate(word):
                characterArray[index].add(character)

        queue = deque()

        queue.append(beginWord)

        for character in len(beginWord):
            


if __name__ == "__main__":

    wl = WordLadder()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(wl.wordLadder(beginWord, endWord, wordList))

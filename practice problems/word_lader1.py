from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        wordSet = set(wordList)
        if targetWord not in wordSet:
            return 0
        q = deque([(startWord, 1)])
        wordLength = len(startWord)
        while q:
            currentWord, level = q.popleft()
            if currentWord == targetWord:
                return level
            for i in range(wordLength):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord = currentWord[:i] + char + currentWord[i + 1:]
                    if newWord in wordSet:
                        q.append((newWord, level + 1))
                        wordSet.remove(newWord)
        return 0
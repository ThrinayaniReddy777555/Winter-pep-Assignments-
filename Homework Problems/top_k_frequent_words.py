import collections
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words) 

        unique_words = list(count.keys())
        unique_words.sort(key=lambda word: (-count[word], word)) 

        return unique_words[:k]

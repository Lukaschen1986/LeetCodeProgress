# -*- coding: utf-8 -*-
from collections import (defaultdict, deque)

def ladderLength(beginWord: str, endWord: str, wordList: list) -> int:
    if endWord not in wordList:
        return 0
    
    dct = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            dct[word[0:i] + "*" + word[i+1:]].append(word)
    
    visited = {beginWord}
    queue = deque([(beginWord, 1)])

    while queue:
        word, depth = queue.popleft()

        for i in range(len(word)):
            key = word[0:i] + "*" + word[i+1:]

            for v in dct[key]:
                if v == endWord:
                    return depth + 1
                else:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, depth+1))
    
    return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    ladderLength(beginWord, endWord, wordList)

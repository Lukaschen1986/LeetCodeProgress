# -*- coding: utf-8 -*-
from collections import (defaultdict, deque)

def ladderPath(beginWord: str, endWord: str, wordList: list) -> int:
    if endWord not in wordList:
        return 0
    
    dct = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            dct[word[0:i] + "*" + word[i+1:]].append(word)
    
    visited = {beginWord}
    queue = deque([beginWord])
    path = {beginWord: None}
    
    while queue:
        word = queue.popleft()
        
        for i in range(len(word)):
            key = word[0:i] + "*" + word[i+1:]
            
            for v in dct[key]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
                    path[v] = word
    
    lst_path = []
    while endWord:
        lst_path.append(endWord)
        endWord = path[endWord]

    return " -> ".join(lst_path[::-1])


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

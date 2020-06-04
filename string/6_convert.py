# -*- coding: utf-8 -*-
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    
    layers = ["" for _ in range(numRows)]
    i = 0
    flag = -1

    for x in s:
        layers[i] += x
        if (i == 0) or (i == numRows-1):
            flag = -flag
        i += flag
    
    return "".join(layers)
    

if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    numRows = 3
    convert(s, numRows)

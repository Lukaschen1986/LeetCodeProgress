# -*- coding: utf-8 -*-
def isValid(s: str) -> bool:
    if len(s) == 1:
        return False
    
    dct = {")":"(", "]":"[", "}":"{"}
    stack = ["?"]
    
    for x in s:
        if x in ["(", "[", "{"]:
            stack.append(x)
        else:
            y = stack.pop()
            if dct[x] != y:
                return False
    
    if len(stack) > 1:
        return False
    
    return True
        
    
if __name__ == "__main__":
    s = "()[]{}"
    s = "([)]"
    s = "{"
    s = "(("
    isValid(s)

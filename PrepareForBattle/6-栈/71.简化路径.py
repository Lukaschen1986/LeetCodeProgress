# -*- coding: utf-8 -*-
def simplifyPath(path: str) -> str:
    lst = path.split("/")
    stack = []

    for s in lst:
        if s in [".", ""]:
            continue
        elif s == "..":
            if stack:  # 神来之笔
                stack.pop()
        else:
            stack.append(s)

    res = "/" + "/".join(stack)
    return res



if __name__ == "__main__":
    # path = "/a/./b/../../c/"
    # path = "/a/./b/././c/"
    # path = "/home/"
    # path = "/../"
    # path = "/home//foo/"
    path = "/a//b////c/d//././/.."
    res = simplifyPath(path)
    print(res)

# -*- coding: utf-8 -*-
import re


def reverseWords(s: str) -> str:
    s = s.strip()
    re_compile = re.compile(r"[ ]+")
    x = re_compile.sub(".", s)
    lst = x.split(".")[::-1]
    return " ".join(lst)


if __name__ == "__main__":
    s = "  Bob    Loves  Alice   "

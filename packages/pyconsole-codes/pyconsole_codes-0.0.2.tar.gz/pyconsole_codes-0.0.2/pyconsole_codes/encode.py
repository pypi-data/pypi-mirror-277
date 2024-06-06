from typing import Any


def encode(word:list[str|Any])->str:
    words = []
    for i in word:
        if type(i)==str:
            words.append(i)
        else:
            words.append(i.encode().decode("utf-8"))
    # print(words)
    return "".join(words)

import re

def tokenize(expression: str) -> list[str]:
    ops = ["and", "or", "not", "(", ")"]
    expression = re.split('(\s+|\(|\))', expression)
    expression = [el for el in expression if el != '' and not el.isspace()]
    stack = []
    newexpr = []
    for el in expression:
        if el in ops:
            if stack:
                newexpr += ["".join(stack)]
                stack = []
            newexpr += [el]
        else:
            stack += el
    
    return newexpr




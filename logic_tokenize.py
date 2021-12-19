import re
import logging as log
def logic_tokenize(expression: str) -> list[str]:
    ops = ["and", "or", "not", "(", ")"]
    expression = re.split('(\s+|\(|\))', expression)
    expression = [el for el in expression if el and not el.isspace()]
    stack = []
    result = []
    for el in expression:
        if el in ops:
            if stack:
                result += ["".join(stack)]
                stack = []
            result += [el]
        else:
            stack += el
    if stack:
        result.append(*stack)
    result = apply_brackets(result)
    return result


def apply_brackets(token_list : list[str or list]) -> list[str or list]:
    """ This is just a wrapper for the recurrency function which changes string brackets into complex structure"""
    def recurrency(token_list : list[str or list]) -> list[str or list]:
        stack = []
        while token_list:
            token = token_list.pop()
            if token == '(':
                stack.append(recurrency(token_list))
            elif token == ')':
                return stack
            else:
                stack.append(token)
        return stack

    token_list.reverse()
    return recurrency(token_list)
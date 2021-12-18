

ops = {
        "and" : 30,
        "or": 20,
        "not" : 10,
        }

def op_pred(op : str) -> int:
    global ops
    try:
        return ops[op]
    except ValueError:
        print("Not an operator supplied to opeator precedence")
        return 0

"""
    Nie działa not na nawiasie
"""
def postfix(expression: list[str]):
    global ops
    specials = ops.keys()
    stack = []
    end = []
    for el in expression.copy():
        if el not in specials:
            end += [el] 
        elif el == "(":
            stack += [el]
        elif el == ")":
            topToken = stack.pop()
            while topToken != '(':
                end.append(topToken)
                topToken = stack.pop()
        else:
            while stack and op_pred(stack[-1]) >= op_pred(el):
                end.append(stack.pop())
            stack += [el]
    return end
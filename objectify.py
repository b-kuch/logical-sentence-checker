import operators as ops
import logging as log

constructors = {
    'and' : ops.And,
    'or' : ops.Or,
}

operators = constructors.keys()

precedence = {
        "and" : 30,
        "or": 20,
        }
    
def objectify(token_list: list[str or list]) -> ops.Operator:
    if not isinstance(token_list, list):
        log.debug(f'token_list is not a list <{token_list}>')
        token_list = [token_list]

    result = None

    token_list.reverse()
    while token_list:
        token = token_list.pop()
        if isinstance(token, list):
            result = objectify(token)
        elif token == 'not':
            result = ops.Not(
                    objectify(token_list.pop()))
        elif token in operators:
            result = constructors[token](
                result, objectify(token_list.pop()))
        else:
            result = ops.Operand(token)

    return result

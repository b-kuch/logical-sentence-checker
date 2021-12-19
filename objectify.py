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
    

def objectify(token_list: list[str or list], counter) -> ops.Operator:
    if not isinstance(token_list, list):
        log.debug(f'token_list is not a list <{token_list}>')
        token_list = [token_list]

    result = None

    token_list.reverse()
    while token_list:
        token = token_list.pop()
        if isinstance(token, list):
            result = objectify(token, counter)
        elif token == 'not':
            result = ops.Not(
                    objectify(token_list.pop(), counter))
        elif token in operators:
            result = constructors[token](
                result, objectify(token_list.pop(), counter))
        else:
            result = create_operand(token, counter)

    return result


def create_operand(token, sentence=None):
    new_operand = ops.Operand(token)
    if sentence:
        sentence.add_variable(new_operand)
    return new_operand


def objectify_wrapper(token_list):
    sentence = Sentence()

    sentence.sentence = objectify(token_list, sentence)

    return sentence


class Sentence():
    def __init__(self) -> None:
        self.variables = set()
        self.sentence : ops.Operator
    
    def add_variable(self, variable):
        self.variables.add(variable)
        
    def __str__(self) -> str:
        return str(self.sentence)

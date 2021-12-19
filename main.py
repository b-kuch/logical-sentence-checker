import logging as log
from os import stat

def get_logical(s):
    return objectify_wrapper(logic_tokenize(s))

def my_bool(arg):
    return isinstance(arg, str) and arg.lower() in ['y', 'yes', 'true', 't']


if __name__=='__main__':
    log.basicConfig(level=log.INFO)
    from logic_tokenize import logic_tokenize
    from objectify import objectify, objectify_wrapper
    statement = \
    """cancelDate != null or cancelDate <= effectiveDate 
    and perm.xd 
    and (not( (typekey == dupa or typekey==pupa) and policyperiod.Date == effectiveDate))"""
    statement = "x or y and z"
    statement = get_logical(statement)
    log.info(repr(statement.sentence))
    log.info(statement)
    vars = [var.value for var in statement.variables]
    vars_values = {var: my_bool(input(f'{var} = ')) for var in vars}
    print(statement.sentence.decide(vars_values))


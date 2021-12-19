import logging as log
from os import stat

def get_logical(s):
    return objectify(logic_tokenize(s))

if __name__=='__main__':
    log.basicConfig(level=log.DEBUG)
    from logic_tokenize import logic_tokenize
    from objectify import objectify
    statement = \
    """cancelDate != null or cancelDate <= effectiveDate 
    and perm.xd 
    and (not( (typekey == dupa or typekey==pupa) and policyperiod.Date == effectiveDate))"""
    statement = "x or y and z"
    statement = get_logical(statement)
    log.info(repr(statement))
    log.info(statement)


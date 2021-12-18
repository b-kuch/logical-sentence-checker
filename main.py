

if __name__=='__main__':
    from tokenize import tokenize
    from postfix import postfix
    statement = "cancelDate != null or cancelDate <= effectiveDate and perm.xd and (not( (typekey == dupa or typekey==pupa) and policyperiod.Date == effectiveDate))"
    statement = tokenize(statement)
    print(statement)
    statement = postfix(statement)
    print(statement)
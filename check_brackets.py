def check_brackets(line):
    left = '({['
    right = ')}]'
    
    S = stack()
    
    for word in line:
        if word in left:
            S.push(word)
        elif word in right:
            if S.isEmpty():
                return False
            if right.index(word) != left.index(S.pop()):
                return False
    return S.isEmpty()
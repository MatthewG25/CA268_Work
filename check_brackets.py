def check_brackets(line):
    left = '({['
    right = ')}]'
    
    left_stack = stack()
    right_stack = stack()
    
    for word in line:
        if word in left:
            left_stack.push(word)
        elif word in right:
            right_stack.push(word)
    if len(left_stack) == len(right_stack):
        return True
    else:
        return False
    
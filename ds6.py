#stack
#valid parentheses
# ()->valid
# {}->valid
# (}->invalid
# ((->invalid
# }}->invalid
#{()}-->valid
#{(})-->invaild
#{()}}-->invalid

# l=[1,30,100,55,70]
# x=max(l)
# print(l.index(x))

#evaluate expression:
#postfix:5 9 +
#prefix:+ 5 9
#infix:5+9


def postfix(s):
    stack=[]
    for char in s:
        if char.isdigit():
            stack.append(int(char))
        else:
            b=stack.pop()
            a=stack.pop()
            if char=='+':
                stack.append(a+b)
            elif char=='-':
                stack.append(a-b)
            elif char=='*':
                stack.append(a*b)
            elif char=='/':
                stack.append(a/b)
    return stack.pop()
s="23+5*"
result=postfix(s)
print(result)
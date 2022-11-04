while True:

    arr = str(input())

    if (arr == '.'):
        break
    else:

        stk = []
        tmp = True
        for s in arr:
            if s=='('or s=='[':
                stk.append(s)
            elif s==')':
                if not stk or stk[-1]=='[':
                    tmp=False
                    break
                elif stk[-1]=='(':
                    stk.pop()
            elif s==']':
                if not stk or stk[-1]=='(':
                    tmp = False
                    break
                elif stk[-1]=='[':
                    stk.pop()
        if tmp == True and not stk:
            print('yes')
        else:
            print('no')


def cheque(obj):
    a,b,c = 0,0,0
    for i in obj:
        if i == '{' or i =='}':
            a +=1
        elif i == '[' or i ==']':
            b +=1
        elif i == '(' or i ==')':
            c +=1
    if a%2 !=0 or b%2 !=0  or c%2 !=0:
        return False
    else:
        return True

print(cheque('{[{[(({[]})]]}]}'))
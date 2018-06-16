
n = int(input())

def answer(s):
    must = ['P', 'A', 'T']
    mark_P = None
    mark_T = None
    if 'P' not in s or 'T' not in s:
        return 'NO'
    for idx, each in enumerate(s):

        if each not in must:
            return 'NO'
        
        if each == 'P':
            if mark_P == None:
                mark_P = idx
            else:
                return 'NO'
        
        if each == 'T':
            if mark_T == None:
                mark_T = idx
            else:
                return 'NO'
    
    if mark_T - mark_P == 2:
        return 'YES'
    elif mark_T- mark_P < 2:
        return 'NO'
    elif mark_T - mark_P > 2:
        if mark_P == 0:
            return 'YES'
        else:
            count = mark_T - mark_P - 2
            count_after_T = len(s) - mark_T - 1
            if (count + 1) * mark_P == count_after_T:
                return 'YES'
            else:
                return 'NO'

if n == 0:
    exit()
for i in range(n):
    seq = input()
    print(answer(seq))

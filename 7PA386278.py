from collections import deque
def abstand(s, t, dateiname='dat.py'):
    dat = open(dateiname,'r')

    L = []
    Q = deque([])
    for l in dat:
        a = list(l)
        a.pop()
        L.append(a)                                #Matrix                                           
                                            
    if L[s[0]][s[1]] == 'P':                        
        Q.append((s[0], s[1]))
        L[s[0]][s[1]] = 0
        
    else:
        return -1

    i, j = s
    x, y = t
            
    while len(Q):                                   #waehrend wir den endpunkt nicht erreicht haben
        i,j = Q.popleft()                           
        if (i, j) == t:
            for q in L:
                print(q)
            return L[x][y]
        
        if  j > 0 and L[i][j - 1] == 'P':
            Q.append((i, j - 1))
            L[i][j - 1] = L[i][j] + 1               #set it equal to LENGTH

        if j < (len(a) - 1) and L[i][j + 1] == 'P':
            Q.append((i, j + 1))
            L[i][j + 1] = L[i][j] + 1

        if i > 0 and L[i - 1][j] == 'P':
            Q.append((i - 1, j))
            L[i - 1][j] = L[i][j] + 1

        if i < (len(L) - 1) and L[i + 1][j]== 'P':
            Q.append((i + 1, j))
            L[i + 1][j] = L[i][j] + 1

    if len(Q) == 0 and s != t:
        return -1

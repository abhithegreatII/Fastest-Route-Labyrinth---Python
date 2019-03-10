from PA9386278test import cmp, swp, L
""" Sortiert die gegebene Liste im Bezug zu cmp und swp. A ist
der Anfang der jeweiligen Teillisten."""

def quicksort(n, cmp, swp, A = 0):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        if not cmp(A, A + 1):
            swp(A + 1, A)
            return 1
        else:    
            return 1

#median of first three elements in list; left list first

    else:
        if cmp(A, A + 1):
            if cmp(A + 1, A + 2):                                       #0 < 1 < 2
                p = A + 1

            elif cmp(A + 2, A + 1):
                if cmp(A, A + 2):                                       #0 < 2 < 1
                    p = A + 2

                elif cmp(A + 2, A):                                     #2 < 0 < 1
                    p = A
                            
        elif cmp(A + 1, A):
            if cmp(A, A + 2):
                if cmp(A + 1, A + 2):                                   #1 < 0 < 2
                    p = A
                    
            elif cmp(A + 2, A):
                if cmp(A + 1, A + 2):                                   #1 < 2 < 0
                    p = A + 2
                    
                elif cmp(A + 2, A + 1):                                   #2 < 1 < 0
                    p = A + 1

#fuer quicksort 

        i, j = A + 1, A + (n-1)
        swp(A, p)
        p = A

        while i <= j:
            if i == j:
                if cmp(j, p):
                    break
                if not cmp(j, p):
                    j -= 1

            elif not cmp(i, p):
                if not cmp(p, j):           # i > p, j < p
                    swp(i, j)
                    i += 1
                    j -= 1

                elif cmp(p, j):             # i > p, j > p
                    j -= 1

            elif cmp(i, p):
                if not cmp(p, j):           # i < p, j < p
                    i += 1

                elif cmp(p, j):             # i < p, j > p
                    i += 1
                    j -= 1

#pivot an stelle i
        swp(j, p)

#rekursiv weiter mit teillisten
        quicksort(j-p, cmp, swp, A = p)
        quicksort(p + n - j -1, cmp, swp, A = j + 1)

    return 1, L

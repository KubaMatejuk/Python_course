def a(m,n):
    if m==0:
        return n+1
    if m>0:
        if n==0:
            return a(m-1,1)
        if n>0:
            return a(m-1,a(m,n-1))

print(a(3,4))
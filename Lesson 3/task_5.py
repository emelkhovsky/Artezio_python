def t():
    s=list(map(float,input().split()))
    n=list(map(abs,s))
    return s[n.index(min(n))]
print(t())
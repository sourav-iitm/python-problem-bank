def next_bigger(n):
    m=list(str(n))
    l=len(m)
    m.reverse()
    f=0
    for ll in range(l+1):
#        print(m[:ll])
        for i in range(ll):
            for j in range(i+1,ll):
                if m[i]>m[j]:
                    q=m[i]
                    m.pop(i)
                    p=sorted(m[:j], reverse=True)
                    m=p+[q]
                    if j+1<=l:
                        n=list(str(n))
                        n.reverse()
                        m=m+n[j+1:]
                    f=1
                    break
            if f==1:
                n.reverse()
                n="".join(n)
                n=int(n)
                break
        if f==1:
            break
    m.reverse()
    m="".join(m)
    m=int(m)
#    print(m,f)
    return (m if m>n else -1)
print(next_bigger(12))
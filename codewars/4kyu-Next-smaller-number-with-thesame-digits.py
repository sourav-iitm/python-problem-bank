def next_smaller(n):
    m=list(str(n))
    l=len(m)
    m.reverse()
    f=0
    for ll in range(l+1):
        for i in range(ll):
            for j in range(i+1,ll):
                if m[i]<m[j]:
                    q=m[i]
                    m.pop(i)
                    p=sorted(m[:j])
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
    if m[0]=="0":
        return -1
    m=int(m)
    return (m if m<n else -1)
a=[1,3,5,2,4,9,8]
a.sort()
b=a;b.sort()
print(a)
print(b)
#tabliczka mnozenia
cyfry=(0,1,2,3,4,5,6,7,8,9)
for a in cyfry:
    for b in cyfry:
        print('%s x %s =%s'% (a,b,a*b))

s=(input("Enter a expression:\n"))
print(s)
n=len(s)
a=s.find('+')
b=s.find('-')
c=s.find('*')
d=s.find('/')

#for ++ or -- or +- or-+

if c==-1 and d==-1:
    if b!=-1 and a!=-1:
        if a<b:
            f=int(s[0:a])
            sec=int(s[a+1:b])
            res1=f+sec
            f=int(s[b+1:n])
            res2=res1-f
            print(res2)
        else:
            f = int(s[0:b])
            sec = int(s[b + 1:a])
            res1 = f - sec
            f = int(s[a + 1:n])
            res2 = res1 + f
            print(res2)
    else:
        if(b==-1):
            t=s.split('+')
            res=int(t[0])+int(t[1])+int(t[2])
            print(res)
        else:
            t=s.split('-')
            res=int(t[0])-int(t[1])-int(t[2])
            print(res)
#for ** or */ or // or /*

elif a==-1 and b==-1:
    if c!=-1 and d!=-1:
        if c<d:
            f=int(s[0:c])
            sec=int(s[c+1:d])
            res1=f*sec
            f=int(s[d+1:n])
            res2=res1/f
            print(res2)
        else:
            f = int(s[0:d])
            sec = int(s[d + 1:c])
            res1 = f / sec
            f = int(s[c + 1:n])
            res2 = res1 * f
            print(res2)
    else:
        if(c!=-1):
            t=s.split('*')
            res=int(t[0])*int(t[1])*int(t[2])
            print(res)
        else:
            t=s.split('/')
            res=int(t[0])/int(t[1])/int(t[2])
            print(res)
#for +* or *+
elif b==-1 and d==-1:
    if a!=-1 and c!=-1:
        if a<c:
            f = int(s[a+1:c])
            sec = int(s[c + 1:n])
            res1 = f * sec
            f = int(s[0:a])
            res2 = res1 + f
            print(res2)
        else:
            f = int(s[0:c])
            sec = int(s[c + 1:a])
            res1 = f * sec
            f = int(s[a+1:n])
            res2 = res1 + f
            print(res2)
#for -/ or /-
elif a==-1 and c==-1:
    if b!=-1 and d!=-1:
        if b<d:
            f = int(s[b+1:d])
            sec = int(s[d + 1:n])
            res1 = f / sec
            f = int(s[0:b])
            res2 = f-res1
            print(res2)
        else:
            f = int(s[0:d])
            sec = int(s[d + 1:b])
            res1 = f / sec
            f = int(s[b+1:n])
            res2 = res1 - f
            print(res2)
#for *- or -*
elif a==-1 and d==-1:
    if b!=-1 and c!=-1:
        if b<c:
            f = int(s[b+1:c])
            sec = int(s[c + 1:n])
            res1 = f * sec
            f = int(s[0:b])
            res2 = f-res1
            print(res2)
        else:
            f = int(s[0:c])
            sec = int(s[c + 1:b])
            res1 = f * sec
            f = int(s[b+1:n])
            res2 = res1-f
            print(res2)
# for /+ or +/
elif b==-1 and c==-1:
    if a!=-1 and d!=-1:
        if a<d:
            f = int(s[a+1:d])
            sec = int(s[d + 1:n])
            res1 = f / sec
            f = int(s[0:a])
            res2 = res1 + f
            print(res2)
        else:
            f = int(s[0:d])
            sec = int(s[d + 1:a])
            res1 = f / sec
            f = int(s[a+1:n])
            res2 = res1 + f
            print(res2)

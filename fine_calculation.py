dd,mm,yy=list(map(int,input().split()))
d,m,y=list(map(int,input().split()))

if yy<y:
    hackos=0
elif y==yy:
    if mm<m:
        hackos=0
    elif mm==m:
        if dd<=d:
            hackos=0
        else:
            hackos=abs(dd-d)*15
    else:
        hackos=abs(m-mm)*500
else:
    hackos=10000
print(hackos)
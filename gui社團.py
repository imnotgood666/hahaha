a,b,c=map(int,input().split())
d=b*b-4*a*c
e,f=int((-b+d**(0.5))//(2*a)),int((-b-d**(0.5))//(2*a))
if d>0:
    print('Two different roots x1=%002d'%e,',x2=%d'%f)
elif d<0:
    print('No real root')
else:
    print("Two same roots x=int %d"%e)
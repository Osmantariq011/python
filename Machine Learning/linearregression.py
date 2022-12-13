import matplotlib
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,5,4,5]
sumx=sum(x)
sumy=sum(y)
sumsquarx=0
sumsquary=0
sumxy=0
for i in range(0,len(x)):
    sq=x[i]*x[i]
    sumsquarx=sumsquarx+sq
    print(sq)

for i in range(0,len(y)):
    sq=y[i]*y[i]
    sumsquary=sumsquary+sq
    print(sumsquary)   
for i in range(0,len(y)):
    sq=x[i]*y[i]
    sumxy=sumxy+sq
    print(sumxy) 
#sumsquarx=sum(x)
print(sumx,sumy,sumsquarx,sumsquary,sumxy)
m=((len(x)*sumxy)-(sumx*sumy))/((len(x)*sumsquarx)-(sumx*sumx))
c=((sumy*sumsquarx)-(sumx*sumxy))/((len(x)*sumsquarx)-(sumx*sumx))
print(m,c)
yprad=[]
for i in range(0,len(x)):
    yp=m*x[i]+c
    yprad.insert(i,yp)
print(yprad) 
plt.scatter(x, y, color='m', marker='o', s=30)
plt.plot(x, yprad)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
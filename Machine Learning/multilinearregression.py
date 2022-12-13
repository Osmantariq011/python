import matplotlib
import matplotlib.pyplot as plt
x_1=[60,62,67,70,71,72,75,78]
x_2=[22,25,24,20,15,14,14,11]
y=[140,155,159,179,192,200,212,215]
sumx_1=sum(x_1)
sumx_2=sum(x_2)
sumy=sum(y)
meanx_1=sumx_1/len(x_1)
meanx_2=sumx_2/len(x_2)
meany=sumy/len(y)
sumsquarx_1=0
sumsquarx_2=0
sumsquary=0
sumx_1y=0
sumx_2y=0
sumx_1x_2=0
for i in range(0,len(x_1)):
    sq=x_1[i]*x_1[i]
    sumsquarx_1=sumsquarx_1+sq
    print(sumsquarx_1)

for i in range(0,len(x_2)):
    sq=x_2[i]*x_2[i]
    sumsquarx_2=sumsquarx_2+sq
    print(sumsquarx_2)

for i in range(0,len(y)):
    sq=y[i]*y[i]
    sumsquary=sumsquary+sq
    print(sumsquary)   
for i in range(0,len(y)):
    sq=x_1[i]*y[i]
    sumx_1y=sumx_1y+sq
    print(sumx_1y) 

for i in range(0,len(y)):
    sq=x_2[i]*y[i]
    sumx_2y=sumx_2y+sq
    print(sumx_2y) 

for i in range(0,len(x_1)):
    sq=x_1[i]*x_2[i]
    sumx_1x_2=sumx_1x_2+sq
    print(sumx_1x_2)   
#sumsquarx=sum(x)
print(sumx_1,sumx_2,sumy,sumsquarx_1,sumsquarx_2,sumsquary,sumx_1y,sumx_2y,sumx_1x_2)
rsumsquarx_1=(sumsquarx_1)-((sumx_1*sumx_1)/len(y))
rsumsquarx_2=(sumsquarx_2)-((sumx_2*sumx_2)/len(y))
rsumx_1y=(sumx_1y)-((sumx_1*sumy)/len(y))
rsumx_2y=(sumx_2y)-((sumx_2*sumy)/len(y))
rsumx_1x_2=(sumx_1x_2)-((sumx_1*sumx_2)/len(y))
b1=((rsumsquarx_2*rsumx_1y)-(rsumx_1x_2*rsumx_2y))/((rsumsquarx_1*rsumsquarx_2)-(rsumx_1x_2*rsumx_1x_2))
b2=((rsumsquarx_1*rsumx_2y)-(rsumx_1x_2*rsumx_1y))/((rsumsquarx_1*rsumsquarx_2)-(rsumx_1x_2*rsumx_1x_2))
b0=meany-(b1*meanx_1)-(b2*meanx_2)
print(rsumsquarx_1,rsumsquarx_2,rsumx_1y,rsumx_2y,rsumx_1x_2)
print(b1,b2,b0,len(y))


yprad=[]
for i in range(0,len(x_2)):
    yp=b0+(b1*x_1[i])+(b2*x_2[i])
    yprad.insert(i,yp)
print(yprad) 
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(x_1, x_2, y, marker='o')
ax.plot(x_1,x_2, yprad)

ax.set_xlabel('X1 Label')
ax.set_ylabel('X2 Label')
ax.set_zlabel('Y Label')

plt.show()
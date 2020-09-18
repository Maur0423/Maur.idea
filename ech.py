def unp(arg):
    s=[]
    for i in arg:
        s+=[i]
    return s 

    def swaprow(M,i,j):
    x=unp(M[i,0:])
    y=unp(M[j,0:])
    for k,b in enumerate(y):
        M[i,k]=b
    for c,d in enumerate(x):
        M[j,c]=d
    return 

    import numpy as np
def ech(ma):
#Assign row and column dimension to (m,n)
     (m,n)= np.shape(ma)
#initialise some control variable
     d=-1
     b=m
#iterate over the matrix column
     for j in range(n):
       d= d+1
       b=b-1
       i=0
       if d>=m-1:
           break
#iterate over the matrix row to see if the entry pivot element meets the condition. 
#If it doesn't, swap with another row
       for s in range(b):
          if ma[d,j]==0 and ma[d+s+1,j]!=0:
             swaprow(ma,d,d+s+1)
             break
       if ma[d,j]==0 and ma[d+1,j]==0:
            d=d-1
            b=b+1
            continue
#iterate over the matrix row to reduce rows to echelon form
#the variable i was initialised in the first for loop.
#this is to ensure it is reduced to zero after each iteration.
       
    
       for k in range(b):
            i+=1
            c = ma[d+i,j]/ma[d,j]
            ma[d+i,0:]=(-c*ma[d,0:]+ma[d+i,0:])
       
     return(ma)
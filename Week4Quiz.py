#Question 1
import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
b=a[1:,1]
b

# qeustion 2
z=list(range(10))
large=z[0]
sorted_=[]
for i in range(1,len(z)):
    if large<z[i]:
        sorted_.append(z[i])
        large+=1
print(sorted_)


# qeustion 3
listings=list(range(1,20))
def max_min(listings:list)->list:
    maximum=listings[0]
    minimum=listings[0]
    for i in range(1,len(listings)):
        if maximum<listings[i]:
            maximum=listings[i]

        if minimum>listings[i]:
            minimum=listings[i]
    print(f'minimum number: {minimum}')
    print(f'maximum number: {maximum}')



# Question 7
def show_stars(rows: int):
    k=1
    for i in range(0,rows):
        for j in range(0,k):
            print("*", end=" ")
        k=k+1
        print()

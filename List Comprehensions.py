# List Comprehensions
# You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

#Sample Input
x = int(input())
y = int(input())
z = int(input())
n = int(input())

#Empty Array
arrs=[]

#Solution
for i in range(0,x+1):
  for j in range(0,y+1):
    for k in range(0,z+1):
      if i+j+k !=n:
        arr=[i,j,k]
        print(arr)
        arrs.append(arr)
print(arrs)

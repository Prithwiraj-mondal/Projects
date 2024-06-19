age = 28
if age %2 == 0:
    print("even")
else:
    print("odd")

a = 5
b = 0
c = a/b
print(c)

a,b = map(int(input().split()))
if b==0:
    print("infinity")
else:
    print(a//b)

array = [1,2,3,4,5]
print(array[0:4:2])
print(array[10])
                        # ==, !=, >=, <=
n = 10
# if n %2 == 0:
#     print("odd")
if n %2 != 0:
    print("odd")
else:
    print("even")
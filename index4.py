# *args - arguments
def sum2(*args):
    total =0
    for i in args:
        total+=i
    print(f"Сумма: {total}")
sum2(5,6,5,6,78)
#####
a = [1,2,3,4]
b = [*a,5,6,7,8,9]
print(b)
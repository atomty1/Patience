# Enter the upper limit: 10
# %  modulo
val = 1
end_point = int(input("Enter the upper limit: "))
while val <= end_point:
    if(val % 2 == 0):
        print(val)
    val = val + 1
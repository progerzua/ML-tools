input_list = [5,6,2,1,6,7,10,12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))

[[print(i,ii) for ii in range(3)] for i in range(5)]


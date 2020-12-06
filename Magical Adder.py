
# Prompt to Enter 3 numbers

print('Please enter 3 values separated by ,')
adder = str(input())
new_adder = adder.split(",")
#print(new_adder)
a =0
b =0
for i in range(len(new_adder)):
        if i != len(new_adder) -1:
             a = a + int(new_adder[i])
        else:
             b = int(new_adder[i])
print(a - b)



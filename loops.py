#for loop

variable = 0
#range only works for integer
for index in range(5):
    # print(index)
    # print(variable)
    variable+=1

for second_index in range(5,8):
    print(second_index)

for third_index in range(10,20,2):
    print(third_index)

# for a in range(0.0,1.0,0.1):
#     print(a)

my_list = [1,2,3,4,"pippo",True]

for item in my_list:
    print(str(item))

    index = 0
    while index < 10:
        print(index)
        index += 1

index = 0
while index < 10:
    if index == 5:
        index += 1
        continue
    elif index == 7:
        break
    print(index)
    index += 1
else:
    print("While loop exited")

index = 0
while index < 10:
    print(index)
    index+=1
else:
    print("Naturally exited")



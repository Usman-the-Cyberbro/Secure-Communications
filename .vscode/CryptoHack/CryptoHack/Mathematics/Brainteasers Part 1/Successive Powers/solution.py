#!/usr/bin/python3

result = []
counter = 0
for i in range(851, 1001):
    for j in range(2,i-1):
        if i%j != 0:
            pass
        else:
            counter += 1
    if counter == 0:
        result.append(i)
    counter = 0

powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
p = []
for i in range(1000):
    for prime in result:    
        for j in range(1000):
        
            if i**j%prime == powers[counter]:
                counter += 1
            else:
                counter = 0
            if counter == 5:
                print('flag is : crypto{'+str(prime)+','+str(i)+'}')
                exit()
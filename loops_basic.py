# 1/ Print all ints from 0 to 150 
for x in range(0, 151):
    print(x)

#  2/ Multiples of five 
for x in range(5,1000,5):
    print(x)

# # 3/ Print ints 1 to 100 
# # if divisable by 5 print 'coding'
# # if divisable by 10 print 'dojo'
for x in range(1, 100):
    if x % 10 and x % 5 == 0:
        print("Coding Dojo")
    elif x% 5 == 0:
        print("Coding")
    else: 
        print(x)
        
#4/Add odd ints 0 to 500000 and print final sum
for x in range(0, 500000):
    sum = 0
    if x % 2 != 0:
        sum += x
print(sum)

#5/ Count down by fours
for x in range(2018, -1, -4):
    print(x)

#6 / Set three variables- lowNum, highNum, mult
#start lowNum
#stop at highNum
#print ints that are mults of mult
lowNum = 5
highNum = 99
mult = 3
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)



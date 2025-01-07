#basic 0-150
for i in range(151):
    print(i)

#mulyiples of five
for i in range (5, 1001,5):
    print(i)

#coding or codingdojo
for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)

#sum
sum = 0
for i in range(1, 500001, 2):
    sum += i
    print(sum)

#Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

#flexible
lownum = 2
highnum = 9
mult = 3
for i in range(lownum, highnum + 1):
    if i % mult == 0:
        print(i)
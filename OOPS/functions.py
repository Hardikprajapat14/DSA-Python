""" def average(a=4, b=6):
    print("the average is", (a+b)/2 ) 
average(4,6) 
average() """


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print ("Average is :", sum / len(numbers))
average(5,6,7,1)
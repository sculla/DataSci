#1
print(7**4)

#2
s = "Hi there Sam!"
print(s.split(' '))

#3
planet = "Earth"
diameter = 12742
print('The diameter of {} is {} kilometers.'.format(planet, diameter))

#4
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

#5
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

#6
print('a tuple is immutable, a list is not. \n this means that the values of a tuple cannot be changed once set')

#7
def domainGet(email):
    print(email.split('@')[1])
domainGet('user@domain.com')

#8
def findDog(string):
    print('dog' in string.split())

findDog('Is there a dog here?')

#9
def countDog(string):
    print(len(list(filter(lambda word: word == 'dog', string.split()))))

countDog('This dog runs faster than the other dog dude!')

#10
seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda x : x[0] == 's',seq)))

#11

def caught_speeding(speed, is_birthday):
    if is_birthday == True:
        speed -= 5
    if speed >= 81:
        print('Big Ticket')
    elif speed in range(60,81):
        print("Small Ticket")
    else:
        print("No Ticket")
caught_speeding(81, True)
caught_speeding(81,False)
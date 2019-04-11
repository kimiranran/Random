#RanranShi
#DSC430




#problem1
import random
class SixSideDie:
    def __init__(self, FaceValue=0):
        self.FaceValue=FaceValue

    def roll(self):
        #get ramdon number from 1~6.
        self.FaceValue=random.randrange(1,7,1)
        return self.FaceValue

    def getFaceValue(self):
        return self.FaceValue

    def __repr__(self):
        return 'SixSideDie({})'.format(self.FaceValue)
#inherit function 'sixidedie' and overriding function'roll'.
class TenSideDie(SixSideDie):
    def roll(self):
        self.FaceValue=random.randrange(1,11,1)
        return self.FaceValue
    def __repr__(self):
        return 'TenSideDie({})'.format(self.FaceValue)

#inherit function 'sixsidedie' and overriding function 'roll'.
class TwentySideDie(SixSideDie):
    def roll(self):
        self.FaceValue = random.randrange(1, 21, 1)
        return self.FaceValue

    def __repr__(self):
        return 'TwentySideDie({})'.format(self.FaceValue)


class Cup:
    #initial sixsidedie, tensidedie and twentysidedie to 1.
    def __init__(self,Six=1,Ten=1,Twenty=1):
        self.Six=Six
        self.Ten=Ten
        self.Twenty=Twenty

        #Set an empty list to save the value of each roll.
        self.SixSideDielist=[]
        for n in range(0,Six):
            d = SixSideDie()
            self.SixSideDielist.append(d)

        self.TenSideDielist = []
        for n in range(0, Ten):
            d = TenSideDie()
            self.TenSideDielist.append(d)

        self.TwentySideDielist = []
        for n in range(0, Twenty):
            d = TwentySideDie()
            self.TwentySideDielist.append(d)

    #sum the total facevalue of each roll for each dice.
    def getsum(self):
        sum=0
        for n in range(self.Six):
            sum += self.SixSideDielist[n].getFaceValue()
        for n in range(self.Ten):
            sum += self.TenSideDielist[n].getFaceValue()
        for n in range(self.Twenty):
            sum += self.TwentySideDielist[n].getFaceValue()
        return sum
    #roll and sum total facevalue.
    def roll(self):

        for n in range(self.Six):
            self.SixSideDielist[n].roll()
        for n in range(self.Ten):
            self.TenSideDielist[n].roll()
        for n in range(self.Twenty):
            self.TwentySideDielist[n].roll()
        return self.getsum()

    def __repr__(self):
        return 'Cup({}, {}, {})'.format(self.Six, self.Ten, self.Twenty)
    
#problem2
a=input('what is your name? (enter one word)')
print('hello', a + ' welcome to Dice game.')
print('Begin balance for', a+' is 100 dollars. ' )
balance = 100
b=input('Hi Do you want play games? (Enter Y or N)')
while b=='Y':
    goal=random.randrange(1,101,1)
    print('You goal is', goal)
    check = True
    while check == True:
        #if they enter a value greater than there balacne
        try:
            c = int(input('How much you want to bet? '))
            if c > balance:
                raise ValueError('You cannot bet more than your balance.')
            elif c < 0:
                raise ValueError('You cannot input negative numbers.')
            print('Your balance is now {}'.format(balance - c))
            d = int(input('How many six sided dice you want to play? '))
            if d < 0:
                raise ValueError('You cannot input negative numbers.')
            e = int(input('How many ten sided dice do you want to play?'))
            if e < 0:
                raise ValueError('You cannot input negative numbers.')
            f = int(input('How many twenty sided dice do you want to play?'))
            if f < 0:
                raise ValueError('You cannot input negative numbers.')
            check = False
        except ValueError as error:
            print(error)
    balance = balance - c
    cup=Cup(d,e,f)
    g=cup.roll()
    print ('the result is', g)
    if g==goal:
        h=10*c
        balance=balance+h
    elif -5 <= g-goal <= 5:
        h=5*c
        balance=balance+h
    elif -10 <=g-goal <=10:
        h=2*c
        balance=balance+h
    print(a, '\'s balance is now', balance )
    b = input('Hi Do you want play games? (Enter Y or N)')
# if user input N while loop will not execute
print('Bye Bye')

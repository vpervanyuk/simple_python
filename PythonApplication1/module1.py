import random

#def get_digit(number, rank):
   # return (number%10**rank)//10**(rank-1)


class Game(object):

    #конструктор
    def __init__(self, tries_count):
        #print("init")
        self.__tries_count = tries_count
        self.digits = [-1,-1,-1,-1]
        self.set_new_number()

    @property
    def number(self):
        return self.digits[0]*1000+self.digits[1]*100+self.digits[2]*10+self.digits[3]

    @number.setter
    def number(self, number):
        self.digits = [x for x in str(number).rjust(4,'0')]
         
    @property
    def bulls(self):
        #print("get bulls")
        return self.__bulls

    def set_new_number(self):
        #print("set_new_number")
        cnt = 0
        for i in range(0,4):
            need_new=True
            while need_new==True and cnt<100:  #цифры повторяется - генерим снова
                cnt+=1
                self.digits[i]=random.randrange(0,9)
                need_new=False
                for j in range(0,4):
                    need_new = (self.digits[i]==self.digits[j]) and (i!=j)
                    if need_new:
                       break
        self.print_state

    def check_bulls_cows(self, guess_number):
        guess = [x for x in str(guess_number).rjust(4,'0')]
        bulls = 0
        cows = 0
        for i in range(0,4):
            if int(self.digits[i]) == int(guess[i]):
                bulls += 1
            for j in range(0,4):
                if int(self.digits[j]) == int(guess[i]) and i!=j:
                    cows += 1
        if bulls == 4:
            code = 1
        else:
            code = 0
        return bulls, cows, code

    def print_state(self):
        #print("print_state")
        print("digits:", self.digits)




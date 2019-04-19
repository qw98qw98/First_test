lmlist=[31,29,31,30,31,30,31,31,30,31,30,31]
nmlist=lmlist.copy()
nmlist[1]=28
daylist=['Sun','Mon','Tue','Wed','Thr','Fri','Sat']
def Runyear(year):
    '''The func to coculate if the year is leapyear'''
    if (year%4 is 0 and year%100 is not 0) or year%400 is 0:
        return True
    return False
def Whatday(year,month,day):
    '''The func to coculate the day is what.'''
    total=0
    for i in range(1,year):
        if Runyear(i):
            total+=366
        else:
            total+=365
    for m in range(0,month-1):
        if Runyear(year):
            total+=lmlist[m]
        else:
            total+=nmlist[m]
    total+=day
    return total%7
class Datefind():
    year=month=day=0
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
class findoput(Datefind):
    def __init__(self):
        super(findoput,self).__init__(year,month,day)
        print(f'Today is {daylist[Whatday(self.year,self.month,self.day)]}.')
def Output(year,month):
    '''Just output.'''
    for day in daylist:
        print(f'{day}   ',end='')
    print('\n')
    print('      '*Whatday(year,month,1),end='')
    list=[]
    if Runyear(year):
        list=lmlist.copy()
    else:
        list=nmlist.copy()
    for i in range(1,list[month-1]+1):
        if Whatday(year,month,i) is 0:
            print('\n')
        print('{:' '<3}   '.format(i),end='')
    print('\n')
if __name__=="__main__":
    while True:
        list=[]
        try:
            list=input().split(' ')
        except:
            break
        else:
            if len(list)is 3:
                year, month, day = map(int, list)
                Datefind(year,month,day)
                findoput()
            elif len(list)is 2:
                year, month=map(int, list)
                Output(year,month)
            else:
                year=int(list[0])
                if Runyear(year):
                    print(f'{year} is leapyear.')
                else:
                    print(f'{year} is normalyear.')

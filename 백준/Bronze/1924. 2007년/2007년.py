import datetime
x, y = map(int, input().split())
dt = datetime.datetime(2007, x, y).weekday()
if dt == 0:
    print('MON')
elif dt == 1:
    print('TUE')
elif dt == 2:
    print('WED')
elif dt == 3:
    print('THU')
elif dt == 4:
    print('FRI')
elif dt == 5:
    print('SAT')
elif dt == 6:
    print('SUN')

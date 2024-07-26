def is_leap(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        return True
    else:
        return False

def is_current_date(Y, M,D):
    if M == 2:
        if is_leap(Y):
            return D<=29
        else:
            return D<=28

    #1 3 5 7 8 10 12
    date1 = [1,3,5,7,8,10,12]
    date2 = [4,6,9,11]

    if M in date1:
        return D<=31
    elif M in date2:
        return D<=30
    else: 
        return False # 1~12 이외의 수

Y, M, D = map(int, input().split())

if is_current_date(Y, M, D):
    if M>=3 and M<=5:
        print("Spring")
    elif M>=6 and M<=8:
        print("Summer")
    elif M>=9 and M<=11:
        print("Fall")
    else:
        print("Winter")
else:
    print(-1)
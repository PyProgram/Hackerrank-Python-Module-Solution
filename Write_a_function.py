def is_leap(year):
    leap = False
    if year in range(1900,100001):
        if (year % 4 == 0) :
            if (year % 100 == 0 or year % 400 == 0) :
                leap = True
                return leap
        else :
            leap= False
            return leap
    else :
        exit()        
year = int(input())
print(is_leap(year))

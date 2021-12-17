import time

def countdown_seconds(number,text):
    while number:
        mins , secs = divmod(number, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print("Countdown : "+timer, end='\r')
        time.sleep(1)
        number-=1
    #time.sleep(1)
    print(text)




def countdown_hours(number,text):
    while number:
        days , hours = divmod(number, 24)
        timer = '{:02d}:{:02d} hour(s)'.format(days,hours)
        print("Countdown : "+timer, end='\r')
        time.sleep(1*3600)
        number-=1
    
    print("\n \n Countdown complete....")
    print(text)
    print('*'*100)

#countdown_hours(2,"test")
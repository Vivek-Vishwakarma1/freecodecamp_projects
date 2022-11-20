def add_time(start, duration, day = None):
    
    m1 = int(start.split(":")[1][:2])     # minutes of duration
    m2 = int(duration.split(":")[1][:2])  # minutes of start time 
    h1 = int(start.split(":")[0])         # hours of duration
    h2 = int(duration.split(":")[0])      # hours of start time 
    day_c = 0                             # day count, becuase of durations hours 
    ampm = start[-2:]                     # am pm of the start time
    
    w_days = ['monday', 'tuesday', 'wednesday', 'thurseday', 'friday', 'saturday', 'sunday']
    
    # time remaining for next day
    if ampm == 'AM': 
        hr_r= 24-h1 
    else: hr_r= 12-h1
    min_remain = 60-m1
    
    # counting how many days ahead we are
    if h2>hr_r:
        day_c = 1
        if (h2-hr_r)//24>=1:
            day_c=(h2-hr_r)//24+1
    
    
    # Duration round off to 24 hour time frame
    if h2>=24:
        h2 =h2%24
        
    
    # Minutes addition
    if m1+m2>=60:
        mins = m1+m2-60
        c= (m1+m2)//60
    else:
        mins = m1+m2
        c = 0
        
    
    # Hour addition
    '''
    case 1: when the first time is in AM and duration could be any time length
    '''
    h_sum = h1+h2+c
    if ampm=='AM':     
        if h1+h2+c>23:
            hrs = h1+h2+c-24
        elif h1+h2+c>=12:
            hrs = h1+h2+c
            if h1+h2+c>12:
                hrs = h1+h2+c-12
            hc = (h1+h2)//12
            ampm = 'PM'
        else:
            hrs = h1+h2+c
            
    elif ampm == 'PM':
        if h_sum==24:
            hrs = h_sum-12
            day_c = 1
        elif h_sum>24:
            hrs = h_sum-24
            day_c = 1

        elif h_sum>=12:
            hrs = h_sum-12
            ampm = 'AM'
            if h1+c ==12:
                day_c += 1
        else:
            hrs = h_sum
            #day_c = 1
        
    else: 
        hrs = h1+h2+c

        
    #string to return
    if day_c==0:
        d_str = ''     #string to return when the durations hours added and may causing change in day
    elif day_c == 1:
        d_str = '(next day)'
    else:
        d_str = f'({day_c} days later)'
        
    #day of week return in string
    if day != None:
        idx = w_days.index(day.lower())   # index of given day
        n_day = (idx+day_c)%7             # index of day which should be out put due to addition of duration hours
        dd = w_days[n_day]                # modified day
    else: dd = None

    

    #formatting minutes 
    if mins<10:
        formated_mins = '0'+str(mins)
    else:
        formated_mins = str(mins)
          

      
    #final calculated time   
    if dd and d_str!='':
        t = str(hrs)+':'+formated_mins+' '+ ampm + ', '+dd.title()+' '+ d_str
    elif dd and d_str=='':
        t = str(hrs)+':'+formated_mins+' '+ ampm + ', '+dd.title()
    elif d_str !='':
        t = str(hrs)+':'+formated_mins+' '+ ampm + ' '+ d_str
    elif d_str=='':
        t = str(hrs)+':'+formated_mins+' '+ ampm
    else:
        t = str(hrs)+':'+formated_mins+' '+ ampm
        
    return  t

add_time("06:12 AM", "03:42")
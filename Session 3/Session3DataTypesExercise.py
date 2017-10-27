print("Session 3 - Data Types Exercise")

# 1.1
a = 3
a + 2   #a+2 = 5

# 1.2
a = a + 1.0
a   #a = 4.0

# 1.3
a = 3   #a = 3

# 1.4
a = 3
a == 5.0
a   #a = false

# 1.5
b = 10
c = b > 9
c   #c = true

# 1.6
5/2 == 5/2.0 #true

###################################################################################################################

#2.1 
3.0 - 1.0 != 5.0 - 3.0  #false

#2.2
3 > 4 or (2 < 3 and 9 > 10) #false

#2.3
4 > 5 or 3 < 4 and 9 > 8    #true

#2.4
not(4 > 3 and 100 > 6)  #false

##############################################################################################################

import time

right_now = time.time() #in seconds
print(right_now)
secs_per_day = 24 * 60 * 60 
secs_per_hour = 60 * 60
secs_per_min = 60

days_since = int(right_now / secs_per_day)
print(days_since, "days since epoch")
midnight_in_seconds = days_since * secs_per_day
secs_since_midnight = right_now - midnight_in_seconds

hours_since_midnight = int(secs_since_midnight / secs_per_hour)
mins_since_midnight = int((secs_since_midnight - (hours_since_midnight * secs_per_hour)) / secs_per_min)
remaining_secs = int(secs_since_midnight - ((hours_since_midnight * secs_per_hour) + (mins_since_midnight * secs_per_min)))

print("Current time since epoch is %d days, %d:%d:%d." % (days_since, hours_since_midnight, mins_since_midnight, remaining_secs))

############################################################################################################

#Prof's answer
import time
print(time.time())
curent = time.time()
seconds = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24
days = current// 60 //60 //24
print("Current time is % days, % hours, % minutes, and % seconds from Epoch", % (days, hours, minutes, seconds))


################################### O P E R A T O R S ######################################3###############

# % - to divide and only get the remainder
# // - to divide and only get the answer as an integer

#############################################################################################################


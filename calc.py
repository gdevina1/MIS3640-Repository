print("Class Session 1, Exercise 2")
print(46+37+38)
print(2017-1996)
print(int(15/3))
print(2**6)
print("how many seconds are there in 42 minutes 42 seconds?")
print(42*60+42)
print("How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.")
print(10/1.61)
print("If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?")
print(6.211180124223602/2562*60) 
print("disclaimer: Math is not really my strong suit.")

print("")

print("Class Session 2, Exercise 1")
print("What is the volume of a sphere with radius 5?")
pi= 3.141592654
print(4/3*pi*(5**3))
print("Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?")
cost_after_discount= 24.95*0.6*60 #cost after 40% discount
shipping_cost= 3+(0.75*59) #shipping cost for first 60
print(cost_after_discount + shipping_cost)
print("If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?")
easy_pace= (8*60)+15 #seconds/1 mile
tempo_pace= (7*60)+12 #seconds/1 mile
total_time_secs= (easy_pace*2) + (tempo_pace*3) #total running time in seconds
total_time_min= total_time_secs/60 #total running time in minutes
print("total running time in minutes is %.2f" % total_time_min)
print("convert 0.1 minutes to seconds gives %  sseconds" % (0.10*60)) #minutes to seconds conversion
print("total running time is 38 min 6 secs, which means I will be home for breakfast by:")
return_time_min= (52+38)-60
return_time_hour= 6+1
return_time_final= str(return_time_hour) + ":" + str(return_time_min) + "am"
print (return_time_final)
print("If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.")
percent_increase=((89-82)/82)*100
print("%.1f %%" % percent_increase)




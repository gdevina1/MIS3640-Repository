#warmup1-sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  if weekday and not vacation:
    return False
  if not weekday and vacation:
    return True
  else:
    return True

#warmup1-monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False

#warmup1-sum_double
def sum_double(a, b):
  sum = a + b
  if a == b:
    return sum * 2
  else:
    return sum

#warmup1-sum_double
def sum_double(a, b):
  sum = a + b
  if a == b:
    return sum * 2
  else:
    return sum

#warmup1-diff21
def diff21(n):
  diff = abs(n - 21)
  if n > 21:
    return 2*diff
  else:
    return diff

#warmup1-parrot_trouble
def parrot_trouble(talking, hour):
  if (talking and (hour < 7 or hour > 20)):
    return True
  else:
    return False

parrot_trouble(talking, 6) 

#warmup1-makes10
def makes10(a, b):
  if int(a + b) == 10:
    return True
  elif (a == 10 or b == 10):
    return True
  else:
    return False

#warmup1-near_hundred
def near_hundred(n):
  if (abs(100-n) <= 10):
    return True
  elif (abs(200 - n) <=10):
    return True
  else:
    return False


#warmup1-pos_neg
def pos_neg(a, b, negative):
  if negative:
    if (a <= 0 and  b <= 0):
      return True
    else:
      return False
  if not negative:
    if((a < 0 and b > 0) or (a > 0 and b < 0)):
      return True
    else:
      return False

#warmup1-not_string
def not_string(str):
  if (len(str) >=3 and str[:3] == "not"):
    return str
  else:
    return "not " + str

    
    
    
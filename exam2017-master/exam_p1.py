trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}

tens = [20, 30, 40, 50, 60, 70, 80, 90]

hundreds = [100, 200, 300, 400, 500, 600, 700, 800, 900]


def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    # '''
    if number < 11:
        num= str(number)
        nums = trans[num]
        return num
    
    if number >= 11 and number < 20:
        tn = int(number - 10)
        tns = str(tn)    
        tns_c = trans[tns]
        return trans.get("10") + " " + tns_c

    # if number >=20 and number < 100:
    #     x = 
      
    if number in tens:
        x = int(number / 10)
        z = str(x)
        y = trans[z]
        return y + " " + trans.get("10")

    if number > 20 and number < 100:
        tn = int(number / 10)
        tns = str(tn)
        tns_c = trans[tns]
        dig = int(number - (tn * 10))
        digs = str(dig)
        digs_c = trans[digs]
        return tns_c + " " + trans.get("10") + " " + digs_c

    if number in hundreds:
        x = int(number/100)
        z = str(x)
        y = trans[z]
        return y + " " + trans.get("100") 

    if number > 100 and number < 1000:
        hun = int(number / 100)
        huns = str(hun)
        huns_c = trans[huns]
        tn =  int(number - (hun * 100))
        tn2 = int(tn / 10)
        tns = str(tn2)
        tns_c = trans[tns]
        dig = int(number - (hun * 100) - (tn2 * 10))
        digs = str(dig)
        digs_c = trans[digs]
        return huns_c + " " + trans.get("100") + " " + tns_c + " " + trans.get("10") + " " + digs_c
        


# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print("---------------------------")
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print("---------------------------")
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print("---------------------------")
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print("---------------------------")
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print("---------------------------")
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()

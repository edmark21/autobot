import os
import sys
from twilio.rest import Client
import json,urllib.request
import os, sys, requests
from opencage.geocoder import OpenCageGeocode
key = 'f6393f9172914083a2bbd1c0b040d953'
geocoder = OpenCageGeocode(key)

o = '''\033[1;33m
                      Version 1
        

      ___  _   _ _____ ___________  _____ _____ 
     / _ \| | | |_   _|  _  | ___ \|  _  |_   _|
    / /_\ \ | | | | | | | | | |_/ /| | | | | |  
    |  _  | | | | | | | | | | ___ \| | | | | |  
    | | | | |_| | | | \ \_/ / |_/ /\ \_/ / | |  
    \_| |_/\___/  \_/  \___/\____/  \___/  \_/  
                                            
                                                                                                                                 
                 
                 
                 Created by
            Edmark Jay Sumampen
                
'''
v1 = '''\033[1;33m
                     	Version 2
        

      ___  _   _ _____ ___________  _____ _____ 
     / _ \| | | |_   _|  _  | ___ \|  _  |_   _|
    / /_\ \ | | | | | | | | | |_/ /| | | | | |  
    |  _  | | | | | | | | | | ___ \| | | | | |  
    | | | | |_| | | | \ \_/ / |_/ /\ \_/ / | |  
    \_| |_/\___/  \_/  \___/\____/  \___/  \_/  
                                            
                      God Mode                      

                                            
                                            
                 
                 
                 Created by
            Edmark Jay Sumampen
                
'''	
	
gml = '''\033[1;33m
                     	Version 2
        

      ___  _   _ _____ ___________  _____ _____ 
     / _ \| | | |_   _|  _  | ___ \|  _  |_   _|
    / /_\ \ | | | | | | | | | |_/ /| | | | | |  
    |  _  | | | | | | | | | | ___ \| | | | | |  
    | | | | |_| | | | \ \_/ / |_/ /\ \_/ / | |  
    \_| |_/\___/  \_/  \___/\____/  \___/  \_/  
                                            
                      God Mode                      

                                            
                                            
                 
                 
                 Created by
            Edmark Jay Sumampen
                
'''

lo = '''\033[1;33m
                     Version 2
        

      ___  _   _ _____ ___________  _____ _____ 
     / _ \| | | |_   _|  _  | ___ \|  _  |_   _|
    / /_\ \ | | | | | | | | | |_/ /| | | | | |  
    |  _  | | | | | | | | | | ___ \| | | | | |  
    | | | | |_| | | | \ \_/ / |_/ /\ \_/ / | |  
    \_| |_/\___/  \_/  \___/\____/  \___/  \_/  
                                                                                                                                                                                              
                 
                 Created by
            Edmark Jay Sumampen
                
'''

os.system('clear')

l = 999

f = open("log.txt", "r")
ff = open("log2.txt", "r")
account_sid = (f.readline())
f.close()
auth_token = (ff.readline())
ff.close()



def main():
    try:
        client = Client(account_sid, auth_token)
        balance_data = client.api.v2010.balance.fetch()
        balance = float(balance_data.balance)
        currency = balance_data.currency

    except:
        print("Acount error!, please check ur account..")
        input("press enter to continue....")
        gmm()
    
    client = Client(account_sid, auth_token)
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency
    for x in range(l):
        print(f'\x1b[34m Your account has {balance:.2f} {currency} left.')
        n = str(input("\033[1;33m\n Enter Phone#: "))
        if n == "menu":
            os.system('clear')
            print(o)
            gmm()
        phone_number = client.lookups \
                       .v1 \
                       .phone_numbers('1' + n) \
                       .fetch(type=['caller-name'])
        pn = (phone_number.caller_name)
        pnn = str(pn['caller_name'])
        if pnn == "None":
                print("\x1b[95m Unavailable Name")
        elif pnn == " WIRELESS CALLER":
                print("\x1b[31m This number is protected by call filter..")
                
        
        else:
                print('\033[32m Name: ' + pnn)
                main()
#9107979456


def gm():
    try:
        client = Client(account_sid, auth_token)
        balance_data = client.api.v2010.balance.fetch()
        balance = float(balance_data.balance)
        currency = balance_data.currency

    except:
        print(" Acount error!, please check ur account..")
        input(" press enter to continue....")
        gmm()
    for x in range(999):
        try:
            print(f'\x1b[34m Your account has {balance:.2f} {currency} left.')
        except:
            print(" Invalid Account!")
            input(" press Enter to continue...")
            gmm()
        pangalan = input('\033[1;33m\n Enter number: ')

        if pangalan == 'menu':
            os.system('clear')
            print(lo)
            gmm()
        phone_number = client.lookups \
                       .v1 \
                       .phone_numbers('+1'+pangalan) \
                       .fetch(add_ons=['ekata_reverse_phone'])
        gg = (phone_number.add_ons['results'])
        ggg = (gg['ekata_reverse_phone']['result'])
        gggg = (ggg['current_addresses'])
        ggggg = (ggg['belongs_to'])
        results = geocoder.reverse_geocode(gggg[0]['lat_long']['latitude'], gggg[0]['lat_long']['longitude'])

        try:
            print("\033[32m\n Name: ", ggggg['name'])
            print(" Age: ",ggggg['age_range']['from'], "-", ggggg['age_range']['to'])
            print(" Gender: ", ggggg['gender'])
            print(" Street: ", gggg[0]['street_line_1'])
            print(" City: ", gggg[0]['city'])
            print(" State: ", results[0]['components']['state'])
            print(" Zipcode: ", results[0]['components']['postcode'])
            print("\n Address Coordinates: ",  gggg[0]['lat_long']['latitude'], gggg[0]['lat_long']['longitude'], "\n")
            gm()
        except:
            print("\x1b[31m Cant find the info of this person")
			
def v2():
    c = input("\33[34m Enter code: ")
    if c == "menu":
        os.system('clear')
        print(o)
        gmm()
    for x in range(20):
        print("\x1b[34m\n credits: ", x ,"/ 20")
        n = input("\033[1;33m Enter number#: ")
        if n == "menu":
            os.system('clear')
            print(o)
            gmm()
        data = urllib.request.urlopen("https://trial.serviceobjects.com/gppl2/api.svc/PhoneInfo/"+n+"/full/"+c+"?format=json").read()
        output = json.loads(data)
        try:
            dd = (output['PhoneInfo']['Contacts'])
            loc = (output['PhoneInfo']['Provider'])
            print ('\033[32m\n Name: '+dd[0]['Name'])
            print (" Steet: "+dd[0]['Address'])
            print (" City: "+dd[0]['City'])
            print (" State: "+dd[0]['State'])
            print(" Address coordinates: " + loc['Latitude'], loc['Longitude'])

        except:
            print(" The code is not working!")
            input("\n\n\n\n\n press enter to continue...")
            os.system('clear')
            print(o)
            v2()
            
    	
    
    	
    
about = '''\033[32m

	Autobot Version2
	Created by: Edmark Jay Sumampen
	
	- helps you to identify phone numbers,
	the name associated with that number 
	and even their addresses.
	
	-This tool is developed to help agents
	get accurate info and provide quality
	leads.
	
	Any questions or suggestions?
	Email me at this address
	edmark.sumampen@gmail.com
	or contact me on facebook at
	edmark.sumampen.1
	
	
	Thank you for using this app..



'''
    			

kk = '''\033[1;33m
	[1] God Mode	= show all info
	[2] Normal mode	= only show the name
	[3] Autobot v1	= open the version1 app
	[4] Change account = change the account
	[5] Show account user & pass
	[6] About

'''
def gmm():
    print(lo)
    print(kk)
    godmode = input("\x1b[31m Select Option: : ")
    if godmode == '1':
        os.system('clear')
        print(gml)
        gm()
    elif godmode == '2':
        os.system('clear')
        print(lo)
        main()
    elif godmode == '3':
        os.system('clear')
        print(o)
        v2()
    elif godmode == '4':
        print()
        os.system('clear')
        af = open("log.txt", "w")
        fa = open("log2.txt", "w")
        print(" account error")
        u = input(" enter user: ")
        af.write(u)
        p = input(" enter pass: ")
        fa.write(p)
        af.close()
        fa.close()
        os.system('clear')
        print(lo)
        gmm()
    elif godmode == '5':
        f = open("log.txt", "r")
        ff = open("log2.txt", "r")
        os.system('clear')
        print("\033[32m\n User: ", f.read())
        print(" Pass: ", ff.read())
        input(" \n\n\n\n press Enter to continue....")
        os.system('clear')
        print(lo)
        gmm()
		
    elif godmode == '6':
        os.system('clear')
        print(about)
        input("\n press Enter to continue....")
        os.system('clear')
        print(lo)
        gmm()
    else:
        print(" Please select from [1-5] option")
        gmm()

gmm()

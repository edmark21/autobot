import os
import sys
from twilio.rest import Client



	
	
gml = '''
                    	V1
        

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

lo = '''
                    V1
        

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
print(lo)
l = 999

# Your Account SID from twilio.com/console
account_sid = "ACb4c7608c9e7d2bbe64c13b2e0aa95c72"
# Your Auth Token from twilio.com/console
auth_token = "91d1a0cd7debdeb32d338fecf7365528"

	
	

def main():
    client = Client(account_sid, auth_token)
    balance_data = client.api.v2010.balance.fetch()
    balance = float(balance_data.balance)
    currency = balance_data.currency
    for x in range(l):
        print(f'\x1b[34mYour account has {balance:.2f} {currency} left.')
        n = str(input("\033[1;33m\nEnter Phone#: "))
        phone_number = client.lookups \
                       .v1 \
                       .phone_numbers('1' + n) \
                       .fetch(type=['caller-name'])
        pn = (phone_number.caller_name)
        pnn = str(pn['caller_name'])
        if pnn == "None":
                print("\x1b[95mUnavailable Name")
        elif pnn == "WIRELESS CALLER":
                print("\x1b[31mThis number is protected by call filter..")
                
        
        else:
                print('\033[32mName: ' + pnn)
                main()
#9107979456


def gm():
	client = Client(account_sid, auth_token)
	balance_data = client.api.v2010.balance.fetch()
	balance = float(balance_data.balance)
	currency = balance_data.currency
	for x in range(999):
		print(f'\x1b[34mYour account has {balance:.2f} {currency} left.')
		pangalan = input('\033[1;33m\nEnter number: ')
		phone_number = client.lookups \
		.v1 \
		.phone_numbers('+1'+pangalan) \
		.fetch(add_ons=['ekata_reverse_phone'])
		gg = (phone_number.add_ons['results'])
		ggg = (gg['ekata_reverse_phone']['result'])
		gggg = (ggg['current_addresses'])
		ggggg = (ggg['belongs_to'])
		print("\033[32m\nName: ", ggggg['name'])
		tf = (ggggg['age_range']['to'])
		print("Age: ",ggggg['age_range']['from'], "-", tf)
		print("Gender: ", ggggg['gender'])
		print("Street: ", gggg[0]['street_line_1'])
		print("City: ", gggg[0]['city'])
		print("Address Coordinates: ",  gggg[0]['lat_long']['latitude'], gggg[0]['lat_long']['longitude'], "\n")
			
		gm()

godmode = input("\x1b[31mEnter God Mode [y/n]: ")
if godmode == "y":
	os.system("clear")
	print(gml)
	gm()
elif godmode == "n":
	main()
	
else:
	print("Please input y for God Mode and n for Normal mode")




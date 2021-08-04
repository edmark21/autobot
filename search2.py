import os
import sys
from twilio.rest import Client



lo = '''\x1b[93m
                       Version 2
        


           _    _ _______ ____  ____   ____ _______ 
       /\  | |  | |__   __/ __ \|  _ \ / __ \__   __|
      /  \ | |  | |  | | | |  | | |_) | |  | | | |   
     / /\ \| |  | |  | | | |  | |  _ <| |  | | | |   
    / ____ \ |__| |  | | | |__| | |_) | |__| | | |   
   /_/    \_\____/   |_|  \____/|____/ \____/  |_|   
                                                   
                                                   
 
                                            
                                            

                                            
        
                 
                 Created by
            Edmark Jay Sumampen
                
'''

os.system('clear')
print(lo)
l = 999

# Your Account SID from twilio.com/console
account_sid = input("\x1b[96mEnter Username: ")
# Your Auth Token from twilio.com/console
auth_token = input("Enter Pass: ")



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


main()

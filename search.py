import os
import sys
from twilio.rest import Client



lo = '''
                    BETA
        
    _  _   _ ___
_________  ___
___ 
   / _ \| | | |_   |  _  | __ \|  _  |_   _|
  / /_\ \ | | | | | | | | | |_/ /| | | | | |  
  |  _  | | | | | | | | | | _ \| | | | | |  
  | | | | |_| | | | \ \_/ / |_/ /\ \_/ / | |  
  \_| |_/\___/  \_/  \___/\____/  \___/  \_/  
                                            
                                            
                 INSURANCE
                 
                 Created by
            Edmark Jay Sumampen
                
'''

os.system('clear')
print(lo)
l = 999

# Your Account SID from twilio.com/console
account_sid = "ACbf4fb9007ab448470fabc34d9b9ff745"
# Your Auth Token from twilio.com/console
auth_token = "2bb18502d0a95a26f782fe77a2bac037"

def main():
    for x in range(l):
        client = Client(account_sid, auth_token)
        balance_data = client.api.v2010.balance.fetch()
        balance = float(balance_data.balance)
        currency = balance_data.currency
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

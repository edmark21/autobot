import os
import sys

lo = '''


                    BETA
        
         ____  ____  ________    ___    
     / \ |   ||   ||       | .'   `.  
    / _ \  | |    | |  |_/ | | \_|/  .-.  \ 
   / ___ \ | '    ' |      | |    | |   | | 
 / /   \ \_\ \__/ /      | |_   \  `-'  / 
|____| |____|`.__.'      |_____|   `.___.'  
                                            
                 INSURANCE
                 
                 Created by
            Edmark Jay Sumampen
                


'''

os.system('clear')
print(lo)
from twilio.rest import Client
l = 999

# Your Account SID from twilio.com/console
account_sid = "ACbf4fb9007ab448470fabc34d9b9ff745"
# Your Auth Token from twilio.com/console
auth_token = "4f16cb657c28f0e8e258456477961675"

def main():
    for x in range(l):
        client = Client(account_sid, auth_token)
        n = str(input("Enter Phone#: "))
        phone_number = client.lookups \
                       .v1 \
                       .phone_numbers('1' + n) \
                       .fetch(type=['caller-name'])
        pn = (phone_number.caller_name)
        pnn = str(pn['caller_name'])
        print('\nName: ' + pnn)
        main()

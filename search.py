import os
import sys

lo = '''


                    BETA
        

    ___  _   _ _____ ___________  _____ _____ 
   / _ \| | | |_   _|  _  | ___ \|  _  |_   _|
  / /_\ \ | | | | | | | | | |_/ /| | | | | |  
  |  _  | | | | | | | | | | ___ \| | | | | |  
  | | | | |_| | | | \ \_/ / |_/ /\ \_/ / | |  
  \_| |_/\___/  \_/  \___/\____/  \___/  \_/  
                                            
                                            

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
auth_token = "2bb18502d0a95a26f782fe77a2bac037"

def main():
    for x in range(l):
        client = Client(account_sid, auth_token)
        n = str(input("\nEnter Phone#: "))
        phone_number = client.lookups \
                       .v1 \
                       .phone_numbers('1' + n) \
                       .fetch(type=['caller-name'])
        pn = (phone_number.caller_name)
        pnn = str(pn['caller_name'])
        print('Name: ' + pnn)
        main()


main()

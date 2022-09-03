from twilio.rest import Client
import json, urllib.request
import os.path
import requests
import bs4
import json, re, os

f = open("username.txt", "r")
ff = open("passwd.txt", "r")
fff = open("key.txt", "r")

a = (f.readline())
f.close()

t = (ff.readline())
ff.close()

key = (fff.readline())
fff.close()

client = Client(a, t)

loo = '''\33[95m

        ********************
           People Search 
                via
         ++++++++++++++++++      

        [1] Phone number
        [2] Full Name
 

'''

kk = '''\33[93m
  [1] Start
  [2] Change account 
  [3] Show account
  [4] About
  

'''

about = '''\033[32m
 
    Autobot Version 1.5
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

lo = '''\33[34m 
  _______       _____      ______       _____ 
  ___    |___  ___  /_________  /_________  /_
  __  /| |  / / /  __/  __ \_  __ \  __ \  __/
  _  ___ / /_/ // /_ / /_/ /  /_/ / /_/ / /_  
  /_/  |_\__,_/ \__/ \____//_.___/\____/\__/  

                     v2


'''

os.system('clear')


def auto():
    
    try:
        p = input("\n \33[93mEnter number: \33[0m")
        if p == "menu":
            os.system("clear")
            gmm()

        try:
            phone_number = client.lookups \
            .v1 \
            .phone_numbers('+1'+p) \
            .fetch(add_ons=['ekata_reverse_phone'], type=['caller-name'])
            data = (phone_number.add_ons['results']['ekata_reverse_phone']
                    ['result']['belongs_to'])

        except:
            print(" Please input Phone number only!....")
            auto()

        pn = (phone_number.caller_name)
        pnn = (pn['caller_name'])

        dataa = (phone_number.add_ons['results']['ekata_reverse_phone']
                 ['result']['current_addresses'])

        try:
            print('\33[34m\n New Prospect Info: \033[32m' + pnn)

        except:
            print("\n \33[34mNew Prospect Info:" + "\033[32m Unavaialble")

        try:
            print("\n Name: ", data['name'])
        except:
            print("\n Name: Not available")

        try:
            print(" Gender: ", data['gender'])
        except:
            print(" Gender: Not available")

        try:
            if data['age_range'] == "Not Available":
                print(" Not available")
            else:
                print(" Age range: ", data['age_range']['from'], "-",
                      data['age_range']['to'])

        except:
            print(" Age: Not available")

        try:
            if dataa[0]['street_line_1'] == "None":
                print(" Street: Not available")
            else:
                print(" Street: ", dataa[0]['street_line_1'])

        except:
            print(" Street: Not available")

        try:
            print(" City: ", dataa[0]['city'])
        except:
            print(" City: Not available")

        try:
            if dataa[0]['state_code'] == "AL":
                print(" State: Alabama (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "AK":
                print(" State: Alaska (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "AZ":
                print(" State: Arizona (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "AR":
                print(" State: Arkansas (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CA":
                print(" State: California (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CZ":
                print(" State: Canal Zone (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CO":
                print(" State: Colorado (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CT":
                print(" State: Connecticut (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "DE":
                print(" State: Delaware (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "DC":
                print(" State: District of Columbia (" +
                      dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "FL":
                print(" State: Florida (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "GA":
                print(" State: Georgia (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "GU":
                print(" State: Guam (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "HI":
                print(" State: Hawaii	(" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "ID":
                print(" State: Idaho (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "IL":
                print(" State: Illinois (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "IN":
                print(" State: Indiana (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "IA":
                print(" State: Iowa (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "KS":
                print(" State: Kansas (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "KY":
                print(" State: Kentucky (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "LA":
                print(" State: Louisiana (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "ME":
                print(" State: Maine (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MD":
                print(" State: Maryland (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MA":
                print(" State: Massachusetts (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MI":
                print(" State: Michigan (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MN":
                print(" State: Minnesota (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MS":
                print(" State: Mississippi (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MO":
                print(" State: Missouri (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MT":
                print(" State: Montana (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NE":
                print(" State: Nebraska (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NV":
                print(" State: Nevada (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NH":
                print(" State: New Hampshire (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NJ":
                print(" State: New Jersey (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NM":
                print(" State: New Mexico (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NY":
                print(" State: New York (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NC":
                print(" State: North Carolina (" + dataa[0]['state_code'] +
                      ")")

            elif dataa[0]['state_code'] == "ND":
                print(" State: North Dakota (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "OH":
                print(" State: Ohio (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "OK":
                print(" State: Oklahoma (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "OR":
                print(" State: Oregon (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "PA":
                print(" State: Pennsylvania (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "PR":
                print(" State: Puerto Rico (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "RI":
                print(" State: Rhode Island (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "SC":
                print(" State: South Carolina (" + dataa[0]['state_code'] +
                      ")")

            elif dataa[0]['state_code'] == "SD":
                print(" State: South Dakota (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "TN":
                print(" State: Tennessee (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "TX":
                print(" State: Texas (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "UT":
                print(" State: Utah (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "VT":
                print(" State: Vermont (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "VI":
                print(" State: Virgin Islands (" + dataa[0]['state_code'] +
                      ")")

            elif dataa[0]['state_code'] == "VA":
                print(" State: Virginia (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WA":
                print(" State: Washington (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WV":
                print(" State: West Virginia (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CO":
                print(" State: Colorado (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WI":
                print(" State: Wisconsin (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WY":
                print(" State: Wyoming (" + dataa[0]['state_code'] + ")")

        except:
            print(" State: Not available")

        try:
            print(" Zipcode: ", dataa[0]['postal_code'])
            print("\n \33[95mAlways ask for Age/Dob & Email")

        except:
            print(" Zipcode: Not avaialble")
            print("\n \33[95mAlways ask for Age/Dob & Email")

        try:
            url = "https://google.com/search?q=" + dataa[0][
                'state_code'] + " time"
            request_result = requests.get(url)
            soup = bs4.BeautifulSoup(request_result.text, "html.parser")
            temp = soup.find("div", class_='BNeawe').text
            print(" Time: ", temp)
            auto()
        except:
            print(" Time: Unavailable")
            auto()

    except:
        print(" Please enter vaild phone number! or Check your Credits..")


def autoe():
    try:
        p = input("\n \33[93mEnter number: \33[0m")
        if p == "menu":
            os.system("clear")
            gmm()

        try:
            phone_number = client.lookups \
            .v1 \
            .phone_numbers('+1'+p) \
            .fetch(add_ons=['ekata_reverse_phone'], type=['caller-name'])
            data = (phone_number.add_ons['results']['ekata_reverse_phone']
                    ['result']['belongs_to'])

        except:
            print(" Please input Phone number only!....")
            autoe()

        pn = (phone_number.caller_name)
        pnn = (pn['caller_name'])

        dataa = (phone_number.add_ons['results']['ekata_reverse_phone']
                 ['result']['current_addresses'])

        try:
            print('\33[34m\n New Prospect Info: \033[32m' + pnn)

        except:
            print("\n \33[34mNew Prospect Info:" + "\033[32m Unavaialble")

        try:
            print("\n Name: ", data['name'])
        except:
            print("\n Name: Not available")

        try:
            print(" Gender: ", data['gender'])
        except:
            print(" Gender: Not available")

        try:
            if data['age_range'] == "Not Available":
                print(" Not available")
            else:
                print(" Age range: ", data['age_range']['from'], "-",
                      data['age_range']['to'])

        except:
            print(" Age: Not available")

        try:
            if dataa[0]['street_line_1'] == "None":
                print(" Street: Not available")
            else:
                print(" Street: ", dataa[0]['street_line_1'])

        except:
            print(" Street: Not available")

        try:
            print(" City: ", dataa[0]['city'])
        except:
            print(" City: Not available")

        try:
            if dataa[0]['state_code'] == "AL":
                print(" State: Alabama (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "AK":
                print(" State: Alaska (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "AZ":
                print(" State: Arizona (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "AR":
                print(" State: Arkansas (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CA":
                print(" State: California (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CZ":
                print(" State: Canal Zone (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CO":
                print(" State: Colorado (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CT":
                print(" State: Connecticut (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "DE":
                print(" State: Delaware (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "DC":
                print(" State: District of Columbia (" +
                      dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "FL":
                print(" State: Florida (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "GA":
                print(" State: Georgia (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "GU":
                print(" State: Guam (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "HI":
                print(" State: Hawaii	(" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "ID":
                print(" State: Idaho (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "IL":
                print(" State: Illinois (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "IN":
                print(" State: Indiana (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "IA":
                print(" State: Iowa (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "KS":
                print(" State: Kansas (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "KY":
                print(" State: Kentucky (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "LA":
                print(" State: Louisiana (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "ME":
                print(" State: Maine (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MD":
                print(" State: Maryland (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MA":
                print(" State: Massachusetts (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MI":
                print(" State: Michigan (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MN":
                print(" State: Minnesota (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MS":
                print(" State: Mississippi (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MO":
                print(" State: Missouri (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "MT":
                print(" State: Montana (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NE":
                print(" State: Nebraska (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NV":
                print(" State: Nevada (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NH":
                print(" State: New Hampshire (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NJ":
                print(" State: New Jersey (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NM":
                print(" State: New Mexico (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NY":
                print(" State: New York (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "NC":
                print(" State: North Carolina (" + dataa[0]['state_code'] +
                      ")")

            elif dataa[0]['state_code'] == "ND":
                print(" State: North Dakota (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "OH":
                print(" State: Ohio (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "OK":
                print(" State: Oklahoma (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "OR":
                print(" State: Oregon (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "PA":
                print(" State: Pennsylvania (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "PR":
                print(" State: Puerto Rico (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "RI":
                print(" State: Rhode Island (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "SC":
                print(" State: South Carolina (" + dataa[0]['state_code'] +
                      ")")

            elif dataa[0]['state_code'] == "SD":
                print(" State: South Dakota (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "TN":
                print(" State: Tennessee (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "TX":
                print(" State: Texas (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "UT":
                print(" State: Utah (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "VT":
                print(" State: Vermont (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "VI":
                print(" State: Virgin Islands (" + dataa[0]['state_code'] +
                      ")")

            elif dataa[0]['state_code'] == "VA":
                print(" State: Virginia (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WA":
                print(" State: Washington (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WV":
                print(" State: West Virginia (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "CO":
                print(" State: Colorado (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WI":
                print(" State: Wisconsin (" + dataa[0]['state_code'] + ")")

            elif dataa[0]['state_code'] == "WY":
                print(" State: Wyoming (" + dataa[0]['state_code'] + ")")

        except:
            print(" State: Not available")

        try:
            print(" Zipcode: ", dataa[0]['postal_code'])
            print("\n \33[95mAlways ask for Age/Dob & Email")

        except:
            print(" Zipcode: Not avaialble")
            print("\n \33[95mAlways ask for Age/Dob & Email")

        try:
            we = requests.get(
                "https://www.melissa.com/v2/lookups/personator/?fullName=&company=&addressLine1=&city=&state=&postalCode=&melissaAddressKey=&phoneNumber="
                + p + "&emailAddress=&freeForm=&fmt=json&id=" + key)
            dwa = json.loads(we.content.decode())
            email = dwa['Records'][0]

            print(" \033[32mEmail: ", email['EmailAddress'])
            print(" Own by:", email['NameFull'])
            autoe()

        except:
            print(" \x1b[31mNo Key Credits left.")
            autoe()

    except:
        print(" Please enter vaild phone number! or Check your Credits..")


def name():
    os.system("clear")
    p = input("\n \33[93mEnter fullname: ")
    if p == "menu":
        sugod()
    try:
        url = requests.get(
            "https://www.melissa.com/v2/lookups/personatorsearch/?name=" + p +
            "&city=&state=&postalCode=&melissaAddressKey=&phoneNumber=&emailAddress=&freeForm=&fmt=json&id="
            + key)
        data = json.loads(url.content.decode())
        info = data['Records']
        s = " "

        for nam in info:
            print("\n \033[32mName: ", nam['FullName'])
            print(
                " Address: ", nam['AddressLine1'] + s + nam['City'] + s +
                nam['State'] + s + nam['PostalCode'])
            print(" Age: ", nam['Age'])
            print(" Dob: ", nam['DateOfBirth'])

        input("\n Press enter to continue..")
        name()
    except:
        print(" Not Found....")
        input(" Press enter to continue..")
        name()


def phone():
    p = input("\n \33[93mEnter number: ")
    os.system('clear')

    if p == "menu":
        sugod()
    elif p == "main":
        gmm()
    try:
        url = requests.get(
            "https://www.melissa.com/v2/lookups/personatorsearch/?name=&city=&state=&postalCode=&melissaAddressKey=&phoneNumber="
            + p + "emailAddress=&freeForm=&fmt=json&id=" + key)
        data = json.loads(url.content.decode())
        info = data['Records']

        s = " "

        for name in info:
            a_string = str(name['DateOfBirth'])
            a_length = len(a_string)
            c = int(a_string[a_length - 2:a_length])
            print("\n \033[32mName: ", name['FullName'])
            print(
                " Address: ", name['AddressLine1'] + s + name['City'] + s +
                name['State'] + s + name['PostalCode'])
            try:
                tuig1 = str(name['DateOfBirth'][0])
                tuig2 = str(name['DateOfBirth'][1])
                tuig3 = str(name['DateOfBirth'][2])
                tuig4 = str(name['DateOfBirth'][3])
                tuig = str(tuig1 + tuig2 + tuig3 + tuig4)

            except:
                print(" No Dob Found")

            print(" Age: ", name['Age'])
            if c == 1:
                print(" DOB: January", tuig)
                phone()
            elif c == 2:
                print(" Febuary", tuig)
                phone()
            elif c == 3:
                print(" DOB: March", tuig)
                phone()
            elif c == 4:
                print(" DOB: April", tuig)
                phone()
            elif c == 5:
                print(" DOB: May", tuig)
                phone()
            elif c == 6:
                print(" DOB: June", tuig)
                phone()
            elif c == 7:
                print(" DOB: July", tuig)
                phone()
            elif c == 8:
                print(" DOB: August", tuig)
                phone()
            elif c == 9:
                print(" DOB: September", tuig)
                phone()
            elif c == 10:
                print(" DOB: October", tuig)
                phone()
            elif c == 11:
                print(" DOB: November", tuig)
                phone()
            elif c == 12:
                print(" DOB: December", tuig)
                phone()
            else:
                print(" No Dob Found...")
                phone()

    except:
        print(" Not Found....")
        phone()


def sugod():
    os.system("clear")
    print(loo)
    try:
        url = requests.get(
            "https://www.melissa.com/v2/lookups/personatorsearch/?name=&city=&state=&postalCode=&melissaAddressKey=&phoneNumber=5129144975emailAddress=&freeForm=&fmt=json&id="
            + key)
        data = json.loads(url.content.decode())
        info = data['Records']
        print(" \033[32mKey status is Up")

        menu = input("\n \33[93mSelect option [1-2]: ")

        if menu == "1":
            os.system('clear')
            phone()

        elif menu == "2":
            os.system('clear')
            name()

        elif menu == "main":
            os.system('clear')
            gmm()

        else:
            sugod()

    except:
        print(" \x1b[31mKey status is Down = Please Update ur key")
        input(" Press Enter to Continue.....")
        os.system("clear")
        gmm()


def gmm():

    #os.system('mode con: cols=51 lines=24')

    print(lo)
    try:
        
        balance_data = client.api.v2010.balance.fetch()
        balance = float(balance_data.balance)
        currency = balance_data.currency
        
        
        print(f'\033[32m \n    Your account has {balance:.2f} Credits left.')

    except:
        print("\033[32m  [!] Please contact Edmark for the Account.")
        print(f'\x1b[31m \n     Your account has 0 Credits left!.')
        

    print(kk)
    godmode = input("\x1b[31m Select Option: \033[32m")

    if godmode == '1':
        os.system('clear')
        print(lo)
        
        auto()

    elif godmode == '2':
        os.system('clear')
        af = open("username.txt", "w")
        fa = open("passwd.txt", "w")
        u = input(" enter user: ")
        af.write(u)
        p = input(" enter pass: ")
        fa.write(p)
        af.close()
        fa.close()
        input(" Please reopen the app!")
        os.system('clear')
        gmm()

    elif godmode == "key":
        os.system('clear')
        af = open("key.txt", "w")
        u = input(" enter key: ")
        af.write(u)
        af.close()
        input(" Please reopen the app!")
        os.system('clear')
        gmm()

    elif godmode == '3':
        
        os.system('clear')
        print("\033[32m\n User: ", a)
        print(" Pass: ", t)
        input(" \n\n\n\n press Enter to continue....")
        os.system('clear')
        gmm()

    elif godmode == '4':
        os.system('clear')
        print(about)
        input("\n    press Enter to continue....")
        os.system('clear')
        gmm()

    elif godmode == "search":
        os.system('clear')
        sugod()

    elif godmode == "email":
        os.system("clear")
        autoe()

    else:
        print(" Please select from [1-4] option")
        input("\n Please Enter to continue...")
        os.system('clear')
        gmm()





gmm()

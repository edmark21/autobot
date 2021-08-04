
import json,urllib.request
import os, sys
os.system('clear')
lo = '''\033[1;33m
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
print(lo)
#def acc():
	
#c = input("\33[34mEnter code: ")
#os.system('clear')
def main():
  c = input("Enter code: ")
  for x in range(20):
    print("\x1b[34m\ncredits: ", x ,"/ 20")
    n = input("\033[1;33mEnter number#: ")
    data = urllib.request.urlopen("https://trial.serviceobjects.com/gppl2/api.svc/PhoneInfo/"+n+"/full/"+c+"?format=json").read()
    output = json.loads(data)
    
    d = (output['PhoneInfo']['Provider'])
    dd = (output['PhoneInfo']['Contacts'])
    print ('\033[32m\nName: '+dd[0]['Name'])
    print ("Steet: "+dd[0]['Address'])
    print ("City: "+dd[0]['City'])
    print ("State: "+dd[0]['State'])
    main()
    
main()


#WS77-RMB3-HQP1 


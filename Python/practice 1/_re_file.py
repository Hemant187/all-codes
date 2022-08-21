import re
import requests

url ='https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/'
msg = requests.get(url).text
msg = msg.splitlines()

patt = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]", msg)
print(patt)
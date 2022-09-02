import csv
import requests
import africastalking as at
from decouple import config

at_username="swahilipothub"
at_api_key="22735d168a4718ff2e22d5cd21118df88b928fc7f708bf4ec8ced24b26db2747"
at_sender="Swahilipot"

at.initialize(at_username, at_api_key)
sms = at.SMS
sms_text = "Greetings from GOYN. Are you still interested in joining the Home-based caregiver training course? If yes, we welcome you to take this test. https://forms.gle/f2o2nYe2Gs7VWsJc6 Thank you!"

api_key = "2f1432e2014d4dec91263ec85f23acdc6db37"

def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

op = open("./upload/small_file.csv", "r")
dt = csv.DictReader(op)
print(dt)
up_dt = []
for r in dt:
	# print(r)
    number = r['Mobile Number']
    name = r['Name']
    url = r['Url']
    if number:
        if number.startswith('0'):
            number = '+254' + number[1:]
        elif number.startswith('7' or '1' or '4'):
            number = '+254' + number
        elif number.startswith('254'):
            number = '+' + number
    if r['Name']:
        message = f"Hi {r['Name'].split()[0]}, {sms_text}"
    
    if r['Url'] and r['Name']:
        message = f"Hi {r['Name'].split()[0]}, {sms_text} \n\n Link: {url}"
    
    if r['Url']:
        message = f"{sms_text} \n\n Link: {url}"
    
    else:
        message = sms_text
    at_sender = config("sender", default=None)

    try:
        sms.send(message, [number], at_sender, callback=on_finish)
        
    except Exception as e:
        print(f'Uh oh we have a problem: {e}')
    
    # if r['Url']:
    #     url = r['Url']
    #     api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    #     data = requests.get(api_url).json()["url"]
    #     if data["status"] == 7:
    #         shortened_url = data["shortLink"]
    #         row = {'Name': r['Name'],
    #             'Mobile Number': r['Mobile Number'],
    #             'Url': r['Url'],
    #             'Short Url': shortened_url}
    #         up_dt.append(row)
# print(up_dt)
# op.close()
# op = open("./output/small_file_output.csv", "w", newline='')
# headers = ['Name', 'Mobile Number', 'Url', 'Short Url']
# data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
# data.writerow(dict((heads, heads) for heads in headers))
# data.writerows(up_dt)

# op.close()
    
import csv
import requests
from time import sleep

api_key = "2f1432e2014d4dec91263ec85f23acdc6db37"

op = open("./upload/update.csv", "r")
dt = csv.DictReader(op)
up_dt = []
for r in dt:
    url = r['Url']
    try:
        if url:
            api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
            data = requests.get(api_url).json()["url"]
            if data["status"] == 7 and data["shortLink"]:
                shortened_url = data["shortLink"]
                row = {
                    'Mobile Number': r['Mobile Number'],
                    'Url': url,
                    'Short Url': shortened_url}
                up_dt.append(row)
                print(up_dt)
                sleep(10)
    except Exception as e:
        print(f'Uh oh we have a problem: {e}')

print(up_dt)
op.close()
op = open("./output/output.csv", "w", newline='')
headers = ['Mobile Number', 'Url', 'Short Url']
data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
data.writerow(dict((heads, heads) for heads in headers))
data.writerows(up_dt)
op.close()
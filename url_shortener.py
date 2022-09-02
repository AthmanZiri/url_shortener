import requests
import csv
import io

# account credentials
username = "athmanziri"
password = "25w*b>*LcC(B(<n"

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
access_token = ''
if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get access token, exiting...")

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

csv_file = open('file.csv', mode='r')
io_string = next(io.StringIO(csv_file))
# next(io_string)
reader = csv.reader(io_string, delimiter=',', quotechar='"')

for row in reader:
    name = row[0]
    number = row[1]
    url = row[2]

    if url:
        # url = "https://airtable.com/shrV8fQpwkoIJ83Ec?prefill_Record_ID=recvZEKYLStqhfRVn&prefill_Name%20of%20Respondent=GOYN-1893&prefill_What%27s%20your%20phone%20number%3F=%2B254711386207&prefill_Are%20you%20currently%20in%20school%3F=Yes&prefill_Have%20you%20completed%20primary%20school%20level%20of%20education%3F=Yes&prefill_Have%20you%20completed%20secondary%20level%20of%20education%3F=Yes&prefill_Have%20you%20completed%20any%20tertiary%20education%20level%3F%20College%20or%20university=&prefill_Which%20course%20did%20you%20take%3F%20E.g.%20%20Certificate%20in%20Project%20management%2C%20Diploma%20in%20Information%20technology%2C%20Bachelors%20of%20Degree%20Education%20=&prefill_Have%20you%20tried%20some%20vocational%20training%20in%20the%20last%20year=Yes&prefill_Which%20training%20course%20did%20you%20take%20%3F=Sign%20writer%2C%20painter%20%26%20printer%20designs"
        # make the POST request to get shortened URL for `url`
        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
        if shorten_res.status_code == 200:
            # if response is OK, get the shortened URL
            link = shorten_res.json().get("link")
            print("Shortened URL:", link)

# data_set = .read().decode("UTF-8")
# csv_file = open('file.csv', mode='r')
# io_string = io.StringIO(csv_file)
# next(io_string)
# reader = csv.reader(io_string, delimiter=',', quotechar='"')

# for row in reader:
#     name = row[0]
#     number = row[1]
#     url = row[2]

# the URL you want to shorten
# url = "https://airtable.com/shrV8fQpwkoIJ83Ec?prefill_Record_ID=recvZEKYLStqhfRVn&prefill_Name%20of%20Respondent=GOYN-1893&prefill_What%27s%20your%20phone%20number%3F=%2B254711386207&prefill_Are%20you%20currently%20in%20school%3F=Yes&prefill_Have%20you%20completed%20primary%20school%20level%20of%20education%3F=Yes&prefill_Have%20you%20completed%20secondary%20level%20of%20education%3F=Yes&prefill_Have%20you%20completed%20any%20tertiary%20education%20level%3F%20College%20or%20university=&prefill_Which%20course%20did%20you%20take%3F%20E.g.%20%20Certificate%20in%20Project%20management%2C%20Diploma%20in%20Information%20technology%2C%20Bachelors%20of%20Degree%20Education%20=&prefill_Have%20you%20tried%20some%20vocational%20training%20in%20the%20last%20year=Yes&prefill_Which%20training%20course%20did%20you%20take%20%3F=Sign%20writer%2C%20painter%20%26%20printer%20designs"
# # make the POST request to get shortened URL for `url`
# shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
# if shorten_res.status_code == 200:
#     # if response is OK, get the shortened URL
#     link = shorten_res.json().get("link")
#     print("Shortened URL:", link)




# api = "2f1432e2014d4dec91263ec85f23acdc6db37"


import requests

api_key = "2f1432e2014d4dec91263ec85f23acdc6db37"
# the URL you want to shorten
url = "https://www.thepythoncode.com/topic/using-apis-in-python"
# preferred name in the URL
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
# or
# api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
# make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)
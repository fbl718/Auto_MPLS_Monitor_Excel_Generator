import io
import sys
import urllib.request
import http.cookiejar


def auto_login():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    data = {'username': 'dc',
            'password': 'zaq12wsx'}
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}
    login_url = 'http://10.18.2.31/cs_system/admin/login.php'
    req = urllib.request.Request(login_url, headers=headers, data=post_data)
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    opener.open(req)
    url = 'http://10.18.2.31/cs_system/admin/index.php#monitor/mplscheckline'
    req = urllib.request.Request(url, headers=headers)
    opener.open(req)
    print('Successfully log in')

import requests
from requests import Session

session=Session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ABTEST=0|1541062039|v1; SUID=8F0980DF2028940A000000005BDABD98; SUID=8F0980DF1F13940A000000005BDABD9A; weixinIndexVisited=1; SUV=006F5960DF80098F5BDABDA0C3D1F729; SNUID=76F07927F9FD816F80D4A11AF947E9F0; ppinf=5|1541062099|1542271699|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2MzolRTAlQjglODglRTAlQjglQjglRTAlQjklOEElRTAlQjglOUElMjAlNUIlRTYlOUMlQkElRTYlOTklQkElNUR8Y3J0OjEwOjE1NDEwNjIwOTl8cmVmbmljazo2MzolRTAlQjglODglRTAlQjglQjglRTAlQjklOEElRTAlQjglOUElMjAlNUIlRTYlOUMlQkElRTYlOTklQkElNUR8dXNlcmlkOjQ0Om85dDJsdURILWFDLV8yNmpRUmVpVzR5UzB2dEVAd2VpeGluLnNvaHUuY29tfA; pprdig=YUL-UemIz8HW9MgBRVU0IkH2Dqz6nGILQsLxsF_wd3-QMP3pnjwQ8ipquiOa4liXkB-z3Aipt-F1BVd_LKmQsoh6I2k5Fly9mP_0w5peE6qXyeizGJmVppUFaJoM4lUFO6zl6euGpgBqC2kzrkbWZdfLhUlOcqwOeEvRzC0QW2Y; sgid=25-37744551-AVvavdMicSRGqaZXV3GZvGcU; sct=2; JSESSIONID=aaaddBJlNiiA2eOnObaBw; ppmdig=154114171500000097c6f4792e7f0c932ab5c0bc2c5d2c96; IPLOC=CN5101',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
proxies = {
    'http': 'http://89.189.183.183:8080',
    'https': 'https://89.189.183.183:8080'
}
session.headers.update(headers)
# session.proxies.update(proxies)
re=session.send(requests.Request(method="GET",url='https://weixin.sogou.com/weixin?query=NBA&type=2').prepare(),proxies=proxies,verify=False)
print(re.status_code)
print(re.text)
print(re.headers.get('origin'))
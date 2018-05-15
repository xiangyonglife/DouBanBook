import requests
import re

rsp = requests.get('https://book.douban.com/latest?icn=index-latestbook-all')
content = rsp.text

pattern = re.compile('<li.*?cover.*?href="(.*?)">.*?h2.*?<a.*?>(.*?)</a>', re.S)
result = re.findall(pattern, content)

##text = '书名%s链接%s'
        ##print(text%(result[1], result[0]))
        ##print('书名{}'.format(result[1]))
if result:
    print('书名\t\t\t\t\t\t链接\n')
    for result in result:
        print(result[1]+'\t\t\t', result[0]+'\n')

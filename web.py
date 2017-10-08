# coding:utf-8
import requests
import json

from datetime import datetime

def uploadSensorValues(date,freq,level):
    url = 'http://192.168.10.101:8888/sound_solution/sensvalues.php'

    sensorsdata = {'datetime':date,'freq':freq,'level':level}
    print (json.dumps(sensorsdata))

    headers = {'content-type': 'application/json'}

    res = requests.post(url, data=json.dumps(sensorsdata), headers=headers, verify=False)

    print (res.json())
    pass

def main():


#   変数宣言
    freq = 0.0    #周波数
    level = 0.0   #レベル
    date = 0
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    for cnt in open('sample.txt').readlines():
#       末尾のデータを格納
        data = cnt[:-1].split(' ')
        freq = data[0]
        level = data[1]
#       データベースの主キーにするための現在時刻の取得

#       データベースにアクセスし、指定のデータを書き込む
        uploadSensorValues(date,freq,level)


if __name__ == '__main__':
    main()

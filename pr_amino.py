# -*- coding: utf-8 -*-
import amino
import time
print("Скрипт написан Liberty. Ссылка на телеграм - @zeroday_0000")
client = amino.Client()

em = str(input('Введите email: '))
par = str(input('Введите passowrd: '))
mes = str(input('Введите текст: '))
vrem = int(input('Введите количество секунд между сообщениями: '))

client.login(email=em, password=par)
sc = client.sub_clients()
lis = []
print('Процесс')

for name, idc in zip(sc.name, sc.comId):
    print(name, idc)
    sub_client = amino.SubClient(comId=idc, profile=client.profile)
    for name, id in zip(sub_client.get_online_users(size=sub_client.get_online_users().userProfileCount).profile.nickname, sub_client.get_online_users(size=sub_client.get_online_users().userProfileCount).profile.userId):
        lis.append(id)
        time.sleep(vrem)
        try:

            sub_client.start_chat(userId=lis, message=mes)
            lis.remove(id)
        except Exception:
            pass
print('Работа завершена')

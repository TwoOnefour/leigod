import requests
import datetime
import hashlib


class Leigod:
    def __init__(self):
        self.session = requests.session()
        self.account_token = None
        self.username = None
        self.password = None
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
        }
        self.if_plain = False

    def encrypt(self, plain):
        m = hashlib.md5()
        m.update(plain.encode())
        return m.hexdigest()

    def login(self):
        if self.if_plain:
            self.password = self.encrypt(self.password)
        res = self.session.post("https://webapi.leigod.com/wap/login/bind", json={
            "password": self.password,  # 密码的加密
            "lang": "en",
            "src_channel": "guanwang",
            "code": "",  # 不用填
            "user_type": "0",
            "username": self.username,
            "country_code": 86
        })
        res_json = res.json()
        if res_json["code"] != 0:
            print(f'{str(datetime.datetime.now())[:-7]}\t{res_json["msg"]}')
        else:
            self.account_token = res_json["data"]["login_info"]["account_token"]

    def pause(self):
        res = self.session.post("https://webapi.leigod.com/api/user/pause", json={
            "lang": "en",
            "account_token": self.account_token
        })
        res_json = res.json()
        if res_json["code"] == 0:
            print(f"{str(datetime.datetime.now())[:-7]}\t暂停成功")
        else:
            print(f'{str(datetime.datetime.now())[:-7]}\t{res_json["msg"]}')

    def logout(self):
        pass

    def run(self):
        self.login()
        self.pause()


if __name__ == "__main__":
    leigod = Leigod()
    leigod.username = ""  # 填入账号
    leigod.password = ""  # 填入密码, 如果不想填入明文密码，请直接修改为md5，并把下面的if_plain改成False
    leigod.if_plain = True
    leigod.run()

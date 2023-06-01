import requests
import datetime
import hashlib


class Leigod:
    def __init__(self):
        self.session = requests.session()
        self.account_token = None

    def encrypt(self, plain):
        m = hashlib.md5()
        m.update(plain.encode())
        return m.hexdigest()

    def login(self):
        password = self.encrypt("")  #  填入密码
        res = self.session.post("https://webapi.leigod.com/wap/login/bind", json={
            "password": password,  # 密码的加密
            "lang": "en",
            "src_channel": "guanwang",
            "code": "",  # 不用填
            "user_type": "0",
            "username": "",  # 填入账号
            "country_code": 86
        })
        res_json = res.json()
        if res_json["code"] != 0:
            print(res_json["msg"])
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
    leigod.run()

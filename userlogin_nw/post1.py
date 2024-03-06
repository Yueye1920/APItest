import json

import allure
import requests
import pytest

'''带参数的post请求'''

@allure.feature('用户登录')
class Testlogin:
    # 请求行
    url_login = 'http://10.17.8.228/missLogin/sso/v1/userlogin'
    # 请求头
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    @allure.story("登录成功")
    def test_login_success(self):
        # 请求体
        login_data = {
            "username": "Vzk5OTExMQ==",
            "password": "Yjg0ZDdmOGQ0ZmE3NzEzZTcwMmFiMGQ5ZDI2MzJkNzU=",
            "captcha": "MjAyNA=="
        }
        # 发起请求（url,data=bady,headers=headers）
        req_login_success = requests.post(self.url_login, data=login_data, headers=self.headers)
        # 响应体转json格式
        response_successs = req_login_success.json()
        # 打印响应体数据
        # print(req_login.text)

        # 此时为python对象字典
        # print(type(response))
        print(response_successs)
        # 响应体美化json
        response_json = json.dumps(response_successs, ensure_ascii=False, indent=4)
        # 此时为字符串
        # print(type(response_json))
        # print(response_json)

        # 提取token
        token = response_successs['tokenid']
        print('tokenid:', token)

        response_code = response_successs.get('code')
        response_result = response_successs.get('result')

        assert req_login_success.status_code == 200
        assert response_successs['tokenid']
        assert response_code == "201"
        assert response_result == "登录成功"

    @allure.story("用户名错误，登录失败")
    def test_login_username_error(self):
        # 请求体
        login_data = {
            "username": "Vzk5OTExMQ",
            "password": "Yjg0ZDdmOGQ0ZmE3NzEzZTcwMmFiMGQ5ZDI2MzJkNzU=",
            "captcha": "MjAyNA=="
        }
        # 发起请求（url,data=bady,headers=headers）
        req_login_user_error = requests.post(self.url_login, data=login_data, headers=self.headers)
        # 响应体转json格式
        response_user_error = req_login_user_error.json()
        # 打印响应体数据
        # print(req_login.text)

        # 此时为python对象字典
        # print(type(response))
        print(response_user_error)
        # 响应体美化json
        response_json = json.dumps(response_user_error, ensure_ascii=False, indent=4)
        # 此时为字符串
        # print(type(response_json))
        # print(response_json)

        response_code = response_user_error.get('code')
        response_result = response_user_error.get('result')

        assert req_login_user_error.status_code == 200
        assert response_code == "422"
        assert response_result == "登录失败"

    @allure.story("密码错误，登录失败")
    def test_login_password_error(self):
        # 请求体
        login_data = {
            "username": "Vzk5OTExMQ==",
            "password": "Yjg0ZDdmOGQ0ZmE3NzEzZTcwMmFiMGQ5ZDI2MzJkNz",
            "captcha": "MjAyNA=="
        }
        # 发起请求（url,data=bady,headers=headers）
        req_login_word_error = requests.post(self.url_login, data=login_data, headers=self.headers)
        # 响应体转json格式
        response_word_error = req_login_word_error.json()
        # 打印响应体数据
        # print(req_login.text)

        # 此时为python对象字典
        # print(type(response))
        print(response_word_error)
        # 响应体美化json
        response_json = json.dumps(response_word_error, ensure_ascii=False, indent=4)
        # 此时为字符串
        # print(type(response_json))
        # print(response_json)

        response_code = response_word_error.get('code')
        response_result = response_word_error.get('result')

        assert req_login_word_error.status_code == 200
        assert response_code == "422"
        assert response_result == "登录失败"


if __name__ == '__main__':
    # Testlogin.test_login_pass()
    # Testlogin.test_login_username_error()
    # Testlogin()
    pytest.main()


# 执行测试用例
# pytest post1.py --alluredir allure-results/
# 生成报告
# allure generate allure-results -o allure-reports/ --clean
# 打开报告
# allure open allure-reports/

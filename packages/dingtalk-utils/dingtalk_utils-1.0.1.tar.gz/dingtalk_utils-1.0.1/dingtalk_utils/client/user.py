import requests

from dingtalk_utils.client.setting import API_URL


class UserClient(object):
    def __init__(self, clientSecret, clientId, authCode, grantType: str = 'authorization_code'):
        '''
        :param clientSecret: 应用密钥。企业内部应用传应用的AppSecret，第三方企业应用传应用的SuiteSecret，第三方个人应用传应用的AppSecret
        :param clientId: 应用id。可使用扫码登录应用或者第三方个人小程序的appId。企业内部应用传应用的AppKey，
                        第三方企业应用传应用的SuiteKey，第三方个人应用传应用的AppId
        :param authCode:  OAuth 2.0 临时授权码
        :param grantType:  如果使用授权码换token，传authorization_code。如果使用刷新token换用户token，传refresh_token。
        '''
        self.clientSecret = clientSecret
        self.clientId = clientId
        self.code = authCode
        self.grantType = grantType

    def get_user_token(self):
        '''
        :return:{"expireIn":7200,"accessToken":"oubwyu5aenfbesctlwwxpis6rzndlm1a","refreshToken":"oubwyu5aenfbesctlwwxpis6rzndlm1a"}
        '''
        resp = requests.post(API_URL + '/v1.0/oauth2/userAccessToken', json={
            "clientSecret": self.clientSecret,
            "clientId": self.clientId,
            "code": self.code,
            "grantType": self.grantType
        }).json()
        return resp

    def get_userinfo(self, token, unionId: str = 'me'):
        '''
        :token: get_token 获取到的accessToken
        :return:
        {
          "nick" : "zhangsan",
          "avatarUrl" : "https://xxx",
          "mobile" : "150xxxx9144",
          "openId" : "123",
          "unionId" : "z21HjQliSzpw0Yxxxx",
          "email" : "zhangsan@alibaba-inc.com",
          "stateCode" : "86"
        }
        '''
        header = {
            "x-acs-dingtalk-access-token": token
        }
        resp = requests.get(API_URL + f'/v1.0/contact/users/{unionId}', headers=header).json()

        return resp

import requests

from dingtalk_utils.client.setting import OAPI_URL


class CorpClient(object):

    def __init__(self, appKey, appSecret):
        '''
        :param appKey: 应用的唯一标识key。
        :param appSecret: 应用的密钥。
        '''
        self.appKey = appKey
        self.appSecret = appSecret

    def get_corp_token(self):
        '''
        :return: {'errcode': 0, 'access_token': '7c1aedaa1d783c89826ee040de33a829', 'errmsg': 'ok', 'expires_in': 7200}
        '''
        resp = requests.get(OAPI_URL + '/gettoken', params={'appkey': self.appKey, 'appsecret': self.appSecret}).json()

        return resp


if __name__ == '__main__':
    c = CorpClient('ding96rniei5hi3hoivs', 'jhuytpenKWtvSJgk8fUBGoD3_V8JE4PRnxT5iQb5wOg4QammN73OtF0K-HeiJoBD')
    c.get_corp_token()

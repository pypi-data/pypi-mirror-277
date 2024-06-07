import requests
from dingtalk_utils.client.setting import OAPI_URL


class DepartmentApi(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def get_dept_detail(self, dept_id, language: str = 'zh_CN'):
        '''
        获取部门详情
        :param dept_id:
        :param language:
        :return:
        '''

        resp = requests.post(OAPI_URL + '/topapi/v2/department/get', params={'access_token': self.access_token},
                             json={'dept_id': dept_id, 'language': language}).json()
        return resp

    def get_dept_listSub(self, dept_id, language: str = 'zh_CN'):
        '''
        获取部门列表  https://oapi.dingtalk.com/topapi/v2/department/listsub
        :param dept_id:
        :param language:
        :return:
        '''

        resp = requests.post(OAPI_URL + '/topapi/v2/department/listsub', params={'access_token': self.access_token},
                             json={'dept_id': dept_id, 'language': language}).json()
        return resp

    def get_dept_child(self, dept_id):
        '''
        获取子部门ID列表  https://oapi.dingtalk.com/topapi/v2/department/listsubid
        :param dept_id:
        :return:
        '''

        resp = requests.post(OAPI_URL + '/topapi/v2/department/listsubid', params={'access_token': self.access_token},
                             json={'dept_id': dept_id}).json()
        return resp

import requests

from dingtalk_utils.client.setting import OAPI_URL


class ContactsApi(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def get_user(self, userid, language: str = 'zh_CN'):
        '''
        查询用户详情
        :param userid: 用户的userId
        :param language: 通讯录语言。zh_CN：中文（默认值）en_US：英文
        :return:
        {
        "errcode":"0",
        "result":{
                "extension":"{\"爱好\":\"旅游\",\"年龄\":\"24\"}",
                "unionid":"z21HjQliSzpw0YWCNxmxxxxx",
                "boss":"true",
                "role_list":{
                        "group_name":"职务",
                        "name":"总监",
                        "id":"100"
                },
                "exclusive_account":false,
                "manager_userid":"manager240",
                "admin":"true",
                "remark":"备注备注",
                "title":"技术总监",
                "hired_date":"1597573616828",
                "userid":"zhangsan",
                "work_place":"未来park",
                "dept_order_list":{
                        "dept_id":"2",
                        "order":"1"
                },
                "real_authed":"true",
                "dept_id_list":"[2,3,4]",
                "job_number":"4",
                "email":"test@xxx.com",
                "leader_in_dept":{
                        "leader":"true",
                        "dept_id":"2"
                },
                "mobile":"18512345678",
                "active":"true",
                "telephone":"010-86123456-2345",
                "avatar":"xxx",
                "hide_mobile":"false",
                "senior":"true",
                "name":"张三",
                "union_emp_ext":{
                        "union_emp_map_list":{
                                "userid":"5000",
                                "corp_id":"dingxxx"
                        },
                        "userid":"500",
                        "corp_id":"dingxxx"
                },
                "state_code":"86"
        },
        "errmsg":"ok"
}
        '''
        resp = requests.post(OAPI_URL + '/topapi/v2/user/get', params={'access_token': self.access_token}, json={
            "language": language,
            "userid": userid
        }).json()
        return resp


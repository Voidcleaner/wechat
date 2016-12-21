import requests
import json
from core.server.wxconfig import WxConfig
from core.cache.tokencache import TokenCache
from core.logger_helper import logger
from core.server.wxauthorize import WxAuthorServer


class WxKF(object):
    _token_cache = TokenCache()
    _wx_author_server = WxAuthorServer()

    def add_kf(self):
        access_token = self._token_cache.get_cache(
            self._token_cache.KEY_ACCESS_TOKEN)
        if access_token:

            url = WxConfig.add_kf + access_token
            data = self.add_kf_data()
            r = requests.post(url, data.encode('utf-8'))
            logger.debug('【微信多客服系统】Response' + str(r.status_code))
            if r.status_code == 200:
                res = r.text
                logger.debug('[微信多客服系统]' + res)
                json_res = json.loads(res)
                if 'errcode' in json.loads(res):
                    errcode = json_res['errcode']
                    return errcode
        else:
            logger.error('微信多客服系统获取不到access_token')

    def add_kf_data(self):
        '''创建客服数据'''
        kf_data = {'kf_account': 'bzw_lolface@a30040693的接口测试号',
                   'nickname': '小包'}
        KF_DATA = json.dumps(kf_data, ensure_ascii=False)
        logger.debug('【微信客服创建客服数据KF_DATA[' + str(KF_DATA) + ']')
        return KF_DATA


    def invite_kf(self):
        access_token = self._token_cache.get_cache(
            self._token_cache.KEY_ACCESS_TOKEN)

        if access_token:

            url = WxConfig.invite_kf + access_token
            invite_data = {'kf_account' : 'bzw_lolface@a30040693的接口测试号',
                           'invite_wx': 'bzw_lolface'}
            r = requests.post(url,json.dumps(
                invite_data, ensure_ascii=False).encode('utf-8'))
            logger.debug('[微信多客服系统]Response' + str(r.status_code))
            if r.status_code == 200:
                res = r.text
                logger.debug('[微信多客服系统]' + res)
                json_res = json.loads(res)
                if 'errcode' in json.loads(res):
                    errcode = json_res('errcode')
                    return errcode
        else:
            logger.error('[微信多客服系统获取不到access_token]')

if __name__ == '__main__':
    wx_kf_server = WxKF()

    wx_kf_server.add_kf()

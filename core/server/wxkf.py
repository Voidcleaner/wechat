import requests
import json
from core.server.wxconfig import Wxconfig
from core.server.tokencache import TokenCache
from core.logger_helper import logger
from core.server.wxauthorize import WxAuthorServer


class WxKF(object):
    _token_cache = TokenCache()
    _wx_author_server = WxAuthorServer()

    def add_kf(self):
        access_token = self._token_cache.get_cache(
            self._token_cache.KEY_ACCESS_TOKEN)
        if access_token:

            url = Wxconfig.kf_add_url + access_token
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
        pass

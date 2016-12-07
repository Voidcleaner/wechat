from core.cache.basecache import BaseCache
from core.logger_helper import logger

class TokenCache(BaseCache):

    _expire_access_token = 7200
    _expire_js_token = 30 * 24 * 3600
    KEY_ACCESS_TOKEN = 'access_token'
    KEY_JSAPI_TICKET = 'jsapi_ticket'

    def set_access_cache(self, key, value):

        res = self.redis_ctl.set(key, value)
        self.redis_ctl.expire(key, self._expire_access_token)
        logger.debug('[微信token缓存]setCache>>>key[%s],value[%s]' %(key, value))
        return res


    def set_js_cache(self, key, value):

        res= self.redis_ctl.set(key, value)
        self.redis_ctl.expire(key, self._expire_js_token)
        logger.debug('[微信token缓存]setCache>>>key[%s],value[%s]' % (key, value))
        return res

    def get_cache(self, key):

        try:
            v = (self.redis_ctl.get(key)).decode('utf-8')
            logger.debug(v)
            logger.debug('[微信token缓存]getCache>>>key[%s],value[%s]' % (key, value))
            return v
        except Exception:
            return None

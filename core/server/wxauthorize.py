from core.logger_helper import logger
import hashlib
import tornado.web
import time
import urllib
from urllib import parse
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class WxSignatureHandler(tornado.web.RequestHandler):
    """

    微信服务器签名验证, 消息回复
    check_signature: 校验signature是否正确

    """
    def data_received(self, chunk):
        pass

    def get(self):
        try:
            signature = self.get_argument('signature')
            timestamp = self.get_argument('timestamp')
            nonce = self.get_argument('nonce')
            echostr = self.get_argument('echostr')
            logger.debug('微信sign校验,signature=' + signature + ',&timestamp=' + timestamp
                         + '&nonce=' + nonce + '&echostr=' + echostr)
            result = self.check_signature(signature, timestamp, nonce)
            if result:
                logger.debug('微信sign校验,返回echostr=' + echostr)
                self.write(echostr)
            else:
                logger.error('微信sign校验,---校验失败')
        except Exception as e:
            logger.error('微信sign校验,---Exception' + str(e))

    def check_signature(self, signature, timestamp, nonce):
        """校验token是否正确"""
        token = 'test12345'
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        logger.debug('sha1=' + sha1 + '&signature=' + signature)
        return sha1 == signature

    def post(self):
        body = self.request.body
        logger.debug('微信消息回复中心收到用户消息' + str(body.decode('utf-8')))
        data = ET.fromstring(body)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        MsgType = data.find('MsgType').text
        if MsgType == 'event':
            '''接收事件推送'''
            try:
                Event = data.find('Event').text
                if Event == 'subscribe':
                    # 关注事件
                    CreateTime = int(time.time())
                    reply_content = '欢迎关注我们的公众号~'
                    out = self.reply_text(FromUserName, ToUserName, CreateTime, reply_content)
                    self.write(out)
            except:
                pass
    def reply_text(self, FromUserName, ToUserName, CreateTime, Content):
        '''回复文本消息模板'''
        textTpl = """<xml> <ToUserName><![CDATA[%s]]></ToUserName> <FromUserName><![CDATA[%s]]></FromUserName> <CreateTime>%s</CreateTime> <MsgType><![CDATA[%s]]></MsgType> <Content><![CDATA[%s]]></Content></xml>"""
        out = textTpl % (FromUserName, ToUserName, CreateTime, 'text', Content)
        return out

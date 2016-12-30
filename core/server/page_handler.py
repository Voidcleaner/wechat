import tornado.web
import core.server.sms


class PageHandler(tornado.web.RequestHandler):
    """
    微信handler处理类
    """

    def get(self, flag):

        if flag == 'index':
            '''首页'''
            self.render('index.html')

        if flag == 'login':
            '''注册及登录'''
            self.render('login.html')
            

    def post(self, flag):
        if flag == 'register':

            phone_number = self.get_argument('phone')
            code = self.get_argument('code')
            if code == '':
                error_msg = '请输入验证码'
            elif sms.verify(number, code):
                self.render('success.html')
            else:
                error_msg = '验证码错误,请重新输入'


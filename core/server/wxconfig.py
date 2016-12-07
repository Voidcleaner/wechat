class WxConfig(object):

    AppID = 'wx574ae3890c06b945'
    AppSecret = '4120b03a73416d01a60c827cf9bb2a81'

    config_get_access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (AppID, AppSecret)

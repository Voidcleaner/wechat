

class WxConfig(object):
    """
    微信开发--基础配置

    """
    AppID = 'wx574ae3890c06b945'  # AppID(应用ID)
    AppSecret = '4120b03a73416d01a60c827cf9bb2a81'  # AppSecret(应用密钥)

    """微信网页开发域名"""
    AppHost = '144.48.4.116'

    '''获取access_token'''
    config_get_access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (AppID, AppSecret)

    '''自定义菜单创建接口'''
    menu_create_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='

    '''自定义菜单查询接口'''
    menu_get_url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token='

    '''自定义菜单删除接口'''
    menu_delete_url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='

    '''多客服接口'''

    kf_inquire_url = 'https://api.weixin.qq.com/cgi-bin/customservice/getkflist?access_token='
    kf_online_inquire_url = 'https://api.weixin.qq.com/cgi-bin/customservice/getonlinekflist?access_token='



    '''微信公众号菜单映射数据'''
    """重定向后会带上state参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节"""
    wx_menu_state_map = {
        'menuIndex0': '%s/page/index' % AppHost,  # 测试菜单1
    }


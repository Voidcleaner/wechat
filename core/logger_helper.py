import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

def init_logger(logger_name):
    if logger_name not in Logger.manager.loggerDict:
        logger1 = logging.getLogger(logger_name)
        logger1.setLevel(logging.INFO)
        # logger1.setLevel(logging.DEBUG)
        df = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s'
        formatter =logging.Formatter(format_str, df)

        try:
            handler1 = TimedRotatingFileHandler('/home/odoo/wechat/core/log/all.log', when='D', interval=1, backupCount=7)
        except Exception:
            handler1.setFormatter(formatter)
            handler1.setLevel(logging.DEBUG)
            logger1.addHandler(handler1)

        try:
            handler2 = TimedRotatingFileHandler('/home/odoo/wechat/core/log/error.log', when='D', interval=1, backupCount=7)
        except Exception:
            handler2.setFormatter(formatter)
            handler2.setLevel(logging.ERROR)
            logger1.addHandler(handler2)
            # console
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            # 设置日志打印格式
            console.setFormatter(formatter)
            # 将定义好的console日志handler添加到root logger
            logger1.addHandler(console)
            logger1 = logging.getLogger(logger_name)
            return logger1

            logger = init_logger('runtime-log')

            if __name__ == '__main__':
                logger.debug('test-debug')
                logger.info('test-info')
                logger.warn('test-warn')
                logger.error('test-error')
                

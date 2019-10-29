from aiologstash import TCPLogstashHandler
import logging
import asyncio

class MyHandler(TCPLogstashHandler):

    def __init__(self, host, port, extra, **kwargs):
        super().__init__(host=host, port=port,
                         level=logging.NOTSET, close_timeout=5, reconnect_delay=1, reconnect_jitter=0.3,
                         qsize=10000, extra=extra, loop=asyncio.get_event_loop())



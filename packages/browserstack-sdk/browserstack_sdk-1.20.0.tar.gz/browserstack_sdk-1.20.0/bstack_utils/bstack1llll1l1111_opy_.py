# coding: UTF-8
import sys
bstack11lll_opy_ = sys.version_info [0] == 2
bstack1llll11_opy_ = 2048
bstack1lll111_opy_ = 7
def bstack11l11ll_opy_ (bstack11l111l_opy_):
    global bstack11l1l_opy_
    bstack1l1l11l_opy_ = ord (bstack11l111l_opy_ [-1])
    bstack1l1ll11_opy_ = bstack11l111l_opy_ [:-1]
    bstack1llll1l_opy_ = bstack1l1l11l_opy_ % len (bstack1l1ll11_opy_)
    bstack1l1l111_opy_ = bstack1l1ll11_opy_ [:bstack1llll1l_opy_] + bstack1l1ll11_opy_ [bstack1llll1l_opy_:]
    if bstack11lll_opy_:
        bstack111ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1llll11_opy_ - (bstack11l1l11_opy_ + bstack1l1l11l_opy_) % bstack1lll111_opy_) for bstack11l1l11_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack111ll1l_opy_ = str () .join ([chr (ord (char) - bstack1llll11_opy_ - (bstack11l1l11_opy_ + bstack1l1l11l_opy_) % bstack1lll111_opy_) for bstack11l1l11_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack111ll1l_opy_)
import threading
bstack1llll11l1l1_opy_ = 1000
bstack1llll11ll1l_opy_ = 5
bstack1llll11l1ll_opy_ = 30
bstack1llll11llll_opy_ = 2
class bstack1llll11lll1_opy_:
    def __init__(self, handler, bstack1llll111lll_opy_=bstack1llll11l1l1_opy_, bstack1llll111l1l_opy_=bstack1llll11ll1l_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1llll111lll_opy_ = bstack1llll111lll_opy_
        self.bstack1llll111l1l_opy_ = bstack1llll111l1l_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack1llll11l111_opy_()
    def bstack1llll11l111_opy_(self):
        self.timer = threading.Timer(self.bstack1llll111l1l_opy_, self.bstack1llll11l11l_opy_)
        self.timer.start()
    def bstack1llll11ll11_opy_(self):
        self.timer.cancel()
    def bstack1llll111ll1_opy_(self):
        self.bstack1llll11ll11_opy_()
        self.bstack1llll11l111_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1llll111lll_opy_:
                t = threading.Thread(target=self.bstack1llll11l11l_opy_)
                t.start()
                self.bstack1llll111ll1_opy_()
    def bstack1llll11l11l_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack1llll111lll_opy_]
        del self.queue[:self.bstack1llll111lll_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1llll11ll11_opy_()
        while len(self.queue) > 0:
            self.bstack1llll11l11l_opy_()
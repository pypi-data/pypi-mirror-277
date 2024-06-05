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
class bstack1l1l1111l1_opy_:
    def __init__(self, handler):
        self._1llll11111l_opy_ = None
        self.handler = handler
        self._1llll1111ll_opy_ = self.bstack1llll111l11_opy_()
        self.patch()
    def patch(self):
        self._1llll11111l_opy_ = self._1llll1111ll_opy_.execute
        self._1llll1111ll_opy_.execute = self.bstack1llll1111l1_opy_()
    def bstack1llll1111l1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l11ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤᒮ"), driver_command, None, this, args)
            response = self._1llll11111l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l11ll_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᒯ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1llll1111ll_opy_.execute = self._1llll11111l_opy_
    @staticmethod
    def bstack1llll111l11_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
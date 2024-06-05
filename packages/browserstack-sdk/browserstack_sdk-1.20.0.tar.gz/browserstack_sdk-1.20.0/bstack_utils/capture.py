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
import sys
class bstack11llll1l11_opy_:
    def __init__(self, handler):
        self._11l1l11ll1_opy_ = sys.stdout.write
        self._11l1l11l1l_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11l1l11l11_opy_
        sys.stdout.error = self.bstack11l1l11lll_opy_
    def bstack11l1l11l11_opy_(self, _str):
        self._11l1l11ll1_opy_(_str)
        if self.handler:
            self.handler({bstack11l11ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ༌"): bstack11l11ll_opy_ (u"ࠪࡍࡓࡌࡏࠨ།"), bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༎"): _str})
    def bstack11l1l11lll_opy_(self, _str):
        self._11l1l11l1l_opy_(_str)
        if self.handler:
            self.handler({bstack11l11ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ༏"): bstack11l11ll_opy_ (u"࠭ࡅࡓࡔࡒࡖࠬ༐"), bstack11l11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ༑"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11l1l11ll1_opy_
        sys.stderr.write = self._11l1l11l1l_opy_
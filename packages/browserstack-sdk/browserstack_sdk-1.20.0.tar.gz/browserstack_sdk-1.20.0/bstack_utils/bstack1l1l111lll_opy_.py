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
from collections import deque
from bstack_utils.constants import *
class bstack1l1ll1ll1l_opy_:
    def __init__(self):
        self._1lllll1ll1l_opy_ = deque()
        self._1llllll1l11_opy_ = {}
        self._1lllll1lll1_opy_ = False
    def bstack1llllll11l1_opy_(self, test_name, bstack1lllll1l1l1_opy_):
        bstack1lllll11lll_opy_ = self._1llllll1l11_opy_.get(test_name, {})
        return bstack1lllll11lll_opy_.get(bstack1lllll1l1l1_opy_, 0)
    def bstack1lllll1ll11_opy_(self, test_name, bstack1lllll1l1l1_opy_):
        bstack1lllll11ll1_opy_ = self.bstack1llllll11l1_opy_(test_name, bstack1lllll1l1l1_opy_)
        self.bstack1lllll1l111_opy_(test_name, bstack1lllll1l1l1_opy_)
        return bstack1lllll11ll1_opy_
    def bstack1lllll1l111_opy_(self, test_name, bstack1lllll1l1l1_opy_):
        if test_name not in self._1llllll1l11_opy_:
            self._1llllll1l11_opy_[test_name] = {}
        bstack1lllll11lll_opy_ = self._1llllll1l11_opy_[test_name]
        bstack1lllll11ll1_opy_ = bstack1lllll11lll_opy_.get(bstack1lllll1l1l1_opy_, 0)
        bstack1lllll11lll_opy_[bstack1lllll1l1l1_opy_] = bstack1lllll11ll1_opy_ + 1
    def bstack1llll1l11l_opy_(self, bstack1llllll11ll_opy_, bstack1lllll1l1ll_opy_):
        bstack1llllll1111_opy_ = self.bstack1lllll1ll11_opy_(bstack1llllll11ll_opy_, bstack1lllll1l1ll_opy_)
        bstack1lllll1l11l_opy_ = bstack11l11lll1l_opy_[bstack1lllll1l1ll_opy_]
        bstack1llllll111l_opy_ = bstack11l11ll_opy_ (u"ࠦࢀࢃ࠭ࡼࡿ࠰ࡿࢂࠨᑕ").format(bstack1llllll11ll_opy_, bstack1lllll1l11l_opy_, bstack1llllll1111_opy_)
        self._1lllll1ll1l_opy_.append(bstack1llllll111l_opy_)
    def bstack1lll1lll1_opy_(self):
        return len(self._1lllll1ll1l_opy_) == 0
    def bstack11ll11l11_opy_(self):
        bstack1lllll1llll_opy_ = self._1lllll1ll1l_opy_.popleft()
        return bstack1lllll1llll_opy_
    def capturing(self):
        return self._1lllll1lll1_opy_
    def bstack1l1l111l_opy_(self):
        self._1lllll1lll1_opy_ = True
    def bstack1ll1111l1l_opy_(self):
        self._1lllll1lll1_opy_ = False
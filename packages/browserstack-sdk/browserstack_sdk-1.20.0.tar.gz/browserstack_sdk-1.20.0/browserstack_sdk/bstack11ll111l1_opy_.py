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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1111l1ll_opy_ as bstack1l1l111ll_opy_
from browserstack_sdk.bstack1ll11l111l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l1lll_opy_
class bstack1llllllll1_opy_:
    def __init__(self, args, logger, bstack11ll1lll11_opy_, bstack11ll11lll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1lll11_opy_ = bstack11ll1lll11_opy_
        self.bstack11ll11lll1_opy_ = bstack11ll11lll1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lllll11l1_opy_ = []
        self.bstack11ll11llll_opy_ = None
        self.bstack1lll111ll_opy_ = []
        self.bstack11ll1l1l1l_opy_ = self.bstack1l1l1l1111_opy_()
        self.bstack1l1ll1llll_opy_ = -1
    def bstack1l11lll11_opy_(self, bstack11ll1ll11l_opy_):
        self.parse_args()
        self.bstack11ll1ll1ll_opy_()
        self.bstack11ll1l1l11_opy_(bstack11ll1ll11l_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11ll1l111l_opy_():
        import importlib
        if getattr(importlib, bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧำ"), False):
            bstack11ll1ll111_opy_ = importlib.find_loader(bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬิ"))
        else:
            bstack11ll1ll111_opy_ = importlib.util.find_spec(bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ี"))
    def bstack11ll1l11ll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1ll1llll_opy_ = -1
        if self.bstack11ll11lll1_opy_ and bstack11l11ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬึ") in self.bstack11ll1lll11_opy_:
            self.bstack1l1ll1llll_opy_ = int(self.bstack11ll1lll11_opy_[bstack11l11ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ื")])
        try:
            bstack11ll1l1ll1_opy_ = [bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳุࠩ"), bstack11l11ll_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶูࠫ"), bstack11l11ll_opy_ (u"ࠩ࠰ࡴฺࠬ")]
            if self.bstack1l1ll1llll_opy_ >= 0:
                bstack11ll1l1ll1_opy_.extend([bstack11l11ll_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ฻"), bstack11l11ll_opy_ (u"ࠫ࠲ࡴࠧ฼")])
            for arg in bstack11ll1l1ll1_opy_:
                self.bstack11ll1l11ll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11ll1ll1ll_opy_(self):
        bstack11ll11llll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11ll11llll_opy_ = bstack11ll11llll_opy_
        return bstack11ll11llll_opy_
    def bstack1llll1l1l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11ll1l111l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111l1lll_opy_)
    def bstack11ll1l1l11_opy_(self, bstack11ll1ll11l_opy_):
        bstack1ll1111l1_opy_ = Config.bstack11l11l11_opy_()
        if bstack11ll1ll11l_opy_:
            self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ฽"))
            self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"࠭ࡔࡳࡷࡨࠫ฾"))
        if bstack1ll1111l1_opy_.bstack11ll1l11l1_opy_():
            self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭฿"))
            self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠨࡖࡵࡹࡪ࠭เ"))
        self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠩ࠰ࡴࠬแ"))
        self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨโ"))
        self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ใ"))
        self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬไ"))
        if self.bstack1l1ll1llll_opy_ > 1:
            self.bstack11ll11llll_opy_.append(bstack11l11ll_opy_ (u"࠭࠭࡯ࠩๅ"))
            self.bstack11ll11llll_opy_.append(str(self.bstack1l1ll1llll_opy_))
    def bstack11ll1ll1l1_opy_(self):
        bstack1lll111ll_opy_ = []
        for spec in self.bstack1lllll11l1_opy_:
            bstack1l1ll111l1_opy_ = [spec]
            bstack1l1ll111l1_opy_ += self.bstack11ll11llll_opy_
            bstack1lll111ll_opy_.append(bstack1l1ll111l1_opy_)
        self.bstack1lll111ll_opy_ = bstack1lll111ll_opy_
        return bstack1lll111ll_opy_
    def bstack1l1l1l1111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11ll1l1l1l_opy_ = True
            return True
        except Exception as e:
            self.bstack11ll1l1l1l_opy_ = False
        return self.bstack11ll1l1l1l_opy_
    def bstack111llll1_opy_(self, bstack11ll1l1111_opy_, bstack1l11lll11_opy_):
        bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧๆ")] = self.bstack11ll1lll11_opy_
        multiprocessing.set_start_method(bstack11l11ll_opy_ (u"ࠨࡵࡳࡥࡼࡴࠧ็"))
        bstack1l1l1111ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111111ll_opy_ = manager.list()
        if bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷ่ࠬ") in self.bstack11ll1lll11_opy_:
            for index, platform in enumerate(self.bstack11ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ้࠭")]):
                bstack1l1l1111ll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11ll1l1111_opy_,
                                                            args=(self.bstack11ll11llll_opy_, bstack1l11lll11_opy_, bstack1111111ll_opy_)))
            bstack11ll1lll1l_opy_ = len(self.bstack11ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹ๊ࠧ")])
        else:
            bstack1l1l1111ll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11ll1l1111_opy_,
                                                        args=(self.bstack11ll11llll_opy_, bstack1l11lll11_opy_, bstack1111111ll_opy_)))
            bstack11ll1lll1l_opy_ = 1
        i = 0
        for t in bstack1l1l1111ll_opy_:
            os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜๋ࠬ")] = str(i)
            if bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ์") in self.bstack11ll1lll11_opy_:
                os.environ[bstack11l11ll_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨํ")] = json.dumps(self.bstack11ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ๎")][i % bstack11ll1lll1l_opy_])
            i += 1
            t.start()
        for t in bstack1l1l1111ll_opy_:
            t.join()
        return list(bstack1111111ll_opy_)
    @staticmethod
    def bstack1l111l11l_opy_(driver, bstack111l1ll1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭๏"), None)
        if item and getattr(item, bstack11l11ll_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩࠬ๐"), None) and not getattr(item, bstack11l11ll_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࡠࡦࡲࡲࡪ࠭๑"), False):
            logger.info(
                bstack11l11ll_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠦ๒"))
            bstack11ll1l1lll_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1l1l111ll_opy_.bstack111l1111_opy_(driver, bstack11ll1l1lll_opy_, item.name, item.module.__name__, item.path, bstack111l1ll1_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
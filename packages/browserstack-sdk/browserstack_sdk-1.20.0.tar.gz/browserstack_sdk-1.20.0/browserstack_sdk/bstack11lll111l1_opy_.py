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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11ll1lll11_opy_, bstack11ll11lll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1lll11_opy_ = bstack11ll1lll11_opy_
        self.bstack11ll11lll1_opy_ = bstack11ll11lll1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l111ll1l1_opy_(bstack11ll11l1ll_opy_):
        bstack11ll11ll11_opy_ = []
        if bstack11ll11l1ll_opy_:
            tokens = str(os.path.basename(bstack11ll11l1ll_opy_)).split(bstack11l11ll_opy_ (u"ࠨ࡟ࠣ๓"))
            camelcase_name = bstack11l11ll_opy_ (u"ࠢࠡࠤ๔").join(t.title() for t in tokens)
            suite_name, bstack11ll11l1l1_opy_ = os.path.splitext(camelcase_name)
            bstack11ll11ll11_opy_.append(suite_name)
        return bstack11ll11ll11_opy_
    @staticmethod
    def bstack11ll11ll1l_opy_(typename):
        if bstack11l11ll_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦ๕") in typename:
            return bstack11l11ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥ๖")
        return bstack11l11ll_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ๗")
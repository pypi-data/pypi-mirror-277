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
from browserstack_sdk.bstack11ll111l1_opy_ import bstack1llllllll1_opy_
from browserstack_sdk.bstack11lll111l1_opy_ import RobotHandler
def bstack1111llll_opy_(framework):
    if framework.lower() == bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᆧ"):
        return bstack1llllllll1_opy_.version()
    elif framework.lower() == bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫᆨ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l11ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ᆩ"):
        import behave
        return behave.__version__
    else:
        return bstack11l11ll_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨᆪ")
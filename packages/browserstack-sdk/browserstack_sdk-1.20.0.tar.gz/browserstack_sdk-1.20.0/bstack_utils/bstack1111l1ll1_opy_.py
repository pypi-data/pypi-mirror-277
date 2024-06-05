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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack111ll11l1l_opy_, bstack1ll1l11l1l_opy_, bstack11l11lll1_opy_, bstack1ll1llll1l_opy_, \
    bstack111ll1llll_opy_
def bstack11l11ll11_opy_(bstack1lll1llll1l_opy_):
    for driver in bstack1lll1llll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11ll1lll1_opy_(driver, status, reason=bstack11l11ll_opy_ (u"ࠫࠬᒰ")):
    bstack1ll1111l1_opy_ = Config.bstack11l11l11_opy_()
    if bstack1ll1111l1_opy_.bstack11ll1l11l1_opy_():
        return
    bstack1l1lll11l_opy_ = bstack1ll111ll1_opy_(bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᒱ"), bstack11l11ll_opy_ (u"࠭ࠧᒲ"), status, reason, bstack11l11ll_opy_ (u"ࠧࠨᒳ"), bstack11l11ll_opy_ (u"ࠨࠩᒴ"))
    driver.execute_script(bstack1l1lll11l_opy_)
def bstack1l1l1l111l_opy_(page, status, reason=bstack11l11ll_opy_ (u"ࠩࠪᒵ")):
    try:
        if page is None:
            return
        bstack1ll1111l1_opy_ = Config.bstack11l11l11_opy_()
        if bstack1ll1111l1_opy_.bstack11ll1l11l1_opy_():
            return
        bstack1l1lll11l_opy_ = bstack1ll111ll1_opy_(bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᒶ"), bstack11l11ll_opy_ (u"ࠫࠬᒷ"), status, reason, bstack11l11ll_opy_ (u"ࠬ࠭ᒸ"), bstack11l11ll_opy_ (u"࠭ࠧᒹ"))
        page.evaluate(bstack11l11ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᒺ"), bstack1l1lll11l_opy_)
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨᒻ"), e)
def bstack1ll111ll1_opy_(type, name, status, reason, bstack1lll111111_opy_, bstack1ll11lll1_opy_):
    bstack1l11l11ll_opy_ = {
        bstack11l11ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᒼ"): type,
        bstack11l11ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᒽ"): {}
    }
    if type == bstack11l11ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᒾ"):
        bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᒿ")][bstack11l11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᓀ")] = bstack1lll111111_opy_
        bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᓁ")][bstack11l11ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᓂ")] = json.dumps(str(bstack1ll11lll1_opy_))
    if type == bstack11l11ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᓃ"):
        bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᓄ")][bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᓅ")] = name
    if type == bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᓆ"):
        bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᓇ")][bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᓈ")] = status
        if status == bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᓉ") and str(reason) != bstack11l11ll_opy_ (u"ࠤࠥᓊ"):
            bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᓋ")][bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᓌ")] = json.dumps(str(reason))
    bstack1ll1lll1_opy_ = bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᓍ").format(json.dumps(bstack1l11l11ll_opy_))
    return bstack1ll1lll1_opy_
def bstack11lllll1l_opy_(url, config, logger, bstack1lll1l1l11_opy_=False):
    hostname = bstack1ll1l11l1l_opy_(url)
    is_private = bstack1ll1llll1l_opy_(hostname)
    try:
        if is_private or bstack1lll1l1l11_opy_:
            file_path = bstack111ll11l1l_opy_(bstack11l11ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᓎ"), bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᓏ"), logger)
            if os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᓐ")) and eval(
                    os.environ.get(bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᓑ"))):
                return
            if (bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᓒ") in config and not config[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᓓ")]):
                os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᓔ")] = str(True)
                bstack1lll1lllll1_opy_ = {bstack11l11ll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨᓕ"): hostname}
                bstack111ll1llll_opy_(bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᓖ"), bstack11l11ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ᓗ"), bstack1lll1lllll1_opy_, logger)
    except Exception as e:
        pass
def bstack1llll111ll_opy_(caps, bstack1llll111111_opy_):
    if bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓘ") in caps:
        caps[bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᓙ")][bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᓚ")] = True
        if bstack1llll111111_opy_:
            caps[bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᓛ")][bstack11l11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᓜ")] = bstack1llll111111_opy_
    else:
        caps[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᓝ")] = True
        if bstack1llll111111_opy_:
            caps[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᓞ")] = bstack1llll111111_opy_
def bstack1llll1lll1l_opy_(bstack1l111ll111_opy_):
    bstack1lll1llllll_opy_ = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᓟ"), bstack11l11ll_opy_ (u"ࠪࠫᓠ"))
    if bstack1lll1llllll_opy_ == bstack11l11ll_opy_ (u"ࠫࠬᓡ") or bstack1lll1llllll_opy_ == bstack11l11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᓢ"):
        threading.current_thread().testStatus = bstack1l111ll111_opy_
    else:
        if bstack1l111ll111_opy_ == bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᓣ"):
            threading.current_thread().testStatus = bstack1l111ll111_opy_
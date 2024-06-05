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
import re
from bstack_utils.bstack1111l1ll1_opy_ import bstack1llll1lll1l_opy_
def bstack1llll1l11l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11l11ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᑻ")):
        return bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᑼ")
    elif fixture_name.startswith(bstack11l11ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᑽ")):
        return bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᑾ")
    elif fixture_name.startswith(bstack11l11ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᑿ")):
        return bstack11l11ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᒀ")
    elif fixture_name.startswith(bstack11l11ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᒁ")):
        return bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᒂ")
def bstack1llll1l11ll_opy_(fixture_name):
    return bool(re.match(bstack11l11ll_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᒃ"), fixture_name))
def bstack1llll1ll111_opy_(fixture_name):
    return bool(re.match(bstack11l11ll_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᒄ"), fixture_name))
def bstack1llll1l1l11_opy_(fixture_name):
    return bool(re.match(bstack11l11ll_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᒅ"), fixture_name))
def bstack1llll1ll1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11l11ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᒆ")):
        return bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᒇ"), bstack11l11ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᒈ")
    elif fixture_name.startswith(bstack11l11ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᒉ")):
        return bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᒊ"), bstack11l11ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᒋ")
    elif fixture_name.startswith(bstack11l11ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᒌ")):
        return bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᒍ"), bstack11l11ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᒎ")
    elif fixture_name.startswith(bstack11l11ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᒏ")):
        return bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᒐ"), bstack11l11ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᒑ")
    return None, None
def bstack1llll1l1ll1_opy_(hook_name):
    if hook_name in [bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᒒ"), bstack11l11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᒓ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1llll1l1lll_opy_(hook_name):
    if hook_name in [bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᒔ"), bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᒕ")]:
        return bstack11l11ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᒖ")
    elif hook_name in [bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᒗ"), bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᒘ")]:
        return bstack11l11ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᒙ")
    elif hook_name in [bstack11l11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᒚ"), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᒛ")]:
        return bstack11l11ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᒜ")
    elif hook_name in [bstack11l11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᒝ"), bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᒞ")]:
        return bstack11l11ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᒟ")
    return hook_name
def bstack1llll1l1l1l_opy_(node, scenario):
    if hasattr(node, bstack11l11ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᒠ")):
        parts = node.nodeid.rsplit(bstack11l11ll_opy_ (u"ࠥ࡟ࠧᒡ"))
        params = parts[-1]
        return bstack11l11ll_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦᒢ").format(scenario.name, params)
    return scenario.name
def bstack1llll1llll1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l11ll_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᒣ")):
            examples = list(node.callspec.params[bstack11l11ll_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬᒤ")].values())
        return examples
    except:
        return []
def bstack1llll1ll11l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1llll1l111l_opy_(report):
    try:
        status = bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒥ")
        if report.passed or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᒦ"))):
            status = bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᒧ")
        elif report.skipped:
            status = bstack11l11ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᒨ")
        bstack1llll1lll1l_opy_(status)
    except:
        pass
def bstack1l1l1lll11_opy_(status):
    try:
        bstack1llll1ll1ll_opy_ = bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᒩ")
        if status == bstack11l11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᒪ"):
            bstack1llll1ll1ll_opy_ = bstack11l11ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᒫ")
        elif status == bstack11l11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᒬ"):
            bstack1llll1ll1ll_opy_ = bstack11l11ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᒭ")
        bstack1llll1lll1l_opy_(bstack1llll1ll1ll_opy_)
    except:
        pass
def bstack1llll1lll11_opy_(item=None, report=None, summary=None, extra=None):
    return
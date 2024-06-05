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
import json
import requests
import logging
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1ll11l1_opy_ as bstack11l1ll11ll_opy_
from bstack_utils.bstack1l1l1l1lll_opy_ import bstack1l1l1l1lll_opy_
from bstack_utils.helper import bstack1l1ll111l_opy_, bstack1l1111llll_opy_, bstack11ll1ll11_opy_, bstack11l1llll1l_opy_, bstack11l1ll1l11_opy_, bstack11ll1l1l_opy_, get_host_info, bstack11ll111111_opy_, bstack11llll11l_opy_, bstack11ll1lllll_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack11ll1lllll_opy_(class_method=False)
def _11ll11l11l_opy_(driver, bstack111l1ll1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l11ll_opy_ (u"ࠫࡴࡹ࡟࡯ࡣࡰࡩࠬ๘"): caps.get(bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ๙"), None),
        bstack11l11ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ๚"): bstack111l1ll1_opy_.get(bstack11l11ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ๛"), None),
        bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧ๜"): caps.get(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ๝"), None),
        bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๞"): caps.get(bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ๟"), None)
    }
  except Exception as error:
    logger.debug(bstack11l11ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩ๠") + str(error))
  return response
def bstack11llllll1_opy_(config):
  return config.get(bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭๡"), False) or any([p.get(bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ๢"), False) == True for p in config.get(bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ๣"), [])])
def bstack1ll1l1ll1l_opy_(config, bstack1l11l1l11l_opy_):
  try:
    if not bstack11ll1ll11_opy_(config):
      return False
    bstack11l1ll1ll1_opy_ = config.get(bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ๤"), False)
    bstack11l1l1lll1_opy_ = config[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭๥")][bstack1l11l1l11l_opy_].get(bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ๦"), None)
    if bstack11l1l1lll1_opy_ != None:
      bstack11l1ll1ll1_opy_ = bstack11l1l1lll1_opy_
    bstack11ll1111l1_opy_ = os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ๧")) is not None and len(os.getenv(bstack11l11ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ๨"))) > 0 and os.getenv(bstack11l11ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ๩")) != bstack11l11ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭๪")
    return bstack11l1ll1ll1_opy_ and bstack11ll1111l1_opy_
  except Exception as error:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡨࡶ࡮࡬ࡹࡪࡰࡪࠤࡹ࡮ࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩ๫") + str(error))
  return False
def bstack1l1111ll1_opy_(bstack11ll11l111_opy_, test_tags):
  bstack11ll11l111_opy_ = os.getenv(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ๬"))
  if bstack11ll11l111_opy_ is None:
    return True
  bstack11ll11l111_opy_ = json.loads(bstack11ll11l111_opy_)
  try:
    include_tags = bstack11ll11l111_opy_[bstack11l11ll_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ๭")] if bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ๮") in bstack11ll11l111_opy_ and isinstance(bstack11ll11l111_opy_[bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ๯")], list) else []
    exclude_tags = bstack11ll11l111_opy_[bstack11l11ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ๰")] if bstack11l11ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭๱") in bstack11ll11l111_opy_ and isinstance(bstack11ll11l111_opy_[bstack11l11ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ๲")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥ๳") + str(error))
  return False
def bstack11l1111l1_opy_(config, bstack11l1lll1l1_opy_, bstack11l1llllll_opy_, bstack11l1ll1l1l_opy_):
  bstack11l1llll11_opy_ = bstack11l1llll1l_opy_(config)
  bstack11ll111l1l_opy_ = bstack11l1ll1l11_opy_(config)
  if bstack11l1llll11_opy_ is None or bstack11ll111l1l_opy_ is None:
    logger.error(bstack11l11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬ๴"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭๵"), bstack11l11ll_opy_ (u"࠭ࡻࡾࠩ๶")))
    data = {
        bstack11l11ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ๷"): config[bstack11l11ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭๸")],
        bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ๹"): config.get(bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭๺"), os.path.basename(os.getcwd())),
        bstack11l11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡗ࡭ࡲ࡫ࠧ๻"): bstack1l1ll111l_opy_(),
        bstack11l11ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ๼"): config.get(bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ๽"), bstack11l11ll_opy_ (u"ࠧࠨ๾")),
        bstack11l11ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ๿"): {
            bstack11l11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩ຀"): bstack11l1lll1l1_opy_,
            bstack11l11ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ກ"): bstack11l1llllll_opy_,
            bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨຂ"): __version__,
            bstack11l11ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ຃"): bstack11l11ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ຄ"),
            bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ຅"): bstack11l11ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪຆ"),
            bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩງ"): bstack11l1ll1l1l_opy_
        },
        bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡴࡪࡰࡪࡷࠬຈ"): settings,
        bstack11l11ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡈࡵ࡮ࡵࡴࡲࡰࠬຉ"): bstack11ll111111_opy_(),
        bstack11l11ll_opy_ (u"ࠬࡩࡩࡊࡰࡩࡳࠬຊ"): bstack11ll1l1l_opy_(),
        bstack11l11ll_opy_ (u"࠭ࡨࡰࡵࡷࡍࡳ࡬࡯ࠨ຋"): get_host_info(),
        bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩຌ"): bstack11ll1ll11_opy_(config)
    }
    headers = {
        bstack11l11ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧຍ"): bstack11l11ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬຎ"),
    }
    config = {
        bstack11l11ll_opy_ (u"ࠪࡥࡺࡺࡨࠨຏ"): (bstack11l1llll11_opy_, bstack11ll111l1l_opy_),
        bstack11l11ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬຐ"): headers
    }
    response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"ࠬࡖࡏࡔࡖࠪຑ"), bstack11l1ll11ll_opy_ + bstack11l11ll_opy_ (u"࠭࠯ࡷ࠴࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠭ຒ"), data, config)
    bstack11ll111l11_opy_ = response.json()
    if bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨຓ")]:
      parsed = json.loads(os.getenv(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩດ"), bstack11l11ll_opy_ (u"ࠩࡾࢁࠬຕ")))
      parsed[bstack11l11ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫຖ")] = bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠫࡩࡧࡴࡢࠩທ")][bstack11l11ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ຘ")]
      os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧນ")] = json.dumps(parsed)
      bstack1l1l1l1lll_opy_.bstack11ll1111ll_opy_(bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠧࡥࡣࡷࡥࠬບ")][bstack11l11ll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩປ")])
      bstack1l1l1l1lll_opy_.bstack11l1lll11l_opy_(bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠩࡧࡥࡹࡧࠧຜ")][bstack11l11ll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬຝ")])
      bstack1l1l1l1lll_opy_.store()
      return bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠫࡩࡧࡴࡢࠩພ")][bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪຟ")], bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"࠭ࡤࡢࡶࡤࠫຠ")][bstack11l11ll_opy_ (u"ࠧࡪࡦࠪມ")]
    else:
      logger.error(bstack11l11ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩຢ") + bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪຣ")])
      if bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ຤")] == bstack11l11ll_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳࠭ລ"):
        for bstack11l1l1llll_opy_ in bstack11ll111l11_opy_[bstack11l11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ຦")]:
          logger.error(bstack11l1l1llll_opy_[bstack11l11ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧວ")])
      return None, None
  except Exception as error:
    logger.error(bstack11l11ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣຨ") +  str(error))
    return None, None
def bstack1l1ll11111_opy_():
  if os.getenv(bstack11l11ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ຩ")) is None:
    return {
        bstack11l11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩສ"): bstack11l11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩຫ"),
        bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬຬ"): bstack11l11ll_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫອ")
    }
  data = {bstack11l11ll_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧຮ"): bstack1l1ll111l_opy_()}
  headers = {
      bstack11l11ll_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧຯ"): bstack11l11ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩະ") + os.getenv(bstack11l11ll_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢັ")),
      bstack11l11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩາ"): bstack11l11ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧຳ")
  }
  response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"ࠬࡖࡕࡕࠩິ"), bstack11l1ll11ll_opy_ + bstack11l11ll_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨີ"), data, { bstack11l11ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨຶ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l11ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤື") + bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ຸࠫ"))
      return {bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵູࠪ"): bstack11l11ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷ຺ࠬ"), bstack11l11ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ົ"): bstack11l11ll_opy_ (u"࠭ࠧຼ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l11ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥຽ") + str(error))
    return {
        bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ຾"): bstack11l11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ຿"),
        bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫເ"): str(error)
    }
def bstack1ll11111_opy_(caps, options):
  try:
    bstack11ll11111l_opy_ = caps.get(bstack11l11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬແ"), {}).get(bstack11l11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩໂ"), caps.get(bstack11l11ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ໃ"), bstack11l11ll_opy_ (u"ࠧࠨໄ")))
    if bstack11ll11111l_opy_:
      logger.warn(bstack11l11ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ໅"))
      return False
    browser = caps.get(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧໆ"), bstack11l11ll_opy_ (u"ࠪࠫ໇")).lower()
    if browser != bstack11l11ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨ່ࠫ"):
      logger.warn(bstack11l11ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮້ࠣ"))
      return False
    browser_version = caps.get(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴ໊ࠧ"), caps.get(bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯໋ࠩ")))
    if browser_version and browser_version != bstack11l11ll_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨ໌") and int(browser_version.split(bstack11l11ll_opy_ (u"ࠩ࠱ࠫໍ"))[0]) <= 94:
      logger.warn(bstack11l11ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠺࠮ࠣ໎"))
      return False
    if not options is None:
      bstack11l1ll1111_opy_ = options.to_capabilities().get(bstack11l11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ໏"), {})
      if bstack11l11ll_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩ໐") in bstack11l1ll1111_opy_.get(bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫ໑"), []):
        logger.warn(bstack11l11ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤ໒"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11l11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥ໓") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack11l1lll111_opy_ = config.get(bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ໔"), {})
    bstack11l1lll111_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭໕")] = os.getenv(bstack11l11ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ໖"))
    bstack11l1ll1lll_opy_ = json.loads(os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭໗"), bstack11l11ll_opy_ (u"࠭ࡻࡾࠩ໘"))).get(bstack11l11ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໙"))
    caps[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ໚")] = True
    if bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ໛") in caps:
      caps[bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫໜ")][bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫໝ")] = bstack11l1lll111_opy_
      caps[bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ໞ")][bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ໟ")][bstack11l11ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໠")] = bstack11l1ll1lll_opy_
    else:
      caps[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ໡")] = bstack11l1lll111_opy_
      caps[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ໢")][bstack11l11ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ໣")] = bstack11l1ll1lll_opy_
  except Exception as error:
    logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠱ࠤࡊࡸࡲࡰࡴ࠽ࠤࠧ໤") +  str(error))
def bstack1llll1ll1l_opy_(driver, bstack11ll111ll1_opy_):
  try:
    setattr(driver, bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ໥"), True)
    session = driver.session_id
    if session:
      bstack11l1lllll1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11l1lllll1_opy_ = False
      bstack11l1lllll1_opy_ = url.scheme in [bstack11l11ll_opy_ (u"ࠨࡨࡵࡶࡳࠦ໦"), bstack11l11ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨ໧")]
      if bstack11l1lllll1_opy_:
        if bstack11ll111ll1_opy_:
          logger.info(bstack11l11ll_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡧࡱࡵࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡮ࡡࡴࠢࡶࡸࡦࡸࡴࡦࡦ࠱ࠤࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡦࡪ࡭ࡩ࡯ࠢࡰࡳࡲ࡫࡮ࡵࡣࡵ࡭ࡱࡿ࠮ࠣ໨"))
      return bstack11ll111ll1_opy_
  except Exception as e:
    logger.error(bstack11l11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࡩ࡯ࡩࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ໩") + str(e))
    return False
def bstack111l1111_opy_(driver, class_name, name, module_name, path, bstack111l1ll1_opy_):
  try:
    bstack11ll1l1lll_opy_ = [class_name] if not class_name is None else []
    bstack11l1lll1ll_opy_ = {
        bstack11l11ll_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣ໪"): True,
        bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡆࡨࡸࡦ࡯࡬ࡴࠤ໫"): {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ໬"): name,
            bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡖࡺࡴࡉࡥࠤ໭"): os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡖࡈࡗ࡙ࡥࡒࡖࡐࡢࡍࡉ࠭໮")),
            bstack11l11ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥ໯"): str(path),
            bstack11l11ll_opy_ (u"ࠤࡶࡧࡴࡶࡥࡍ࡫ࡶࡸࠧ໰"): [module_name, *bstack11ll1l1lll_opy_, name],
        },
        bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧ໱"): _11ll11l11l_opy_(driver, bstack111l1ll1_opy_)
    }
    logger.debug(bstack11l11ll_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧ໲"))
    logger.debug(driver.execute_async_script(bstack1l1l1l1lll_opy_.perform_scan, {bstack11l11ll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧ໳"): name}))
    logger.debug(driver.execute_async_script(bstack1l1l1l1lll_opy_.bstack11ll111lll_opy_, bstack11l1lll1ll_opy_))
    logger.info(bstack11l11ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤ໴"))
  except Exception as bstack11l1ll111l_opy_:
    logger.error(bstack11l11ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤ໵") + str(path) + bstack11l11ll_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥ໶") + str(bstack11l1ll111l_opy_))
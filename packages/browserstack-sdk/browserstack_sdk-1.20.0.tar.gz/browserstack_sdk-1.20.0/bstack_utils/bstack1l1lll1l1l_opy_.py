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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11ll111111_opy_, bstack11ll1l1l_opy_, get_host_info, bstack11l1llll1l_opy_, bstack11l1ll1l11_opy_, bstack111ll1ll11_opy_, bstack1l1111llll_opy_, \
    bstack111ll1l111_opy_, bstack111ll11l11_opy_, bstack11llll11l_opy_, bstack11l11l1111_opy_, bstack1lll1lll11_opy_, bstack11ll1lllll_opy_, bstack1lll1lll1l_opy_, bstack1l1ll111l_opy_
from bstack_utils.bstack1llll1l1111_opy_ import bstack1llll11lll1_opy_
from bstack_utils.bstack1l111l1lll_opy_ import bstack1l1111l1l1_opy_
import bstack_utils.bstack1111l1ll_opy_ as bstack1l1l111ll_opy_
from bstack_utils.constants import bstack11l11l1l1l_opy_
bstack1lll11ll1l1_opy_ = [
    bstack11l11ll_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᔢ"), bstack11l11ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᔣ"), bstack11l11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᔤ"), bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᔥ"),
    bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᔦ"), bstack11l11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᔧ"), bstack11l11ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᔨ")
]
bstack1lll11l1l1l_opy_ = bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᔩ")
logger = logging.getLogger(__name__)
class bstack1l1l1111l_opy_:
    bstack1llll1l1111_opy_ = None
    bs_config = None
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lll11ll1ll_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll11lll11_opy_()
        bstack11l1llll11_opy_ = bstack11l1llll1l_opy_(bs_config)
        bstack11ll111l1l_opy_ = bstack11l1ll1l11_opy_(bs_config)
        bstack1lll11111_opy_ = False
        bstack1l1l1l111_opy_ = False
        if bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࠫᔪ") in bs_config:
            bstack1lll11111_opy_ = True
        else:
            bstack1l1l1l111_opy_ = True
        bstack1l1llll11l_opy_ = {
            bstack11l11ll_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᔫ"): cls.bstack1lll1l1ll_opy_(bstack1lll11ll1ll_opy_.get(bstack11l11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪᔬ"), bstack11l11ll_opy_ (u"ࠪࠫᔭ"))),
            bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᔮ"): bstack1l1l111ll_opy_.bstack11llllll1_opy_(bs_config),
            bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᔯ"): bs_config.get(bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᔰ"), False),
            bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᔱ"): bstack1l1l1l111_opy_,
            bstack11l11ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᔲ"): bstack1lll11111_opy_
        }
        data = {
            bstack11l11ll_opy_ (u"ࠩࡩࡳࡷࡳࡡࡵࠩᔳ"): bstack11l11ll_opy_ (u"ࠪ࡮ࡸࡵ࡮ࠨᔴ"),
            bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡤࡴࡡ࡮ࡧࠪᔵ"): bs_config.get(bstack11l11ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᔶ"), bstack11l11ll_opy_ (u"࠭ࠧᔷ")),
            bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᔸ"): bs_config.get(bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᔹ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᔺ"): bs_config.get(bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᔻ")),
            bstack11l11ll_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᔼ"): bs_config.get(bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᔽ"), bstack11l11ll_opy_ (u"࠭ࠧᔾ")),
            bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹࡥࡴࡪ࡯ࡨࠫᔿ"): datetime.datetime.now().isoformat(),
            bstack11l11ll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᕀ"): bstack111ll1ll11_opy_(bs_config),
            bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠬᕁ"): get_host_info(),
            bstack11l11ll_opy_ (u"ࠪࡧ࡮ࡥࡩ࡯ࡨࡲࠫᕂ"): bstack11ll1l1l_opy_(),
            bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡶࡺࡴ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᕃ"): os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᕄ")),
            bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࡸࡥࡳࡷࡱࠫᕅ"): os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬᕆ"), False),
            bstack11l11ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡡࡦࡳࡳࡺࡲࡰ࡮ࠪᕇ"): bstack11ll111111_opy_(),
            bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧᕈ"): bstack1l1llll11l_opy_,
            bstack11l11ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡢࡺࡪࡸࡳࡪࡱࡱࠫᕉ"): {
                bstack11l11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫᕊ"): bstack1lll11ll1ll_opy_.get(bstack11l11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ᕋ"), bstack11l11ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ᕌ")),
                bstack11l11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪᕍ"): bstack1lll11ll1ll_opy_.get(bstack11l11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᕎ")),
                bstack11l11ll_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᕏ"): bstack1lll11ll1ll_opy_.get(bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᕐ"))
            }
        }
        config = {
            bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡩࠩᕑ"): (bstack11l1llll11_opy_, bstack11ll111l1l_opy_),
            bstack11l11ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᕒ"): cls.default_headers()
        }
        response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"࠭ࡐࡐࡕࡗࠫᕓ"), cls.request_url(bstack11l11ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹࠧᕔ")), data, config)
        if response.status_code != 200:
            os.environ[bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᕕ")] = bstack11l11ll_opy_ (u"ࠩࡱࡹࡱࡲࠧᕖ")
            os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩᕗ")] = bstack11l11ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᕘ")
            os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᕙ")] = bstack11l11ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᕚ")
            os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᕛ")] = bstack11l11ll_opy_ (u"ࠣࡰࡸࡰࡱࠨᕜ")
            os.environ[bstack11l11ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᕝ")] = bstack11l11ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᕞ")
            bstack1lll1l11ll1_opy_ = response.json()
            if bstack1lll1l11ll1_opy_ and bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᕟ")]:
                error_message = bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᕠ")]
                if bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶ࡙ࡿࡰࡦࠩᕡ")] == bstack11l11ll_opy_ (u"ࠧࡆࡔࡕࡓࡗࡥࡉࡏࡘࡄࡐࡎࡊ࡟ࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࠬᕢ"):
                    logger.error(error_message)
                elif bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࡔࡺࡲࡨࠫᕣ")] == bstack11l11ll_opy_ (u"ࠩࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠨᕤ"):
                    logger.info(error_message)
                elif bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡖࡼࡴࡪ࠭ᕥ")] == bstack11l11ll_opy_ (u"ࠫࡊࡘࡒࡐࡔࡢࡗࡉࡑ࡟ࡅࡇࡓࡖࡊࡉࡁࡕࡇࡇࠫᕦ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l11ll_opy_ (u"ࠧࡊࡡࡵࡣࠣࡹࡵࡲ࡯ࡢࡦࠣࡸࡴࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡚ࠥࡥࡴࡶࠣࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢᕧ"))
            return [None, None, None]
        bstack1lll1l11ll1_opy_ = response.json()
        os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᕨ")] = bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᕩ")]
        if cls.bstack1lll1l1ll_opy_(bstack1lll11ll1ll_opy_.get(bstack11l11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩᕪ"), bstack11l11ll_opy_ (u"ࠩࠪᕫ"))) is True:
            logger.debug(bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࠡࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᕬ"))
            os.environ[bstack11l11ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᕭ")] = bstack11l11ll_opy_ (u"ࠬࡺࡲࡶࡧࠪᕮ")
            if bstack1lll1l11ll1_opy_.get(bstack11l11ll_opy_ (u"࠭ࡪࡸࡶࠪᕯ")):
                os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᕰ")] = bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠨ࡬ࡺࡸࠬᕱ")]
                os.environ[bstack11l11ll_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭ᕲ")] = json.dumps({
                    bstack11l11ll_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬᕳ"): bstack11l1llll11_opy_,
                    bstack11l11ll_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭ᕴ"): bstack11ll111l1l_opy_
                })
            if bstack1lll1l11ll1_opy_.get(bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᕵ")):
                os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᕶ")] = bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᕷ")]
            if bstack1lll1l11ll1_opy_.get(bstack11l11ll_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᕸ")):
                os.environ[bstack11l11ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᕹ")] = str(bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᕺ")])
        return [bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠫ࡯ࡽࡴࠨᕻ")], bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᕼ")], bstack1lll1l11ll1_opy_[bstack11l11ll_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᕽ")]]
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def stop(cls, bstack1lll1l1l111_opy_ = None):
        if not cls.on():
            return
        if os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᕾ")] == bstack11l11ll_opy_ (u"ࠣࡰࡸࡰࡱࠨᕿ") or os.environ[bstack11l11ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᖀ")] == bstack11l11ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᖁ"):
            print(bstack11l11ll_opy_ (u"ࠫࡊ࡞ࡃࡆࡒࡗࡍࡔࡔࠠࡊࡐࠣࡷࡹࡵࡰࡃࡷ࡬ࡰࡩ࡛ࡰࡴࡶࡵࡩࡦࡳࠠࡓࡇࡔ࡙ࡊ࡙ࡔࠡࡖࡒࠤ࡙ࡋࡓࡕࠢࡒࡆࡘࡋࡒࡗࡃࡅࡍࡑࡏࡔ࡚ࠢ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬᖂ"))
            return {
                bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᖃ"): bstack11l11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᖄ"),
                bstack11l11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖅ"): bstack11l11ll_opy_ (u"ࠨࡖࡲ࡯ࡪࡴ࠯ࡣࡷ࡬ࡰࡩࡏࡄࠡ࡫ࡶࠤࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠬࠡࡤࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡰ࡭࡬࡮ࡴࠡࡪࡤࡺࡪࠦࡦࡢ࡫࡯ࡩࡩ࠭ᖆ")
            }
        else:
            cls.bstack1llll1l1111_opy_.shutdown()
            data = {
                bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᖇ"): bstack1l1ll111l_opy_()
            }
            if not bstack1lll1l1l111_opy_ is None:
                data[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡳࡥࡵࡣࡧࡥࡹࡧࠧᖈ")] = [{
                    bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᖉ"): bstack11l11ll_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪᖊ"),
                    bstack11l11ll_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭ᖋ"): bstack1lll1l1l111_opy_
                }]
            config = {
                bstack11l11ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᖌ"): cls.default_headers()
            }
            bstack111l1lll11_opy_ = bstack11l11ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩᖍ").format(os.environ[bstack11l11ll_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣᖎ")])
            bstack1lll1l11111_opy_ = cls.request_url(bstack111l1lll11_opy_)
            response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"ࠪࡔ࡚࡚ࠧᖏ"), bstack1lll1l11111_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l11ll_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥᖐ"))
    @classmethod
    def bstack11lll1lll1_opy_(cls):
        if cls.bstack1llll1l1111_opy_ is None:
            return
        cls.bstack1llll1l1111_opy_.shutdown()
    @classmethod
    def bstack11111111_opy_(cls):
        if cls.on():
            print(
                bstack11l11ll_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨᖑ").format(os.environ[bstack11l11ll_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧᖒ")]))
    @classmethod
    def bstack1lll11lll11_opy_(cls):
        if cls.bstack1llll1l1111_opy_ is not None:
            return
        cls.bstack1llll1l1111_opy_ = bstack1llll11lll1_opy_(cls.bstack1lll1l111ll_opy_)
        cls.bstack1llll1l1111_opy_.start()
    @classmethod
    def bstack1l1111111l_opy_(cls, bstack11llll11ll_opy_, bstack1lll1l1111l_opy_=bstack11l11ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ᖓ")):
        if not cls.on():
            return
        bstack1ll1l1ll1_opy_ = bstack11llll11ll_opy_[bstack11l11ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᖔ")]
        bstack1lll11lllll_opy_ = {
            bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᖕ"): bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧᖖ"),
            bstack11l11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᖗ"): bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧᖘ"),
            bstack11l11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᖙ"): bstack11l11ll_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙࡫ࡪࡲࡳࡩࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ᖚ"),
            bstack11l11ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᖛ"): bstack11l11ll_opy_ (u"ࠩࡏࡳ࡬ࡥࡕࡱ࡮ࡲࡥࡩ࠭ᖜ"),
            bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᖝ"): bstack11l11ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨᖞ"),
            bstack11l11ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᖟ"): bstack11l11ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨᖠ"),
            bstack11l11ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᖡ"): bstack11l11ll_opy_ (u"ࠨࡅࡅࡘࡤ࡛ࡰ࡭ࡱࡤࡨࠬᖢ")
        }.get(bstack1ll1l1ll1_opy_)
        if bstack1lll1l1111l_opy_ == bstack11l11ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᖣ"):
            cls.bstack1lll11lll11_opy_()
            cls.bstack1llll1l1111_opy_.add(bstack11llll11ll_opy_)
        elif bstack1lll1l1111l_opy_ == bstack11l11ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᖤ"):
            cls.bstack1lll1l111ll_opy_([bstack11llll11ll_opy_], bstack1lll1l1111l_opy_)
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def bstack1lll1l111ll_opy_(cls, bstack11llll11ll_opy_, bstack1lll1l1111l_opy_=bstack11l11ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᖥ")):
        config = {
            bstack11l11ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᖦ"): cls.default_headers()
        }
        response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"࠭ࡐࡐࡕࡗࠫᖧ"), cls.request_url(bstack1lll1l1111l_opy_), bstack11llll11ll_opy_, config)
        bstack11ll111l11_opy_ = response.json()
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def bstack1111llll1_opy_(cls, bstack1l11111l1l_opy_):
        bstack1lll11l1ll1_opy_ = []
        for log in bstack1l11111l1l_opy_:
            bstack1lll11ll111_opy_ = {
                bstack11l11ll_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᖨ"): bstack11l11ll_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪᖩ"),
                bstack11l11ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᖪ"): log[bstack11l11ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᖫ")],
                bstack11l11ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᖬ"): log[bstack11l11ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᖭ")],
                bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭ᖮ"): {},
                bstack11l11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖯ"): log[bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᖰ")],
            }
            if bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖱ") in log:
                bstack1lll11ll111_opy_[bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖲ")] = log[bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖳ")]
            elif bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᖴ") in log:
                bstack1lll11ll111_opy_[bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖵ")] = log[bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖶ")]
            bstack1lll11l1ll1_opy_.append(bstack1lll11ll111_opy_)
        cls.bstack1l1111111l_opy_({
            bstack11l11ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᖷ"): bstack11l11ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᖸ"),
            bstack11l11ll_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᖹ"): bstack1lll11l1ll1_opy_
        })
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def bstack1lll1l1l11l_opy_(cls, steps):
        bstack1lll11l1lll_opy_ = []
        for step in steps:
            bstack1lll11llll1_opy_ = {
                bstack11l11ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᖺ"): bstack11l11ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨᖻ"),
                bstack11l11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᖼ"): step[bstack11l11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᖽ")],
                bstack11l11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᖾ"): step[bstack11l11ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᖿ")],
                bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᗀ"): step[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᗁ")],
                bstack11l11ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᗂ"): step[bstack11l11ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᗃ")]
            }
            if bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᗄ") in step:
                bstack1lll11llll1_opy_[bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᗅ")] = step[bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᗆ")]
            elif bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᗇ") in step:
                bstack1lll11llll1_opy_[bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᗈ")] = step[bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᗉ")]
            bstack1lll11l1lll_opy_.append(bstack1lll11llll1_opy_)
        cls.bstack1l1111111l_opy_({
            bstack11l11ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᗊ"): bstack11l11ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᗋ"),
            bstack11l11ll_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ᗌ"): bstack1lll11l1lll_opy_
        })
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def bstack111l1111l_opy_(cls, screenshot):
        cls.bstack1l1111111l_opy_({
            bstack11l11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᗍ"): bstack11l11ll_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᗎ"),
            bstack11l11ll_opy_ (u"ࠫࡱࡵࡧࡴࠩᗏ"): [{
                bstack11l11ll_opy_ (u"ࠬࡱࡩ࡯ࡦࠪᗐ"): bstack11l11ll_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨᗑ"),
                bstack11l11ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᗒ"): bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠨ࡜ࠪᗓ"),
                bstack11l11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᗔ"): screenshot[bstack11l11ll_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩᗕ")],
                bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᗖ"): screenshot[bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᗗ")]
            }]
        }, bstack1lll1l1111l_opy_=bstack11l11ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᗘ"))
    @classmethod
    @bstack11ll1lllll_opy_(class_method=True)
    def bstack111111l11_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l1111111l_opy_({
            bstack11l11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᗙ"): bstack11l11ll_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬᗚ"),
            bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᗛ"): {
                bstack11l11ll_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᗜ"): cls.current_test_uuid(),
                bstack11l11ll_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥᗝ"): cls.bstack11llll1lll_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᗞ"), None) is None or os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᗟ")] == bstack11l11ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᗠ"):
            return False
        return True
    @classmethod
    def bstack1lll1l1ll_opy_(cls, framework=bstack11l11ll_opy_ (u"ࠣࠤᗡ")):
        if framework not in bstack11l11l1l1l_opy_:
            return False
        bstack1lll11lll1l_opy_ = not bstack1lll1lll1l_opy_()
        return bstack1lll1lll11_opy_(cls.bs_config.get(bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᗢ"), bstack1lll11lll1l_opy_))
    @staticmethod
    def request_url(url):
        return bstack11l11ll_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩᗣ").format(bstack1lll11l1l1l_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack11l11ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᗤ"): bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᗥ"),
            bstack11l11ll_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩᗦ"): bstack11l11ll_opy_ (u"ࠧࡵࡴࡸࡩࠬᗧ")
        }
        if os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᗨ"), None):
            headers[bstack11l11ll_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᗩ")] = bstack11l11ll_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᗪ").format(os.environ[bstack11l11ll_opy_ (u"ࠦࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠧᗫ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᗬ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᗭ"), None)
    @staticmethod
    def bstack11lll1l1ll_opy_():
        if getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᗮ"), None):
            return {
                bstack11l11ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᗯ"): bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᗰ"),
                bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᗱ"): getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᗲ"), None)
            }
        if getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᗳ"), None):
            return {
                bstack11l11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᗴ"): bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᗵ"),
                bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᗶ"): getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᗷ"), None)
            }
        return None
    @staticmethod
    def bstack11llll1lll_opy_(driver):
        return {
            bstack111ll11l11_opy_(): bstack111ll1l111_opy_(driver)
        }
    @staticmethod
    def bstack1lll11ll11l_opy_(exception_info, report):
        return [{bstack11l11ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᗸ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11ll11ll1l_opy_(typename):
        if bstack11l11ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᗹ") in typename:
            return bstack11l11ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᗺ")
        return bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᗻ")
    @staticmethod
    def bstack1lll1l11lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l1111l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l111ll1l1_opy_(test, hook_name=None):
        bstack1lll1l111l1_opy_ = test.parent
        if hook_name in [bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᗼ"), bstack11l11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᗽ"), bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᗾ"), bstack11l11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᗿ")]:
            bstack1lll1l111l1_opy_ = test
        scope = []
        while bstack1lll1l111l1_opy_ is not None:
            scope.append(bstack1lll1l111l1_opy_.name)
            bstack1lll1l111l1_opy_ = bstack1lll1l111l1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1lll1l11l1l_opy_(hook_type):
        if hook_type == bstack11l11ll_opy_ (u"ࠦࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠤᘀ"):
            return bstack11l11ll_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡭ࡵ࡯࡬ࠤᘁ")
        elif hook_type == bstack11l11ll_opy_ (u"ࠨࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠥᘂ"):
            return bstack11l11ll_opy_ (u"ࠢࡕࡧࡤࡶࡩࡵࡷ࡯ࠢ࡫ࡳࡴࡱࠢᘃ")
    @staticmethod
    def bstack1lll1l11l11_opy_(bstack1lllll11l1_opy_):
        try:
            if not bstack1l1l1111l_opy_.on():
                return bstack1lllll11l1_opy_
            if os.environ.get(bstack11l11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࠨᘄ"), None) == bstack11l11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᘅ"):
                tests = os.environ.get(bstack11l11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠢᘆ"), None)
                if tests is None or tests == bstack11l11ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᘇ"):
                    return bstack1lllll11l1_opy_
                bstack1lllll11l1_opy_ = tests.split(bstack11l11ll_opy_ (u"ࠬ࠲ࠧᘈ"))
                return bstack1lllll11l1_opy_
        except Exception as exc:
            print(bstack11l11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡸࡥࡳࡷࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠿ࠦࠢᘉ"), str(exc))
        return bstack1lllll11l1_opy_
    @classmethod
    def bstack11lll1l1l1_opy_(cls, event: str, bstack11llll11ll_opy_: bstack1l1111l1l1_opy_):
        bstack11llll111l_opy_ = {
            bstack11l11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᘊ"): event,
            bstack11llll11ll_opy_.bstack1l1111ll1l_opy_(): bstack11llll11ll_opy_.bstack1l11111111_opy_(event)
        }
        bstack1l1l1111l_opy_.bstack1l1111111l_opy_(bstack11llll111l_opy_)
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
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1111ll1_opy_ = {}
        bstack1l111lllll_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬീ"), bstack11l11ll_opy_ (u"ࠬ࠭ു"))
        if not bstack1l111lllll_opy_:
            return bstack1ll1111ll1_opy_
        try:
            bstack1l11l11111_opy_ = json.loads(bstack1l111lllll_opy_)
            if bstack11l11ll_opy_ (u"ࠨ࡯ࡴࠤൂ") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠢࡰࡵࠥൃ")] = bstack1l11l11111_opy_[bstack11l11ll_opy_ (u"ࠣࡱࡶࠦൄ")]
            if bstack11l11ll_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ൅") in bstack1l11l11111_opy_ or bstack11l11ll_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨെ") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢേ")] = bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤൈ"), bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ൉")))
            if bstack11l11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣൊ") in bstack1l11l11111_opy_ or bstack11l11ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨോ") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢൌ")] = bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ്ࠦ"), bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤൎ")))
            if bstack11l11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ൏") in bstack1l11l11111_opy_ or bstack11l11ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢ൐") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣ൑")] = bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ൒"), bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ൓")))
            if bstack11l11ll_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥൔ") in bstack1l11l11111_opy_ or bstack11l11ll_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣൕ") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤൖ")] = bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨൗ"), bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ൘")))
            if bstack11l11ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥ൙") in bstack1l11l11111_opy_ or bstack11l11ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ൚") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ൛")] = bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ൜"), bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ൝")))
            if bstack11l11ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ൞") in bstack1l11l11111_opy_ or bstack11l11ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤൟ") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥൠ")] = bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧൡ"), bstack1l11l11111_opy_.get(bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧൢ")))
            if bstack11l11ll_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨൣ") in bstack1l11l11111_opy_:
                bstack1ll1111ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢ൤")] = bstack1l11l11111_opy_[bstack11l11ll_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣ൥")]
        except Exception as error:
            logger.error(bstack11l11ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡢࡶࡤ࠾ࠥࠨ൦") +  str(error))
        return bstack1ll1111ll1_opy_
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
from uuid import uuid4
from bstack_utils.helper import bstack1l1ll111l_opy_, bstack111llll11l_opy_
from bstack_utils.bstack1l1ll1l1ll_opy_ import bstack1llll1llll1_opy_
class bstack1l1111l1l1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l1111l11l_opy_=None, framework=None, tags=[], scope=[], bstack1lll1ll1lll_opy_=None, bstack1lll1ll1111_opy_=True, bstack1lll1l1lll1_opy_=None, bstack1ll1l1ll1_opy_=None, result=None, duration=None, bstack11lll11l1l_opy_=None, meta={}):
        self.bstack11lll11l1l_opy_ = bstack11lll11l1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1lll1ll1111_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l1111l11l_opy_ = bstack1l1111l11l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1lll1ll1lll_opy_ = bstack1lll1ll1lll_opy_
        self.bstack1lll1l1lll1_opy_ = bstack1lll1l1lll1_opy_
        self.bstack1ll1l1ll1_opy_ = bstack1ll1l1ll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11lll1l11l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1lll1lll111_opy_(self):
        bstack1lll1lll11l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᓤ"): bstack1lll1lll11l_opy_,
            bstack11l11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᓥ"): bstack1lll1lll11l_opy_,
            bstack11l11ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᓦ"): bstack1lll1lll11l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l11ll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᓧ") + key)
            setattr(self, key, val)
    def bstack1lll1l1l1ll_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᓨ"): self.name,
            bstack11l11ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᓩ"): {
                bstack11l11ll_opy_ (u"࠭࡬ࡢࡰࡪࠫᓪ"): bstack11l11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᓫ"),
                bstack11l11ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᓬ"): self.code
            },
            bstack11l11ll_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᓭ"): self.scope,
            bstack11l11ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᓮ"): self.tags,
            bstack11l11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᓯ"): self.framework,
            bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᓰ"): self.bstack1l1111l11l_opy_
        }
    def bstack1lll1ll111l_opy_(self):
        return {
         bstack11l11ll_opy_ (u"࠭࡭ࡦࡶࡤࠫᓱ"): self.meta
        }
    def bstack1lll1ll1l11_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᓲ"): {
                bstack11l11ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᓳ"): self.bstack1lll1ll1lll_opy_
            }
        }
    def bstack1lll1l1l1l1_opy_(self, bstack1lll1ll11ll_opy_, details):
        step = next(filter(lambda st: st[bstack11l11ll_opy_ (u"ࠩ࡬ࡨࠬᓴ")] == bstack1lll1ll11ll_opy_, self.meta[bstack11l11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᓵ")]), None)
        step.update(details)
    def bstack1lll1lll1ll_opy_(self, bstack1lll1ll11ll_opy_):
        step = next(filter(lambda st: st[bstack11l11ll_opy_ (u"ࠫ࡮ࡪࠧᓶ")] == bstack1lll1ll11ll_opy_, self.meta[bstack11l11ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᓷ")]), None)
        step.update({
            bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᓸ"): bstack1l1ll111l_opy_()
        })
    def bstack11lllll111_opy_(self, bstack1lll1ll11ll_opy_, result, duration=None):
        bstack1lll1l1lll1_opy_ = bstack1l1ll111l_opy_()
        if bstack1lll1ll11ll_opy_ is not None and self.meta.get(bstack11l11ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᓹ")):
            step = next(filter(lambda st: st[bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫᓺ")] == bstack1lll1ll11ll_opy_, self.meta[bstack11l11ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᓻ")]), None)
            step.update({
                bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᓼ"): bstack1lll1l1lll1_opy_,
                bstack11l11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᓽ"): duration if duration else bstack111llll11l_opy_(step[bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᓾ")], bstack1lll1l1lll1_opy_),
                bstack11l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᓿ"): result.result,
                bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᔀ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1lll1l1ll1l_opy_):
        if self.meta.get(bstack11l11ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᔁ")):
            self.meta[bstack11l11ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᔂ")].append(bstack1lll1l1ll1l_opy_)
        else:
            self.meta[bstack11l11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᔃ")] = [ bstack1lll1l1ll1l_opy_ ]
    def bstack1lll1ll1l1l_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᔄ"): self.bstack11lll1l11l_opy_(),
            **self.bstack1lll1l1l1ll_opy_(),
            **self.bstack1lll1lll111_opy_(),
            **self.bstack1lll1ll111l_opy_()
        }
    def bstack1lll1llll11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᔅ"): self.bstack1lll1l1lll1_opy_,
            bstack11l11ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᔆ"): self.duration,
            bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᔇ"): self.result.result
        }
        if data[bstack11l11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᔈ")] == bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᔉ"):
            data[bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᔊ")] = self.result.bstack11ll11ll1l_opy_()
            data[bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᔋ")] = [{bstack11l11ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᔌ"): self.result.bstack111lllll1l_opy_()}]
        return data
    def bstack1lll1l1llll_opy_(self):
        return {
            bstack11l11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᔍ"): self.bstack11lll1l11l_opy_(),
            **self.bstack1lll1l1l1ll_opy_(),
            **self.bstack1lll1lll111_opy_(),
            **self.bstack1lll1llll11_opy_(),
            **self.bstack1lll1ll111l_opy_()
        }
    def bstack1l11111111_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l11ll_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨᔎ") in event:
            return self.bstack1lll1ll1l1l_opy_()
        elif bstack11l11ll_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᔏ") in event:
            return self.bstack1lll1l1llll_opy_()
    def bstack1l1111ll1l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1lll1l1lll1_opy_ = time if time else bstack1l1ll111l_opy_()
        self.duration = duration if duration else bstack111llll11l_opy_(self.bstack1l1111l11l_opy_, self.bstack1lll1l1lll1_opy_)
        if result:
            self.result = result
class bstack11lll11l11_opy_(bstack1l1111l1l1_opy_):
    def __init__(self, hooks=[], bstack1l1111lll1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1111lll1_opy_ = bstack1l1111lll1_opy_
        super().__init__(*args, **kwargs, bstack1ll1l1ll1_opy_=bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᔐ"))
    @classmethod
    def bstack1lll1l1ll11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࠭ᔑ"): id(step),
                bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡸࡵࠩᔒ"): step.name,
                bstack11l11ll_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ᔓ"): step.keyword,
            })
        return bstack11lll11l11_opy_(
            **kwargs,
            meta={
                bstack11l11ll_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧᔔ"): {
                    bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᔕ"): feature.name,
                    bstack11l11ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ᔖ"): feature.filename,
                    bstack11l11ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᔗ"): feature.description
                },
                bstack11l11ll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬᔘ"): {
                    bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᔙ"): scenario.name
                },
                bstack11l11ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᔚ"): steps,
                bstack11l11ll_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨᔛ"): bstack1llll1llll1_opy_(test)
            }
        )
    def bstack1lll1lll1l1_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᔜ"): self.hooks
        }
    def bstack1lll1ll1ll1_opy_(self):
        if self.bstack1l1111lll1_opy_:
            return {
                bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᔝ"): self.bstack1l1111lll1_opy_
            }
        return {}
    def bstack1lll1l1llll_opy_(self):
        return {
            **super().bstack1lll1l1llll_opy_(),
            **self.bstack1lll1lll1l1_opy_()
        }
    def bstack1lll1ll1l1l_opy_(self):
        return {
            **super().bstack1lll1ll1l1l_opy_(),
            **self.bstack1lll1ll1ll1_opy_()
        }
    def bstack1l1111ll1l_opy_(self):
        return bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᔞ")
class bstack1l1111l1ll_opy_(bstack1l1111l1l1_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack1ll1l1ll1_opy_=bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᔟ"))
    def bstack1l111l11ll_opy_(self):
        return self.hook_type
    def bstack1lll1ll11l1_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᔠ"): self.hook_type
        }
    def bstack1lll1l1llll_opy_(self):
        return {
            **super().bstack1lll1l1llll_opy_(),
            **self.bstack1lll1ll11l1_opy_()
        }
    def bstack1lll1ll1l1l_opy_(self):
        return {
            **super().bstack1lll1ll1l1l_opy_(),
            **self.bstack1lll1ll11l1_opy_()
        }
    def bstack1l1111ll1l_opy_(self):
        return bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧᔡ")
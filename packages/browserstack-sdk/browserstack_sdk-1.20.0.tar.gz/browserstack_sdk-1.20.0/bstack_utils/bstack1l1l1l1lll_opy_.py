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
class bstack11l1l1l11l_opy_(object):
  bstack1lllll1ll_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠩࢁࠫ໷")), bstack11l11ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ໸"))
  bstack11l1l1l1ll_opy_ = os.path.join(bstack1lllll1ll_opy_, bstack11l11ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠴ࡪࡴࡱࡱࠫ໹"))
  bstack11l1l1ll11_opy_ = None
  perform_scan = None
  bstack1ll11l1l1l_opy_ = None
  bstack11llll1l1_opy_ = None
  bstack11ll111lll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠧ໺")):
      cls.instance = super(bstack11l1l1l11l_opy_, cls).__new__(cls)
      cls.instance.bstack11l1l1l111_opy_()
    return cls.instance
  def bstack11l1l1l111_opy_(self):
    try:
      with open(self.bstack11l1l1l1ll_opy_, bstack11l11ll_opy_ (u"࠭ࡲࠨ໻")) as bstack111l11l1l_opy_:
        bstack11l1l1l1l1_opy_ = bstack111l11l1l_opy_.read()
        data = json.loads(bstack11l1l1l1l1_opy_)
        if bstack11l11ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ໼") in data:
          self.bstack11l1lll11l_opy_(data[bstack11l11ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ໽")])
        if bstack11l11ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ໾") in data:
          self.bstack11ll1111ll_opy_(data[bstack11l11ll_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ໿")])
    except:
      pass
  def bstack11ll1111ll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11l11ll_opy_ (u"ࠫࡸࡩࡡ࡯ࠩༀ")]
      self.bstack1ll11l1l1l_opy_ = scripts[bstack11l11ll_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩ༁")]
      self.bstack11llll1l1_opy_ = scripts[bstack11l11ll_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪ༂")]
      self.bstack11ll111lll_opy_ = scripts[bstack11l11ll_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬ༃")]
  def bstack11l1lll11l_opy_(self, bstack11l1l1ll11_opy_):
    if bstack11l1l1ll11_opy_ != None and len(bstack11l1l1ll11_opy_) != 0:
      self.bstack11l1l1ll11_opy_ = bstack11l1l1ll11_opy_
  def store(self):
    try:
      with open(self.bstack11l1l1l1ll_opy_, bstack11l11ll_opy_ (u"ࠨࡹࠪ༄")) as file:
        json.dump({
          bstack11l11ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࠦ༅"): self.bstack11l1l1ll11_opy_,
          bstack11l11ll_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࡶࠦ༆"): {
            bstack11l11ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ༇"): self.perform_scan,
            bstack11l11ll_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤ༈"): self.bstack1ll11l1l1l_opy_,
            bstack11l11ll_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥ༉"): self.bstack11llll1l1_opy_,
            bstack11l11ll_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠧ༊"): self.bstack11ll111lll_opy_
          }
        }, file)
    except:
      pass
  def bstack11l1l1l1_opy_(self, bstack11l1l1ll1l_opy_):
    try:
      return any(command.get(bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭་")) == bstack11l1l1ll1l_opy_ for command in self.bstack11l1l1ll11_opy_)
    except:
      return False
bstack1l1l1l1lll_opy_ = bstack11l1l1l11l_opy_()
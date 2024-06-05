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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11ll1l1_opy_
import tempfile
import json
bstack1111lll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪ፹"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l11ll_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧ፺"),
      datefmt=bstack11l11ll_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ፻"),
      stream=sys.stdout
    )
  return logger
def bstack1111lll11l_opy_():
  global bstack1111lll1ll_opy_
  if os.path.exists(bstack1111lll1ll_opy_):
    os.remove(bstack1111lll1ll_opy_)
def bstack1ll11l1ll1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1l11l111_opy_(config, log_level):
  bstack1111ll1111_opy_ = log_level
  if bstack11l11ll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭፼") in config and config[bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧ፽")] in bstack11l11ll1l1_opy_:
    bstack1111ll1111_opy_ = bstack11l11ll1l1_opy_[config[bstack11l11ll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ፾")]]
  if config.get(bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩ፿"), False):
    logging.getLogger().setLevel(bstack1111ll1111_opy_)
    return bstack1111ll1111_opy_
  global bstack1111lll1ll_opy_
  bstack1ll11l1ll1_opy_()
  bstack1111ll11l1_opy_ = logging.Formatter(
    fmt=bstack11l11ll_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ᎀ"),
    datefmt=bstack11l11ll_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫᎁ")
  )
  bstack1111ll11ll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1111lll1ll_opy_)
  file_handler.setFormatter(bstack1111ll11l1_opy_)
  bstack1111ll11ll_opy_.setFormatter(bstack1111ll11l1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1111ll11ll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l11ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬᎂ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1111ll11ll_opy_.setLevel(bstack1111ll1111_opy_)
  logging.getLogger().addHandler(bstack1111ll11ll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1111ll1111_opy_
def bstack1111lll111_opy_(config):
  try:
    bstack1111ll1ll1_opy_ = set([
      bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᎃ"), bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᎄ"), bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᎅ"), bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᎆ"), bstack11l11ll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠪᎇ"),
      bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬᎈ"), bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᎉ"), bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬᎊ"), bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᎋ")
    ])
    bstack1111ll1lll_opy_ = bstack11l11ll_opy_ (u"࠭ࠧᎌ")
    with open(bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪᎍ")) as bstack1111lll1l1_opy_:
      bstack1111ll1l11_opy_ = bstack1111lll1l1_opy_.read()
      bstack1111ll1lll_opy_ = re.sub(bstack11l11ll_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩᎎ"), bstack11l11ll_opy_ (u"ࠩࠪᎏ"), bstack1111ll1l11_opy_, flags=re.M)
      bstack1111ll1lll_opy_ = re.sub(
        bstack11l11ll_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭᎐") + bstack11l11ll_opy_ (u"ࠫࢁ࠭᎑").join(bstack1111ll1ll1_opy_) + bstack11l11ll_opy_ (u"ࠬ࠯࠮ࠫࠦࠪ᎒"),
        bstack11l11ll_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨ᎓"),
        bstack1111ll1lll_opy_, flags=re.M | re.I
      )
    def bstack1111l1lll1_opy_(dic):
      bstack1111ll111l_opy_ = {}
      for key, value in dic.items():
        if key in bstack1111ll1ll1_opy_:
          bstack1111ll111l_opy_[key] = bstack11l11ll_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫ᎔")
        else:
          if isinstance(value, dict):
            bstack1111ll111l_opy_[key] = bstack1111l1lll1_opy_(value)
          else:
            bstack1111ll111l_opy_[key] = value
      return bstack1111ll111l_opy_
    bstack1111ll111l_opy_ = bstack1111l1lll1_opy_(config)
    return {
      bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ᎕"): bstack1111ll1lll_opy_,
      bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ᎖"): json.dumps(bstack1111ll111l_opy_)
    }
  except Exception as e:
    return {}
def bstack1111llll1_opy_(config):
  global bstack1111lll1ll_opy_
  try:
    if config.get(bstack11l11ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬ᎗"), False):
      return
    uuid = os.getenv(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ᎘"))
    if not uuid or uuid == bstack11l11ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ᎙"):
      return
    bstack1111ll1l1l_opy_ = [bstack11l11ll_opy_ (u"࠭ࡲࡦࡳࡸ࡭ࡷ࡫࡭ࡦࡰࡷࡷ࠳ࡺࡸࡵࠩ᎚"), bstack11l11ll_opy_ (u"ࠧࡑ࡫ࡳࡪ࡮ࡲࡥࠨ᎛"), bstack11l11ll_opy_ (u"ࠨࡲࡼࡴࡷࡵࡪࡦࡥࡷ࠲ࡹࡵ࡭࡭ࠩ᎜"), bstack1111lll1ll_opy_]
    bstack1ll11l1ll1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯࡯ࡳ࡬ࡹ࠭ࠨ᎝") + uuid + bstack11l11ll_opy_ (u"ࠪ࠲ࡹࡧࡲ࠯ࡩࡽࠫ᎞"))
    with tarfile.open(output_file, bstack11l11ll_opy_ (u"ࠦࡼࡀࡧࡻࠤ᎟")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1111ll1l1l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1111lll111_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1111l1llll_opy_ = data.encode()
        tarinfo.size = len(bstack1111l1llll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1111l1llll_opy_))
    bstack1l1llll1ll_opy_ = MultipartEncoder(
      fields= {
        bstack11l11ll_opy_ (u"ࠬࡪࡡࡵࡣࠪᎠ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l11ll_opy_ (u"࠭ࡲࡣࠩᎡ")), bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾ࠭ࡨࡼ࡬ࡴࠬᎢ")),
        bstack11l11ll_opy_ (u"ࠨࡥ࡯࡭ࡪࡴࡴࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᎣ"): uuid
      }
    )
    response = requests.post(
      bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡹࡵࡲ࡯ࡢࡦ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦᎤ"),
      data=bstack1l1llll1ll_opy_,
      headers={bstack11l11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᎥ"): bstack1l1llll1ll_opy_.content_type},
      auth=(config[bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭Ꭶ")], config[bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᎧ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬᎨ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l11ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭Ꭹ") + str(e))
  finally:
    try:
      bstack1111lll11l_opy_()
    except:
      pass
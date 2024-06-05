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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack111l11ll_opy_, bstack11llll11l_opy_
class bstack1ll1ll1ll_opy_:
  working_dir = os.getcwd()
  bstack111l1l1l1_opy_ = False
  config = {}
  binary_path = bstack11l11ll_opy_ (u"ࠩࠪᏱ")
  bstack1llllllll11_opy_ = bstack11l11ll_opy_ (u"ࠪࠫᏲ")
  bstack1lll11l1_opy_ = False
  bstack11111111l1_opy_ = None
  bstack1111l11l1l_opy_ = {}
  bstack11111l1ll1_opy_ = 300
  bstack1111l11l11_opy_ = False
  logger = None
  bstack11111l11l1_opy_ = False
  bstack11111lll11_opy_ = bstack11l11ll_opy_ (u"ࠫࠬᏳ")
  bstack1lllllll11l_opy_ = {
    bstack11l11ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᏴ") : 1,
    bstack11l11ll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧᏵ") : 2,
    bstack11l11ll_opy_ (u"ࠧࡦࡦࡪࡩࠬ᏶") : 3,
    bstack11l11ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ᏷") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111l1l111_opy_(self):
    bstack1llllllllll_opy_ = bstack11l11ll_opy_ (u"ࠩࠪᏸ")
    bstack1llllllll1l_opy_ = sys.platform
    bstack1111l1111l_opy_ = bstack11l11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᏹ")
    if re.match(bstack11l11ll_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦᏺ"), bstack1llllllll1l_opy_) != None:
      bstack1llllllllll_opy_ = bstack11l11ll111_opy_ + bstack11l11ll_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨᏻ")
      self.bstack11111lll11_opy_ = bstack11l11ll_opy_ (u"࠭࡭ࡢࡥࠪᏼ")
    elif re.match(bstack11l11ll_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧᏽ"), bstack1llllllll1l_opy_) != None:
      bstack1llllllllll_opy_ = bstack11l11ll111_opy_ + bstack11l11ll_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤ᏾")
      bstack1111l1111l_opy_ = bstack11l11ll_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧ᏿")
      self.bstack11111lll11_opy_ = bstack11l11ll_opy_ (u"ࠪࡻ࡮ࡴࠧ᐀")
    else:
      bstack1llllllllll_opy_ = bstack11l11ll111_opy_ + bstack11l11ll_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢᐁ")
      self.bstack11111lll11_opy_ = bstack11l11ll_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫᐂ")
    return bstack1llllllllll_opy_, bstack1111l1111l_opy_
  def bstack111111111l_opy_(self):
    try:
      bstack1llllll1l1l_opy_ = [os.path.join(expanduser(bstack11l11ll_opy_ (u"ࠨࡾࠣᐃ")), bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᐄ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll1l1l_opy_:
        if(self.bstack1llllll1ll1_opy_(path)):
          return path
      raise bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡱࡨࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᐅ")
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦᐆ").format(e))
  def bstack1llllll1ll1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack111111ll1l_opy_(self, bstack1llllllllll_opy_, bstack1111l1111l_opy_):
    try:
      bstack111111llll_opy_ = self.bstack111111111l_opy_()
      bstack1lllllll1ll_opy_ = os.path.join(bstack111111llll_opy_, bstack11l11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ᐇ"))
      bstack11111l1111_opy_ = os.path.join(bstack111111llll_opy_, bstack1111l1111l_opy_)
      if os.path.exists(bstack11111l1111_opy_):
        self.logger.info(bstack11l11ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᐈ").format(bstack11111l1111_opy_))
        return bstack11111l1111_opy_
      if os.path.exists(bstack1lllllll1ll_opy_):
        self.logger.info(bstack11l11ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥᐉ").format(bstack1lllllll1ll_opy_))
        return self.bstack11111l1l11_opy_(bstack1lllllll1ll_opy_, bstack1111l1111l_opy_)
      self.logger.info(bstack11l11ll_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦᐊ").format(bstack1llllllllll_opy_))
      response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"ࠧࡈࡇࡗࠫᐋ"), bstack1llllllllll_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1lllllll1ll_opy_, bstack11l11ll_opy_ (u"ࠨࡹࡥࠫᐌ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l11ll_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࢃࠢᐍ").format(bstack1lllllll1ll_opy_))
        return self.bstack11111l1l11_opy_(bstack1lllllll1ll_opy_, bstack1111l1111l_opy_)
      else:
        raise(bstack11l11ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࢂࠨᐎ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧᐏ").format(e))
  def bstack1111l111l1_opy_(self, bstack1llllllllll_opy_, bstack1111l1111l_opy_):
    try:
      retry = 2
      bstack11111l1111_opy_ = None
      bstack11111lll1l_opy_ = False
      while retry > 0:
        bstack11111l1111_opy_ = self.bstack111111ll1l_opy_(bstack1llllllllll_opy_, bstack1111l1111l_opy_)
        bstack11111lll1l_opy_ = self.bstack1111l11ll1_opy_(bstack1llllllllll_opy_, bstack1111l1111l_opy_, bstack11111l1111_opy_)
        if bstack11111lll1l_opy_:
          break
        retry -= 1
      return bstack11111l1111_opy_, bstack11111lll1l_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤᐐ").format(e))
    return bstack11111l1111_opy_, False
  def bstack1111l11ll1_opy_(self, bstack1llllllllll_opy_, bstack1111l1111l_opy_, bstack11111l1111_opy_, bstack11111llll1_opy_ = 0):
    if bstack11111llll1_opy_ > 1:
      return False
    if bstack11111l1111_opy_ == None or os.path.exists(bstack11111l1111_opy_) == False:
      self.logger.warn(bstack11l11ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᐑ"))
      return False
    bstack111111l1ll_opy_ = bstack11l11ll_opy_ (u"ࠢ࡟࠰࠭ࡄࡵ࡫ࡲࡤࡻ࡟࠳ࡨࡲࡩࠡ࡞ࡧ࠲ࡡࡪࠫ࠯࡞ࡧ࠯ࠧᐒ")
    command = bstack11l11ll_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧᐓ").format(bstack11111l1111_opy_)
    bstack1llllll1lll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111111l1ll_opy_, bstack1llllll1lll_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l11ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣᐔ"))
      return False
  def bstack11111l1l11_opy_(self, bstack1lllllll1ll_opy_, bstack1111l1111l_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllllll1ll_opy_)
      shutil.unpack_archive(bstack1lllllll1ll_opy_, working_dir)
      bstack11111l1111_opy_ = os.path.join(working_dir, bstack1111l1111l_opy_)
      os.chmod(bstack11111l1111_opy_, 0o755)
      return bstack11111l1111_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᐕ"))
  def bstack1111l111ll_opy_(self):
    try:
      percy = str(self.config.get(bstack11l11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᐖ"), bstack11l11ll_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᐗ"))).lower()
      if percy != bstack11l11ll_opy_ (u"ࠨࡴࡳࡷࡨࠦᐘ"):
        return False
      self.bstack1lll11l1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᐙ").format(e))
  def bstack11111lllll_opy_(self):
    try:
      bstack11111lllll_opy_ = str(self.config.get(bstack11l11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᐚ"), bstack11l11ll_opy_ (u"ࠤࡤࡹࡹࡵࠢᐛ"))).lower()
      return bstack11111lllll_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᐜ").format(e))
  def init(self, bstack111l1l1l1_opy_, config, logger):
    self.bstack111l1l1l1_opy_ = bstack111l1l1l1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111l111ll_opy_():
      return
    self.bstack1111l11l1l_opy_ = config.get(bstack11l11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᐝ"), {})
    self.bstack11111ll111_opy_ = config.get(bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᐞ"), bstack11l11ll_opy_ (u"ࠨࡡࡶࡶࡲࠦᐟ"))
    try:
      bstack1llllllllll_opy_, bstack1111l1111l_opy_ = self.bstack1111l1l111_opy_()
      bstack11111l1111_opy_, bstack11111lll1l_opy_ = self.bstack1111l111l1_opy_(bstack1llllllllll_opy_, bstack1111l1111l_opy_)
      if bstack11111lll1l_opy_:
        self.binary_path = bstack11111l1111_opy_
        thread = Thread(target=self.bstack1111111ll1_opy_)
        thread.start()
      else:
        self.bstack11111l11l1_opy_ = True
        self.logger.error(bstack11l11ll_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾ࠮࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡖࡥࡳࡥࡼࠦᐠ").format(bstack11111l1111_opy_))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᐡ").format(e))
  def bstack111111l11l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l11ll_opy_ (u"ࠩ࡯ࡳ࡬࠭ᐢ"), bstack11l11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰࡯ࡳ࡬࠭ᐣ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡕࡻࡳࡩ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࡴࠢࡤࡸࠥࢁࡽࠣᐤ").format(logfile))
      self.bstack1llllllll11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࠡࡲࡤࡸ࡭࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᐥ").format(e))
  def bstack1111111ll1_opy_(self):
    bstack11111ll1ll_opy_ = self.bstack1lllllllll1_opy_()
    if bstack11111ll1ll_opy_ == None:
      self.bstack11111l11l1_opy_ = True
      self.logger.error(bstack11l11ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠤᐦ"))
      return False
    command_args = [bstack11l11ll_opy_ (u"ࠢࡢࡲࡳ࠾ࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠣᐧ") if self.bstack111l1l1l1_opy_ else bstack11l11ll_opy_ (u"ࠨࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠬᐨ")]
    bstack111111l1l1_opy_ = self.bstack111111ll11_opy_()
    if bstack111111l1l1_opy_ != None:
      command_args.append(bstack11l11ll_opy_ (u"ࠤ࠰ࡧࠥࢁࡽࠣᐩ").format(bstack111111l1l1_opy_))
    env = os.environ.copy()
    env[bstack11l11ll_opy_ (u"ࠥࡔࡊࡘࡃ࡚ࡡࡗࡓࡐࡋࡎࠣᐪ")] = bstack11111ll1ll_opy_
    bstack11111111ll_opy_ = [self.binary_path]
    self.bstack111111l11l_opy_()
    self.bstack11111111l1_opy_ = self.bstack1111l11111_opy_(bstack11111111ll_opy_ + command_args, env)
    self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧᐫ"))
    bstack11111llll1_opy_ = 0
    while self.bstack11111111l1_opy_.poll() == None:
      bstack11111ll1l1_opy_ = self.bstack11111l11ll_opy_()
      if bstack11111ll1l1_opy_:
        self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣᐬ"))
        self.bstack1111l11l11_opy_ = True
        return True
      bstack11111llll1_opy_ += 1
      self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤᐭ").format(bstack11111llll1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧᐮ").format(bstack11111llll1_opy_))
    self.bstack11111l11l1_opy_ = True
    return False
  def bstack11111l11ll_opy_(self, bstack11111llll1_opy_ = 0):
    try:
      if bstack11111llll1_opy_ > 10:
        return False
      bstack11111l1l1l_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨᐯ"), bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪᐰ"))
      bstack11111ll11l_opy_ = bstack11111l1l1l_opy_ + bstack11l11l1lll_opy_
      response = requests.get(bstack11111ll11l_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack1lllllllll1_opy_(self):
    bstack1lllllll111_opy_ = bstack11l11ll_opy_ (u"ࠪࡥࡵࡶࠧᐱ") if self.bstack111l1l1l1_opy_ else bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᐲ")
    bstack111l1lll11_opy_ = bstack11l11ll_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠦᐳ").format(self.config[bstack11l11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᐴ")], bstack1lllllll111_opy_)
    uri = bstack111l11ll_opy_(bstack111l1lll11_opy_)
    try:
      response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"ࠧࡈࡇࡗࠫᐵ"), uri, {}, {bstack11l11ll_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᐶ"): (self.config[bstack11l11ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᐷ")], self.config[bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᐸ")])})
      if response.status_code == 200:
        bstack11111l1lll_opy_ = response.json()
        if bstack11l11ll_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᐹ") in bstack11111l1lll_opy_:
          return bstack11111l1lll_opy_[bstack11l11ll_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᐺ")]
        else:
          raise bstack11l11ll_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᐻ").format(bstack11111l1lll_opy_)
      else:
        raise bstack11l11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᐼ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᐽ").format(e))
  def bstack111111ll11_opy_(self):
    bstack111111lll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᐾ"))
    try:
      if bstack11l11ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᐿ") not in self.bstack1111l11l1l_opy_:
        self.bstack1111l11l1l_opy_[bstack11l11ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᑀ")] = 2
      with open(bstack111111lll1_opy_, bstack11l11ll_opy_ (u"ࠬࡽࠧᑁ")) as fp:
        json.dump(self.bstack1111l11l1l_opy_, fp)
      return bstack111111lll1_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᑂ").format(e))
  def bstack1111l11111_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11111lll11_opy_ == bstack11l11ll_opy_ (u"ࠧࡸ࡫ࡱࠫᑃ"):
        bstack1111111111_opy_ = [bstack11l11ll_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᑄ"), bstack11l11ll_opy_ (u"ࠩ࠲ࡧࠬᑅ")]
        cmd = bstack1111111111_opy_ + cmd
      cmd = bstack11l11ll_opy_ (u"ࠪࠤࠬᑆ").join(cmd)
      self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣᑇ").format(cmd))
      with open(self.bstack1llllllll11_opy_, bstack11l11ll_opy_ (u"ࠧࡧࠢᑈ")) as bstack111111l111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111111l111_opy_, text=True, stderr=bstack111111l111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11111l11l1_opy_ = True
      self.logger.error(bstack11l11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᑉ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1111l11l11_opy_:
        self.logger.info(bstack11l11ll_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣᑊ"))
        cmd = [self.binary_path, bstack11l11ll_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦᑋ")]
        self.bstack1111l11111_opy_(cmd)
        self.bstack1111l11l11_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᑌ").format(cmd, e))
  def bstack1lllll1l11_opy_(self):
    if not self.bstack1lll11l1_opy_:
      return
    try:
      bstack1lllllll1l1_opy_ = 0
      while not self.bstack1111l11l11_opy_ and bstack1lllllll1l1_opy_ < self.bstack11111l1ll1_opy_:
        if self.bstack11111l11l1_opy_:
          self.logger.info(bstack11l11ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣᑍ"))
          return
        time.sleep(1)
        bstack1lllllll1l1_opy_ += 1
      os.environ[bstack11l11ll_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪᑎ")] = str(self.bstack1111111lll_opy_())
      self.logger.info(bstack11l11ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨᑏ"))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᑐ").format(e))
  def bstack1111111lll_opy_(self):
    if self.bstack111l1l1l1_opy_:
      return
    try:
      bstack1111111l1l_opy_ = [platform[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᑑ")].lower() for platform in self.config.get(bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᑒ"), [])]
      bstack1111111l11_opy_ = sys.maxsize
      bstack11111l111l_opy_ = bstack11l11ll_opy_ (u"ࠩࠪᑓ")
      for browser in bstack1111111l1l_opy_:
        if browser in self.bstack1lllllll11l_opy_:
          bstack1111l11lll_opy_ = self.bstack1lllllll11l_opy_[browser]
        if bstack1111l11lll_opy_ < bstack1111111l11_opy_:
          bstack1111111l11_opy_ = bstack1111l11lll_opy_
          bstack11111l111l_opy_ = browser
      return bstack11111l111l_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᑔ").format(e))
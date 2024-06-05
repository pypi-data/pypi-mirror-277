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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from uuid import uuid4
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack11111llll_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l1l111lll_opy_ import bstack1l1ll1ll1l_opy_
import time
import requests
def bstack1111111l_opy_():
  global CONFIG
  headers = {
        bstack11l11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack11l11ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack1ll11llll_opy_(CONFIG, bstack1l1l111111_opy_)
  try:
    response = requests.get(bstack1l1l111111_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1ll1ll111_opy_ = response.json()[bstack11l11ll_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack11111l11_opy_.format(response.json()))
      return bstack1ll1ll111_opy_
    else:
      logger.debug(bstack11lll111l_opy_.format(bstack11l11ll_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack11lll111l_opy_.format(e))
def bstack1lll1111_opy_(hub_url):
  global CONFIG
  url = bstack11l11ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack11l11ll_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack11l11ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack11l11ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack1ll11llll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111l1l1ll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1lll1l1lll_opy_.format(hub_url, e))
def bstack1l111l1ll_opy_():
  try:
    global bstack1l11ll11_opy_
    bstack1ll1ll111_opy_ = bstack1111111l_opy_()
    bstack1l111lll_opy_ = []
    results = []
    for bstack1l11l1l11_opy_ in bstack1ll1ll111_opy_:
      bstack1l111lll_opy_.append(bstack111lll111_opy_(target=bstack1lll1111_opy_,args=(bstack1l11l1l11_opy_,)))
    for t in bstack1l111lll_opy_:
      t.start()
    for t in bstack1l111lll_opy_:
      results.append(t.join())
    bstack11l1l111_opy_ = {}
    for item in results:
      hub_url = item[bstack11l11ll_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack11l11ll_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack11l1l111_opy_[hub_url] = latency
    bstack1l11l111l_opy_ = min(bstack11l1l111_opy_, key= lambda x: bstack11l1l111_opy_[x])
    bstack1l11ll11_opy_ = bstack1l11l111l_opy_
    logger.debug(bstack111l11ll1_opy_.format(bstack1l11l111l_opy_))
  except Exception as e:
    logger.debug(bstack1lll111lll_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack1lll11l11l_opy_
from bstack_utils.config import Config
from bstack_utils.helper import bstack1lll1ll1ll_opy_, bstack11llll11l_opy_, bstack111l11ll_opy_, bstack11l11lll1_opy_, bstack11ll1ll11_opy_, \
  Notset, bstack11llllll_opy_, \
  bstack1ll111ll1l_opy_, bstack1lllll1111_opy_, bstack1l11l1ll11_opy_, bstack11ll1l1l_opy_, bstack1111l11l1_opy_, bstack1ll11ll1l1_opy_, \
  bstack1lll1lll1l_opy_, \
  bstack1ll1ll1lll_opy_, bstack1ll11lll11_opy_, bstack1l1l1llll_opy_, bstack1l1llll1l1_opy_, \
  bstack1l1l111l11_opy_, bstack1l1111lll_opy_, bstack1lll1lll11_opy_
from bstack_utils.bstack1lll111l1_opy_ import bstack1111llll_opy_
from bstack_utils.bstack1ll11111ll_opy_ import bstack1l1l1111l1_opy_
from bstack_utils.bstack1111l1ll1_opy_ import bstack11ll1lll1_opy_, bstack1l1l1l111l_opy_
from bstack_utils.bstack1l1lll1l1l_opy_ import bstack1l1l1111l_opy_
from bstack_utils.bstack1l1l1l1lll_opy_ import bstack1l1l1l1lll_opy_
from bstack_utils.proxy import bstack111l1lll1_opy_, bstack1ll11llll_opy_, bstack1ll11ll111_opy_, bstack11111lll1_opy_
import bstack_utils.bstack1111l1ll_opy_ as bstack1l1l111ll_opy_
from browserstack_sdk.bstack11ll111l1_opy_ import *
from browserstack_sdk.bstack1ll11l111l_opy_ import *
from bstack_utils.bstack1l1ll1l1ll_opy_ import bstack1l1l1lll11_opy_
bstack1ll1lll11_opy_ = bstack11l11ll_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ࢀ")
bstack1lllll1l1_opy_ = bstack11l11ll_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭ࢁ")
from ._version import __version__
bstack1lll1111l1_opy_ = None
CONFIG = {}
bstack1l11ll111_opy_ = {}
bstack1l11l1l1ll_opy_ = {}
bstack1ll1ll1l_opy_ = None
bstack11l11111_opy_ = None
bstack1l1ll111_opy_ = None
bstack11ll1l1l1_opy_ = -1
bstack1111ll11_opy_ = 0
bstack111l11l1_opy_ = bstack11l11l111_opy_
bstack11l1ll1l_opy_ = 1
bstack111ll1lll_opy_ = False
bstack11lll1l1_opy_ = False
bstack111l1l111_opy_ = bstack11l11ll_opy_ (u"ࠨࠩࢂ")
bstack1llll1l11_opy_ = bstack11l11ll_opy_ (u"ࠩࠪࢃ")
bstack1111ll11l_opy_ = False
bstack1ll11l1111_opy_ = True
bstack1l1l1l1l1l_opy_ = bstack11l11ll_opy_ (u"ࠪࠫࢄ")
bstack1l111111_opy_ = []
bstack1l11ll11_opy_ = bstack11l11ll_opy_ (u"ࠫࠬࢅ")
bstack11lll1l1l_opy_ = False
bstack1llll1l1ll_opy_ = None
bstack1lll1l111l_opy_ = None
bstack1l1l111l1_opy_ = None
bstack11l1lllll_opy_ = -1
bstack1ll1lll1l1_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠬࢄࠧࢆ")), bstack11l11ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ࢇ"), bstack11l11ll_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬ࢈"))
bstack11ll111ll_opy_ = 0
bstack1l1l11l1ll_opy_ = 0
bstack11l1ll11_opy_ = []
bstack1lll11l1ll_opy_ = []
bstack1llll11l11_opy_ = []
bstack11ll1l11_opy_ = []
bstack1ll1111ll_opy_ = bstack11l11ll_opy_ (u"ࠨࠩࢉ")
bstack11111l1l_opy_ = bstack11l11ll_opy_ (u"ࠩࠪࢊ")
bstack1llll1111l_opy_ = False
bstack11ll1111_opy_ = False
bstack11lllllll_opy_ = {}
bstack111ll11l_opy_ = None
bstack11l111ll_opy_ = None
bstack1l1l1llll1_opy_ = None
bstack1ll1l11lll_opy_ = None
bstack11l1111l_opy_ = None
bstack111ll1l11_opy_ = None
bstack1llll11l1l_opy_ = None
bstack11ll1l1ll_opy_ = None
bstack1lll11ll_opy_ = None
bstack1llllll111_opy_ = None
bstack111llllll_opy_ = None
bstack1lll111l1l_opy_ = None
bstack1l1ll1lll_opy_ = None
bstack1lll1l1l_opy_ = None
bstack1l11ll111l_opy_ = None
bstack11l11111l_opy_ = None
bstack1l11l1l111_opy_ = None
bstack1l1llllll_opy_ = None
bstack1ll1l1l11_opy_ = None
bstack1lll1111ll_opy_ = None
bstack11lllll1_opy_ = None
bstack1l1ll1l111_opy_ = False
bstack1ll1111lll_opy_ = bstack11l11ll_opy_ (u"ࠥࠦࢋ")
logger = bstack1lll11l11l_opy_.get_logger(__name__, bstack111l11l1_opy_)
bstack1ll1111l1_opy_ = Config.bstack11l11l11_opy_()
percy = bstack1ll1ll1ll_opy_()
bstack1lll11l1_opy_ = bstack1l1ll1ll1l_opy_()
def bstack111111ll1_opy_():
  global CONFIG
  global bstack1llll1111l_opy_
  global bstack1ll1111l1_opy_
  bstack1lllllllll_opy_ = bstack1111ll1l_opy_(CONFIG)
  if bstack11ll1ll11_opy_(CONFIG):
    if (bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ࢌ") in bstack1lllllllll_opy_ and str(bstack1lllllllll_opy_[bstack11l11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࢍ")]).lower() == bstack11l11ll_opy_ (u"࠭ࡴࡳࡷࡨࠫࢎ")):
      bstack1llll1111l_opy_ = True
    bstack1ll1111l1_opy_.bstack1ll11l11ll_opy_(bstack1lllllllll_opy_.get(bstack11l11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ࢏"), False))
  else:
    bstack1llll1111l_opy_ = True
    bstack1ll1111l1_opy_.bstack1ll11l11ll_opy_(True)
def bstack1lll1l1l1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1l1l11ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1l1l11_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l11ll_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ࢐") == args[i].lower() or bstack11l11ll_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ࢑") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1l1l1l1l_opy_
      bstack1l1l1l1l1l_opy_ += bstack11l11ll_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ࢒") + path
      return path
  return None
bstack1lll1111l_opy_ = re.compile(bstack11l11ll_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ࢓"))
def bstack1l111l1l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1lll1111l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l11ll_opy_ (u"ࠧࠪࡻࠣ࢔") + group + bstack11l11ll_opy_ (u"ࠨࡽࠣ࢕"), os.environ.get(group))
  return value
def bstack1lllll1l1l_opy_():
  bstack1ll111l11_opy_ = bstack1l1l1l11_opy_()
  if bstack1ll111l11_opy_ and os.path.exists(os.path.abspath(bstack1ll111l11_opy_)):
    fileName = bstack1ll111l11_opy_
  if bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢖") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࢗ")])) and not bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ࢘") in locals():
    fileName = os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")]
  if bstack11l11ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    bstack111lll_opy_ = os.path.abspath(fileName)
  else:
    bstack111lll_opy_ = bstack11l11ll_opy_ (u"࢛ࠬ࠭")
  bstack1ll1l1llll_opy_ = os.getcwd()
  bstack1l1ll1ll_opy_ = bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ࢜")
  bstack11111111l_opy_ = bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ࢝")
  while (not os.path.exists(bstack111lll_opy_)) and bstack1ll1l1llll_opy_ != bstack11l11ll_opy_ (u"ࠣࠤ࢞"):
    bstack111lll_opy_ = os.path.join(bstack1ll1l1llll_opy_, bstack1l1ll1ll_opy_)
    if not os.path.exists(bstack111lll_opy_):
      bstack111lll_opy_ = os.path.join(bstack1ll1l1llll_opy_, bstack11111111l_opy_)
    if bstack1ll1l1llll_opy_ != os.path.dirname(bstack1ll1l1llll_opy_):
      bstack1ll1l1llll_opy_ = os.path.dirname(bstack1ll1l1llll_opy_)
    else:
      bstack1ll1l1llll_opy_ = bstack11l11ll_opy_ (u"ࠤࠥ࢟")
  if not os.path.exists(bstack111lll_opy_):
    bstack1ll111111_opy_(
      bstack1l1ll1l1_opy_.format(os.getcwd()))
  try:
    with open(bstack111lll_opy_, bstack11l11ll_opy_ (u"ࠪࡶࠬࢠ")) as stream:
      yaml.add_implicit_resolver(bstack11l11ll_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧࢡ"), bstack1lll1111l_opy_)
      yaml.add_constructor(bstack11l11ll_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࢢ"), bstack1l111l1l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack111lll_opy_, bstack11l11ll_opy_ (u"࠭ࡲࠨࢣ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1ll111111_opy_(bstack11ll1lll_opy_.format(str(exc)))
def bstack1ll1111l11_opy_(config):
  bstack1l1ll1ll11_opy_ = bstack1lll1lllll_opy_(config)
  for option in list(bstack1l1ll1ll11_opy_):
    if option.lower() in bstack1lll111l_opy_ and option != bstack1lll111l_opy_[option.lower()]:
      bstack1l1ll1ll11_opy_[bstack1lll111l_opy_[option.lower()]] = bstack1l1ll1ll11_opy_[option]
      del bstack1l1ll1ll11_opy_[option]
  return config
def bstack1ll1lll11l_opy_():
  global bstack1l11l1l1ll_opy_
  for key, bstack11111lll_opy_ in bstack11ll11ll_opy_.items():
    if isinstance(bstack11111lll_opy_, list):
      for var in bstack11111lll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l11l1l1ll_opy_[key] = os.environ[var]
          break
    elif bstack11111lll_opy_ in os.environ and os.environ[bstack11111lll_opy_] and str(os.environ[bstack11111lll_opy_]).strip():
      bstack1l11l1l1ll_opy_[key] = os.environ[bstack11111lll_opy_]
  if bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩࢤ") in os.environ:
    bstack1l11l1l1ll_opy_[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢥ")] = {}
    bstack1l11l1l1ll_opy_[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢦ")][bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢧ")] = os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ")]
def bstack1ll1ll1l11_opy_():
  global bstack1l11ll111_opy_
  global bstack1l1l1l1l1l_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack11l11ll_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࢩ").lower() == val.lower():
      bstack1l11ll111_opy_[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")] = {}
      bstack1l11ll111_opy_[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢫ")][bstack11l11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢬ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1lll11l1l_opy_ in bstack1l111l111_opy_.items():
    if isinstance(bstack1lll11l1l_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1lll11l1l_opy_:
          if idx < len(sys.argv) and bstack11l11ll_opy_ (u"ࠩ࠰࠱ࠬࢭ") + var.lower() == val.lower() and not key in bstack1l11ll111_opy_:
            bstack1l11ll111_opy_[key] = sys.argv[idx + 1]
            bstack1l1l1l1l1l_opy_ += bstack11l11ll_opy_ (u"ࠪࠤ࠲࠳ࠧࢮ") + var + bstack11l11ll_opy_ (u"ࠫࠥ࠭ࢯ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack11l11ll_opy_ (u"ࠬ࠳࠭ࠨࢰ") + bstack1lll11l1l_opy_.lower() == val.lower() and not key in bstack1l11ll111_opy_:
          bstack1l11ll111_opy_[key] = sys.argv[idx + 1]
          bstack1l1l1l1l1l_opy_ += bstack11l11ll_opy_ (u"࠭ࠠ࠮࠯ࠪࢱ") + bstack1lll11l1l_opy_ + bstack11l11ll_opy_ (u"ࠧࠡࠩࢲ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack11l1l11ll_opy_(config):
  bstack11l1llll1_opy_ = config.keys()
  for bstack1ll1l111l1_opy_, bstack1l11111ll_opy_ in bstack11ll111l_opy_.items():
    if bstack1l11111ll_opy_ in bstack11l1llll1_opy_:
      config[bstack1ll1l111l1_opy_] = config[bstack1l11111ll_opy_]
      del config[bstack1l11111ll_opy_]
  for bstack1ll1l111l1_opy_, bstack1l11111ll_opy_ in bstack1lll1ll11l_opy_.items():
    if isinstance(bstack1l11111ll_opy_, list):
      for bstack111ll1111_opy_ in bstack1l11111ll_opy_:
        if bstack111ll1111_opy_ in bstack11l1llll1_opy_:
          config[bstack1ll1l111l1_opy_] = config[bstack111ll1111_opy_]
          del config[bstack111ll1111_opy_]
          break
    elif bstack1l11111ll_opy_ in bstack11l1llll1_opy_:
      config[bstack1ll1l111l1_opy_] = config[bstack1l11111ll_opy_]
      del config[bstack1l11111ll_opy_]
  for bstack111ll1111_opy_ in list(config):
    for bstack1l1lll11ll_opy_ in bstack1llll11l_opy_:
      if bstack111ll1111_opy_.lower() == bstack1l1lll11ll_opy_.lower() and bstack111ll1111_opy_ != bstack1l1lll11ll_opy_:
        config[bstack1l1lll11ll_opy_] = config[bstack111ll1111_opy_]
        del config[bstack111ll1111_opy_]
  bstack1l1l1lllll_opy_ = [{}]
  if not config.get(bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫࢳ")):
    config[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢴ")] = [{}]
  bstack1l1l1lllll_opy_ = config[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࢵ")]
  for platform in bstack1l1l1lllll_opy_:
    for bstack111ll1111_opy_ in list(platform):
      for bstack1l1lll11ll_opy_ in bstack1llll11l_opy_:
        if bstack111ll1111_opy_.lower() == bstack1l1lll11ll_opy_.lower() and bstack111ll1111_opy_ != bstack1l1lll11ll_opy_:
          platform[bstack1l1lll11ll_opy_] = platform[bstack111ll1111_opy_]
          del platform[bstack111ll1111_opy_]
  for bstack1ll1l111l1_opy_, bstack1l11111ll_opy_ in bstack1lll1ll11l_opy_.items():
    for platform in bstack1l1l1lllll_opy_:
      if isinstance(bstack1l11111ll_opy_, list):
        for bstack111ll1111_opy_ in bstack1l11111ll_opy_:
          if bstack111ll1111_opy_ in platform:
            platform[bstack1ll1l111l1_opy_] = platform[bstack111ll1111_opy_]
            del platform[bstack111ll1111_opy_]
            break
      elif bstack1l11111ll_opy_ in platform:
        platform[bstack1ll1l111l1_opy_] = platform[bstack1l11111ll_opy_]
        del platform[bstack1l11111ll_opy_]
  for bstack111llll11_opy_ in bstack11111l111_opy_:
    if bstack111llll11_opy_ in config:
      if not bstack11111l111_opy_[bstack111llll11_opy_] in config:
        config[bstack11111l111_opy_[bstack111llll11_opy_]] = {}
      config[bstack11111l111_opy_[bstack111llll11_opy_]].update(config[bstack111llll11_opy_])
      del config[bstack111llll11_opy_]
  for platform in bstack1l1l1lllll_opy_:
    for bstack111llll11_opy_ in bstack11111l111_opy_:
      if bstack111llll11_opy_ in list(platform):
        if not bstack11111l111_opy_[bstack111llll11_opy_] in platform:
          platform[bstack11111l111_opy_[bstack111llll11_opy_]] = {}
        platform[bstack11111l111_opy_[bstack111llll11_opy_]].update(platform[bstack111llll11_opy_])
        del platform[bstack111llll11_opy_]
  config = bstack1ll1111l11_opy_(config)
  return config
def bstack11l111l11_opy_(config):
  global bstack1llll1l11_opy_
  if bstack11ll1ll11_opy_(config) and bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࢶ") in config and str(config[bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩࢷ")]).lower() != bstack11l11ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬࢸ"):
    if not bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢹ") in config:
      config[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢺ")] = {}
    if not bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࢻ") in config[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢼ")]:
      bstack1l1ll111l_opy_ = datetime.datetime.now()
      bstack11ll1111l_opy_ = bstack1l1ll111l_opy_.strftime(bstack11l11ll_opy_ (u"ࠫࠪࡪ࡟ࠦࡤࡢࠩࡍࠫࡍࠨࢽ"))
      hostname = socket.gethostname()
      bstack1l1llll1_opy_ = bstack11l11ll_opy_ (u"ࠬ࠭ࢾ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l11ll_opy_ (u"࠭ࡻࡾࡡࡾࢁࡤࢁࡽࠨࢿ").format(bstack11ll1111l_opy_, hostname, bstack1l1llll1_opy_)
      config[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࣀ")][bstack11l11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣁ")] = identifier
    bstack1llll1l11_opy_ = config[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࣂ")][bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣃ")]
  return config
def bstack1l1lll111l_opy_():
  bstack11111ll1l_opy_ =  bstack11ll1l1l_opy_()[bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠪࣄ")]
  return bstack11111ll1l_opy_ if bstack11111ll1l_opy_ else -1
def bstack1ll11l1l_opy_(bstack11111ll1l_opy_):
  global CONFIG
  if not bstack11l11ll_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧࣅ") in CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")]:
    return
  CONFIG[bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣇ")] = CONFIG[bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣈ")].replace(
    bstack11l11ll_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫࣉ"),
    str(bstack11111ll1l_opy_)
  )
def bstack1ll1l11l1_opy_():
  global CONFIG
  if not bstack11l11ll_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ࣊") in CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣋")]:
    return
  bstack1l1ll111l_opy_ = datetime.datetime.now()
  bstack11ll1111l_opy_ = bstack1l1ll111l_opy_.strftime(bstack11l11ll_opy_ (u"ࠬࠫࡤ࠮ࠧࡥ࠱ࠪࡎ࠺ࠦࡏࠪ࣌"))
  CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣍")] = CONFIG[bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣎")].replace(
    bstack11l11ll_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃ࣏ࠧ"),
    bstack11ll1111l_opy_
  )
def bstack1l11l1l1l1_opy_():
  global CONFIG
  if bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ") in CONFIG and not bool(CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")]):
    del CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭")]
    return
  if not bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ") in CONFIG:
    CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣔ")] = bstack11l11ll_opy_ (u"ࠧࠤࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣕ")
  if bstack11l11ll_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧࣖ") in CONFIG[bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣗ")]:
    bstack1ll1l11l1_opy_()
    os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧࣘ")] = CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣙ")]
  if not bstack11l11ll_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧࣚ") in CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣛ")]:
    return
  bstack11111ll1l_opy_ = bstack11l11ll_opy_ (u"ࠧࠨࣜ")
  bstack11l11l1l1_opy_ = bstack1l1lll111l_opy_()
  if bstack11l11l1l1_opy_ != -1:
    bstack11111ll1l_opy_ = bstack11l11ll_opy_ (u"ࠨࡅࡌࠤࠬࣝ") + str(bstack11l11l1l1_opy_)
  if bstack11111ll1l_opy_ == bstack11l11ll_opy_ (u"ࠩࠪࣞ"):
    bstack111l11l11_opy_ = bstack1llllll11l_opy_(CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ࣟ")])
    if bstack111l11l11_opy_ != -1:
      bstack11111ll1l_opy_ = str(bstack111l11l11_opy_)
  if bstack11111ll1l_opy_:
    bstack1ll11l1l_opy_(bstack11111ll1l_opy_)
    os.environ[bstack11l11ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ࣠")] = CONFIG[bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣡")]
def bstack1ll11ll11l_opy_(bstack1ll111llll_opy_, bstack111ll11l1_opy_, path):
  bstack1l1l1111_opy_ = {
    bstack11l11ll_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ࣢"): bstack111ll11l1_opy_
  }
  if os.path.exists(path):
    bstack11l111l1l_opy_ = json.load(open(path, bstack11l11ll_opy_ (u"ࠧࡳࡤࣣࠪ")))
  else:
    bstack11l111l1l_opy_ = {}
  bstack11l111l1l_opy_[bstack1ll111llll_opy_] = bstack1l1l1111_opy_
  with open(path, bstack11l11ll_opy_ (u"ࠣࡹ࠮ࠦࣤ")) as outfile:
    json.dump(bstack11l111l1l_opy_, outfile)
def bstack1llllll11l_opy_(bstack1ll111llll_opy_):
  bstack1ll111llll_opy_ = str(bstack1ll111llll_opy_)
  bstack1lllll1ll_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠩࢁࠫࣥ")), bstack11l11ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࣦࠪ"))
  try:
    if not os.path.exists(bstack1lllll1ll_opy_):
      os.makedirs(bstack1lllll1ll_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠫࢃ࠭ࣧ")), bstack11l11ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬࣨ"), bstack11l11ll_opy_ (u"࠭࠮ࡣࡷ࡬ࡰࡩ࠳࡮ࡢ࡯ࡨ࠱ࡨࡧࡣࡩࡧ࠱࡮ࡸࡵ࡮ࠨࣩ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l11ll_opy_ (u"ࠧࡸࠩ࣪")):
        pass
      with open(file_path, bstack11l11ll_opy_ (u"ࠣࡹ࠮ࠦ࣫")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l11ll_opy_ (u"ࠩࡵࠫ࣬")) as bstack111l11l1l_opy_:
      bstack11l1lll1l_opy_ = json.load(bstack111l11l1l_opy_)
    if bstack1ll111llll_opy_ in bstack11l1lll1l_opy_:
      bstack1l11l1ll1l_opy_ = bstack11l1lll1l_opy_[bstack1ll111llll_opy_][bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣭ࠧ")]
      bstack1ll1lll1l_opy_ = int(bstack1l11l1ll1l_opy_) + 1
      bstack1ll11ll11l_opy_(bstack1ll111llll_opy_, bstack1ll1lll1l_opy_, file_path)
      return bstack1ll1lll1l_opy_
    else:
      bstack1ll11ll11l_opy_(bstack1ll111llll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11111l1l1_opy_.format(str(e)))
    return -1
def bstack11111ll11_opy_(config):
  if not config[bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࣮࠭")] or not config[bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ࣯")]:
    return True
  else:
    return False
def bstack1l1lll1lll_opy_(config, index=0):
  global bstack1111ll11l_opy_
  bstack1l11l11ll1_opy_ = {}
  caps = bstack1l1l1ll1l_opy_ + bstack1l1ll1l11_opy_
  if bstack1111ll11l_opy_:
    caps += bstack1ll111l1l_opy_
  for key in config:
    if key in caps + [bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࣰࠩ")]:
      continue
    bstack1l11l11ll1_opy_[key] = config[key]
  if bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ") in config:
    for bstack11lll1ll1_opy_ in config[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࣲࠫ")][index]:
      if bstack11lll1ll1_opy_ in caps + [bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧࣳ"), bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫࣴ")]:
        continue
      bstack1l11l11ll1_opy_[bstack11lll1ll1_opy_] = config[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣵ")][index][bstack11lll1ll1_opy_]
  bstack1l11l11ll1_opy_[bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࣶࠧ")] = socket.gethostname()
  if bstack11l11ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࣷ") in bstack1l11l11ll1_opy_:
    del (bstack1l11l11ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨࣸ")])
  return bstack1l11l11ll1_opy_
def bstack1lll1l111_opy_(config):
  global bstack1111ll11l_opy_
  bstack111111lll_opy_ = {}
  caps = bstack1l1ll1l11_opy_
  if bstack1111ll11l_opy_:
    caps += bstack1ll111l1l_opy_
  for key in caps:
    if key in config:
      bstack111111lll_opy_[key] = config[key]
  return bstack111111lll_opy_
def bstack1l1lllllll_opy_(bstack1l11l11ll1_opy_, bstack111111lll_opy_):
  bstack1lll1l11_opy_ = {}
  for key in bstack1l11l11ll1_opy_.keys():
    if key in bstack11ll111l_opy_:
      bstack1lll1l11_opy_[bstack11ll111l_opy_[key]] = bstack1l11l11ll1_opy_[key]
    else:
      bstack1lll1l11_opy_[key] = bstack1l11l11ll1_opy_[key]
  for key in bstack111111lll_opy_:
    if key in bstack11ll111l_opy_:
      bstack1lll1l11_opy_[bstack11ll111l_opy_[key]] = bstack111111lll_opy_[key]
    else:
      bstack1lll1l11_opy_[key] = bstack111111lll_opy_[key]
  return bstack1lll1l11_opy_
def bstack1l1llll11_opy_(config, index=0):
  global bstack1111ll11l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l11l11l1l_opy_ = bstack1lll1ll1ll_opy_(bstack11lll1lll_opy_, config, logger)
  bstack111111lll_opy_ = bstack1lll1l111_opy_(config)
  bstack1l1l11l11_opy_ = bstack1l1ll1l11_opy_
  bstack1l1l11l11_opy_ += bstack1l11llll1l_opy_
  bstack111111lll_opy_ = update(bstack111111lll_opy_, bstack1l11l11l1l_opy_)
  if bstack1111ll11l_opy_:
    bstack1l1l11l11_opy_ += bstack1ll111l1l_opy_
  if bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࣹࠫ") in config:
    if bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࣺࠧ") in config[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣻ")][index]:
      caps[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩࣼ")] = config[bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨࣽ")][index][bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫࣾ")]
    if bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨࣿ") in config[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫऀ")][index]:
      caps[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪँ")] = str(config[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ं")][index][bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬः")])
    bstack1l1ll11l1_opy_ = bstack1lll1ll1ll_opy_(bstack11lll1lll_opy_, config[bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨऄ")][index], logger)
    bstack1l1l11l11_opy_ += list(bstack1l1ll11l1_opy_.keys())
    for bstack1l1111l1l_opy_ in bstack1l1l11l11_opy_:
      if bstack1l1111l1l_opy_ in config[bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index]:
        if bstack1l1111l1l_opy_ == bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩआ"):
          try:
            bstack1l1ll11l1_opy_[bstack1l1111l1l_opy_] = str(config[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack1l1111l1l_opy_] * 1.0)
          except:
            bstack1l1ll11l1_opy_[bstack1l1111l1l_opy_] = str(config[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack1l1111l1l_opy_])
        else:
          bstack1l1ll11l1_opy_[bstack1l1111l1l_opy_] = config[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack1l1111l1l_opy_]
        del (config[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧऊ")][index][bstack1l1111l1l_opy_])
    bstack111111lll_opy_ = update(bstack111111lll_opy_, bstack1l1ll11l1_opy_)
  bstack1l11l11ll1_opy_ = bstack1l1lll1lll_opy_(config, index)
  for bstack111ll1111_opy_ in bstack1l1ll1l11_opy_ + [bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऋ"), bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧऌ")] + list(bstack1l11l11l1l_opy_.keys()):
    if bstack111ll1111_opy_ in bstack1l11l11ll1_opy_:
      bstack111111lll_opy_[bstack111ll1111_opy_] = bstack1l11l11ll1_opy_[bstack111ll1111_opy_]
      del (bstack1l11l11ll1_opy_[bstack111ll1111_opy_])
  if bstack11llllll_opy_(config):
    bstack1l11l11ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧऍ")] = True
    caps.update(bstack111111lll_opy_)
    caps[bstack11l11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩऎ")] = bstack1l11l11ll1_opy_
  else:
    bstack1l11l11ll1_opy_[bstack11l11ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩए")] = False
    caps.update(bstack1l1lllllll_opy_(bstack1l11l11ll1_opy_, bstack111111lll_opy_))
    if bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨऐ") in caps:
      caps[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬऑ")] = caps[bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऒ")]
      del (caps[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫओ")])
    if bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨऔ") in caps:
      caps[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪक")] = caps[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪख")]
      del (caps[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫग")])
  return caps
def bstack1lll1ll1l_opy_():
  global bstack1l11ll11_opy_
  if bstack1l1l1l11ll_opy_() <= version.parse(bstack11l11ll_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫघ")):
    if bstack1l11ll11_opy_ != bstack11l11ll_opy_ (u"ࠬ࠭ङ"):
      return bstack11l11ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢच") + bstack1l11ll11_opy_ + bstack11l11ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦछ")
    return bstack111l111ll_opy_
  if bstack1l11ll11_opy_ != bstack11l11ll_opy_ (u"ࠨࠩज"):
    return bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦझ") + bstack1l11ll11_opy_ + bstack11l11ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦञ")
  return bstack1111ll1l1_opy_
def bstack1l11l1l1_opy_(options):
  return hasattr(options, bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬट"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack111lll1ll_opy_(options, bstack1111111l1_opy_):
  for bstack1l1ll1111_opy_ in bstack1111111l1_opy_:
    if bstack1l1ll1111_opy_ in [bstack11l11ll_opy_ (u"ࠬࡧࡲࡨࡵࠪठ"), bstack11l11ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪड")]:
      continue
    if bstack1l1ll1111_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1ll1111_opy_] = update(options._experimental_options[bstack1l1ll1111_opy_],
                                                         bstack1111111l1_opy_[bstack1l1ll1111_opy_])
    else:
      options.add_experimental_option(bstack1l1ll1111_opy_, bstack1111111l1_opy_[bstack1l1ll1111_opy_])
  if bstack11l11ll_opy_ (u"ࠧࡢࡴࡪࡷࠬढ") in bstack1111111l1_opy_:
    for arg in bstack1111111l1_opy_[bstack11l11ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ण")]:
      options.add_argument(arg)
    del (bstack1111111l1_opy_[bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧत")])
  if bstack11l11ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ") in bstack1111111l1_opy_:
    for ext in bstack1111111l1_opy_[bstack11l11ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨद")]:
      options.add_extension(ext)
    del (bstack1111111l1_opy_[bstack11l11ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩध")])
def bstack1l1l1l1l_opy_(options, bstack1lll1llll1_opy_):
  if bstack11l11ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन") in bstack1lll1llll1_opy_:
    for bstack11l11l11l_opy_ in bstack1lll1llll1_opy_[bstack11l11ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")]:
      if bstack11l11l11l_opy_ in options._preferences:
        options._preferences[bstack11l11l11l_opy_] = update(options._preferences[bstack11l11l11l_opy_], bstack1lll1llll1_opy_[bstack11l11ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧप")][bstack11l11l11l_opy_])
      else:
        options.set_preference(bstack11l11l11l_opy_, bstack1lll1llll1_opy_[bstack11l11ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨफ")][bstack11l11l11l_opy_])
  if bstack11l11ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨब") in bstack1lll1llll1_opy_:
    for arg in bstack1lll1llll1_opy_[bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࡴࠩभ")]:
      options.add_argument(arg)
def bstack1ll111l1_opy_(options, bstack11lllll11_opy_):
  if bstack11l11ll_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭म") in bstack11lllll11_opy_:
    options.use_webview(bool(bstack11lllll11_opy_[bstack11l11ll_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧय")]))
  bstack111lll1ll_opy_(options, bstack11lllll11_opy_)
def bstack11llll11_opy_(options, bstack11lll11l1_opy_):
  for bstack1ll1l1111_opy_ in bstack11lll11l1_opy_:
    if bstack1ll1l1111_opy_ in [bstack11l11ll_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫर"), bstack11l11ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ")]:
      continue
    options.set_capability(bstack1ll1l1111_opy_, bstack11lll11l1_opy_[bstack1ll1l1111_opy_])
  if bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧल") in bstack11lll11l1_opy_:
    for arg in bstack11lll11l1_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨळ")]:
      options.add_argument(arg)
  if bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨऴ") in bstack11lll11l1_opy_:
    options.bstack1ll1llll11_opy_(bool(bstack11lll11l1_opy_[bstack11l11ll_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩव")]))
def bstack1lll11l1l1_opy_(options, bstack1l11lll1ll_opy_):
  for bstack1l111l1l1_opy_ in bstack1l11lll1ll_opy_:
    if bstack1l111l1l1_opy_ in [bstack11l11ll_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪश"), bstack11l11ll_opy_ (u"ࠧࡢࡴࡪࡷࠬष")]:
      continue
    options._options[bstack1l111l1l1_opy_] = bstack1l11lll1ll_opy_[bstack1l111l1l1_opy_]
  if bstack11l11ll_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस") in bstack1l11lll1ll_opy_:
    for bstack1l11l1l1l_opy_ in bstack1l11lll1ll_opy_[bstack11l11ll_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ह")]:
      options.bstack1l1l11l1_opy_(
        bstack1l11l1l1l_opy_, bstack1l11lll1ll_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧऺ")][bstack1l11l1l1l_opy_])
  if bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࡴࠩऻ") in bstack1l11lll1ll_opy_:
    for arg in bstack1l11lll1ll_opy_[bstack11l11ll_opy_ (u"ࠬࡧࡲࡨࡵ़ࠪ")]:
      options.add_argument(arg)
def bstack1l11l11l11_opy_(options, caps):
  if not hasattr(options, bstack11l11ll_opy_ (u"࠭ࡋࡆ࡛ࠪऽ")):
    return
  if options.KEY == bstack11l11ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬा") and options.KEY in caps:
    bstack111lll1ll_opy_(options, caps[bstack11l11ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ि")])
  elif options.KEY == bstack11l11ll_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧी") and options.KEY in caps:
    bstack1l1l1l1l_opy_(options, caps[bstack11l11ll_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨु")])
  elif options.KEY == bstack11l11ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬू") and options.KEY in caps:
    bstack11llll11_opy_(options, caps[bstack11l11ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ृ")])
  elif options.KEY == bstack11l11ll_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॄ") and options.KEY in caps:
    bstack1ll111l1_opy_(options, caps[bstack11l11ll_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨॅ")])
  elif options.KEY == bstack11l11ll_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॆ") and options.KEY in caps:
    bstack1lll11l1l1_opy_(options, caps[bstack11l11ll_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨे")])
def bstack1l11ll1l1_opy_(caps):
  global bstack1111ll11l_opy_
  if isinstance(os.environ.get(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫै")), str):
    bstack1111ll11l_opy_ = eval(os.getenv(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬॉ")))
  if bstack1111ll11l_opy_:
    if bstack1lll1l1l1_opy_() < version.parse(bstack11l11ll_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫॊ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l11ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ो")
    if bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬौ") in caps:
      browser = caps[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ्࠭")]
    elif bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪॎ") in caps:
      browser = caps[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫॏ")]
    browser = str(browser).lower()
    if browser == bstack11l11ll_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫॐ") or browser == bstack11l11ll_opy_ (u"ࠬ࡯ࡰࡢࡦࠪ॑"):
      browser = bstack11l11ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮॒࠭")
    if browser == bstack11l11ll_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨ॓"):
      browser = bstack11l11ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ॔")
    if browser not in [bstack11l11ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩॕ"), bstack11l11ll_opy_ (u"ࠪࡩࡩ࡭ࡥࠨॖ"), bstack11l11ll_opy_ (u"ࠫ࡮࡫ࠧॗ"), bstack11l11ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬक़"), bstack11l11ll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧख़")]:
      return None
    try:
      package = bstack11l11ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩग़").format(browser)
      name = bstack11l11ll_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩज़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l11l1l1_opy_(options):
        return None
      for bstack111ll1111_opy_ in caps.keys():
        options.set_capability(bstack111ll1111_opy_, caps[bstack111ll1111_opy_])
      bstack1l11l11l11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1llll11ll_opy_(options, bstack11lll1111_opy_):
  if not bstack1l11l1l1_opy_(options):
    return
  for bstack111ll1111_opy_ in bstack11lll1111_opy_.keys():
    if bstack111ll1111_opy_ in bstack1l11llll1l_opy_:
      continue
    if bstack111ll1111_opy_ in options._caps and type(options._caps[bstack111ll1111_opy_]) in [dict, list]:
      options._caps[bstack111ll1111_opy_] = update(options._caps[bstack111ll1111_opy_], bstack11lll1111_opy_[bstack111ll1111_opy_])
    else:
      options.set_capability(bstack111ll1111_opy_, bstack11lll1111_opy_[bstack111ll1111_opy_])
  bstack1l11l11l11_opy_(options, bstack11lll1111_opy_)
  if bstack11l11ll_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨड़") in options._caps:
    if options._caps[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨढ़")] and options._caps[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩफ़")].lower() != bstack11l11ll_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭य़"):
      del options._caps[bstack11l11ll_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬॠ")]
def bstack111l111l1_opy_(proxy_config):
  if bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॡ") in proxy_config:
    proxy_config[bstack11l11ll_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪॢ")] = proxy_config[bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॣ")]
    del (proxy_config[bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ।")])
  if bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ॥") in proxy_config and proxy_config[bstack11l11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ०")].lower() != bstack11l11ll_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭१"):
    proxy_config[bstack11l11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ२")] = bstack11l11ll_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨ३")
  if bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲࠧ४") in proxy_config:
    proxy_config[bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭५")] = bstack11l11ll_opy_ (u"ࠫࡵࡧࡣࠨ६")
  return proxy_config
def bstack1ll1ll1l1l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७") in config:
    return proxy
  config[bstack11l11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")] = bstack111l111l1_opy_(config[bstack11l11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭९")])
  if proxy == None:
    proxy = Proxy(config[bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ॰")])
  return proxy
def bstack1l1lll1l_opy_(self):
  global CONFIG
  global bstack1lll111l1l_opy_
  try:
    proxy = bstack1ll11ll111_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l11ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧॱ")):
        proxies = bstack111l1lll1_opy_(proxy, bstack1lll1ll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11ll1_opy_ = proxies.popitem()
          if bstack11l11ll_opy_ (u"ࠥ࠾࠴࠵ࠢॲ") in bstack1ll11ll1_opy_:
            return bstack1ll11ll1_opy_
          else:
            return bstack11l11ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧॳ") + bstack1ll11ll1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤॴ").format(str(e)))
  return bstack1lll111l1l_opy_(self)
def bstack1l1l1l11l1_opy_():
  global CONFIG
  return bstack11111lll1_opy_(CONFIG) and bstack1ll11ll1l1_opy_() and bstack1l1l1l11ll_opy_() >= version.parse(bstack1lll1l1111_opy_)
def bstack11ll11l1l_opy_():
  global CONFIG
  return (bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩॵ") in CONFIG or bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॶ") in CONFIG) and bstack1lll1lll1l_opy_()
def bstack1lll1lllll_opy_(config):
  bstack1l1ll1ll11_opy_ = {}
  if bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॷ") in config:
    bstack1l1ll1ll11_opy_ = config[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ॸ")]
  if bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩॹ") in config:
    bstack1l1ll1ll11_opy_ = config[bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪॺ")]
  proxy = bstack1ll11ll111_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l11ll_opy_ (u"ࠬ࠴ࡰࡢࡥࠪॻ")) and os.path.isfile(proxy):
      bstack1l1ll1ll11_opy_[bstack11l11ll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩॼ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l11ll_opy_ (u"ࠧ࠯ࡲࡤࡧࠬॽ")):
        proxies = bstack1ll11llll_opy_(config, bstack1lll1ll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11ll1_opy_ = proxies.popitem()
          if bstack11l11ll_opy_ (u"ࠣ࠼࠲࠳ࠧॾ") in bstack1ll11ll1_opy_:
            parsed_url = urlparse(bstack1ll11ll1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l11ll_opy_ (u"ࠤ࠽࠳࠴ࠨॿ") + bstack1ll11ll1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1l1ll1ll11_opy_[bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ঀ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1l1ll1ll11_opy_[bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧঁ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1l1ll1ll11_opy_[bstack11l11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨং")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1l1ll1ll11_opy_[bstack11l11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩঃ")] = str(parsed_url.password)
  return bstack1l1ll1ll11_opy_
def bstack1111ll1l_opy_(config):
  if bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ঄") in config:
    return config[bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭অ")]
  return {}
def bstack1llll111ll_opy_(caps):
  global bstack1llll1l11_opy_
  if bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪআ") in caps:
    caps[bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫই")][bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪঈ")] = True
    if bstack1llll1l11_opy_:
      caps[bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭উ")][bstack11l11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨঊ")] = bstack1llll1l11_opy_
  else:
    caps[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬঋ")] = True
    if bstack1llll1l11_opy_:
      caps[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩঌ")] = bstack1llll1l11_opy_
def bstack1ll1l1l1ll_opy_():
  global CONFIG
  if not bstack11ll1ll11_opy_(CONFIG):
    return
  if bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭঍") in CONFIG and bstack1lll1lll11_opy_(CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ঎")]):
    if (
      bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨএ") in CONFIG
      and bstack1lll1lll11_opy_(CONFIG[bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩঐ")].get(bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪ঑")))
    ):
      logger.debug(bstack11l11ll_opy_ (u"ࠢࡍࡱࡦࡥࡱࠦࡢࡪࡰࡤࡶࡾࠦ࡮ࡰࡶࠣࡷࡹࡧࡲࡵࡧࡧࠤࡦࡹࠠࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡦࡰࡤࡦࡱ࡫ࡤࠣ঒"))
      return
    bstack1l1ll1ll11_opy_ = bstack1lll1lllll_opy_(CONFIG)
    bstack1lll1l1ll1_opy_(CONFIG[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫও")], bstack1l1ll1ll11_opy_)
def bstack1lll1l1ll1_opy_(key, bstack1l1ll1ll11_opy_):
  global bstack1lll1111l1_opy_
  logger.info(bstack1111ll1ll_opy_)
  try:
    bstack1lll1111l1_opy_ = Local()
    bstack11ll1ll1l_opy_ = {bstack11l11ll_opy_ (u"ࠩ࡮ࡩࡾ࠭ঔ"): key}
    bstack11ll1ll1l_opy_.update(bstack1l1ll1ll11_opy_)
    logger.debug(bstack1llll1l1_opy_.format(str(bstack11ll1ll1l_opy_)))
    bstack1lll1111l1_opy_.start(**bstack11ll1ll1l_opy_)
    if bstack1lll1111l1_opy_.isRunning():
      logger.info(bstack11l1lll1_opy_)
  except Exception as e:
    bstack1ll111111_opy_(bstack11111ll1_opy_.format(str(e)))
def bstack1l1111111_opy_():
  global bstack1lll1111l1_opy_
  if bstack1lll1111l1_opy_.isRunning():
    logger.info(bstack11lll11l_opy_)
    bstack1lll1111l1_opy_.stop()
  bstack1lll1111l1_opy_ = None
def bstack1l11lll1l1_opy_(bstack1ll111lll1_opy_=[]):
  global CONFIG
  bstack1ll1llll1_opy_ = []
  bstack1ll1l111ll_opy_ = [bstack11l11ll_opy_ (u"ࠪࡳࡸ࠭ক"), bstack11l11ll_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧখ"), bstack11l11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩগ"), bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨঘ"), bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬঙ"), bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩচ")]
  try:
    for err in bstack1ll111lll1_opy_:
      bstack11ll11ll1_opy_ = {}
      for k in bstack1ll1l111ll_opy_:
        val = CONFIG[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬছ")][int(err[bstack11l11ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩজ")])].get(k)
        if val:
          bstack11ll11ll1_opy_[k] = val
      if(err[bstack11l11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪঝ")] != bstack11l11ll_opy_ (u"ࠬ࠭ঞ")):
        bstack11ll11ll1_opy_[bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬট")] = {
          err[bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬঠ")]: err[bstack11l11ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧড")]
        }
        bstack1ll1llll1_opy_.append(bstack11ll11ll1_opy_)
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫঢ") + str(e))
  finally:
    return bstack1ll1llll1_opy_
def bstack1lll1l11l_opy_(file_name):
  bstack1ll1ll11l_opy_ = []
  try:
    bstack1lllll1ll1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1lllll1ll1_opy_):
      with open(bstack1lllll1ll1_opy_) as f:
        bstack1lll11ll1_opy_ = json.load(f)
        bstack1ll1ll11l_opy_ = bstack1lll11ll1_opy_
      os.remove(bstack1lllll1ll1_opy_)
    return bstack1ll1ll11l_opy_
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬণ") + str(e))
    return bstack1ll1ll11l_opy_
def bstack11l11ll11_opy_():
  global bstack1ll1111lll_opy_
  global bstack1l111111_opy_
  global bstack11l1ll11_opy_
  global bstack1lll11l1ll_opy_
  global bstack1llll11l11_opy_
  global bstack11111l1l_opy_
  global CONFIG
  bstack1l1lll111_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬত"))
  if bstack1l1lll111_opy_ in [bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫথ"), bstack11l11ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬদ")]:
    bstack1l1l1ll1l1_opy_()
  percy.shutdown()
  if bstack1ll1111lll_opy_:
    logger.warning(bstack111111l1_opy_.format(str(bstack1ll1111lll_opy_)))
  else:
    try:
      bstack11l111l1l_opy_ = bstack1ll111ll1l_opy_(bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ধ"), logger)
      if bstack11l111l1l_opy_.get(bstack11l11ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ন")) and bstack11l111l1l_opy_.get(bstack11l11ll_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ঩")).get(bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬপ")):
        logger.warning(bstack111111l1_opy_.format(str(bstack11l111l1l_opy_[bstack11l11ll_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩফ")][bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧব")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1l11ll1l1l_opy_)
  global bstack1lll1111l1_opy_
  if bstack1lll1111l1_opy_:
    bstack1l1111111_opy_()
  try:
    for driver in bstack1l111111_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1ll111lll_opy_)
  if bstack11111l1l_opy_ == bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬভ"):
    bstack1llll11l11_opy_ = bstack1lll1l11l_opy_(bstack11l11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨম"))
  if bstack11111l1l_opy_ == bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨয") and len(bstack1lll11l1ll_opy_) == 0:
    bstack1lll11l1ll_opy_ = bstack1lll1l11l_opy_(bstack11l11ll_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧর"))
    if len(bstack1lll11l1ll_opy_) == 0:
      bstack1lll11l1ll_opy_ = bstack1lll1l11l_opy_(bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ঱"))
  bstack1ll1l1lll_opy_ = bstack11l11ll_opy_ (u"ࠫࠬল")
  if len(bstack11l1ll11_opy_) > 0:
    bstack1ll1l1lll_opy_ = bstack1l11lll1l1_opy_(bstack11l1ll11_opy_)
  elif len(bstack1lll11l1ll_opy_) > 0:
    bstack1ll1l1lll_opy_ = bstack1l11lll1l1_opy_(bstack1lll11l1ll_opy_)
  elif len(bstack1llll11l11_opy_) > 0:
    bstack1ll1l1lll_opy_ = bstack1l11lll1l1_opy_(bstack1llll11l11_opy_)
  elif len(bstack11ll1l11_opy_) > 0:
    bstack1ll1l1lll_opy_ = bstack1l11lll1l1_opy_(bstack11ll1l11_opy_)
  if bool(bstack1ll1l1lll_opy_):
    bstack1111l1111_opy_(bstack1ll1l1lll_opy_)
  else:
    bstack1111l1111_opy_()
  bstack1lllll1111_opy_(bstack1l111ll1l_opy_, logger)
  bstack1lll11l11l_opy_.bstack1111llll1_opy_(CONFIG)
  if len(bstack1llll11l11_opy_) > 0:
    sys.exit(len(bstack1llll11l11_opy_))
def bstack1l11111l_opy_(bstack1l11l1lll_opy_, frame):
  global bstack1ll1111l1_opy_
  logger.error(bstack1ll1l111_opy_)
  bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨ঳"), bstack1l11l1lll_opy_)
  if hasattr(signal, bstack11l11ll_opy_ (u"࠭ࡓࡪࡩࡱࡥࡱࡹࠧ঴")):
    bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ঵"), signal.Signals(bstack1l11l1lll_opy_).name)
  else:
    bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨশ"), bstack11l11ll_opy_ (u"ࠩࡖࡍࡌ࡛ࡎࡌࡐࡒ࡛ࡓ࠭ষ"))
  bstack1l1lll111_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫস"))
  if bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫহ"):
    bstack1l1l1111l_opy_.stop(bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ঺")))
  bstack11l11ll11_opy_()
  sys.exit(1)
def bstack1ll111111_opy_(err):
  logger.critical(bstack11l11l1l_opy_.format(str(err)))
  bstack1111l1111_opy_(bstack11l11l1l_opy_.format(str(err)), True)
  atexit.unregister(bstack11l11ll11_opy_)
  bstack1l1l1ll1l1_opy_()
  sys.exit(1)
def bstack1ll11l11l1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1111l1111_opy_(message, True)
  atexit.unregister(bstack11l11ll11_opy_)
  bstack1l1l1ll1l1_opy_()
  sys.exit(1)
def bstack111ll1ll_opy_():
  global CONFIG
  global bstack1l11ll111_opy_
  global bstack1l11l1l1ll_opy_
  global bstack1ll11l1111_opy_
  CONFIG = bstack1lllll1l1l_opy_()
  load_dotenv(CONFIG.get(bstack11l11ll_opy_ (u"࠭ࡥ࡯ࡸࡉ࡭ࡱ࡫ࠧ঻")))
  bstack1ll1lll11l_opy_()
  bstack1ll1ll1l11_opy_()
  CONFIG = bstack11l1l11ll_opy_(CONFIG)
  update(CONFIG, bstack1l11l1l1ll_opy_)
  update(CONFIG, bstack1l11ll111_opy_)
  CONFIG = bstack11l111l11_opy_(CONFIG)
  bstack1ll11l1111_opy_ = bstack11ll1ll11_opy_(CONFIG)
  bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ়"), bstack1ll11l1111_opy_)
  if (bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫঽ") in CONFIG and bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬা") in bstack1l11ll111_opy_) or (
          bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ি") in CONFIG and bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧী") not in bstack1l11l1l1ll_opy_):
    if os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩু")):
      CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨূ")] = os.getenv(bstack11l11ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫৃ"))
    else:
      bstack1l11l1l1l1_opy_()
  elif (bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫৄ") not in CONFIG and bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ৅") in CONFIG) or (
          bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭৆") in bstack1l11l1l1ll_opy_ and bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧে") not in bstack1l11ll111_opy_):
    del (CONFIG[bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧৈ")])
  if bstack11111ll11_opy_(CONFIG):
    bstack1ll111111_opy_(bstack1111l1l1_opy_)
  bstack1l11ll11ll_opy_()
  bstack1l11l111ll_opy_()
  if bstack1111ll11l_opy_:
    CONFIG[bstack11l11ll_opy_ (u"࠭ࡡࡱࡲࠪ৉")] = bstack1lllllll11_opy_(CONFIG)
    logger.info(bstack1l1lll11l1_opy_.format(CONFIG[bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࠫ৊")]))
  if not bstack1ll11l1111_opy_:
    CONFIG[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫো")] = [{}]
def bstack1ll11ll1l_opy_(config, bstack111l1l1l1_opy_):
  global CONFIG
  global bstack1111ll11l_opy_
  CONFIG = config
  bstack1111ll11l_opy_ = bstack111l1l1l1_opy_
def bstack1l11l111ll_opy_():
  global CONFIG
  global bstack1111ll11l_opy_
  if bstack11l11ll_opy_ (u"ࠩࡤࡴࡵ࠭ৌ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1111ll111_opy_)
    bstack1111ll11l_opy_ = True
    bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦ্ࠩ"), True)
def bstack1lllllll11_opy_(config):
  bstack1llll111l1_opy_ = bstack11l11ll_opy_ (u"ࠫࠬৎ")
  app = config[bstack11l11ll_opy_ (u"ࠬࡧࡰࡱࠩ৏")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l1ll1l1l_opy_:
      if os.path.exists(app):
        bstack1llll111l1_opy_ = bstack1l1l11l1l_opy_(config, app)
      elif bstack1lll1llll_opy_(app):
        bstack1llll111l1_opy_ = app
      else:
        bstack1ll111111_opy_(bstack1l111lll1_opy_.format(app))
    else:
      if bstack1lll1llll_opy_(app):
        bstack1llll111l1_opy_ = app
      elif os.path.exists(app):
        bstack1llll111l1_opy_ = bstack1l1l11l1l_opy_(app)
      else:
        bstack1ll111111_opy_(bstack1l111111l_opy_)
  else:
    if len(app) > 2:
      bstack1ll111111_opy_(bstack1lll11lll1_opy_)
    elif len(app) == 2:
      if bstack11l11ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ৐") in app and bstack11l11ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ৑") in app:
        if os.path.exists(app[bstack11l11ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭৒")]):
          bstack1llll111l1_opy_ = bstack1l1l11l1l_opy_(config, app[bstack11l11ll_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ৓")], app[bstack11l11ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭৔")])
        else:
          bstack1ll111111_opy_(bstack1l111lll1_opy_.format(app))
      else:
        bstack1ll111111_opy_(bstack1lll11lll1_opy_)
    else:
      for key in app:
        if key in bstack1ll11llll1_opy_:
          if key == bstack11l11ll_opy_ (u"ࠫࡵࡧࡴࡩࠩ৕"):
            if os.path.exists(app[key]):
              bstack1llll111l1_opy_ = bstack1l1l11l1l_opy_(config, app[key])
            else:
              bstack1ll111111_opy_(bstack1l111lll1_opy_.format(app))
          else:
            bstack1llll111l1_opy_ = app[key]
        else:
          bstack1ll111111_opy_(bstack1llll1ll1_opy_)
  return bstack1llll111l1_opy_
def bstack1lll1llll_opy_(bstack1llll111l1_opy_):
  import re
  bstack11l1lll11_opy_ = re.compile(bstack11l11ll_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ৖"))
  bstack1111l1l11_opy_ = re.compile(bstack11l11ll_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥৗ"))
  if bstack11l11ll_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭৘") in bstack1llll111l1_opy_ or re.fullmatch(bstack11l1lll11_opy_, bstack1llll111l1_opy_) or re.fullmatch(bstack1111l1l11_opy_, bstack1llll111l1_opy_):
    return True
  else:
    return False
def bstack1l1l11l1l_opy_(config, path, bstack1llllll1ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l11ll_opy_ (u"ࠨࡴࡥࠫ৙")).read()).hexdigest()
  bstack1ll1l1lll1_opy_ = bstack1ll111ll11_opy_(md5_hash)
  bstack1llll111l1_opy_ = None
  if bstack1ll1l1lll1_opy_:
    logger.info(bstack1l1ll11lll_opy_.format(bstack1ll1l1lll1_opy_, md5_hash))
    return bstack1ll1l1lll1_opy_
  bstack1l1llll1ll_opy_ = MultipartEncoder(
    fields={
      bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ৚"): (os.path.basename(path), open(os.path.abspath(path), bstack11l11ll_opy_ (u"ࠪࡶࡧ࠭৛")), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨড়")),
      bstack11l11ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨঢ়"): bstack1llllll1ll_opy_
    }
  )
  response = requests.post(bstack1lll1lll_opy_, data=bstack1l1llll1ll_opy_,
                           headers={bstack11l11ll_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ৞"): bstack1l1llll1ll_opy_.content_type},
                           auth=(config[bstack11l11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩয়")], config[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫৠ")]))
  try:
    res = json.loads(response.text)
    bstack1llll111l1_opy_ = res[bstack11l11ll_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪৡ")]
    logger.info(bstack1l11l1111l_opy_.format(bstack1llll111l1_opy_))
    bstack11l1l1111_opy_(md5_hash, bstack1llll111l1_opy_)
  except ValueError as err:
    bstack1ll111111_opy_(bstack1ll1l1l1_opy_.format(str(err)))
  return bstack1llll111l1_opy_
def bstack1l11ll11ll_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack11l1ll1l_opy_
  bstack1ll1111ll1_opy_ = 1
  bstack1l1lll1l11_opy_ = 1
  if bstack11l11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪৢ") in CONFIG:
    bstack1l1lll1l11_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫৣ")]
  else:
    bstack1l1lll1l11_opy_ = bstack1l11111l1_opy_(framework_name, args) or 1
  if bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৤") in CONFIG:
    bstack1ll1111ll1_opy_ = len(CONFIG[bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৥")])
  bstack11l1ll1l_opy_ = int(bstack1l1lll1l11_opy_) * int(bstack1ll1111ll1_opy_)
def bstack1l11111l1_opy_(framework_name, args):
  if framework_name == bstack1l11l1lll1_opy_ and args and bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ০") in args:
      bstack11l1l1ll_opy_ = args.index(bstack11l11ll_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭১"))
      return int(args[bstack11l1l1ll_opy_ + 1]) or 1
  return 1
def bstack1ll111ll11_opy_(md5_hash):
  bstack1ll1111111_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠩࢁࠫ২")), bstack11l11ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ৩"), bstack11l11ll_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ৪"))
  if os.path.exists(bstack1ll1111111_opy_):
    bstack11l1ll111_opy_ = json.load(open(bstack1ll1111111_opy_, bstack11l11ll_opy_ (u"ࠬࡸࡢࠨ৫")))
    if md5_hash in bstack11l1ll111_opy_:
      bstack1ll11l1ll_opy_ = bstack11l1ll111_opy_[md5_hash]
      bstack11l1l11l1_opy_ = datetime.datetime.now()
      bstack1111l11ll_opy_ = datetime.datetime.strptime(bstack1ll11l1ll_opy_[bstack11l11ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ৬")], bstack11l11ll_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ৭"))
      if (bstack11l1l11l1_opy_ - bstack1111l11ll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll11l1ll_opy_[bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭৮")]):
        return None
      return bstack1ll11l1ll_opy_[bstack11l11ll_opy_ (u"ࠩ࡬ࡨࠬ৯")]
  else:
    return None
def bstack11l1l1111_opy_(md5_hash, bstack1llll111l1_opy_):
  bstack1lllll1ll_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠪࢂࠬৰ")), bstack11l11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫৱ"))
  if not os.path.exists(bstack1lllll1ll_opy_):
    os.makedirs(bstack1lllll1ll_opy_)
  bstack1ll1111111_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠬࢄࠧ৲")), bstack11l11ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭৳"), bstack11l11ll_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ৴"))
  bstack11l1l1l11_opy_ = {
    bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫ৵"): bstack1llll111l1_opy_,
    bstack11l11ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ৶"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l11ll_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ৷")),
    bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ৸"): str(__version__)
  }
  if os.path.exists(bstack1ll1111111_opy_):
    bstack11l1ll111_opy_ = json.load(open(bstack1ll1111111_opy_, bstack11l11ll_opy_ (u"ࠬࡸࡢࠨ৹")))
  else:
    bstack11l1ll111_opy_ = {}
  bstack11l1ll111_opy_[md5_hash] = bstack11l1l1l11_opy_
  with open(bstack1ll1111111_opy_, bstack11l11ll_opy_ (u"ࠨࡷࠬࠤ৺")) as outfile:
    json.dump(bstack11l1ll111_opy_, outfile)
def bstack11l111ll1_opy_(self):
  return
def bstack1111lll1l_opy_(self):
  return
def bstack1l1lllll11_opy_(self):
  global bstack1l1ll1lll_opy_
  bstack1l1ll1lll_opy_(self)
def bstack1l1lllll1l_opy_():
  global bstack1l1l111l1_opy_
  bstack1l1l111l1_opy_ = True
def bstack111lll11l_opy_(self):
  global bstack111l1l111_opy_
  global bstack1ll1ll1l_opy_
  global bstack11l111ll_opy_
  try:
    if bstack11l11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ৻") in bstack111l1l111_opy_ and self.session_id != None and bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬৼ"), bstack11l11ll_opy_ (u"ࠩࠪ৽")) != bstack11l11ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ৾"):
      bstack1lll11lll_opy_ = bstack11l11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ৿") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ਀")
      if bstack1lll11lll_opy_ == bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ਁ"):
        bstack1l1l111l11_opy_(logger)
      if self != None:
        bstack11ll1lll1_opy_(self, bstack1lll11lll_opy_, bstack11l11ll_opy_ (u"ࠧ࠭ࠢࠪਂ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l11ll_opy_ (u"ࠨࠩਃ")
    if bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ਄") in bstack111l1l111_opy_ and getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩਅ"), None):
      bstack1llllllll1_opy_.bstack1l111l11l_opy_(self, bstack11lllllll_opy_, logger, wait=True)
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧਆ") + str(e))
  bstack11l111ll_opy_(self)
  self.session_id = None
def bstack1l1l1ll11_opy_(self, command_executor=bstack11l11ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨਇ"), *args, **kwargs):
  bstack111111ll_opy_ = bstack111ll11l_opy_(self, command_executor, *args, **kwargs)
  try:
    logger.debug(bstack11l11ll_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪਈ").format(str(command_executor)))
    logger.debug(bstack11l11ll_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾࠩਉ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫਊ") in command_executor._url:
      bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ਋"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭਌") in command_executor):
    bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ਍"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1l1111l_opy_.bstack111111l11_opy_(self)
  return bstack111111ll_opy_
def bstack1ll1lllll_opy_(args):
  return bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭਎") in str(args)
def bstack1lll1ll11_opy_(self, driver_command, *args, **kwargs):
  global bstack1lll1111ll_opy_
  global bstack1l1ll1l111_opy_
  bstack11l1l1ll1_opy_ = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪਏ"), None) and bstack11l11lll1_opy_(
          threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ਐ"), None)
  bstack1l1l11ll1_opy_ = getattr(self, bstack11l11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ਑"), None) != None and getattr(self, bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ਒"), None) == True
  if not bstack1l1ll1l111_opy_ and bstack1ll11l1111_opy_ and bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪਓ") in CONFIG and CONFIG[bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫਔ")] == True and bstack1l1l1l1lll_opy_.bstack11l1l1l1_opy_(driver_command) and (bstack1l1l11ll1_opy_ or bstack11l1l1ll1_opy_) and not bstack1ll1lllll_opy_(args):
    try:
      bstack1l1ll1l111_opy_ = True
      logger.debug(bstack11l11ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧਕ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l11ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫਖ").format(str(err)))
    bstack1l1ll1l111_opy_ = False
  response = bstack1lll1111ll_opy_(self, driver_command, *args, **kwargs)
  if bstack11l11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ਗ") in str(bstack111l1l111_opy_).lower() and bstack1l1l1111l_opy_.on():
    try:
      if driver_command == bstack11l11ll_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬਘ"):
        bstack1l1l1111l_opy_.bstack111l1111l_opy_({
            bstack11l11ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨਙ"): response[bstack11l11ll_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩਚ")],
            bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫਛ"): bstack1l1l1111l_opy_.current_test_uuid() if bstack1l1l1111l_opy_.current_test_uuid() else bstack1l1l1111l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack1l1ll1l1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1ll1ll1l_opy_
  global bstack11ll1l1l1_opy_
  global bstack1l1ll111_opy_
  global bstack111ll1lll_opy_
  global bstack11lll1l1_opy_
  global bstack111l1l111_opy_
  global bstack111ll11l_opy_
  global bstack1l111111_opy_
  global bstack11l1lllll_opy_
  global bstack11lllllll_opy_
  CONFIG[bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧਜ")] = str(bstack111l1l111_opy_) + str(__version__)
  command_executor = bstack1lll1ll1l_opy_()
  logger.debug(bstack1llll11lll_opy_.format(command_executor))
  proxy = bstack1ll1ll1l1l_opy_(CONFIG, proxy)
  bstack1l11l1l11l_opy_ = 0 if bstack11ll1l1l1_opy_ < 0 else bstack11ll1l1l1_opy_
  try:
    if bstack111ll1lll_opy_ is True:
      bstack1l11l1l11l_opy_ = int(multiprocessing.current_process().name)
    elif bstack11lll1l1_opy_ is True:
      bstack1l11l1l11l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l11l1l11l_opy_ = 0
  bstack11lll1111_opy_ = bstack1l1llll11_opy_(CONFIG, bstack1l11l1l11l_opy_)
  logger.debug(bstack11lll1l11_opy_.format(str(bstack11lll1111_opy_)))
  if bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਝ") in CONFIG and bstack1lll1lll11_opy_(CONFIG[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫਞ")]):
    bstack1llll111ll_opy_(bstack11lll1111_opy_)
  if bstack1l1l111ll_opy_.bstack1ll1l1ll1l_opy_(CONFIG, bstack1l11l1l11l_opy_) and bstack1l1l111ll_opy_.bstack1ll11111_opy_(bstack11lll1111_opy_, options):
    threading.current_thread().a11yPlatform = True
    bstack1l1l111ll_opy_.set_capabilities(bstack11lll1111_opy_, CONFIG)
  if desired_capabilities:
    bstack1l111l11_opy_ = bstack11l1l11ll_opy_(desired_capabilities)
    bstack1l111l11_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨਟ")] = bstack11llllll_opy_(CONFIG)
    bstack1lll1ll1_opy_ = bstack1l1llll11_opy_(bstack1l111l11_opy_)
    if bstack1lll1ll1_opy_:
      bstack11lll1111_opy_ = update(bstack1lll1ll1_opy_, bstack11lll1111_opy_)
    desired_capabilities = None
  if options:
    bstack1llll11ll_opy_(options, bstack11lll1111_opy_)
  if not options:
    options = bstack1l11ll1l1_opy_(bstack11lll1111_opy_)
  bstack11lllllll_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਠ"))[bstack1l11l1l11l_opy_]
  if proxy and bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪਡ")):
    options.proxy(proxy)
  if options and bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪਢ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l1l1l11ll_opy_() < version.parse(bstack11l11ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫਣ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11lll1111_opy_)
  logger.info(bstack1ll1l1ll11_opy_)
  if bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ਤ")):
    bstack111ll11l_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ਥ")):
    bstack111ll11l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨਦ")):
    bstack111ll11l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack111ll11l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l1111ll_opy_ = bstack11l11ll_opy_ (u"ࠩࠪਧ")
    if bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫਨ")):
      bstack1l1111ll_opy_ = self.caps.get(bstack11l11ll_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ਩"))
    else:
      bstack1l1111ll_opy_ = self.capabilities.get(bstack11l11ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧਪ"))
    if bstack1l1111ll_opy_:
      bstack1l1l1llll_opy_(bstack1l1111ll_opy_)
      if bstack1l1l1l11ll_opy_() <= version.parse(bstack11l11ll_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ਫ")):
        self.command_executor._url = bstack11l11ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣਬ") + bstack1l11ll11_opy_ + bstack11l11ll_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧਭ")
      else:
        self.command_executor._url = bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦਮ") + bstack1l1111ll_opy_ + bstack11l11ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦਯ")
      logger.debug(bstack11l11lll_opy_.format(bstack1l1111ll_opy_))
    else:
      logger.debug(bstack1l1l11l111_opy_.format(bstack11l11ll_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧਰ")))
  except Exception as e:
    logger.debug(bstack1l1l11l111_opy_.format(e))
  if bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ਱") in bstack111l1l111_opy_:
    bstack1l1lll1ll1_opy_(bstack11ll1l1l1_opy_, bstack11l1lllll_opy_)
  bstack1ll1ll1l_opy_ = self.session_id
  if bstack11l11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ਲ") in bstack111l1l111_opy_ or bstack11l11ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧਲ਼") in bstack111l1l111_opy_ or bstack11l11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ਴") in bstack111l1l111_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1l1l1111l_opy_.bstack111111l11_opy_(self)
  bstack1l111111_opy_.append(self)
  if bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਵ") in CONFIG and bstack11l11ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਸ਼") in CONFIG[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ਷")][bstack1l11l1l11l_opy_]:
    bstack1l1ll111_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨਸ")][bstack1l11l1l11l_opy_][bstack11l11ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫਹ")]
  logger.debug(bstack11l11llll_opy_.format(bstack1ll1ll1l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1llll1l1l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11lll1l1l_opy_
      if(bstack11l11ll_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤ਺") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠨࢀࠪ਻")), bstack11l11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬਼ࠩ"), bstack11l11ll_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬ਽")), bstack11l11ll_opy_ (u"ࠫࡼ࠭ਾ")) as fp:
          fp.write(bstack11l11ll_opy_ (u"ࠧࠨਿ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l11ll_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣੀ")))):
          with open(args[1], bstack11l11ll_opy_ (u"ࠧࡳࠩੁ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l11ll_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧੂ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1ll1lll11_opy_)
            lines.insert(1, bstack1lllll1l1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l11ll_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ੃")), bstack11l11ll_opy_ (u"ࠪࡻࠬ੄")) as bstack11l11l1ll_opy_:
              bstack11l11l1ll_opy_.writelines(lines)
        CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭੅")] = str(bstack111l1l111_opy_) + str(__version__)
        bstack1l11l1l11l_opy_ = 0 if bstack11ll1l1l1_opy_ < 0 else bstack11ll1l1l1_opy_
        try:
          if bstack111ll1lll_opy_ is True:
            bstack1l11l1l11l_opy_ = int(multiprocessing.current_process().name)
          elif bstack11lll1l1_opy_ is True:
            bstack1l11l1l11l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l11l1l11l_opy_ = 0
        CONFIG[bstack11l11ll_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧ੆")] = False
        CONFIG[bstack11l11ll_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧੇ")] = True
        bstack11lll1111_opy_ = bstack1l1llll11_opy_(CONFIG, bstack1l11l1l11l_opy_)
        logger.debug(bstack11lll1l11_opy_.format(str(bstack11lll1111_opy_)))
        if CONFIG.get(bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫੈ")):
          bstack1llll111ll_opy_(bstack11lll1111_opy_)
        if bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੉") in CONFIG and bstack11l11ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ੊") in CONFIG[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ੋ")][bstack1l11l1l11l_opy_]:
          bstack1l1ll111_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧੌ")][bstack1l11l1l11l_opy_][bstack11l11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧ੍ࠪ")]
        args.append(os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"࠭ࡾࠨ੎")), bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ੏"), bstack11l11ll_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪ੐")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11lll1111_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l11ll_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦੑ"))
      bstack11lll1l1l_opy_ = True
      return bstack1l11ll111l_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11l1llll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack11ll1l1l1_opy_
    global bstack1l1ll111_opy_
    global bstack111ll1lll_opy_
    global bstack11lll1l1_opy_
    global bstack111l1l111_opy_
    CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ੒")] = str(bstack111l1l111_opy_) + str(__version__)
    bstack1l11l1l11l_opy_ = 0 if bstack11ll1l1l1_opy_ < 0 else bstack11ll1l1l1_opy_
    try:
      if bstack111ll1lll_opy_ is True:
        bstack1l11l1l11l_opy_ = int(multiprocessing.current_process().name)
      elif bstack11lll1l1_opy_ is True:
        bstack1l11l1l11l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l11l1l11l_opy_ = 0
    CONFIG[bstack11l11ll_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ੓")] = True
    bstack11lll1111_opy_ = bstack1l1llll11_opy_(CONFIG, bstack1l11l1l11l_opy_)
    logger.debug(bstack11lll1l11_opy_.format(str(bstack11lll1111_opy_)))
    if CONFIG.get(bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ੔")):
      bstack1llll111ll_opy_(bstack11lll1111_opy_)
    if bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੕") in CONFIG and bstack11l11ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ੖") in CONFIG[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੗")][bstack1l11l1l11l_opy_]:
      bstack1l1ll111_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ੘")][bstack1l11l1l11l_opy_][bstack11l11ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਖ਼")]
    import urllib
    import json
    bstack1lll1ll1l1_opy_ = bstack11l11ll_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ਗ਼") + urllib.parse.quote(json.dumps(bstack11lll1111_opy_))
    browser = self.connect(bstack1lll1ll1l1_opy_)
    return browser
except Exception as e:
    pass
def bstack111lll1l_opy_():
    if not bstack1ll11l1111_opy_:
      return
    global bstack11lll1l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack11l1llll_opy_
        bstack11lll1l1l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1llll1l1l1_opy_
      bstack11lll1l1l_opy_ = True
    except Exception as e:
      pass
def bstack1l1l1ll1_opy_(context, bstack11llll1l_opy_):
  try:
    context.page.evaluate(bstack11l11ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨਜ਼"), bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪੜ")+ json.dumps(bstack11llll1l_opy_) + bstack11l11ll_opy_ (u"ࠢࡾࡿࠥ੝"))
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨਫ਼"), e)
def bstack1llll11ll1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l11ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ੟"), bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ੠") + json.dumps(message) + bstack11l11ll_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ੡") + json.dumps(level) + bstack11l11ll_opy_ (u"ࠬࢃࡽࠨ੢"))
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤ੣"), e)
def bstack1ll11lllll_opy_(self, url):
  global bstack1lll1l1l_opy_
  try:
    bstack11lllll1l_opy_(url)
  except Exception as err:
    logger.debug(bstack1l1l1ll1ll_opy_.format(str(err)))
  try:
    bstack1lll1l1l_opy_(self, url)
  except Exception as e:
    try:
      bstack1l1lll1ll_opy_ = str(e)
      if any(err_msg in bstack1l1lll1ll_opy_ for err_msg in bstack1l11l1111_opy_):
        bstack11lllll1l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l1l1ll1ll_opy_.format(str(err)))
    raise e
def bstack1ll1ll11l1_opy_(self):
  global bstack1lll1l111l_opy_
  bstack1lll1l111l_opy_ = self
  return
def bstack1lll1l11l1_opy_(self):
  global bstack1llll1l1ll_opy_
  bstack1llll1l1ll_opy_ = self
  return
def bstack1l1llll1l_opy_(test_name, bstack1l1ll1111l_opy_):
  global CONFIG
  if CONFIG.get(bstack11l11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭੤"), False):
    bstack1l11l11lll_opy_ = os.path.relpath(bstack1l1ll1111l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l11l11lll_opy_)
    bstack1l11llll11_opy_ = suite_name + bstack11l11ll_opy_ (u"ࠣ࠯ࠥ੥") + test_name
    threading.current_thread().percySessionName = bstack1l11llll11_opy_
def bstack1ll1l1l1l_opy_(self, test, *args, **kwargs):
  global bstack1l1l1llll1_opy_
  test_name = None
  bstack1l1ll1111l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1ll1111l_opy_ = str(test.source)
  bstack1l1llll1l_opy_(test_name, bstack1l1ll1111l_opy_)
  bstack1l1l1llll1_opy_(self, test, *args, **kwargs)
def bstack1llll1llll_opy_(driver, bstack1l11llll11_opy_):
  if not bstack1llll1111l_opy_ and bstack1l11llll11_opy_:
      bstack1l11l11ll_opy_ = {
          bstack11l11ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ੦"): bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ੧"),
          bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ੨"): {
              bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ੩"): bstack1l11llll11_opy_
          }
      }
      bstack1ll1lll1_opy_ = bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ੪").format(json.dumps(bstack1l11l11ll_opy_))
      driver.execute_script(bstack1ll1lll1_opy_)
  if bstack11l11111_opy_:
      bstack1lll11llll_opy_ = {
          bstack11l11ll_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ੫"): bstack11l11ll_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ੬"),
          bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ੭"): {
              bstack11l11ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ੮"): bstack1l11llll11_opy_ + bstack11l11ll_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭੯"),
              bstack11l11ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫੰ"): bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫੱ")
          }
      }
      if bstack11l11111_opy_.status == bstack11l11ll_opy_ (u"ࠧࡑࡃࡖࡗࠬੲ"):
          bstack1l1lllll1_opy_ = bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ੳ").format(json.dumps(bstack1lll11llll_opy_))
          driver.execute_script(bstack1l1lllll1_opy_)
          bstack11ll1lll1_opy_(driver, bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩੴ"))
      elif bstack11l11111_opy_.status == bstack11l11ll_opy_ (u"ࠪࡊࡆࡏࡌࠨੵ"):
          reason = bstack11l11ll_opy_ (u"ࠦࠧ੶")
          bstack1llll1lll_opy_ = bstack1l11llll11_opy_ + bstack11l11ll_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭੷")
          if bstack11l11111_opy_.message:
              reason = str(bstack11l11111_opy_.message)
              bstack1llll1lll_opy_ = bstack1llll1lll_opy_ + bstack11l11ll_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭੸") + reason
          bstack1lll11llll_opy_[bstack11l11ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ੹")] = {
              bstack11l11ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ੺"): bstack11l11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ੻"),
              bstack11l11ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ੼"): bstack1llll1lll_opy_
          }
          bstack1l1lllll1_opy_ = bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ੽").format(json.dumps(bstack1lll11llll_opy_))
          driver.execute_script(bstack1l1lllll1_opy_)
          bstack11ll1lll1_opy_(driver, bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ੾"), reason)
          bstack1l1111lll_opy_(reason, str(bstack11l11111_opy_), str(bstack11ll1l1l1_opy_), logger)
def bstack11llll111_opy_(driver, test):
  if CONFIG.get(bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ੿"), False) and CONFIG.get(bstack11l11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪ઀"), bstack11l11ll_opy_ (u"ࠣࡣࡸࡸࡴࠨઁ")) == bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦં"):
      bstack1111l111l_opy_ = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ઃ"), None)
      bstack1ll111111l_opy_(driver, bstack1111l111l_opy_)
  if bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ઄"), None) and bstack11l11lll1_opy_(
          threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫઅ"), None):
      logger.info(bstack11l11ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠥࠨઆ"))
      bstack1l1l111ll_opy_.bstack111l1111_opy_(driver, class_name=test.parent.name, name=test.name, module_name=None,
                              path=test.source, bstack111l1ll1_opy_=bstack11lllllll_opy_)
def bstack1lll11ll1l_opy_(test, bstack1l11llll11_opy_):
    try:
      data = {}
      if test:
        data[bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬઇ")] = bstack1l11llll11_opy_
      if bstack11l11111_opy_:
        if bstack11l11111_opy_.status == bstack11l11ll_opy_ (u"ࠨࡒࡄࡗࡘ࠭ઈ"):
          data[bstack11l11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩઉ")] = bstack11l11ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪઊ")
        elif bstack11l11111_opy_.status == bstack11l11ll_opy_ (u"ࠫࡋࡇࡉࡍࠩઋ"):
          data[bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬઌ")] = bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ઍ")
          if bstack11l11111_opy_.message:
            data[bstack11l11ll_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ઎")] = str(bstack11l11111_opy_.message)
      user = CONFIG[bstack11l11ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪએ")]
      key = CONFIG[bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬઐ")]
      url = bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨઑ").format(user, key, bstack1ll1ll1l_opy_)
      headers = {
        bstack11l11ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ઒"): bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨઓ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll1111l_opy_.format(str(e)))
def bstack111ll1ll1_opy_(test, bstack1l11llll11_opy_):
  global CONFIG
  global bstack1llll1l1ll_opy_
  global bstack1lll1l111l_opy_
  global bstack1ll1ll1l_opy_
  global bstack11l11111_opy_
  global bstack1l1ll111_opy_
  global bstack1ll1l11lll_opy_
  global bstack11l1111l_opy_
  global bstack111ll1l11_opy_
  global bstack11lllll1_opy_
  global bstack1l111111_opy_
  global bstack11lllllll_opy_
  try:
    if not bstack1ll1ll1l_opy_:
      with open(os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"࠭ࡾࠨઔ")), bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧક"), bstack11l11ll_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪખ"))) as f:
        bstack11llll1ll_opy_ = json.loads(bstack11l11ll_opy_ (u"ࠤࡾࠦગ") + f.read().strip() + bstack11l11ll_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬઘ") + bstack11l11ll_opy_ (u"ࠦࢂࠨઙ"))
        bstack1ll1ll1l_opy_ = bstack11llll1ll_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l111111_opy_:
    for driver in bstack1l111111_opy_:
      if bstack1ll1ll1l_opy_ == driver.session_id:
        if test:
          bstack11llll111_opy_(driver, test)
        bstack1llll1llll_opy_(driver, bstack1l11llll11_opy_)
  elif bstack1ll1ll1l_opy_:
    bstack1lll11ll1l_opy_(test, bstack1l11llll11_opy_)
  if bstack1llll1l1ll_opy_:
    bstack11l1111l_opy_(bstack1llll1l1ll_opy_)
  if bstack1lll1l111l_opy_:
    bstack111ll1l11_opy_(bstack1lll1l111l_opy_)
  if bstack1l1l111l1_opy_:
    bstack11lllll1_opy_()
def bstack1l11llll_opy_(self, test, *args, **kwargs):
  bstack1l11llll11_opy_ = None
  if test:
    bstack1l11llll11_opy_ = str(test.name)
  bstack111ll1ll1_opy_(test, bstack1l11llll11_opy_)
  bstack1ll1l11lll_opy_(self, test, *args, **kwargs)
def bstack1l1l1l11l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1llll11l1l_opy_
  global CONFIG
  global bstack1l111111_opy_
  global bstack1ll1ll1l_opy_
  bstack1l11ll1l_opy_ = None
  try:
    if bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫચ"), None):
      try:
        if not bstack1ll1ll1l_opy_:
          with open(os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"࠭ࡾࠨછ")), bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧજ"), bstack11l11ll_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪઝ"))) as f:
            bstack11llll1ll_opy_ = json.loads(bstack11l11ll_opy_ (u"ࠤࡾࠦઞ") + f.read().strip() + bstack11l11ll_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬટ") + bstack11l11ll_opy_ (u"ࠦࢂࠨઠ"))
            bstack1ll1ll1l_opy_ = bstack11llll1ll_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1l111111_opy_:
        for driver in bstack1l111111_opy_:
          if bstack1ll1ll1l_opy_ == driver.session_id:
            bstack1l11ll1l_opy_ = driver
    bstack1ll111l1l1_opy_ = bstack1l1l111ll_opy_.bstack1l1111ll1_opy_(CONFIG, test.tags)
    if bstack1l11ll1l_opy_:
      threading.current_thread().isA11yTest = bstack1l1l111ll_opy_.bstack1llll1ll1l_opy_(bstack1l11ll1l_opy_, bstack1ll111l1l1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1ll111l1l1_opy_
  except:
    pass
  bstack1llll11l1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l11111_opy_
  bstack11l11111_opy_ = self._test
def bstack1ll11ll1ll_opy_():
  global bstack1ll1lll1l1_opy_
  try:
    if os.path.exists(bstack1ll1lll1l1_opy_):
      os.remove(bstack1ll1lll1l1_opy_)
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨડ") + str(e))
def bstack111ll111_opy_():
  global bstack1ll1lll1l1_opy_
  bstack11l111l1l_opy_ = {}
  try:
    if not os.path.isfile(bstack1ll1lll1l1_opy_):
      with open(bstack1ll1lll1l1_opy_, bstack11l11ll_opy_ (u"࠭ࡷࠨઢ")):
        pass
      with open(bstack1ll1lll1l1_opy_, bstack11l11ll_opy_ (u"ࠢࡸ࠭ࠥણ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1ll1lll1l1_opy_):
      bstack11l111l1l_opy_ = json.load(open(bstack1ll1lll1l1_opy_, bstack11l11ll_opy_ (u"ࠨࡴࡥࠫત")))
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫથ") + str(e))
  finally:
    return bstack11l111l1l_opy_
def bstack1l1lll1ll1_opy_(platform_index, item_index):
  global bstack1ll1lll1l1_opy_
  try:
    bstack11l111l1l_opy_ = bstack111ll111_opy_()
    bstack11l111l1l_opy_[item_index] = platform_index
    with open(bstack1ll1lll1l1_opy_, bstack11l11ll_opy_ (u"ࠥࡻ࠰ࠨદ")) as outfile:
      json.dump(bstack11l111l1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩધ") + str(e))
def bstack1l1ll11l1l_opy_(bstack1111l11l_opy_):
  global CONFIG
  bstack1l1ll11l_opy_ = bstack11l11ll_opy_ (u"ࠬ࠭ન")
  if not bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ઩") in CONFIG:
    logger.info(bstack11l11ll_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫપ"))
  try:
    platform = CONFIG[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫફ")][bstack1111l11l_opy_]
    if bstack11l11ll_opy_ (u"ࠩࡲࡷࠬબ") in platform:
      bstack1l1ll11l_opy_ += str(platform[bstack11l11ll_opy_ (u"ࠪࡳࡸ࠭ભ")]) + bstack11l11ll_opy_ (u"ࠫ࠱ࠦࠧમ")
    if bstack11l11ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨય") in platform:
      bstack1l1ll11l_opy_ += str(platform[bstack11l11ll_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩર")]) + bstack11l11ll_opy_ (u"ࠧ࠭ࠢࠪ઱")
    if bstack11l11ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬલ") in platform:
      bstack1l1ll11l_opy_ += str(platform[bstack11l11ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ળ")]) + bstack11l11ll_opy_ (u"ࠪ࠰ࠥ࠭઴")
    if bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭વ") in platform:
      bstack1l1ll11l_opy_ += str(platform[bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧશ")]) + bstack11l11ll_opy_ (u"࠭ࠬࠡࠩષ")
    if bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬસ") in platform:
      bstack1l1ll11l_opy_ += str(platform[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭હ")]) + bstack11l11ll_opy_ (u"ࠩ࠯ࠤࠬ઺")
    if bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ઻") in platform:
      bstack1l1ll11l_opy_ += str(platform[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲ઼ࠬ")]) + bstack11l11ll_opy_ (u"ࠬ࠲ࠠࠨઽ")
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭ા") + str(e))
  finally:
    if bstack1l1ll11l_opy_[len(bstack1l1ll11l_opy_) - 2:] == bstack11l11ll_opy_ (u"ࠧ࠭ࠢࠪિ"):
      bstack1l1ll11l_opy_ = bstack1l1ll11l_opy_[:-2]
    return bstack1l1ll11l_opy_
def bstack1l1l1ll111_opy_(path, bstack1l1ll11l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l11l11l1_opy_ = ET.parse(path)
    bstack1ll1l111l_opy_ = bstack1l11l11l1_opy_.getroot()
    bstack11ll11l1_opy_ = None
    for suite in bstack1ll1l111l_opy_.iter(bstack11l11ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧી")):
      if bstack11l11ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩુ") in suite.attrib:
        suite.attrib[bstack11l11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨૂ")] += bstack11l11ll_opy_ (u"ࠫࠥ࠭ૃ") + bstack1l1ll11l_opy_
        bstack11ll11l1_opy_ = suite
    bstack1lllll111l_opy_ = None
    for robot in bstack1ll1l111l_opy_.iter(bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫૄ")):
      bstack1lllll111l_opy_ = robot
    bstack1ll1l11ll1_opy_ = len(bstack1lllll111l_opy_.findall(bstack11l11ll_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬૅ")))
    if bstack1ll1l11ll1_opy_ == 1:
      bstack1lllll111l_opy_.remove(bstack1lllll111l_opy_.findall(bstack11l11ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭૆"))[0])
      bstack1l1ll1lll1_opy_ = ET.Element(bstack11l11ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧે"), attrib={bstack11l11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧૈ"): bstack11l11ll_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪૉ"), bstack11l11ll_opy_ (u"ࠫ࡮ࡪࠧ૊"): bstack11l11ll_opy_ (u"ࠬࡹ࠰ࠨો")})
      bstack1lllll111l_opy_.insert(1, bstack1l1ll1lll1_opy_)
      bstack1ll1lll111_opy_ = None
      for suite in bstack1lllll111l_opy_.iter(bstack11l11ll_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬૌ")):
        bstack1ll1lll111_opy_ = suite
      bstack1ll1lll111_opy_.append(bstack11ll11l1_opy_)
      bstack11lll11ll_opy_ = None
      for status in bstack11ll11l1_opy_.iter(bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹ્ࠧ")):
        bstack11lll11ll_opy_ = status
      bstack1ll1lll111_opy_.append(bstack11lll11ll_opy_)
    bstack1l11l11l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭૎") + str(e))
def bstack1111lllll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1llllll_opy_
  global CONFIG
  if bstack11l11ll_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ૏") in options:
    del options[bstack11l11ll_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢૐ")]
  bstack1l1l1111_opy_ = bstack111ll111_opy_()
  for bstack11l1l1lll_opy_ in bstack1l1l1111_opy_.keys():
    path = os.path.join(os.getcwd(), bstack11l11ll_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫ૑"), str(bstack11l1l1lll_opy_), bstack11l11ll_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩ૒"))
    bstack1l1l1ll111_opy_(path, bstack1l1ll11l1l_opy_(bstack1l1l1111_opy_[bstack11l1l1lll_opy_]))
  bstack1ll11ll1ll_opy_()
  return bstack1l1llllll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11lll1ll_opy_(self, ff_profile_dir):
  global bstack11ll1l1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack11ll1l1ll_opy_(self, ff_profile_dir)
def bstack1l11lll11l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1llll1l11_opy_
  bstack111l11111_opy_ = []
  if bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૓") in CONFIG:
    bstack111l11111_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૔")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l11ll_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ૕")],
      pabot_args[bstack11l11ll_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ૖")],
      argfile,
      pabot_args.get(bstack11l11ll_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ૗")),
      pabot_args[bstack11l11ll_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ૘")],
      platform[0],
      bstack1llll1l11_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l11ll_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ૙")] or [(bstack11l11ll_opy_ (u"ࠨࠢ૚"), None)]
    for platform in enumerate(bstack111l11111_opy_)
  ]
def bstack1l11lll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1111lll1_opy_=bstack11l11ll_opy_ (u"ࠧࠨ૛")):
  global bstack1llllll111_opy_
  self.platform_index = platform_index
  self.bstack1l11lllll_opy_ = bstack1111lll1_opy_
  bstack1llllll111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1l11l11l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack111llllll_opy_
  global bstack1l1l1l1l1l_opy_
  bstack1ll1ll1ll1_opy_ = copy.deepcopy(item)
  if not bstack11l11ll_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ૜") in item.options:
    bstack1ll1ll1ll1_opy_.options[bstack11l11ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૝")] = []
  bstack111l1l11_opy_ = bstack1ll1ll1ll1_opy_.options[bstack11l11ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ૞")].copy()
  for v in bstack1ll1ll1ll1_opy_.options[bstack11l11ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭૟")]:
    if bstack11l11ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫૠ") in v:
      bstack111l1l11_opy_.remove(v)
    if bstack11l11ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ૡ") in v:
      bstack111l1l11_opy_.remove(v)
    if bstack11l11ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫૢ") in v:
      bstack111l1l11_opy_.remove(v)
  bstack111l1l11_opy_.insert(0, bstack11l11ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪૣ").format(bstack1ll1ll1ll1_opy_.platform_index))
  bstack111l1l11_opy_.insert(0, bstack11l11ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩ૤").format(bstack1ll1ll1ll1_opy_.bstack1l11lllll_opy_))
  bstack1ll1ll1ll1_opy_.options[bstack11l11ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ૥")] = bstack111l1l11_opy_
  if bstack1l1l1l1l1l_opy_:
    bstack1ll1ll1ll1_opy_.options[bstack11l11ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭૦")].insert(0, bstack11l11ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ૧").format(bstack1l1l1l1l1l_opy_))
  return bstack111llllll_opy_(caller_id, datasources, is_last, bstack1ll1ll1ll1_opy_, outs_dir)
def bstack1l1l11lll1_opy_(command, item_index):
  if bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ૨")):
    os.environ[bstack11l11ll_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ૩")] = json.dumps(CONFIG[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")][item_index % bstack1111ll11_opy_])
  global bstack1l1l1l1l1l_opy_
  if bstack1l1l1l1l1l_opy_:
    command[0] = command[0].replace(bstack11l11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ૫"), bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧ૬") + str(
      item_index) + bstack11l11ll_opy_ (u"ࠫࠥ࠭૭") + bstack1l1l1l1l1l_opy_, 1)
  else:
    command[0] = command[0].replace(bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ૮"),
                                    bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪ૯") + str(item_index), 1)
def bstack1l1l111l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1lll11ll_opy_
  bstack1l1l11lll1_opy_(command, item_index)
  return bstack1lll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11l1111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1lll11ll_opy_
  bstack1l1l11lll1_opy_(command, item_index)
  return bstack1lll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l11llllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1lll11ll_opy_
  bstack1l1l11lll1_opy_(command, item_index)
  return bstack1lll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1l11ll1l11_opy_(self, runner, quiet=False, capture=True):
  global bstack1l11l11l_opy_
  bstack1l1ll11ll_opy_ = bstack1l11l11l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l11ll_opy_ (u"ࠧࡦࡺࡦࡩࡵࡺࡩࡰࡰࡢࡥࡷࡸࠧ૰")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l11ll_opy_ (u"ࠨࡧࡻࡧࡤࡺࡲࡢࡥࡨࡦࡦࡩ࡫ࡠࡣࡵࡶࠬ૱")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1ll11ll_opy_
def bstack1l1l1lll1l_opy_(self, name, context, *args):
  os.environ[bstack11l11ll_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ૲")] = json.dumps(CONFIG[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૳")][int(threading.current_thread()._name) % bstack1111ll11_opy_])
  global bstack1llllll1l_opy_
  if name == bstack11l11ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠬ૴"):
    bstack1llllll1l_opy_(self, name, context, *args)
    try:
      if not bstack1llll1111l_opy_:
        bstack1l11ll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11l1l1_opy_(bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ૵")) else context.browser
        bstack11llll1l_opy_ = str(self.feature.name)
        bstack1l1l1ll1_opy_(context, bstack11llll1l_opy_)
        bstack1l11ll1l_opy_.execute_script(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ૶") + json.dumps(bstack11llll1l_opy_) + bstack11l11ll_opy_ (u"ࠧࡾࡿࠪ૷"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack11l11ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ૸").format(str(e)))
  elif name == bstack11l11ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫૹ"):
    bstack1llllll1l_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack11l11ll_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬૺ")):
        self.driver_before_scenario = True
      if (not bstack1llll1111l_opy_):
        scenario_name = args[0].name
        feature_name = bstack11llll1l_opy_ = str(self.feature.name)
        bstack11llll1l_opy_ = feature_name + bstack11l11ll_opy_ (u"ࠫࠥ࠳ࠠࠨૻ") + scenario_name
        bstack1l11ll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11l1l1_opy_(bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫૼ")) else context.browser
        if self.driver_before_scenario:
          bstack1l1l1ll1_opy_(context, bstack11llll1l_opy_)
          bstack1l11ll1l_opy_.execute_script(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ૽") + json.dumps(bstack11llll1l_opy_) + bstack11l11ll_opy_ (u"ࠧࡾࡿࠪ૾"))
    except Exception as e:
      logger.debug(bstack11l11ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩ૿").format(str(e)))
  elif name == bstack11l11ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ଀"):
    try:
      bstack1ll1l1ll_opy_ = args[0].status.name
      bstack1l11ll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩଁ") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1ll1l1ll_opy_).lower() == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫଂ"):
        bstack1lllll11_opy_ = bstack11l11ll_opy_ (u"ࠬ࠭ଃ")
        bstack1ll1llllll_opy_ = bstack11l11ll_opy_ (u"࠭ࠧ଄")
        bstack1ll1l1l11l_opy_ = bstack11l11ll_opy_ (u"ࠧࠨଅ")
        try:
          import traceback
          bstack1lllll11_opy_ = self.exception.__class__.__name__
          bstack11ll1ll1_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1ll1llllll_opy_ = bstack11l11ll_opy_ (u"ࠨࠢࠪଆ").join(bstack11ll1ll1_opy_)
          bstack1ll1l1l11l_opy_ = bstack11ll1ll1_opy_[-1]
        except Exception as e:
          logger.debug(bstack111ll11ll_opy_.format(str(e)))
        bstack1lllll11_opy_ += bstack1ll1l1l11l_opy_
        bstack1llll11ll1_opy_(context, json.dumps(str(args[0].name) + bstack11l11ll_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣଇ") + str(bstack1ll1llllll_opy_)),
                            bstack11l11ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤଈ"))
        if self.driver_before_scenario:
          bstack1l1l1l111l_opy_(getattr(context, bstack11l11ll_opy_ (u"ࠫࡵࡧࡧࡦࠩଉ"), None), bstack11l11ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧଊ"), bstack1lllll11_opy_)
          bstack1l11ll1l_opy_.execute_script(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫଋ") + json.dumps(str(args[0].name) + bstack11l11ll_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨଌ") + str(bstack1ll1llllll_opy_)) + bstack11l11ll_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨ଍"))
        if self.driver_before_scenario:
          bstack11ll1lll1_opy_(bstack1l11ll1l_opy_, bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ଎"), bstack11l11ll_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢଏ") + str(bstack1lllll11_opy_))
      else:
        bstack1llll11ll1_opy_(context, bstack11l11ll_opy_ (u"ࠦࡕࡧࡳࡴࡧࡧࠥࠧଐ"), bstack11l11ll_opy_ (u"ࠧ࡯࡮ࡧࡱࠥ଑"))
        if self.driver_before_scenario:
          bstack1l1l1l111l_opy_(getattr(context, bstack11l11ll_opy_ (u"࠭ࡰࡢࡩࡨࠫ଒"), None), bstack11l11ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢଓ"))
        bstack1l11ll1l_opy_.execute_script(bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ଔ") + json.dumps(str(args[0].name) + bstack11l11ll_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨକ")) + bstack11l11ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩଖ"))
        if self.driver_before_scenario:
          bstack11ll1lll1_opy_(bstack1l11ll1l_opy_, bstack11l11ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦଗ"))
    except Exception as e:
      logger.debug(bstack11l11ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧଘ").format(str(e)))
  elif name == bstack11l11ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ଙ"):
    try:
      bstack1l11ll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11l1l1_opy_(bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ଚ")) else context.browser
      if context.failed is True:
        bstack11ll1l11l_opy_ = []
        bstack111l11lll_opy_ = []
        bstack1l11lllll1_opy_ = []
        bstack111111l1l_opy_ = bstack11l11ll_opy_ (u"ࠨࠩଛ")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack11ll1l11l_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack11ll1ll1_opy_ = traceback.format_tb(exc_tb)
            bstack1ll11l11_opy_ = bstack11l11ll_opy_ (u"ࠩࠣࠫଜ").join(bstack11ll1ll1_opy_)
            bstack111l11lll_opy_.append(bstack1ll11l11_opy_)
            bstack1l11lllll1_opy_.append(bstack11ll1ll1_opy_[-1])
        except Exception as e:
          logger.debug(bstack111ll11ll_opy_.format(str(e)))
        bstack1lllll11_opy_ = bstack11l11ll_opy_ (u"ࠪࠫଝ")
        for i in range(len(bstack11ll1l11l_opy_)):
          bstack1lllll11_opy_ += bstack11ll1l11l_opy_[i] + bstack1l11lllll1_opy_[i] + bstack11l11ll_opy_ (u"ࠫࡡࡴࠧଞ")
        bstack111111l1l_opy_ = bstack11l11ll_opy_ (u"ࠬࠦࠧଟ").join(bstack111l11lll_opy_)
        if not self.driver_before_scenario:
          bstack1llll11ll1_opy_(context, bstack111111l1l_opy_, bstack11l11ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧଠ"))
          bstack1l1l1l111l_opy_(getattr(context, bstack11l11ll_opy_ (u"ࠧࡱࡣࡪࡩࠬଡ"), None), bstack11l11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣଢ"), bstack1lllll11_opy_)
          bstack1l11ll1l_opy_.execute_script(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧଣ") + json.dumps(bstack111111l1l_opy_) + bstack11l11ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪତ"))
          bstack11ll1lll1_opy_(bstack1l11ll1l_opy_, bstack11l11ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦଥ"), bstack11l11ll_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥଦ") + str(bstack1lllll11_opy_))
          bstack1l11lll1l_opy_ = bstack1l1llll1l1_opy_(bstack111111l1l_opy_, self.feature.name, logger)
          if (bstack1l11lll1l_opy_ != None):
            bstack11ll1l11_opy_.append(bstack1l11lll1l_opy_)
      else:
        if not self.driver_before_scenario:
          bstack1llll11ll1_opy_(context, bstack11l11ll_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤଧ") + str(self.feature.name) + bstack11l11ll_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤନ"), bstack11l11ll_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ଩"))
          bstack1l1l1l111l_opy_(getattr(context, bstack11l11ll_opy_ (u"ࠩࡳࡥ࡬࡫ࠧପ"), None), bstack11l11ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥଫ"))
          bstack1l11ll1l_opy_.execute_script(bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩବ") + json.dumps(bstack11l11ll_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣଭ") + str(self.feature.name) + bstack11l11ll_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣମ")) + bstack11l11ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ଯ"))
          bstack11ll1lll1_opy_(bstack1l11ll1l_opy_, bstack11l11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨର"))
          bstack1l11lll1l_opy_ = bstack1l1llll1l1_opy_(bstack111111l1l_opy_, self.feature.name, logger)
          if (bstack1l11lll1l_opy_ != None):
            bstack11ll1l11_opy_.append(bstack1l11lll1l_opy_)
    except Exception as e:
      logger.debug(bstack11l11ll_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ଱").format(str(e)))
  else:
    bstack1llllll1l_opy_(self, name, context, *args)
  if name in [bstack11l11ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪଲ"), bstack11l11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬଳ")]:
    bstack1llllll1l_opy_(self, name, context, *args)
    if (name == bstack11l11ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭଴") and self.driver_before_scenario) or (
            name == bstack11l11ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ଵ") and not self.driver_before_scenario):
      try:
        bstack1l11ll1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11l1l1_opy_(bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ଶ")) else context.browser
        bstack1l11ll1l_opy_.quit()
      except Exception:
        pass
def bstack1l1l11ll1l_opy_(config, startdir):
  return bstack11l11ll_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨଷ").format(bstack11l11ll_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣସ"))
notset = Notset()
def bstack11l1l111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11l11111l_opy_
  if str(name).lower() == bstack11l11ll_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪହ"):
    return bstack11l11ll_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ଺")
  else:
    return bstack11l11111l_opy_(self, name, default, skip)
def bstack1l1l11lll_opy_(item, when):
  global bstack1l11l1l111_opy_
  try:
    bstack1l11l1l111_opy_(item, when)
  except Exception as e:
    pass
def bstack1llll1ll_opy_():
  return
def bstack1ll111ll1_opy_(type, name, status, reason, bstack1lll111111_opy_, bstack1ll11lll1_opy_):
  bstack1l11l11ll_opy_ = {
    bstack11l11ll_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ଻"): type,
    bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴ଼ࠩ"): {}
  }
  if type == bstack11l11ll_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩଽ"):
    bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫା")][bstack11l11ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨି")] = bstack1lll111111_opy_
    bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ୀ")][bstack11l11ll_opy_ (u"ࠫࡩࡧࡴࡢࠩୁ")] = json.dumps(str(bstack1ll11lll1_opy_))
  if type == bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ୂ"):
    bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩୃ")][bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬୄ")] = name
  if type == bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ୅"):
    bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ୆")][bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪେ")] = status
    if status == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫୈ"):
      bstack1l11l11ll_opy_[bstack11l11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ୉")][bstack11l11ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭୊")] = json.dumps(str(reason))
  bstack1ll1lll1_opy_ = bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬୋ").format(json.dumps(bstack1l11l11ll_opy_))
  return bstack1ll1lll1_opy_
def bstack1l1l1l1ll_opy_(driver_command, response):
    if driver_command == bstack11l11ll_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬୌ"):
        bstack1l1l1111l_opy_.bstack111l1111l_opy_({
            bstack11l11ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ୍"): response[bstack11l11ll_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ୎")],
            bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ୏"): bstack1l1l1111l_opy_.current_test_uuid()
        })
def bstack1l11ll1lll_opy_(item, call, rep):
  global bstack1ll1l1l11_opy_
  global bstack1l111111_opy_
  global bstack1llll1111l_opy_
  name = bstack11l11ll_opy_ (u"ࠬ࠭୐")
  try:
    if rep.when == bstack11l11ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ୑"):
      bstack1ll1ll1l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1llll1111l_opy_:
          name = str(rep.nodeid)
          bstack1l1lll11l_opy_ = bstack1ll111ll1_opy_(bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ୒"), name, bstack11l11ll_opy_ (u"ࠨࠩ୓"), bstack11l11ll_opy_ (u"ࠩࠪ୔"), bstack11l11ll_opy_ (u"ࠪࠫ୕"), bstack11l11ll_opy_ (u"ࠫࠬୖ"))
          threading.current_thread().bstack1lllllll1l_opy_ = name
          for driver in bstack1l111111_opy_:
            if bstack1ll1ll1l_opy_ == driver.session_id:
              driver.execute_script(bstack1l1lll11l_opy_)
      except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬୗ").format(str(e)))
      try:
        bstack1l1l1lll11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ୘"):
          status = bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ୙") if rep.outcome.lower() == bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ୚") else bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ୛")
          reason = bstack11l11ll_opy_ (u"ࠪࠫଡ଼")
          if status == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫଢ଼"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ୞") if status == bstack11l11ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ୟ") else bstack11l11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ୠ")
          data = name + bstack11l11ll_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪୡ") if status == bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩୢ") else name + bstack11l11ll_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭ୣ") + reason
          bstack111lll11_opy_ = bstack1ll111ll1_opy_(bstack11l11ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭୤"), bstack11l11ll_opy_ (u"ࠬ࠭୥"), bstack11l11ll_opy_ (u"࠭ࠧ୦"), bstack11l11ll_opy_ (u"ࠧࠨ୧"), level, data)
          for driver in bstack1l111111_opy_:
            if bstack1ll1ll1l_opy_ == driver.session_id:
              driver.execute_script(bstack111lll11_opy_)
      except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ୨").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭୩").format(str(e)))
  bstack1ll1l1l11_opy_(item, call, rep)
def bstack1ll111111l_opy_(driver, bstack1l1lll11_opy_):
  PercySDK.screenshot(driver, bstack1l1lll11_opy_)
def bstack1l11l111l1_opy_(driver):
  if bstack1lll11l1_opy_.bstack1lll1lll1_opy_() is True or bstack1lll11l1_opy_.capturing() is True:
    return
  bstack1lll11l1_opy_.bstack1l1l111l_opy_()
  while not bstack1lll11l1_opy_.bstack1lll1lll1_opy_():
    bstack11l1ll11l_opy_ = bstack1lll11l1_opy_.bstack11ll11l11_opy_()
    bstack1ll111111l_opy_(driver, bstack11l1ll11l_opy_)
  bstack1lll11l1_opy_.bstack1ll1111l1l_opy_()
def bstack1ll1ll111l_opy_(sequence, driver_command, response = None, bstack1ll1l11111_opy_ = None, args = None):
    try:
      if sequence != bstack11l11ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ୪"):
        return
      if not CONFIG.get(bstack11l11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ୫"), False):
        return
      bstack11l1ll11l_opy_ = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ୬"), None)
      for command in bstack1l1ll111ll_opy_:
        if command == driver_command:
          for driver in bstack1l111111_opy_:
            bstack1l11l111l1_opy_(driver)
      bstack1ll111l1ll_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩ୭"), bstack11l11ll_opy_ (u"ࠢࡢࡷࡷࡳࠧ୮"))
      if driver_command in bstack1ll1lll1ll_opy_[bstack1ll111l1ll_opy_]:
        bstack1lll11l1_opy_.bstack1llll1l11l_opy_(bstack11l1ll11l_opy_, driver_command)
    except Exception as e:
      pass
def bstack1l1l1lll1_opy_(framework_name):
  global bstack111l1l111_opy_
  global bstack11lll1l1l_opy_
  global bstack11ll1111_opy_
  bstack111l1l111_opy_ = framework_name
  logger.info(bstack1l1l11ll_opy_.format(bstack111l1l111_opy_.split(bstack11l11ll_opy_ (u"ࠨ࠯ࠪ୯"))[0]))
  bstack111111ll1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll11l1111_opy_:
      Service.start = bstack11l111ll1_opy_
      Service.stop = bstack1111lll1l_opy_
      webdriver.Remote.get = bstack1ll11lllll_opy_
      WebDriver.close = bstack1l1lllll11_opy_
      WebDriver.quit = bstack111lll11l_opy_
      webdriver.Remote.__init__ = bstack1l1ll1l1l1_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1ll11l1111_opy_ and bstack1l1l1111l_opy_.on():
      webdriver.Remote.__init__ = bstack1l1l1ll11_opy_
    WebDriver.execute = bstack1lll1ll11_opy_
    bstack11lll1l1l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll11l1111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1lllll1l_opy_
  except Exception as e:
    pass
  bstack111lll1l_opy_()
  if not bstack11lll1l1l_opy_:
    bstack1ll11l11l1_opy_(bstack11l11ll_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ୰"), bstack11ll11111_opy_)
  if bstack1l1l1l11l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1l1lll1l_opy_
    except Exception as e:
      logger.error(bstack1l1l11ll11_opy_.format(str(e)))
  if bstack11ll11l1l_opy_():
    bstack1ll1ll1lll_opy_(CONFIG, logger)
  if (bstack11l11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩୱ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if CONFIG.get(bstack11l11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ୲"), False):
          bstack1l1l1111l1_opy_(bstack1ll1ll111l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11lll1ll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1lll1l11l1_opy_
      except Exception as e:
        logger.warn(bstack1ll1l11l11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import bstack1l1l11llll_opy_
        bstack1l1l11llll_opy_.close = bstack1ll1ll11l1_opy_
      except Exception as e:
        logger.debug(bstack1ll1ll1111_opy_ + str(e))
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1ll1l11l11_opy_)
    Output.start_test = bstack1ll1l1l1l_opy_
    Output.end_test = bstack1l11llll_opy_
    TestStatus.__init__ = bstack1l1l1l11l_opy_
    QueueItem.__init__ = bstack1l11lll1_opy_
    pabot._create_items = bstack1l11lll11l_opy_
    try:
      from pabot import __version__ as bstack1l11ll1ll_opy_
      if version.parse(bstack1l11ll1ll_opy_) >= version.parse(bstack11l11ll_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬ୳")):
        pabot._run = bstack1l11llllll_opy_
      elif version.parse(bstack1l11ll1ll_opy_) >= version.parse(bstack11l11ll_opy_ (u"࠭࠲࠯࠳࠶࠲࠵࠭୴")):
        pabot._run = bstack11l1111ll_opy_
      else:
        pabot._run = bstack1l1l111l1l_opy_
    except Exception as e:
      pabot._run = bstack1l1l111l1l_opy_
    pabot._create_command_for_execution = bstack1l1l11l11l_opy_
    pabot._report_results = bstack1111lllll_opy_
  if bstack11l11ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ୵") in str(framework_name).lower():
    if not bstack1ll11l1111_opy_:
      return
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1lll11ll11_opy_)
    Runner.run_hook = bstack1l1l1lll1l_opy_
    Step.run = bstack1l11ll1l11_opy_
  if bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ୶") in str(framework_name).lower():
    if not bstack1ll11l1111_opy_:
      return
    try:
      if CONFIG.get(bstack11l11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ୷"), False):
          bstack1l1l1111l1_opy_(bstack1ll1ll111l_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l1l11ll1l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1llll1ll_opy_
      Config.getoption = bstack11l1l111l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l11ll1lll_opy_
    except Exception as e:
      pass
def bstack1111l1lll_opy_():
  global CONFIG
  if bstack11l11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ୸") in CONFIG and int(CONFIG[bstack11l11ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ୹")]) > 1:
    logger.warn(bstack11l1l11l_opy_)
def bstack1lllll1lll_opy_(arg, bstack1l11lll11_opy_, bstack1ll1ll11l_opy_=None):
  global CONFIG
  global bstack1l11ll11_opy_
  global bstack1111ll11l_opy_
  global bstack1ll11l1111_opy_
  global bstack1ll1111l1_opy_
  bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ୺")
  if bstack1l11lll11_opy_ and isinstance(bstack1l11lll11_opy_, str):
    bstack1l11lll11_opy_ = eval(bstack1l11lll11_opy_)
  CONFIG = bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭୻")]
  bstack1l11ll11_opy_ = bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ୼")]
  bstack1111ll11l_opy_ = bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ୽")]
  bstack1ll11l1111_opy_ = bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ୾")]
  bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ୿"), bstack1ll11l1111_opy_)
  os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭஀")] = bstack1l1lll111_opy_
  os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫ஁")] = json.dumps(CONFIG)
  os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭ஂ")] = bstack1l11ll11_opy_
  os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨஃ")] = str(bstack1111ll11l_opy_)
  os.environ[bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧ஄")] = str(True)
  if bstack1l11l1ll11_opy_(arg, [bstack11l11ll_opy_ (u"ࠩ࠰ࡲࠬஅ"), bstack11l11ll_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫஆ")]) != -1:
    os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬஇ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll11l1l1_opy_)
    return
  bstack1ll1l1l111_opy_()
  global bstack11l1ll1l_opy_
  global bstack11ll1l1l1_opy_
  global bstack1llll1l11_opy_
  global bstack1l1l1l1l1l_opy_
  global bstack1lll11l1ll_opy_
  global bstack11ll1111_opy_
  global bstack111ll1lll_opy_
  arg.append(bstack11l11ll_opy_ (u"ࠧ࠳ࡗࠣஈ"))
  arg.append(bstack11l11ll_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡍࡰࡦࡸࡰࡪࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪ࡯ࡳࡳࡷࡺࡥࡥ࠼ࡳࡽࡹ࡫ࡳࡵ࠰ࡓࡽࡹ࡫ࡳࡵ࡙ࡤࡶࡳ࡯࡮ࡨࠤஉ"))
  arg.append(bstack11l11ll_opy_ (u"ࠢ࠮࡙ࠥஊ"))
  arg.append(bstack11l11ll_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡖ࡫ࡩࠥ࡮࡯ࡰ࡭࡬ࡱࡵࡲࠢ஋"))
  global bstack111ll11l_opy_
  global bstack11l111ll_opy_
  global bstack1lll1111ll_opy_
  global bstack1llll11l1l_opy_
  global bstack11ll1l1ll_opy_
  global bstack1llllll111_opy_
  global bstack111llllll_opy_
  global bstack1l1ll1lll_opy_
  global bstack1lll1l1l_opy_
  global bstack1lll111l1l_opy_
  global bstack11l11111l_opy_
  global bstack1l11l1l111_opy_
  global bstack1ll1l1l11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111ll11l_opy_ = webdriver.Remote.__init__
    bstack11l111ll_opy_ = WebDriver.quit
    bstack1l1ll1lll_opy_ = WebDriver.close
    bstack1lll1l1l_opy_ = WebDriver.get
    bstack1lll1111ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11111lll1_opy_(CONFIG) and bstack1ll11ll1l1_opy_():
    if bstack1l1l1l11ll_opy_() < version.parse(bstack1lll1l1111_opy_):
      logger.error(bstack1llll11111_opy_.format(bstack1l1l1l11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lll111l1l_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l1l11ll11_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11l11111l_opy_ = Config.getoption
    from _pytest import runner
    bstack1l11l1l111_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack111l1lll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll1l1l11_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ஌"))
  bstack1llll1l11_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ஍"), {}).get(bstack11l11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭எ"))
  bstack111ll1lll_opy_ = True
  bstack1l1l1lll1_opy_(bstack1ll1l1l1l1_opy_)
  os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ஏ")] = CONFIG[bstack11l11ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨஐ")]
  os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ஑")] = CONFIG[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫஒ")]
  os.environ[bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬஓ")] = bstack1ll11l1111_opy_.__str__()
  from _pytest.config import main as bstack111ll1l1l_opy_
  bstack11l111lll_opy_ = []
  try:
    bstack1l1lllll_opy_ = bstack111ll1l1l_opy_(arg)
    if bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧஔ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l111l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l111lll_opy_.append(bstack111l111l_opy_)
    try:
      bstack1ll111l111_opy_ = (bstack11l111lll_opy_, int(bstack1l1lllll_opy_))
      bstack1ll1ll11l_opy_.append(bstack1ll111l111_opy_)
    except:
      bstack1ll1ll11l_opy_.append((bstack11l111lll_opy_, bstack1l1lllll_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11l111lll_opy_.append({bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩக"): bstack11l11ll_opy_ (u"ࠬࡖࡲࡰࡥࡨࡷࡸࠦࠧ஖") + os.environ.get(bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭஗")), bstack11l11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭஘"): traceback.format_exc(), bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧங"): int(os.environ.get(bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩச")))})
    bstack1ll1ll11l_opy_.append((bstack11l111lll_opy_, 1))
def bstack1llll111_opy_(arg):
  global bstack1l1l11l1ll_opy_
  bstack1l1l1lll1_opy_(bstack1ll1ll1l1_opy_)
  os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ஛")] = str(bstack1111ll11l_opy_)
  from behave.__main__ import main as bstack1l111llll_opy_
  status_code = bstack1l111llll_opy_(arg)
  if status_code != 0:
    bstack1l1l11l1ll_opy_ = status_code
def bstack1ll111ll_opy_():
  logger.info(bstack1l11ll1111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪஜ"), help=bstack11l11ll_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡣࡰࡰࡩ࡭࡬࠭஝"))
  parser.add_argument(bstack11l11ll_opy_ (u"࠭࠭ࡶࠩஞ"), bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫட"), help=bstack11l11ll_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ஠"))
  parser.add_argument(bstack11l11ll_opy_ (u"ࠩ࠰࡯ࠬ஡"), bstack11l11ll_opy_ (u"ࠪ࠱࠲ࡱࡥࡺࠩ஢"), help=bstack11l11ll_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠬண"))
  parser.add_argument(bstack11l11ll_opy_ (u"ࠬ࠳ࡦࠨத"), bstack11l11ll_opy_ (u"࠭࠭࠮ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ஥"), help=bstack11l11ll_opy_ (u"࡚ࠧࡱࡸࡶࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭஦"))
  bstack1l1ll11l11_opy_ = parser.parse_args()
  try:
    bstack1ll11ll11_opy_ = bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡨࡧࡱࡩࡷ࡯ࡣ࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬ஧")
    if bstack1l1ll11l11_opy_.framework and bstack1l1ll11l11_opy_.framework not in (bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩந"), bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫன")):
      bstack1ll11ll11_opy_ = bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪப")
    bstack1ll1ll11_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll11ll11_opy_)
    bstack1l1llll111_opy_ = open(bstack1ll1ll11_opy_, bstack11l11ll_opy_ (u"ࠬࡸࠧ஫"))
    bstack1ll11111l_opy_ = bstack1l1llll111_opy_.read()
    bstack1l1llll111_opy_.close()
    if bstack1l1ll11l11_opy_.username:
      bstack1ll11111l_opy_ = bstack1ll11111l_opy_.replace(bstack11l11ll_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭஬"), bstack1l1ll11l11_opy_.username)
    if bstack1l1ll11l11_opy_.key:
      bstack1ll11111l_opy_ = bstack1ll11111l_opy_.replace(bstack11l11ll_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ஭"), bstack1l1ll11l11_opy_.key)
    if bstack1l1ll11l11_opy_.framework:
      bstack1ll11111l_opy_ = bstack1ll11111l_opy_.replace(bstack11l11ll_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩம"), bstack1l1ll11l11_opy_.framework)
    file_name = bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬய")
    file_path = os.path.abspath(file_name)
    bstack1llll1l111_opy_ = open(file_path, bstack11l11ll_opy_ (u"ࠪࡻࠬர"))
    bstack1llll1l111_opy_.write(bstack1ll11111l_opy_)
    bstack1llll1l111_opy_.close()
    logger.info(bstack1llllll1l1_opy_)
    try:
      os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ற")] = bstack1l1ll11l11_opy_.framework if bstack1l1ll11l11_opy_.framework != None else bstack11l11ll_opy_ (u"ࠧࠨல")
      config = yaml.safe_load(bstack1ll11111l_opy_)
      config[bstack11l11ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ள")] = bstack11l11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠭ࡴࡧࡷࡹࡵ࠭ழ")
      bstack1lll11l11_opy_(bstack111ll111l_opy_, config)
    except Exception as e:
      logger.debug(bstack1l1l1lll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll11l111_opy_.format(str(e)))
def bstack1lll11l11_opy_(bstack1ll1l1ll1_opy_, config, bstack11111l11l_opy_={}):
  global bstack1ll11l1111_opy_
  global bstack11111l1l_opy_
  global bstack1ll1111l1_opy_
  if not config:
    return
  bstack111l1ll1l_opy_ = bstack111lllll1_opy_ if not bstack1ll11l1111_opy_ else (
    bstack1ll1l11ll_opy_ if bstack11l11ll_opy_ (u"ࠨࡣࡳࡴࠬவ") in config else bstack1l1l111ll1_opy_)
  bstack1lll11111_opy_ = False
  bstack1l1l1l111_opy_ = False
  if bstack1ll11l1111_opy_ is True:
      if bstack11l11ll_opy_ (u"ࠩࡤࡴࡵ࠭ஶ") in config:
          bstack1lll11111_opy_ = True
      else:
          bstack1l1l1l111_opy_ = True
  bstack1l1llll11l_opy_ = {
      bstack11l11ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪஷ"): bstack1l1l1111l_opy_.bstack1lll1l1ll_opy_(bstack11111l1l_opy_),
      bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫஸ"): bstack1l1l111ll_opy_.bstack11llllll1_opy_(config),
      bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫஹ"): config.get(bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ஺"), False),
      bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ஻"): bstack1l1l1l111_opy_,
      bstack11l11ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ஼"): bstack1lll11111_opy_
  }
  data = {
    bstack11l11ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ஽"): config[bstack11l11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬா")],
    bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧி"): config[bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨீ")],
    bstack11l11ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪு"): bstack1ll1l1ll1_opy_,
    bstack11l11ll_opy_ (u"ࠧࡥࡧࡷࡩࡨࡺࡥࡥࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫூ"): os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ௃"), bstack11111l1l_opy_),
    bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ௄"): bstack1ll1111ll_opy_,
    bstack11l11ll_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰࠬ௅"): bstack1ll11lll11_opy_(),
    bstack11l11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧெ"): {
      bstack11l11ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪே"): str(config[bstack11l11ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ை")]) if bstack11l11ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ௉") in config else bstack11l11ll_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤொ"),
      bstack11l11ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨ࡚ࡪࡸࡳࡪࡱࡱࠫோ"): sys.version,
      bstack11l11ll_opy_ (u"ࠪࡶࡪ࡬ࡥࡳࡴࡨࡶࠬௌ"): bstack11l111l1_opy_(os.getenv(bstack11l11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨ்"), bstack11l11ll_opy_ (u"ࠧࠨ௎"))),
      bstack11l11ll_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ௏"): bstack11l11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧௐ"),
      bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩ௑"): bstack111l1ll1l_opy_,
      bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧ௒"): bstack1l1llll11l_opy_,
      bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡣࡺࡻࡩࡥࠩ௓"): os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ௔")],
      bstack11l11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ௕"): bstack1111llll_opy_(os.environ.get(bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ௖"), bstack11111l1l_opy_)),
      bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪௗ"): config[bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௘")] if config[bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௙")] else bstack11l11ll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ௚"),
      bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௛"): str(config[bstack11l11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௜")]) if bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௝") in config else bstack11l11ll_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ௞"),
      bstack11l11ll_opy_ (u"ࠨࡱࡶࠫ௟"): sys.platform,
      bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ௠"): socket.gethostname(),
      bstack11l11ll_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ௡"): bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭௢"))
    }
  }
  if not bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௣")) is None:
    data[bstack11l11ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ௤")][bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡏࡨࡸࡦࡪࡡࡵࡣࠪ௥")] = {
      bstack11l11ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ௦"): bstack11l11ll_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧ௧"),
      bstack11l11ll_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪ௨"): bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௩")),
      bstack11l11ll_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࡓࡻ࡭ࡣࡧࡵࠫ௪"): bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡎࡰࠩ௫"))
    }
  update(data[bstack11l11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ௬")], bstack11111l11l_opy_)
  try:
    response = bstack11llll11l_opy_(bstack11l11ll_opy_ (u"ࠨࡒࡒࡗ࡙࠭௭"), bstack111l11ll_opy_(bstack1l11ll11l_opy_), data, {
      bstack11l11ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧ௮"): (config[bstack11l11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ௯")], config[bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ௰")])
    })
    if response:
      logger.debug(bstack1l1l1l1ll1_opy_.format(bstack1ll1l1ll1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1ll11l11l_opy_.format(str(e)))
def bstack11l111l1_opy_(framework):
  return bstack11l11ll_opy_ (u"ࠧࢁࡽ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤ௱").format(str(framework), __version__) if framework else bstack11l11ll_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ௲").format(
    __version__)
def bstack1ll1l1l111_opy_():
  global CONFIG
  global bstack111l11l1_opy_
  if bool(CONFIG):
    return
  try:
    bstack111ll1ll_opy_()
    logger.debug(bstack111111111_opy_.format(str(CONFIG)))
    bstack111l11l1_opy_ = bstack1lll11l11l_opy_.bstack1l11l111_opy_(CONFIG, bstack111l11l1_opy_)
    bstack111111ll1_opy_()
  except Exception as e:
    logger.error(bstack11l11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠦ௳") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll11lll1l_opy_
  atexit.register(bstack11l11ll11_opy_)
  signal.signal(signal.SIGINT, bstack1l11111l_opy_)
  signal.signal(signal.SIGTERM, bstack1l11111l_opy_)
def bstack1ll11lll1l_opy_(exctype, value, traceback):
  global bstack1l111111_opy_
  try:
    for driver in bstack1l111111_opy_:
      bstack11ll1lll1_opy_(driver, bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ௴"), bstack11l11ll_opy_ (u"ࠤࡖࡩࡸࡹࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ௵") + str(value))
  except Exception:
    pass
  bstack1111l1111_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1111l1111_opy_(message=bstack11l11ll_opy_ (u"ࠪࠫ௶"), bstack1llll1lll1_opy_ = False):
  global CONFIG
  bstack1l1l1l1l11_opy_ = bstack11l11ll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡉࡽࡩࡥࡱࡶ࡬ࡳࡳ࠭௷") if bstack1llll1lll1_opy_ else bstack11l11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ௸")
  try:
    if message:
      bstack11111l11l_opy_ = {
        bstack1l1l1l1l11_opy_ : str(message)
      }
      bstack1lll11l11_opy_(bstack11l1l1l1l_opy_, CONFIG, bstack11111l11l_opy_)
    else:
      bstack1lll11l11_opy_(bstack11l1l1l1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll1llll_opy_.format(str(e)))
def bstack11lll111_opy_(bstack1l11ll1ll1_opy_, size):
  bstack1ll11lll_opy_ = []
  while len(bstack1l11ll1ll1_opy_) > size:
    bstack1llll1111_opy_ = bstack1l11ll1ll1_opy_[:size]
    bstack1ll11lll_opy_.append(bstack1llll1111_opy_)
    bstack1l11ll1ll1_opy_ = bstack1l11ll1ll1_opy_[size:]
  bstack1ll11lll_opy_.append(bstack1l11ll1ll1_opy_)
  return bstack1ll11lll_opy_
def bstack1l1111l1_opy_(args):
  if bstack11l11ll_opy_ (u"࠭࠭࡮ࠩ௹") in args and bstack11l11ll_opy_ (u"ࠧࡱࡦࡥࠫ௺") in args:
    return True
  return False
def run_on_browserstack(bstack1l11l1llll_opy_=None, bstack1ll1ll11l_opy_=None, bstack111lllll_opy_=False):
  global CONFIG
  global bstack1l11ll11_opy_
  global bstack1111ll11l_opy_
  global bstack11111l1l_opy_
  global bstack1ll1111l1_opy_
  bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠨࠩ௻")
  bstack1lllll1111_opy_(bstack1l111ll1l_opy_, logger)
  if bstack1l11l1llll_opy_ and isinstance(bstack1l11l1llll_opy_, str):
    bstack1l11l1llll_opy_ = eval(bstack1l11l1llll_opy_)
  if bstack1l11l1llll_opy_:
    CONFIG = bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ௼")]
    bstack1l11ll11_opy_ = bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ௽")]
    bstack1111ll11l_opy_ = bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭௾")]
    bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ௿"), bstack1111ll11l_opy_)
    bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ఀ")
  bstack1ll1111l1_opy_.bstack1l1llllll1_opy_(bstack11l11ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩఁ"), uuid4().__str__())
  logger.debug(bstack11l11ll_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࡀࠫం") + bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫః")))
  if not bstack111lllll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1ll11l1l1_opy_)
      return
    if sys.argv[1] == bstack11l11ll_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ఄ") or sys.argv[1] == bstack11l11ll_opy_ (u"ࠫ࠲ࡼࠧఅ"):
      logger.info(bstack11l11ll_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁࠬఆ").format(__version__))
      return
    if sys.argv[1] == bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬఇ"):
      bstack1ll111ll_opy_()
      return
  args = sys.argv
  bstack1ll1l1l111_opy_()
  global bstack11l1ll1l_opy_
  global bstack1111ll11_opy_
  global bstack111ll1lll_opy_
  global bstack11lll1l1_opy_
  global bstack11ll1l1l1_opy_
  global bstack1llll1l11_opy_
  global bstack1l1l1l1l1l_opy_
  global bstack11l1ll11_opy_
  global bstack1lll11l1ll_opy_
  global bstack11ll1111_opy_
  global bstack11ll111ll_opy_
  bstack1111ll11_opy_ = len(CONFIG.get(bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪఈ"), []))
  if not bstack1l1lll111_opy_:
    if args[1] == bstack11l11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨఉ") or args[1] == bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪఊ"):
      bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪఋ")
      args = args[2:]
    elif args[1] == bstack11l11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪఌ"):
      bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ఍")
      args = args[2:]
    elif args[1] == bstack11l11ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬఎ"):
      bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ఏ")
      args = args[2:]
    elif args[1] == bstack11l11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩఐ"):
      bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ఑")
      args = args[2:]
    elif args[1] == bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪఒ"):
      bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫఓ")
      args = args[2:]
    elif args[1] == bstack11l11ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬఔ"):
      bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭క")
      args = args[2:]
    else:
      if not bstack11l11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪఖ") in CONFIG or str(CONFIG[bstack11l11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫగ")]).lower() in [bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩఘ"), bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫఙ")]:
        bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫచ")
        args = args[1:]
      elif str(CONFIG[bstack11l11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨఛ")]).lower() == bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬజ"):
        bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఝ")
        args = args[1:]
      elif str(CONFIG[bstack11l11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫఞ")]).lower() == bstack11l11ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨట"):
        bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩఠ")
        args = args[1:]
      elif str(CONFIG[bstack11l11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧడ")]).lower() == bstack11l11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬఢ"):
        bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ణ")
        args = args[1:]
      elif str(CONFIG[bstack11l11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪత")]).lower() == bstack11l11ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨథ"):
        bstack1l1lll111_opy_ = bstack11l11ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩద")
        args = args[1:]
      else:
        os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬధ")] = bstack1l1lll111_opy_
        bstack1ll111111_opy_(bstack1llllllll_opy_)
  os.environ[bstack11l11ll_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬన")] = bstack1l1lll111_opy_
  bstack11111l1l_opy_ = bstack1l1lll111_opy_
  global bstack1l11ll111l_opy_
  if bstack1l11l1llll_opy_:
    try:
      os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ఩")] = bstack1l1lll111_opy_
      bstack1lll11l11_opy_(bstack111lll1l1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1ll11l1lll_opy_.format(str(e)))
  global bstack111ll11l_opy_
  global bstack11l111ll_opy_
  global bstack1l1l1llll1_opy_
  global bstack1ll1l11lll_opy_
  global bstack111ll1l11_opy_
  global bstack11l1111l_opy_
  global bstack1llll11l1l_opy_
  global bstack11ll1l1ll_opy_
  global bstack1lll11ll_opy_
  global bstack1llllll111_opy_
  global bstack111llllll_opy_
  global bstack1l1ll1lll_opy_
  global bstack1llllll1l_opy_
  global bstack1l11l11l_opy_
  global bstack1lll1l1l_opy_
  global bstack1lll111l1l_opy_
  global bstack11l11111l_opy_
  global bstack1l11l1l111_opy_
  global bstack1l1llllll_opy_
  global bstack1ll1l1l11_opy_
  global bstack1lll1111ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111ll11l_opy_ = webdriver.Remote.__init__
    bstack11l111ll_opy_ = WebDriver.quit
    bstack1l1ll1lll_opy_ = WebDriver.close
    bstack1lll1l1l_opy_ = WebDriver.get
    bstack1lll1111ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l11ll111l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    global bstack11lllll1_opy_
    from QWeb.keywords import browser
    bstack11lllll1_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11111lll1_opy_(CONFIG) and bstack1ll11ll1l1_opy_():
    if bstack1l1l1l11ll_opy_() < version.parse(bstack1lll1l1111_opy_):
      logger.error(bstack1llll11111_opy_.format(bstack1l1l1l11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lll111l1l_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l1l11ll11_opy_.format(str(e)))
  if not CONFIG.get(bstack11l11ll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨప"), False) and not bstack1l11l1llll_opy_:
    logger.info(bstack1ll1lllll1_opy_)
  if bstack1l1lll111_opy_ != bstack11l11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧఫ") or (bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨబ") and not bstack1l11l1llll_opy_):
    bstack1l111l1ll_opy_()
  if (bstack1l1lll111_opy_ in [bstack11l11ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨభ"), bstack11l11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩమ"), bstack11l11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬయ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11lll1ll_opy_
        bstack11l1111l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll1l11l11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import bstack1l1l11llll_opy_
        bstack111ll1l11_opy_ = bstack1l1l11llll_opy_.close
      except Exception as e:
        logger.debug(bstack1ll1ll1111_opy_ + str(e))
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1ll1l11l11_opy_)
    if bstack1l1lll111_opy_ != bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ర"):
      bstack1ll11ll1ll_opy_()
    bstack1l1l1llll1_opy_ = Output.start_test
    bstack1ll1l11lll_opy_ = Output.end_test
    bstack1llll11l1l_opy_ = TestStatus.__init__
    bstack1lll11ll_opy_ = pabot._run
    bstack1llllll111_opy_ = QueueItem.__init__
    bstack111llllll_opy_ = pabot._create_command_for_execution
    bstack1l1llllll_opy_ = pabot._report_results
  if bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ఱ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1lll11ll11_opy_)
    bstack1llllll1l_opy_ = Runner.run_hook
    bstack1l11l11l_opy_ = Step.run
  if bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧల"):
    try:
      from _pytest.config import Config
      bstack11l11111l_opy_ = Config.getoption
      from _pytest import runner
      bstack1l11l1l111_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack111l1lll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll1l1l11_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l11ll_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩళ"))
  try:
    framework_name = bstack11l11ll_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨఴ") if bstack1l1lll111_opy_ in [bstack11l11ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩవ"), bstack11l11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪశ"), bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ష")] else bstack1lll1ll111_opy_(bstack1l1lll111_opy_)
    bstack1l1l1111l_opy_.launch(CONFIG, {
      bstack11l11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧస"): bstack11l11ll_opy_ (u"ࠧࡼ࠲ࢀ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭హ").format(framework_name) if bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ఺") and bstack1111l11l1_opy_() else framework_name,
      bstack11l11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭఻"): bstack1111llll_opy_(framework_name),
      bstack11l11ll_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ఼"): __version__,
      bstack11l11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬఽ"): bstack1l1lll111_opy_
    })
  except Exception as e:
    logger.debug(bstack1l11lll111_opy_.format(bstack11l11ll_opy_ (u"ࠬࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬా"), str(e)))
  if bstack1l1lll111_opy_ in bstack1l1lll1111_opy_:
    try:
      framework_name = bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬి") if bstack1l1lll111_opy_ in [bstack11l11ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ీ"), bstack11l11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧు")] else bstack1l1lll111_opy_
      if bstack1ll11l1111_opy_ and bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩూ") in CONFIG and CONFIG[bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪృ")] == True:
        if bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫౄ") in CONFIG:
          os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭౅")] = os.getenv(bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧె"), json.dumps(CONFIG[bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧే")]))
          CONFIG[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨై")].pop(bstack11l11ll_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ౉"), None)
          CONFIG[bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪొ")].pop(bstack11l11ll_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩో"), None)
        bstack1111l1l1l_opy_, bstack11ll11lll_opy_ = bstack1l1l111ll_opy_.bstack11l1111l1_opy_(CONFIG, bstack1l1lll111_opy_, bstack1111llll_opy_(framework_name), str(bstack1l1l1l11ll_opy_()))
        if not bstack1111l1l1l_opy_ is None:
          os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪౌ")] = bstack1111l1l1l_opy_
          os.environ[bstack11l11ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡕࡇࡖࡘࡤࡘࡕࡏࡡࡌࡈ్ࠬ")] = str(bstack11ll11lll_opy_)
    except Exception as e:
      logger.debug(bstack1l11lll111_opy_.format(bstack11l11ll_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౎"), str(e)))
  if bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ౏"):
    bstack111ll1lll_opy_ = True
    if bstack1l11l1llll_opy_ and bstack111lllll_opy_:
      bstack1llll1l11_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭౐"), {}).get(bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ౑"))
      bstack1l1l1lll1_opy_(bstack1lll11111l_opy_)
    elif bstack1l11l1llll_opy_:
      bstack1llll1l11_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ౒"), {}).get(bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ౓"))
      global bstack1l111111_opy_
      try:
        if bstack1l1111l1_opy_(bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౔")]) and multiprocessing.current_process().name == bstack11l11ll_opy_ (u"ࠧ࠱ౕࠩ"):
          bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨౖࠫ")].remove(bstack11l11ll_opy_ (u"ࠩ࠰ࡱࠬ౗"))
          bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ౘ")].remove(bstack11l11ll_opy_ (u"ࠫࡵࡪࡢࠨౙ"))
          bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨౚ")] = bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౛")][0]
          with open(bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౜")], bstack11l11ll_opy_ (u"ࠨࡴࠪౝ")) as f:
            bstack1lllllll1_opy_ = f.read()
          bstack1l1ll1l11l_opy_ = bstack11l11ll_opy_ (u"ࠤࠥࠦ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡧ࡯ࠥ࡯࡭ࡱࡱࡵࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥ࠼ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩ࠭ࢁࡽࠪ࠽ࠣࡪࡷࡵ࡭ࠡࡲࡧࡦࠥ࡯࡭ࡱࡱࡵࡸࠥࡖࡤࡣ࠽ࠣࡳ࡬ࡥࡤࡣࠢࡀࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭࠾ࠎࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࡺࡲࡺ࠼ࠍࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࡪࡾࡣࡦࡲࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡢࡵࠣࡩ࠿ࠐࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࡳ࡬ࡥࡤࡣࠪࡶࡩࡱ࡬ࠬࡢࡴࡪ࠰ࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠩࠋࡒࡧࡦ࠳ࡪ࡯ࡠࡤࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࡖࡤࡣࠪࠬ࠲ࡸ࡫ࡴࡠࡶࡵࡥࡨ࡫ࠨࠪ࡞ࡱࠦࠧࠨ౞").format(str(bstack1l11l1llll_opy_))
          bstack1llll11l1_opy_ = bstack1l1ll1l11l_opy_ + bstack1lllllll1_opy_
          bstack1ll11111l1_opy_ = bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭౟")] + bstack11l11ll_opy_ (u"ࠫࡤࡨࡳࡵࡣࡦ࡯ࡤࡺࡥ࡮ࡲ࠱ࡴࡾ࠭ౠ")
          with open(bstack1ll11111l1_opy_, bstack11l11ll_opy_ (u"ࠬࡽࠧౡ")):
            pass
          with open(bstack1ll11111l1_opy_, bstack11l11ll_opy_ (u"ࠨࡷࠬࠤౢ")) as f:
            f.write(bstack1llll11l1_opy_)
          import subprocess
          bstack1lllll11l_opy_ = subprocess.run([bstack11l11ll_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢౣ"), bstack1ll11111l1_opy_])
          if os.path.exists(bstack1ll11111l1_opy_):
            os.unlink(bstack1ll11111l1_opy_)
          os._exit(bstack1lllll11l_opy_.returncode)
        else:
          if bstack1l1111l1_opy_(bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ౤")]):
            bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౥")].remove(bstack11l11ll_opy_ (u"ࠪ࠱ࡲ࠭౦"))
            bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౧")].remove(bstack11l11ll_opy_ (u"ࠬࡶࡤࡣࠩ౨"))
            bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౩")] = bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౪")][0]
          bstack1l1l1lll1_opy_(bstack1lll11111l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ౫")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l11ll_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫ౬")] = bstack11l11ll_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬ౭")
          mod_globals[bstack11l11ll_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭౮")] = os.path.abspath(bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ౯")])
          exec(open(bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౰")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l11ll_opy_ (u"ࠧࡄࡣࡸ࡫࡭ࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠧ౱").format(str(e)))
          for driver in bstack1l111111_opy_:
            bstack1ll1ll11l_opy_.append({
              bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭౲"): bstack1l11l1llll_opy_[bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౳")],
              bstack11l11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ౴"): str(e),
              bstack11l11ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ౵"): multiprocessing.current_process().name
            })
            bstack11ll1lll1_opy_(driver, bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ౶"), bstack11l11ll_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ౷") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l111111_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1111ll11l_opy_, CONFIG, logger)
      bstack1ll1l1l1ll_opy_()
      bstack1111l1lll_opy_()
      bstack1l11lll11_opy_ = {
        bstack11l11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౸"): args[0],
        bstack11l11ll_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ౹"): CONFIG,
        bstack11l11ll_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ౺"): bstack1l11ll11_opy_,
        bstack11l11ll_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ౻"): bstack1111ll11l_opy_
      }
      percy.bstack1lllll1l11_opy_()
      if bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ౼") in CONFIG:
        bstack1l1l1111ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111111ll_opy_ = manager.list()
        if bstack1l1111l1_opy_(args):
          for index, platform in enumerate(CONFIG[bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౽")]):
            if index == 0:
              bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౾")] = args
            bstack1l1l1111ll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1l11lll11_opy_, bstack1111111ll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ౿")]):
            bstack1l1l1111ll_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1l11lll11_opy_, bstack1111111ll_opy_)))
        for t in bstack1l1l1111ll_opy_:
          t.start()
        for t in bstack1l1l1111ll_opy_:
          t.join()
        bstack11l1ll11_opy_ = list(bstack1111111ll_opy_)
      else:
        if bstack1l1111l1_opy_(args):
          bstack1l11lll11_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫಀ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1l11lll11_opy_,))
          test.start()
          test.join()
        else:
          bstack1l1l1lll1_opy_(bstack1lll11111l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l11ll_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫಁ")] = bstack11l11ll_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬಂ")
          mod_globals[bstack11l11ll_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭ಃ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ಄") or bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಅ"):
    percy.init(bstack1111ll11l_opy_, CONFIG, logger)
    percy.bstack1lllll1l11_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1ll1l11l11_opy_)
    bstack1ll1l1l1ll_opy_()
    bstack1l1l1lll1_opy_(bstack1l11l1lll1_opy_)
    if bstack1ll11l1111_opy_:
      bstack1l11ll11ll_opy_(bstack1l11l1lll1_opy_, args)
      if bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬಆ") in args:
        i = args.index(bstack11l11ll_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ಇ"))
        args.pop(i)
        args.pop(i)
      if bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಈ") not in CONFIG:
        CONFIG[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ")] = [{}]
        bstack1111ll11_opy_ = 1
      if bstack11l1ll1l_opy_ == 0:
        bstack11l1ll1l_opy_ = 1
      args.insert(0, str(bstack11l1ll1l_opy_))
      args.insert(0, str(bstack11l11ll_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩಊ")))
    if bstack1l1l1111l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l11l1ll1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11ll1llll_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l11ll_opy_ (u"ࠧࡘࡏࡃࡑࡗࡣࡔࡖࡔࡊࡑࡑࡗࠧಋ"),
        ).parse_args(bstack1l11l1ll1_opy_)
        bstack1lll111ll1_opy_ = args.index(bstack1l11l1ll1_opy_[0]) if len(bstack1l11l1ll1_opy_) > 0 else len(args)
        args.insert(bstack1lll111ll1_opy_, str(bstack11l11ll_opy_ (u"࠭࠭࠮࡮࡬ࡷࡹ࡫࡮ࡦࡴࠪಌ")))
        args.insert(bstack1lll111ll1_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡳࡱࡥࡳࡹࡥ࡬ࡪࡵࡷࡩࡳ࡫ࡲ࠯ࡲࡼࠫ಍"))))
        if bstack1lll1lll11_opy_(os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭ಎ"))) and str(os.environ.get(bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ಏ"), bstack11l11ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨಐ"))) != bstack11l11ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ಑"):
          for bstack1l1ll1ll1_opy_ in bstack11ll1llll_opy_:
            args.remove(bstack1l1ll1ll1_opy_)
          bstack11l11ll1_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩಒ")).split(bstack11l11ll_opy_ (u"࠭ࠬࠨಓ"))
          for bstack1l11llll1_opy_ in bstack11l11ll1_opy_:
            args.append(bstack1l11llll1_opy_)
      except Exception as e:
        logger.error(bstack11l11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡧࡴࡵࡣࡦ࡬࡮ࡴࡧࠡ࡮࡬ࡷࡹ࡫࡮ࡦࡴࠣࡪࡴࡸࠠࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࠥಔ").format(e))
    pabot.main(args)
  elif bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩಕ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1ll1l11l11_opy_)
    for a in args:
      if bstack11l11ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨಖ") in a:
        bstack11ll1l1l1_opy_ = int(a.split(bstack11l11ll_opy_ (u"ࠪ࠾ࠬಗ"))[1])
      if bstack11l11ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨಘ") in a:
        bstack1llll1l11_opy_ = str(a.split(bstack11l11ll_opy_ (u"ࠬࡀࠧಙ"))[1])
      if bstack11l11ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ಚ") in a:
        bstack1l1l1l1l1l_opy_ = str(a.split(bstack11l11ll_opy_ (u"ࠧ࠻ࠩಛ"))[1])
    bstack1lll111l11_opy_ = None
    if bstack11l11ll_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧಜ") in args:
      i = args.index(bstack11l11ll_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨಝ"))
      args.pop(i)
      bstack1lll111l11_opy_ = args.pop(i)
    if bstack1lll111l11_opy_ is not None:
      global bstack11l1lllll_opy_
      bstack11l1lllll_opy_ = bstack1lll111l11_opy_
    bstack1l1l1lll1_opy_(bstack1l11l1lll1_opy_)
    run_cli(args)
    if bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧಞ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l111l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll1ll11l_opy_.append(bstack111l111l_opy_)
  elif bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫಟ"):
    percy.init(bstack1111ll11l_opy_, CONFIG, logger)
    percy.bstack1lllll1l11_opy_()
    bstack11111l1ll_opy_ = bstack1llllllll1_opy_(args, logger, CONFIG, bstack1ll11l1111_opy_)
    bstack11111l1ll_opy_.bstack1llll1l1l_opy_()
    bstack1ll1l1l1ll_opy_()
    bstack11lll1l1_opy_ = True
    bstack11ll1111_opy_ = bstack11111l1ll_opy_.bstack1l1l1l1111_opy_()
    bstack11111l1ll_opy_.bstack1l11lll11_opy_(bstack1llll1111l_opy_)
    bstack11ll1l111_opy_ = bstack11111l1ll_opy_.bstack111llll1_opy_(bstack1lllll1lll_opy_, {
      bstack11l11ll_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭ಠ"): bstack1l11ll11_opy_,
      bstack11l11ll_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨಡ"): bstack1111ll11l_opy_,
      bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪಢ"): bstack1ll11l1111_opy_
    })
    try:
      bstack11l111lll_opy_, bstack1ll1ll11ll_opy_ = map(list, zip(*bstack11ll1l111_opy_))
      bstack1lll11l1ll_opy_ = bstack11l111lll_opy_[0]
      for status_code in bstack1ll1ll11ll_opy_:
        if status_code != 0:
          bstack11ll111ll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡨࡶࡷࡵࡲࡴࠢࡤࡲࡩࠦࡳࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠲ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠼ࠣࡿࢂࠨಣ").format(str(e)))
  elif bstack1l1lll111_opy_ == bstack11l11ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩತ"):
    try:
      from behave.__main__ import main as bstack1l111llll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll11l11l1_opy_(e, bstack1lll11ll11_opy_)
    bstack1ll1l1l1ll_opy_()
    bstack11lll1l1_opy_ = True
    bstack1l1ll1llll_opy_ = 1
    if bstack11l11ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪಥ") in CONFIG:
      bstack1l1ll1llll_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫದ")]
    if bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಧ") in CONFIG:
      bstack111l1llll_opy_ = int(bstack1l1ll1llll_opy_) * int(len(CONFIG[bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩನ")]))
    else:
      bstack111l1llll_opy_ = int(bstack1l1ll1llll_opy_)
    config = Configuration(args)
    bstack1l11ll11l1_opy_ = config.paths
    if len(bstack1l11ll11l1_opy_) == 0:
      import glob
      pattern = bstack11l11ll_opy_ (u"ࠧࠫࠬ࠲࠮࠳࡬ࡥࡢࡶࡸࡶࡪ࠭಩")
      bstack1l1l1ll11l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l1l1ll11l_opy_)
      config = Configuration(args)
      bstack1l11ll11l1_opy_ = config.paths
    bstack1lllll11l1_opy_ = [os.path.normpath(item) for item in bstack1l11ll11l1_opy_]
    bstack1l1111l11_opy_ = [os.path.normpath(item) for item in args]
    bstack1llll1ll11_opy_ = [item for item in bstack1l1111l11_opy_ if item not in bstack1lllll11l1_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l11ll_opy_ (u"ࠨࡹ࡬ࡲࡩࡵࡷࡴࠩಪ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lllll11l1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack111l1ll11_opy_)))
                    for bstack111l1ll11_opy_ in bstack1lllll11l1_opy_]
    bstack1lll111ll_opy_ = []
    for spec in bstack1lllll11l1_opy_:
      bstack1l1ll111l1_opy_ = []
      bstack1l1ll111l1_opy_ += bstack1llll1ll11_opy_
      bstack1l1ll111l1_opy_.append(spec)
      bstack1lll111ll_opy_.append(bstack1l1ll111l1_opy_)
    execution_items = []
    for bstack1l1ll111l1_opy_ in bstack1lll111ll_opy_:
      if bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಫ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ")]):
          item = {}
          item[bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࠨಭ")] = bstack11l11ll_opy_ (u"ࠬࠦࠧಮ").join(bstack1l1ll111l1_opy_)
          item[bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬಯ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l11ll_opy_ (u"ࠧࡢࡴࡪࠫರ")] = bstack11l11ll_opy_ (u"ࠨࠢࠪಱ").join(bstack1l1ll111l1_opy_)
        item[bstack11l11ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨಲ")] = 0
        execution_items.append(item)
    bstack1lll11l111_opy_ = bstack11lll111_opy_(execution_items, bstack111l1llll_opy_)
    for execution_item in bstack1lll11l111_opy_:
      bstack1l1l1111ll_opy_ = []
      for item in execution_item:
        bstack1l1l1111ll_opy_.append(bstack111lll111_opy_(name=str(item[bstack11l11ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩಳ")]),
                                             target=bstack1llll111_opy_,
                                             args=(item[bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࠨ಴")],)))
      for t in bstack1l1l1111ll_opy_:
        t.start()
      for t in bstack1l1l1111ll_opy_:
        t.join()
  else:
    bstack1ll111111_opy_(bstack1llllllll_opy_)
  if not bstack1l11l1llll_opy_:
    bstack1l1l1ll1l1_opy_()
  bstack1lll11l11l_opy_.bstack1ll11l1ll1_opy_()
def browserstack_initialize(bstack1111lll11_opy_=None):
  run_on_browserstack(bstack1111lll11_opy_, None, True)
def bstack1l1l1ll1l1_opy_():
  global CONFIG
  global bstack11111l1l_opy_
  global bstack11ll111ll_opy_
  global bstack1l1l11l1ll_opy_
  global bstack1ll1111l1_opy_
  bstack1l1l1111l_opy_.stop(bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬವ")))
  bstack1l1l1111l_opy_.bstack11111111_opy_()
  if bstack1l1l111ll_opy_.bstack11llllll1_opy_(CONFIG):
    bstack1l1l111ll_opy_.bstack1l1ll11111_opy_()
  [bstack11l11ll1l_opy_, bstack1lllll11ll_opy_] = get_build_link()
  if bstack11l11ll1l_opy_ is not None and bstack1l1lll111l_opy_() != -1:
    sessions = bstack1l1l11111_opy_(bstack11l11ll1l_opy_)
    bstack1l1l1l1l1_opy_(sessions, bstack1lllll11ll_opy_)
  if bstack11111l1l_opy_ == bstack11l11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಶ") and bstack11ll111ll_opy_ != 0:
    sys.exit(bstack11ll111ll_opy_)
  if bstack11111l1l_opy_ == bstack11l11ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧಷ") and bstack1l1l11l1ll_opy_ != 0:
    sys.exit(bstack1l1l11l1ll_opy_)
def bstack1lll1ll111_opy_(bstack1ll1l1111l_opy_):
  if bstack1ll1l1111l_opy_:
    return bstack1ll1l1111l_opy_.capitalize()
  else:
    return bstack11l11ll_opy_ (u"ࠨࠩಸ")
def bstack111l1l1l_opy_(bstack111ll1l1_opy_):
  if bstack11l11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧಹ") in bstack111ll1l1_opy_ and bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ಺")] != bstack11l11ll_opy_ (u"ࠫࠬ಻"):
    return bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧ಼ࠪ")]
  else:
    bstack1l11llll11_opy_ = bstack11l11ll_opy_ (u"ࠨࠢಽ")
    if bstack11l11ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧಾ") in bstack111ll1l1_opy_ and bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨಿ")] != None:
      bstack1l11llll11_opy_ += bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩೀ")] + bstack11l11ll_opy_ (u"ࠥ࠰ࠥࠨು")
      if bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠫࡴࡹࠧೂ")] == bstack11l11ll_opy_ (u"ࠧ࡯࡯ࡴࠤೃ"):
        bstack1l11llll11_opy_ += bstack11l11ll_opy_ (u"ࠨࡩࡐࡕࠣࠦೄ")
      bstack1l11llll11_opy_ += (bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫ೅")] or bstack11l11ll_opy_ (u"ࠨࠩೆ"))
      return bstack1l11llll11_opy_
    else:
      bstack1l11llll11_opy_ += bstack1lll1ll111_opy_(bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪೇ")]) + bstack11l11ll_opy_ (u"ࠥࠤࠧೈ") + (
              bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭೉")] or bstack11l11ll_opy_ (u"ࠬ࠭ೊ")) + bstack11l11ll_opy_ (u"ࠨࠬࠡࠤೋ")
      if bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠧࡰࡵࠪೌ")] == bstack11l11ll_opy_ (u"࡙ࠣ࡬ࡲࡩࡵࡷࡴࠤ್"):
        bstack1l11llll11_opy_ += bstack11l11ll_opy_ (u"ࠤ࡚࡭ࡳࠦࠢ೎")
      bstack1l11llll11_opy_ += bstack111ll1l1_opy_[bstack11l11ll_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ೏")] or bstack11l11ll_opy_ (u"ࠫࠬ೐")
      return bstack1l11llll11_opy_
def bstack11l1ll1l1_opy_(bstack1ll11l1l11_opy_):
  if bstack1ll11l1l11_opy_ == bstack11l11ll_opy_ (u"ࠧࡪ࡯࡯ࡧࠥ೑"):
    return bstack11l11ll_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡅࡲࡱࡵࡲࡥࡵࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ೒")
  elif bstack1ll11l1l11_opy_ == bstack11l11ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ೓"):
    return bstack11l11ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡆࡢ࡫࡯ࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ೔")
  elif bstack1ll11l1l11_opy_ == bstack11l11ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤೕ"):
    return bstack11l11ll_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡖࡡࡴࡵࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪೖ")
  elif bstack1ll11l1l11_opy_ == bstack11l11ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ೗"):
    return bstack11l11ll_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡉࡷࡸ࡯ࡳ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ೘")
  elif bstack1ll11l1l11_opy_ == bstack11l11ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢ೙"):
    return bstack11l11ll_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࠦࡩࡪࡧ࠳࠳࠸࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࠨ࡫ࡥࡢ࠵࠵࠺ࠧࡄࡔࡪ࡯ࡨࡳࡺࡺ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ೚")
  elif bstack1ll11l1l11_opy_ == bstack11l11ll_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠤ೛"):
    return bstack11l11ll_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࡗࡻ࡮࡯࡫ࡱ࡫ࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ೜")
  else:
    return bstack11l11ll_opy_ (u"ࠪࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࠧೝ") + bstack1lll1ll111_opy_(
      bstack1ll11l1l11_opy_) + bstack11l11ll_opy_ (u"ࠫࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪೞ")
def bstack11l111111_opy_(session):
  return bstack11l11ll_opy_ (u"ࠬࡂࡴࡳࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡵࡳࡼࠨ࠾࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠢࡶࡩࡸࡹࡩࡰࡰ࠰ࡲࡦࡳࡥࠣࡀ࠿ࡥࠥ࡮ࡲࡦࡨࡀࠦࢀࢃࠢࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤࡢࡦࡱࡧ࡮࡬ࠤࡁࡿࢂࡂ࠯ࡢࡀ࠿࠳ࡹࡪ࠾ࡼࡿࡾࢁࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼࠰ࡶࡵࡂࠬ೟").format(
    session[bstack11l11ll_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪೠ")], bstack111l1l1l_opy_(session), bstack11l1ll1l1_opy_(session[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡵࡣࡷࡹࡸ࠭ೡ")]),
    bstack11l1ll1l1_opy_(session[bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨೢ")]),
    bstack1lll1ll111_opy_(session[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪೣ")] or session[bstack11l11ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ೤")] or bstack11l11ll_opy_ (u"ࠫࠬ೥")) + bstack11l11ll_opy_ (u"ࠧࠦࠢ೦") + (session[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ೧")] or bstack11l11ll_opy_ (u"ࠧࠨ೨")),
    session[bstack11l11ll_opy_ (u"ࠨࡱࡶࠫ೩")] + bstack11l11ll_opy_ (u"ࠤࠣࠦ೪") + session[bstack11l11ll_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ೫")], session[bstack11l11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭೬")] or bstack11l11ll_opy_ (u"ࠬ࠭೭"),
    session[bstack11l11ll_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪ೮")] if session[bstack11l11ll_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫ೯")] else bstack11l11ll_opy_ (u"ࠨࠩ೰"))
def bstack1l1l1l1l1_opy_(sessions, bstack1lllll11ll_opy_):
  try:
    bstack1llllll11_opy_ = bstack11l11ll_opy_ (u"ࠤࠥೱ")
    if not os.path.exists(bstack1llll111l_opy_):
      os.mkdir(bstack1llll111l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l11ll_opy_ (u"ࠪࡥࡸࡹࡥࡵࡵ࠲ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨೲ")), bstack11l11ll_opy_ (u"ࠫࡷ࠭ೳ")) as f:
      bstack1llllll11_opy_ = f.read()
    bstack1llllll11_opy_ = bstack1llllll11_opy_.replace(bstack11l11ll_opy_ (u"ࠬࢁࠥࡓࡇࡖ࡙ࡑ࡚ࡓࡠࡅࡒ࡙ࡓ࡚ࠥࡾࠩ೴"), str(len(sessions)))
    bstack1llllll11_opy_ = bstack1llllll11_opy_.replace(bstack11l11ll_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠩࢂ࠭೵"), bstack1lllll11ll_opy_)
    bstack1llllll11_opy_ = bstack1llllll11_opy_.replace(bstack11l11ll_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊࠫࡽࠨ೶"),
                                              sessions[0].get(bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡣࡰࡩࠬ೷")) if sessions[0] else bstack11l11ll_opy_ (u"ࠩࠪ೸"))
    with open(os.path.join(bstack1llll111l_opy_, bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧ೹")), bstack11l11ll_opy_ (u"ࠫࡼ࠭೺")) as stream:
      stream.write(bstack1llllll11_opy_.split(bstack11l11ll_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩ೻"))[0])
      for session in sessions:
        stream.write(bstack11l111111_opy_(session))
      stream.write(bstack1llllll11_opy_.split(bstack11l11ll_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪ೼"))[1])
    logger.info(bstack11l11ll_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࡦࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡥࡹ࡮ࡲࡤࠡࡣࡵࡸ࡮࡬ࡡࡤࡶࡶࠤࡦࡺࠠࡼࡿࠪ೽").format(bstack1llll111l_opy_));
  except Exception as e:
    logger.debug(bstack1ll1l11l_opy_.format(str(e)))
def bstack1l1l11111_opy_(bstack11l11ll1l_opy_):
  global CONFIG
  try:
    host = bstack11l11ll_opy_ (u"ࠨࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧࠫ೾") if bstack11l11ll_opy_ (u"ࠩࡤࡴࡵ࠭೿") in CONFIG else bstack11l11ll_opy_ (u"ࠪࡥࡵ࡯ࠧഀ")
    user = CONFIG[bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ഁ")]
    key = CONFIG[bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨം")]
    bstack111l1l11l_opy_ = bstack11l11ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬഃ") if bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࠫഄ") in CONFIG else bstack11l11ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪഅ")
    url = bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡾࢁ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠰࡭ࡷࡴࡴࠧആ").format(user, key, host, bstack111l1l11l_opy_,
                                                                                bstack11l11ll1l_opy_)
    headers = {
      bstack11l11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩഇ"): bstack11l11ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧഈ"),
    }
    proxies = bstack1ll11llll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack11l11ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠪഉ")], response.json()))
  except Exception as e:
    logger.debug(bstack1l111ll11_opy_.format(str(e)))
def get_build_link():
  global CONFIG
  global bstack1ll1111ll_opy_
  try:
    if bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩഊ") in CONFIG:
      host = bstack11l11ll_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦࠪഋ") if bstack11l11ll_opy_ (u"ࠨࡣࡳࡴࠬഌ") in CONFIG else bstack11l11ll_opy_ (u"ࠩࡤࡴ࡮࠭഍")
      user = CONFIG[bstack11l11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬഎ")]
      key = CONFIG[bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧഏ")]
      bstack111l1l11l_opy_ = bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫഐ") if bstack11l11ll_opy_ (u"࠭ࡡࡱࡲࠪ഑") in CONFIG else bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩഒ")
      url = bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡽࢀ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠱࡮ࡸࡵ࡮ࠨഓ").format(user, key, host, bstack111l1l11l_opy_)
      headers = {
        bstack11l11ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨഔ"): bstack11l11ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ക"),
      }
      if bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ഖ") in CONFIG:
        params = {bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪഗ"): CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩഘ")], bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪങ"): CONFIG[bstack11l11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪച")]}
      else:
        params = {bstack11l11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧഛ"): CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ജ")]}
      proxies = bstack1ll11llll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1111l111_opy_ = response.json()[0][bstack11l11ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡤࡸ࡭ࡱࡪࠧഝ")]
        if bstack1111l111_opy_:
          bstack1lllll11ll_opy_ = bstack1111l111_opy_[bstack11l11ll_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩഞ")].split(bstack11l11ll_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨ࠳ࡢࡶ࡫࡯ࡨࠬട"))[0] + bstack11l11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹ࠯ࠨഠ") + bstack1111l111_opy_[
            bstack11l11ll_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫഡ")]
          logger.info(bstack1l1lll1l1_opy_.format(bstack1lllll11ll_opy_))
          bstack1ll1111ll_opy_ = bstack1111l111_opy_[bstack11l11ll_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬഢ")]
          bstack1lll1l1l1l_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ണ")]
          if bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ത") in CONFIG:
            bstack1lll1l1l1l_opy_ += bstack11l11ll_opy_ (u"ࠬࠦࠧഥ") + CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨദ")]
          if bstack1lll1l1l1l_opy_ != bstack1111l111_opy_[bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬധ")]:
            logger.debug(bstack1l1l11111l_opy_.format(bstack1111l111_opy_[bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ന")], bstack1lll1l1l1l_opy_))
          return [bstack1111l111_opy_[bstack11l11ll_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬഩ")], bstack1lllll11ll_opy_]
    else:
      logger.warn(bstack1l111ll1_opy_)
  except Exception as e:
    logger.debug(bstack111llll1l_opy_.format(str(e)))
  return [None, None]
def bstack11lllll1l_opy_(url, bstack1lll1l1l11_opy_=False):
  global CONFIG
  global bstack1ll1111lll_opy_
  if not bstack1ll1111lll_opy_:
    hostname = bstack1ll1l11l1l_opy_(url)
    is_private = bstack1ll1llll1l_opy_(hostname)
    if (bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧപ") in CONFIG and not bstack1lll1lll11_opy_(CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨഫ")])) and (is_private or bstack1lll1l1l11_opy_):
      bstack1ll1111lll_opy_ = hostname
def bstack1ll1l11l1l_opy_(url):
  return urlparse(url).hostname
def bstack1ll1llll1l_opy_(hostname):
  for bstack1l1ll11ll1_opy_ in bstack1l11l1ll_opy_:
    regex = re.compile(bstack1l1ll11ll1_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l1l11l1l1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11ll1l1l1_opy_
  bstack1lllll111_opy_ = not (bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩബ"), None) and bstack11l11lll1_opy_(
          threading.current_thread(), bstack11l11ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬഭ"), None))
  bstack11l1ll1ll_opy_ = getattr(driver, bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧമ"), None) != True
  if not bstack1l1l111ll_opy_.bstack1ll1l1ll1l_opy_(CONFIG, bstack11ll1l1l1_opy_) or (bstack11l1ll1ll_opy_ and bstack1lllll111_opy_):
    logger.warning(bstack11l11ll_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦയ"))
    return {}
  try:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ര"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1l1l1lll_opy_.bstack1ll11l1l1l_opy_)
    return results
  except Exception:
    logger.error(bstack11l11ll_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧറ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11ll1l1l1_opy_
  bstack1lllll111_opy_ = not (bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨല"), None) and bstack11l11lll1_opy_(
          threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫള"), None))
  bstack11l1ll1ll_opy_ = getattr(driver, bstack11l11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ഴ"), None) != True
  if not bstack1l1l111ll_opy_.bstack1ll1l1ll1l_opy_(CONFIG, bstack11ll1l1l1_opy_) or (bstack11l1ll1ll_opy_ and bstack1lllll111_opy_):
    logger.warning(bstack11l11ll_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦവ"))
    return {}
  try:
    logger.debug(bstack11l11ll_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ശ"))
    logger.debug(perform_scan(driver))
    bstack1lll1l11ll_opy_ = driver.execute_async_script(bstack1l1l1l1lll_opy_.bstack11llll1l1_opy_)
    return bstack1lll1l11ll_opy_
  except Exception:
    logger.error(bstack11l11ll_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥഷ"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11ll1l1l1_opy_
  bstack1lllll111_opy_ = not (bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧസ"), None) and bstack11l11lll1_opy_(
          threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഹ"), None))
  bstack11l1ll1ll_opy_ = getattr(driver, bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬഺ"), None) != True
  if not bstack1l1l111ll_opy_.bstack1ll1l1ll1l_opy_(CONFIG, bstack11ll1l1l1_opy_) or (bstack11l1ll1ll_opy_ and bstack1lllll111_opy_):
    logger.warning(bstack11l11ll_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡵ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮഻ࠣ"))
    return {}
  try:
    bstack1ll111l11l_opy_ = driver.execute_async_script(bstack1l1l1l1lll_opy_.perform_scan, {bstack11l11ll_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ഼ࠧ"): kwargs.get(bstack11l11ll_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩഽ"), None) or bstack11l11ll_opy_ (u"ࠩࠪാ")})
    return bstack1ll111l11l_opy_
  except Exception:
    logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡲࡶࡰࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮࠯ࠤി"))
    return {}
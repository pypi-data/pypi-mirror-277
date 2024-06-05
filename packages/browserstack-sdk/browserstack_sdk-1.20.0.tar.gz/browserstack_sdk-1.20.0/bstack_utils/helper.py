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
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack11l11ll11l_opy_, bstack1l11l1ll_opy_, bstack111l111ll_opy_, bstack1111ll1l1_opy_,
                                    bstack11l1l11111_opy_, bstack11l11ll1ll_opy_)
from bstack_utils.messages import bstack11111l1l1_opy_, bstack1l1l11ll11_opy_
from bstack_utils.proxy import bstack1ll11llll_opy_, bstack1ll11ll111_opy_
bstack1ll1111l1_opy_ = Config.bstack11l11l11_opy_()
logger = logging.getLogger(__name__)
def bstack11l1llll1l_opy_(config):
    return config[bstack11l11ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᆫ")]
def bstack11l1ll1l11_opy_(config):
    return config[bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᆬ")]
def bstack1lll1lll1l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l11ll1l_opy_(obj):
    values = []
    bstack111l1l1lll_opy_ = re.compile(bstack11l11ll_opy_ (u"ࡵࠦࡣࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࡟ࡨ࠰ࠪࠢᆭ"), re.I)
    for key in obj.keys():
        if bstack111l1l1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111ll1ll11_opy_(config):
    tags = []
    tags.extend(bstack111l11ll1l_opy_(os.environ))
    tags.extend(bstack111l11ll1l_opy_(config))
    return tags
def bstack111l11ll11_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111ll1ll1l_opy_(bstack111ll11lll_opy_):
    if not bstack111ll11lll_opy_:
        return bstack11l11ll_opy_ (u"ࠫࠬᆮ")
    return bstack11l11ll_opy_ (u"ࠧࢁࡽࠡࠪࡾࢁ࠮ࠨᆯ").format(bstack111ll11lll_opy_.name, bstack111ll11lll_opy_.email)
def bstack11ll111111_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111llll1l1_opy_ = repo.common_dir
        info = {
            bstack11l11ll_opy_ (u"ࠨࡳࡩࡣࠥᆰ"): repo.head.commit.hexsha,
            bstack11l11ll_opy_ (u"ࠢࡴࡪࡲࡶࡹࡥࡳࡩࡣࠥᆱ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l11ll_opy_ (u"ࠣࡤࡵࡥࡳࡩࡨࠣᆲ"): repo.active_branch.name,
            bstack11l11ll_opy_ (u"ࠤࡷࡥ࡬ࠨᆳ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࠨᆴ"): bstack111ll1ll1l_opy_(repo.head.commit.committer),
            bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸ࡟ࡥࡣࡷࡩࠧᆵ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l11ll_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࠧᆶ"): bstack111ll1ll1l_opy_(repo.head.commit.author),
            bstack11l11ll_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡥࡤࡢࡶࡨࠦᆷ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l11ll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᆸ"): repo.head.commit.message,
            bstack11l11ll_opy_ (u"ࠣࡴࡲࡳࡹࠨᆹ"): repo.git.rev_parse(bstack11l11ll_opy_ (u"ࠤ࠰࠱ࡸ࡮࡯ࡸ࠯ࡷࡳࡵࡲࡥࡷࡧ࡯ࠦᆺ")),
            bstack11l11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡰࡰࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᆻ"): bstack111llll1l1_opy_,
            bstack11l11ll_opy_ (u"ࠦࡼࡵࡲ࡬ࡶࡵࡩࡪࡥࡧࡪࡶࡢࡨ࡮ࡸࠢᆼ"): subprocess.check_output([bstack11l11ll_opy_ (u"ࠧ࡭ࡩࡵࠤᆽ"), bstack11l11ll_opy_ (u"ࠨࡲࡦࡸ࠰ࡴࡦࡸࡳࡦࠤᆾ"), bstack11l11ll_opy_ (u"ࠢ࠮࠯ࡪ࡭ࡹ࠳ࡣࡰ࡯ࡰࡳࡳ࠳ࡤࡪࡴࠥᆿ")]).strip().decode(
                bstack11l11ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᇀ")),
            bstack11l11ll_opy_ (u"ࠤ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦᇁ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡶࡣࡸ࡯࡮ࡤࡧࡢࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᇂ"): repo.git.rev_list(
                bstack11l11ll_opy_ (u"ࠦࢀࢃ࠮࠯ࡽࢀࠦᇃ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111llll1ll_opy_ = []
        for remote in remotes:
            bstack11l11l11ll_opy_ = {
                bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᇄ"): remote.name,
                bstack11l11ll_opy_ (u"ࠨࡵࡳ࡮ࠥᇅ"): remote.url,
            }
            bstack111llll1ll_opy_.append(bstack11l11l11ll_opy_)
        bstack111l1l11l1_opy_ = {
            bstack11l11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇆ"): bstack11l11ll_opy_ (u"ࠣࡩ࡬ࡸࠧᇇ"),
            **info,
            bstack11l11ll_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡵࠥᇈ"): bstack111llll1ll_opy_
        }
        bstack111l1l11l1_opy_ = bstack111lll11l1_opy_(bstack111l1l11l1_opy_)
        return bstack111l1l11l1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᇉ").format(err))
        return {}
def bstack111lll11l1_opy_(bstack111l1l11l1_opy_):
    bstack111lll1lll_opy_ = bstack111lllll11_opy_(bstack111l1l11l1_opy_)
    if bstack111lll1lll_opy_ and bstack111lll1lll_opy_ > bstack11l1l11111_opy_:
        bstack111ll1l11l_opy_ = bstack111lll1lll_opy_ - bstack11l1l11111_opy_
        bstack11l1111l1l_opy_ = bstack111lll1l1l_opy_(bstack111l1l11l1_opy_[bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᇊ")], bstack111ll1l11l_opy_)
        bstack111l1l11l1_opy_[bstack11l11ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᇋ")] = bstack11l1111l1l_opy_
        logger.info(bstack11l11ll_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣᇌ")
                    .format(bstack111lllll11_opy_(bstack111l1l11l1_opy_) / 1024))
    return bstack111l1l11l1_opy_
def bstack111lllll11_opy_(bstack1l1l1111_opy_):
    try:
        if bstack1l1l1111_opy_:
            bstack11l1111ll1_opy_ = json.dumps(bstack1l1l1111_opy_)
            bstack111ll111l1_opy_ = sys.getsizeof(bstack11l1111ll1_opy_)
            return bstack111ll111l1_opy_
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢᇍ").format(e))
    return -1
def bstack111lll1l1l_opy_(field, bstack111l1ll1ll_opy_):
    try:
        bstack111ll111ll_opy_ = len(bytes(bstack11l11ll1ll_opy_, bstack11l11ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᇎ")))
        bstack111l1l1111_opy_ = bytes(field, bstack11l11ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᇏ"))
        bstack111lll11ll_opy_ = len(bstack111l1l1111_opy_)
        bstack11l111lll1_opy_ = ceil(bstack111lll11ll_opy_ - bstack111l1ll1ll_opy_ - bstack111ll111ll_opy_)
        if bstack11l111lll1_opy_ > 0:
            bstack111l1l1l1l_opy_ = bstack111l1l1111_opy_[:bstack11l111lll1_opy_].decode(bstack11l11ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᇐ"), errors=bstack11l11ll_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫᇑ")) + bstack11l11ll1ll_opy_
            return bstack111l1l1l1l_opy_
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥᇒ").format(e))
    return field
def bstack11ll1l1l_opy_():
    env = os.environ
    if (bstack11l11ll_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᇓ") in env and len(env[bstack11l11ll_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᇔ")]) > 0) or (
            bstack11l11ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᇕ") in env and len(env[bstack11l11ll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᇖ")]) > 0):
        return {
            bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᇗ"): bstack11l11ll_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧᇘ"),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᇙ"): env.get(bstack11l11ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᇚ")),
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇛ"): env.get(bstack11l11ll_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥᇜ")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇝ"): env.get(bstack11l11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᇞ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦࡈࡏࠢᇟ")) == bstack11l11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᇠ") and bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣᇡ"))):
        return {
            bstack11l11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇢ"): bstack11l11ll_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥᇣ"),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇤ"): env.get(bstack11l11ll_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᇥ")),
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇦ"): env.get(bstack11l11ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤᇧ")),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇨ"): env.get(bstack11l11ll_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥᇩ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠣࡅࡌࠦᇪ")) == bstack11l11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᇫ") and bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥᇬ"))):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇭ"): bstack11l11ll_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣᇮ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇯ"): env.get(bstack11l11ll_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢᇰ")),
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇱ"): env.get(bstack11l11ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᇲ")),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᇳ"): env.get(bstack11l11ll_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᇴ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠧࡉࡉࠣᇵ")) == bstack11l11ll_opy_ (u"ࠨࡴࡳࡷࡨࠦᇶ") and env.get(bstack11l11ll_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣᇷ")) == bstack11l11ll_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥᇸ"):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᇹ"): bstack11l11ll_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧᇺ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᇻ"): None,
            bstack11l11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᇼ"): None,
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇽ"): None
        }
    if env.get(bstack11l11ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥᇾ")) and env.get(bstack11l11ll_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦᇿ")):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሀ"): bstack11l11ll_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨሁ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢሂ"): env.get(bstack11l11ll_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥሃ")),
            bstack11l11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሄ"): None,
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨህ"): env.get(bstack11l11ll_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥሆ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠤࡆࡍࠧሇ")) == bstack11l11ll_opy_ (u"ࠥࡸࡷࡻࡥࠣለ") and bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥሉ"))):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥሊ"): bstack11l11ll_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧላ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥሌ"): env.get(bstack11l11ll_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦል")),
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦሎ"): None,
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤሏ"): env.get(bstack11l11ll_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤሐ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠧࡉࡉࠣሑ")) == bstack11l11ll_opy_ (u"ࠨࡴࡳࡷࡨࠦሒ") and bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥሓ"))):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨሔ"): bstack11l11ll_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧሕ"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨሖ"): env.get(bstack11l11ll_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥሗ")),
            bstack11l11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢመ"): env.get(bstack11l11ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦሙ")),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨሚ"): env.get(bstack11l11ll_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦማ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠤࡆࡍࠧሜ")) == bstack11l11ll_opy_ (u"ࠥࡸࡷࡻࡥࠣም") and bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢሞ"))):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥሟ"): bstack11l11ll_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨሠ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥሡ"): env.get(bstack11l11ll_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧሢ")),
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦሣ"): env.get(bstack11l11ll_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣሤ")),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥሥ"): env.get(bstack11l11ll_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣሦ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠨࡃࡊࠤሧ")) == bstack11l11ll_opy_ (u"ࠢࡵࡴࡸࡩࠧረ") and bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦሩ"))):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሪ"): bstack11l11ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨራ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢሬ"): env.get(bstack11l11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦር")),
            bstack11l11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሮ"): env.get(bstack11l11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤሯ")) or env.get(bstack11l11ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦሰ")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣሱ"): env.get(bstack11l11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧሲ"))
        }
    if bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨሳ"))):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥሴ"): bstack11l11ll_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨስ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥሶ"): bstack11l11ll_opy_ (u"ࠣࡽࢀࡿࢂࠨሷ").format(env.get(bstack11l11ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬሸ")), env.get(bstack11l11ll_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪሹ"))),
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨሺ"): env.get(bstack11l11ll_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦሻ")),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧሼ"): env.get(bstack11l11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢሽ"))
        }
    if bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥሾ"))):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሿ"): bstack11l11ll_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧቀ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቁ"): bstack11l11ll_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦቂ").format(env.get(bstack11l11ll_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬቃ")), env.get(bstack11l11ll_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨቄ")), env.get(bstack11l11ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩቅ")), env.get(bstack11l11ll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ቆ"))),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧቇ"): env.get(bstack11l11ll_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣቈ")),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ቉"): env.get(bstack11l11ll_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢቊ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣቋ")) and env.get(bstack11l11ll_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥቌ")):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቍ"): bstack11l11ll_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍࠧ቎"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ቏"): bstack11l11ll_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽࠣቐ").format(env.get(bstack11l11ll_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩቑ")), env.get(bstack11l11ll_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬቒ")), env.get(bstack11l11ll_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨቓ"))),
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦቔ"): env.get(bstack11l11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥቕ")),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥቖ"): env.get(bstack11l11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ቗"))
        }
    if any([env.get(bstack11l11ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦቘ")), env.get(bstack11l11ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨ቙")), env.get(bstack11l11ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧቚ"))]):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቛ"): bstack11l11ll_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥቜ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቝ"): env.get(bstack11l11ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ቞")),
            bstack11l11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ቟"): env.get(bstack11l11ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧበ")),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢቡ"): env.get(bstack11l11ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢቢ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣባ")):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤቤ"): bstack11l11ll_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧብ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤቦ"): env.get(bstack11l11ll_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤቧ")),
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥቨ"): env.get(bstack11l11ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣቩ")),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤቪ"): env.get(bstack11l11ll_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤቫ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨቬ")) or env.get(bstack11l11ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣቭ")):
        return {
            bstack11l11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧቮ"): bstack11l11ll_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤቯ"),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧተ"): env.get(bstack11l11ll_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢቱ")),
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨቲ"): bstack11l11ll_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧታ") if env.get(bstack11l11ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣቴ")) else None,
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨት"): env.get(bstack11l11ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨቶ"))
        }
    if any([env.get(bstack11l11ll_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢቷ")), env.get(bstack11l11ll_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦቸ")), env.get(bstack11l11ll_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦቹ"))]):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥቺ"): bstack11l11ll_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧቻ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥቼ"): None,
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥች"): env.get(bstack11l11ll_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨቾ")),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤቿ"): env.get(bstack11l11ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨኀ"))
        }
    if env.get(bstack11l11ll_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣኁ")):
        return {
            bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦኂ"): bstack11l11ll_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥኃ"),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኄ"): env.get(bstack11l11ll_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣኅ")),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧኆ"): bstack11l11ll_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁࠧኇ").format(env.get(bstack11l11ll_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨኈ"))) if env.get(bstack11l11ll_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤ኉")) else None,
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኊ"): env.get(bstack11l11ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥኋ"))
        }
    if bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥኌ"))):
        return {
            bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣኍ"): bstack11l11ll_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽࠧ኎"),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ኏"): env.get(bstack11l11ll_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎࠥነ")),
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤኑ"): env.get(bstack11l11ll_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦኒ")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣና"): env.get(bstack11l11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧኔ"))
        }
    if bstack1lll1lll11_opy_(env.get(bstack11l11ll_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧን"))):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥኖ"): bstack11l11ll_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹࠢኗ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥኘ"): bstack11l11ll_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤኙ").format(env.get(bstack11l11ll_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭ኚ")), env.get(bstack11l11ll_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧኛ")), env.get(bstack11l11ll_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫኜ"))),
            bstack11l11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢኝ"): env.get(bstack11l11ll_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣኞ")),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኟ"): env.get(bstack11l11ll_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣአ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠤࡆࡍࠧኡ")) == bstack11l11ll_opy_ (u"ࠥࡸࡷࡻࡥࠣኢ") and env.get(bstack11l11ll_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦኣ")) == bstack11l11ll_opy_ (u"ࠧ࠷ࠢኤ"):
        return {
            bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦእ"): bstack11l11ll_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢኦ"),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኧ"): bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧከ").format(env.get(bstack11l11ll_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧኩ"))),
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨኪ"): None,
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦካ"): None,
        }
    if env.get(bstack11l11ll_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤኬ")):
        return {
            bstack11l11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧክ"): bstack11l11ll_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥኮ"),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧኯ"): None,
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧኰ"): env.get(bstack11l11ll_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧ኱")),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦኲ"): env.get(bstack11l11ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧኳ"))
        }
    if any([env.get(bstack11l11ll_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥኴ")), env.get(bstack11l11ll_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣኵ")), env.get(bstack11l11ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢ኶")), env.get(bstack11l11ll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦ኷"))]):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤኸ"): bstack11l11ll_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣኹ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤኺ"): None,
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤኻ"): env.get(bstack11l11ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤኼ")) or None,
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣኽ"): env.get(bstack11l11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧኾ"), 0)
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ኿")):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥዀ"): bstack11l11ll_opy_ (u"ࠨࡇࡰࡅࡇࠦ዁"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥዂ"): None,
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥዃ"): env.get(bstack11l11ll_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢዄ")),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤዅ"): env.get(bstack11l11ll_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥ዆"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ዇")):
        return {
            bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦወ"): bstack11l11ll_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥዉ"),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦዊ"): env.get(bstack11l11ll_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣዋ")),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧዌ"): env.get(bstack11l11ll_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢው")),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦዎ"): env.get(bstack11l11ll_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦዏ"))
        }
    return {bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨዐ"): None}
def get_host_info():
    return {
        bstack11l11ll_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥዑ"): platform.node(),
        bstack11l11ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦዒ"): platform.system(),
        bstack11l11ll_opy_ (u"ࠥࡸࡾࡶࡥࠣዓ"): platform.machine(),
        bstack11l11ll_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧዔ"): platform.version(),
        bstack11l11ll_opy_ (u"ࠧࡧࡲࡤࡪࠥዕ"): platform.architecture()[0]
    }
def bstack1ll11ll1l1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111ll11l11_opy_():
    if bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧዖ")):
        return bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭዗")
    return bstack11l11ll_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧዘ")
def bstack111ll1l111_opy_(driver):
    info = {
        bstack11l11ll_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨዙ"): driver.capabilities,
        bstack11l11ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧዚ"): driver.session_id,
        bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬዛ"): driver.capabilities.get(bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪዜ"), None),
        bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨዝ"): driver.capabilities.get(bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨዞ"), None),
        bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪዟ"): driver.capabilities.get(bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨዠ"), None),
    }
    if bstack111ll11l11_opy_() == bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩዡ"):
        info[bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬዢ")] = bstack11l11ll_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫዣ") if bstack111l1l1l1_opy_() else bstack11l11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨዤ")
    return info
def bstack111l1l1l1_opy_():
    if bstack1ll1111l1_opy_.get_property(bstack11l11ll_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ዥ")):
        return True
    if bstack1lll1lll11_opy_(os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩዦ"), None)):
        return True
    return False
def bstack11llll11l_opy_(bstack111l1ll1l1_opy_, url, data, config):
    headers = config.get(bstack11l11ll_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪዧ"), None)
    proxies = bstack1ll11llll_opy_(config, url)
    auth = config.get(bstack11l11ll_opy_ (u"ࠪࡥࡺࡺࡨࠨየ"), None)
    response = requests.request(
            bstack111l1ll1l1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11lll111_opy_(bstack1l11ll1ll1_opy_, size):
    bstack1ll11lll_opy_ = []
    while len(bstack1l11ll1ll1_opy_) > size:
        bstack1llll1111_opy_ = bstack1l11ll1ll1_opy_[:size]
        bstack1ll11lll_opy_.append(bstack1llll1111_opy_)
        bstack1l11ll1ll1_opy_ = bstack1l11ll1ll1_opy_[size:]
    bstack1ll11lll_opy_.append(bstack1l11ll1ll1_opy_)
    return bstack1ll11lll_opy_
def bstack11l11l1111_opy_(message, bstack111lllllll_opy_=False):
    os.write(1, bytes(message, bstack11l11ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪዩ")))
    os.write(1, bytes(bstack11l11ll_opy_ (u"ࠬࡢ࡮ࠨዪ"), bstack11l11ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬያ")))
    if bstack111lllllll_opy_:
        with open(bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ዬ") + os.environ[bstack11l11ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧይ")] + bstack11l11ll_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧዮ"), bstack11l11ll_opy_ (u"ࠪࡥࠬዯ")) as f:
            f.write(message + bstack11l11ll_opy_ (u"ࠫࡡࡴࠧደ"))
def bstack11l11111ll_opy_():
    return os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨዱ")].lower() == bstack11l11ll_opy_ (u"࠭ࡴࡳࡷࡨࠫዲ")
def bstack111l11ll_opy_(bstack111l1lll11_opy_):
    return bstack11l11ll_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ዳ").format(bstack11l11ll11l_opy_, bstack111l1lll11_opy_)
def bstack1l1ll111l_opy_():
    return bstack1l1111llll_opy_().replace(tzinfo=None).isoformat() + bstack11l11ll_opy_ (u"ࠨ࡜ࠪዴ")
def bstack111llll11l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l11ll_opy_ (u"ࠩ࡝ࠫድ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l11ll_opy_ (u"ࠪ࡞ࠬዶ")))).total_seconds() * 1000
def bstack111l1l111l_opy_(timestamp):
    return bstack111ll1111l_opy_(timestamp).isoformat() + bstack11l11ll_opy_ (u"ࠫ࡟࠭ዷ")
def bstack11l11l111l_opy_(bstack11l1111111_opy_):
    date_format = bstack11l11ll_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪዸ")
    bstack11l11111l1_opy_ = datetime.datetime.strptime(bstack11l1111111_opy_, date_format)
    return bstack11l11111l1_opy_.isoformat() + bstack11l11ll_opy_ (u"࡚࠭ࠨዹ")
def bstack111lll111l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧዺ")
    else:
        return bstack11l11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨዻ")
def bstack1lll1lll11_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l11ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧዼ")
def bstack111l1l1ll1_opy_(val):
    return val.__str__().lower() == bstack11l11ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩዽ")
def bstack11ll1lllll_opy_(bstack111ll11ll1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111ll11ll1_opy_ as e:
                print(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦዾ").format(func.__name__, bstack111ll11ll1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11l111ll11_opy_(bstack111llllll1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111llllll1_opy_(cls, *args, **kwargs)
            except bstack111ll11ll1_opy_ as e:
                print(bstack11l11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧዿ").format(bstack111llllll1_opy_.__name__, bstack111ll11ll1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11l111ll11_opy_
    else:
        return decorator
def bstack11ll1ll11_opy_(bstack11ll1lll11_opy_):
    if bstack11l11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪጀ") in bstack11ll1lll11_opy_ and bstack111l1l1ll1_opy_(bstack11ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫጁ")]):
        return False
    if bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪጂ") in bstack11ll1lll11_opy_ and bstack111l1l1ll1_opy_(bstack11ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫጃ")]):
        return False
    return True
def bstack1111l11l1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1lll1ll1l_opy_(hub_url):
    if bstack1l1l1l11ll_opy_() <= version.parse(bstack11l11ll_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪጄ")):
        if hub_url != bstack11l11ll_opy_ (u"ࠫࠬጅ"):
            return bstack11l11ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨጆ") + hub_url + bstack11l11ll_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥጇ")
        return bstack111l111ll_opy_
    if hub_url != bstack11l11ll_opy_ (u"ࠧࠨገ"):
        return bstack11l11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥጉ") + hub_url + bstack11l11ll_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥጊ")
    return bstack1111ll1l1_opy_
def bstack111ll11111_opy_():
    return isinstance(os.getenv(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩጋ")), str)
def bstack1ll1l11l1l_opy_(url):
    return urlparse(url).hostname
def bstack1ll1llll1l_opy_(hostname):
    for bstack1l1ll11ll1_opy_ in bstack1l11l1ll_opy_:
        regex = re.compile(bstack1l1ll11ll1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111ll11l1l_opy_(bstack111l11llll_opy_, file_name, logger):
    bstack1lllll1ll_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠫࢃ࠭ጌ")), bstack111l11llll_opy_)
    try:
        if not os.path.exists(bstack1lllll1ll_opy_):
            os.makedirs(bstack1lllll1ll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠬࢄࠧግ")), bstack111l11llll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l11ll_opy_ (u"࠭ࡷࠨጎ")):
                pass
            with open(file_path, bstack11l11ll_opy_ (u"ࠢࡸ࠭ࠥጏ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11111l1l1_opy_.format(str(e)))
def bstack111ll1llll_opy_(file_name, key, value, logger):
    file_path = bstack111ll11l1l_opy_(bstack11l11ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨጐ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11l111l1l_opy_ = json.load(open(file_path, bstack11l11ll_opy_ (u"ࠩࡵࡦࠬ጑")))
        else:
            bstack11l111l1l_opy_ = {}
        bstack11l111l1l_opy_[key] = value
        with open(file_path, bstack11l11ll_opy_ (u"ࠥࡻ࠰ࠨጒ")) as outfile:
            json.dump(bstack11l111l1l_opy_, outfile)
def bstack1ll111ll1l_opy_(file_name, logger):
    file_path = bstack111ll11l1l_opy_(bstack11l11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫጓ"), file_name, logger)
    bstack11l111l1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l11ll_opy_ (u"ࠬࡸࠧጔ")) as bstack111l11l1l_opy_:
            bstack11l111l1l_opy_ = json.load(bstack111l11l1l_opy_)
    return bstack11l111l1l_opy_
def bstack1lllll1111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪጕ") + file_path + bstack11l11ll_opy_ (u"ࠧࠡࠩ጖") + str(e))
def bstack1l1l1l11ll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l11ll_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥ጗")
def bstack11llllll_opy_(config):
    if bstack11l11ll_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨጘ") in config:
        del (config[bstack11l11ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩጙ")])
        return False
    if bstack1l1l1l11ll_opy_() < version.parse(bstack11l11ll_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪጚ")):
        return False
    if bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫጛ")):
        return True
    if bstack11l11ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ጜ") in config and config[bstack11l11ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧጝ")] is False:
        return False
    else:
        return True
def bstack1l11l1ll11_opy_(args_list, bstack111ll1l1ll_opy_):
    index = -1
    for value in bstack111ll1l1ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11lll111ll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11lll111ll_opy_ = bstack11lll111ll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨጞ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩጟ"), exception=exception)
    def bstack11ll11ll1l_opy_(self):
        if self.result != bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪጠ"):
            return None
        if bstack11l11ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢጡ") in self.exception_type:
            return bstack11l11ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨጢ")
        return bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢጣ")
    def bstack111lllll1l_opy_(self):
        if self.result != bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧጤ"):
            return None
        if self.bstack11lll111ll_opy_:
            return self.bstack11lll111ll_opy_
        return bstack111l11lll1_opy_(self.exception)
def bstack111l11lll1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1ll11l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11l11lll1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll1ll1lll_opy_(config, logger):
    try:
        import playwright
        bstack111l1l1l11_opy_ = playwright.__file__
        bstack111l1lllll_opy_ = os.path.split(bstack111l1l1l11_opy_)
        bstack11l111l1l1_opy_ = bstack111l1lllll_opy_[0] + bstack11l11ll_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫጥ")
        os.environ[bstack11l11ll_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝ࠬጦ")] = bstack1ll11ll111_opy_(config)
        with open(bstack11l111l1l1_opy_, bstack11l11ll_opy_ (u"ࠪࡶࠬጧ")) as f:
            bstack1lllllll1_opy_ = f.read()
            bstack11l111l11l_opy_ = bstack11l11ll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪጨ")
            bstack11l111llll_opy_ = bstack1lllllll1_opy_.find(bstack11l111l11l_opy_)
            if bstack11l111llll_opy_ == -1:
              process = subprocess.Popen(bstack11l11ll_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤጩ"), shell=True, cwd=bstack111l1lllll_opy_[0])
              process.wait()
              bstack111l11l1ll_opy_ = bstack11l11ll_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭ጪ")
              bstack111llll111_opy_ = bstack11l11ll_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦጫ")
              bstack111lll1111_opy_ = bstack1lllllll1_opy_.replace(bstack111l11l1ll_opy_, bstack111llll111_opy_)
              with open(bstack11l111l1l1_opy_, bstack11l11ll_opy_ (u"ࠨࡹࠪጬ")) as f:
                f.write(bstack111lll1111_opy_)
    except Exception as e:
        logger.error(bstack1l1l11ll11_opy_.format(str(e)))
def bstack1ll11lll11_opy_():
  try:
    bstack11l1111lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩጭ"))
    bstack11l11l11l1_opy_ = []
    if os.path.exists(bstack11l1111lll_opy_):
      with open(bstack11l1111lll_opy_) as f:
        bstack11l11l11l1_opy_ = json.load(f)
      os.remove(bstack11l1111lll_opy_)
    return bstack11l11l11l1_opy_
  except:
    pass
  return []
def bstack1l1l1llll_opy_(bstack1l1111ll_opy_):
  try:
    bstack11l11l11l1_opy_ = []
    bstack11l1111lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪጮ"))
    if os.path.exists(bstack11l1111lll_opy_):
      with open(bstack11l1111lll_opy_) as f:
        bstack11l11l11l1_opy_ = json.load(f)
    bstack11l11l11l1_opy_.append(bstack1l1111ll_opy_)
    with open(bstack11l1111lll_opy_, bstack11l11ll_opy_ (u"ࠫࡼ࠭ጯ")) as f:
        json.dump(bstack11l11l11l1_opy_, f)
  except:
    pass
def bstack1l1l111l11_opy_(logger, bstack11l11l1l11_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l11ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨጰ"), bstack11l11ll_opy_ (u"࠭ࠧጱ"))
    if test_name == bstack11l11ll_opy_ (u"ࠧࠨጲ"):
        test_name = threading.current_thread().__dict__.get(bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠧጳ"), bstack11l11ll_opy_ (u"ࠩࠪጴ"))
    bstack111lll1l11_opy_ = bstack11l11ll_opy_ (u"ࠪ࠰ࠥ࠭ጵ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11l11l1l11_opy_:
        bstack1l11l1l11l_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫጶ"), bstack11l11ll_opy_ (u"ࠬ࠶ࠧጷ"))
        bstack1l11lll1l_opy_ = {bstack11l11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫጸ"): test_name, bstack11l11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ጹ"): bstack111lll1l11_opy_, bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧጺ"): bstack1l11l1l11l_opy_}
        bstack11l111l1ll_opy_ = []
        bstack11l1111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨጻ"))
        if os.path.exists(bstack11l1111l11_opy_):
            with open(bstack11l1111l11_opy_) as f:
                bstack11l111l1ll_opy_ = json.load(f)
        bstack11l111l1ll_opy_.append(bstack1l11lll1l_opy_)
        with open(bstack11l1111l11_opy_, bstack11l11ll_opy_ (u"ࠪࡻࠬጼ")) as f:
            json.dump(bstack11l111l1ll_opy_, f)
    else:
        bstack1l11lll1l_opy_ = {bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩጽ"): test_name, bstack11l11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫጾ"): bstack111lll1l11_opy_, bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬጿ"): str(multiprocessing.current_process().name)}
        if bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫፀ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l11lll1l_opy_)
  except Exception as e:
      logger.warn(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧፁ").format(e))
def bstack1l1111lll_opy_(error_message, test_name, index, logger):
  try:
    bstack111l1llll1_opy_ = []
    bstack1l11lll1l_opy_ = {bstack11l11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧፂ"): test_name, bstack11l11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩፃ"): error_message, bstack11l11ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪፄ"): index}
    bstack111ll1l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ፅ"))
    if os.path.exists(bstack111ll1l1l1_opy_):
        with open(bstack111ll1l1l1_opy_) as f:
            bstack111l1llll1_opy_ = json.load(f)
    bstack111l1llll1_opy_.append(bstack1l11lll1l_opy_)
    with open(bstack111ll1l1l1_opy_, bstack11l11ll_opy_ (u"࠭ࡷࠨፆ")) as f:
        json.dump(bstack111l1llll1_opy_, f)
  except Exception as e:
    logger.warn(bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥፇ").format(e))
def bstack1l1llll1l1_opy_(bstack111111l1l_opy_, name, logger):
  try:
    bstack1l11lll1l_opy_ = {bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ፈ"): name, bstack11l11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨፉ"): bstack111111l1l_opy_, bstack11l11ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩፊ"): str(threading.current_thread()._name)}
    return bstack1l11lll1l_opy_
  except Exception as e:
    logger.warn(bstack11l11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡢࡦࡪࡤࡺࡪࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣፋ").format(e))
  return
def bstack111l1lll1l_opy_():
    return platform.system() == bstack11l11ll_opy_ (u"ࠬ࡝ࡩ࡯ࡦࡲࡻࡸ࠭ፌ")
def bstack1lll1ll1ll_opy_(bstack11l111ll1l_opy_, config, logger):
    bstack111l1l11ll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11l111ll1l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡱࡺࡥࡳࠢࡦࡳࡳ࡬ࡩࡨࠢ࡮ࡩࡾࡹࠠࡣࡻࠣࡶࡪ࡭ࡥࡹࠢࡰࡥࡹࡩࡨ࠻ࠢࡾࢁࠧፍ").format(e))
    return bstack111l1l11ll_opy_
def bstack11l111l111_opy_(bstack111lll1ll1_opy_, bstack11l111111l_opy_):
    bstack111ll1lll1_opy_ = version.parse(bstack111lll1ll1_opy_)
    bstack111l1ll111_opy_ = version.parse(bstack11l111111l_opy_)
    if bstack111ll1lll1_opy_ > bstack111l1ll111_opy_:
        return 1
    elif bstack111ll1lll1_opy_ < bstack111l1ll111_opy_:
        return -1
    else:
        return 0
def bstack1l1111llll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111ll1111l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
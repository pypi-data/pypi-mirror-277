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
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l1llll11_opy_, bstack11l1l11ll_opy_, update, bstack1l11ll1l1_opy_,
                                       bstack1l1l11ll1l_opy_, bstack1llll1ll_opy_, bstack11l111ll1_opy_, bstack1111lll1l_opy_,
                                       bstack1l1lllll11_opy_, bstack1llll11ll_opy_, bstack1ll11l11l1_opy_, bstack1ll11ll1l_opy_,
                                       bstack1ll1ll1l1l_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll1lllll_opy_)
from browserstack_sdk.bstack11ll111l1_opy_ import bstack1llllllll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1lll11l11l_opy_
from bstack_utils.capture import bstack11llll1l11_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack11l11l111_opy_, bstack1lll1l1111_opy_, bstack1l11l1111_opy_, \
    bstack1ll1l1l1l1_opy_
from bstack_utils.helper import bstack11l11lll1_opy_, bstack111ll1111l_opy_, bstack1l1111llll_opy_, bstack1ll11ll1l1_opy_, bstack11l11111ll_opy_, bstack1l1ll111l_opy_, \
    bstack111lll111l_opy_, \
    bstack111l11ll11_opy_, bstack1l1l1l11ll_opy_, bstack1lll1ll1l_opy_, bstack111ll11111_opy_, bstack1111l11l1_opy_, Notset, \
    bstack11llllll_opy_, bstack111llll11l_opy_, bstack111l11lll1_opy_, Result, bstack111l1l111l_opy_, bstack111l1ll11l_opy_, bstack11ll1lllll_opy_, \
    bstack1l1l1llll_opy_, bstack1l1l111l11_opy_, bstack1lll1lll11_opy_, bstack111l1lll1l_opy_
from bstack_utils.bstack111l11111l_opy_ import bstack111l111111_opy_
from bstack_utils.messages import bstack1l1l11l111_opy_, bstack11l11lll_opy_, bstack1ll1l1ll11_opy_, bstack1llll11lll_opy_, bstack111l1lll_opy_, \
    bstack1l1l11ll11_opy_, bstack1llll11111_opy_, bstack11lll1l11_opy_, bstack1l1l1ll1ll_opy_, bstack11l11llll_opy_, \
    bstack11ll11111_opy_, bstack1l1l11ll_opy_
from bstack_utils.proxy import bstack1ll11ll111_opy_, bstack111l1lll1_opy_
from bstack_utils.bstack1l1ll1l1ll_opy_ import bstack1llll1lll11_opy_, bstack1llll1l1ll1_opy_, bstack1llll1l1lll_opy_, bstack1llll1ll111_opy_, \
    bstack1llll1l1l11_opy_, bstack1llll1l1l1l_opy_, bstack1llll1ll11l_opy_, bstack1l1l1lll11_opy_, bstack1llll1l111l_opy_
from bstack_utils.bstack1ll11111ll_opy_ import bstack1l1l1111l1_opy_
from bstack_utils.bstack1111l1ll1_opy_ import bstack1ll111ll1_opy_, bstack11lllll1l_opy_, bstack1llll111ll_opy_, \
    bstack11ll1lll1_opy_, bstack1l1l1l111l_opy_
from bstack_utils.bstack1l111l1lll_opy_ import bstack11lll11l11_opy_
from bstack_utils.bstack1l1lll1l1l_opy_ import bstack1l1l1111l_opy_
import bstack_utils.bstack1111l1ll_opy_ as bstack1l1l111ll_opy_
from bstack_utils.bstack1l1l1l1lll_opy_ import bstack1l1l1l1lll_opy_
bstack111ll11l_opy_ = None
bstack11l111ll_opy_ = None
bstack1llll11l1l_opy_ = None
bstack11ll1l1ll_opy_ = None
bstack1llllll111_opy_ = None
bstack111llllll_opy_ = None
bstack1lll111l1l_opy_ = None
bstack1l1ll1lll_opy_ = None
bstack1lll1l1l_opy_ = None
bstack1l11ll111l_opy_ = None
bstack11l11111l_opy_ = None
bstack1l11l1l111_opy_ = None
bstack1ll1l1l11_opy_ = None
bstack111l1l111_opy_ = bstack11l11ll_opy_ (u"ࠨࠩᘋ")
CONFIG = {}
bstack1111ll11l_opy_ = False
bstack1l11ll11_opy_ = bstack11l11ll_opy_ (u"ࠩࠪᘌ")
bstack1llll1l11_opy_ = bstack11l11ll_opy_ (u"ࠪࠫᘍ")
bstack111ll1lll_opy_ = False
bstack1l111111_opy_ = []
bstack111l11l1_opy_ = bstack11l11l111_opy_
bstack1ll1lll1l1l_opy_ = bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᘎ")
bstack1ll1lll11l1_opy_ = False
bstack11lllllll_opy_ = {}
bstack1l1ll1l111_opy_ = False
logger = bstack1lll11l11l_opy_.get_logger(__name__, bstack111l11l1_opy_)
store = {
    bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᘏ"): []
}
bstack1ll1llll1l1_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11llllll11_opy_ = {}
current_test_uuid = None
def bstack1l1l1ll1_opy_(page, bstack11llll1l_opy_):
    try:
        page.evaluate(bstack11l11ll_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᘐ"),
                      bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫᘑ") + json.dumps(
                          bstack11llll1l_opy_) + bstack11l11ll_opy_ (u"ࠣࡿࢀࠦᘒ"))
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢᘓ"), e)
def bstack1llll11ll1_opy_(page, message, level):
    try:
        page.evaluate(bstack11l11ll_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᘔ"), bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩᘕ") + json.dumps(
            message) + bstack11l11ll_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨᘖ") + json.dumps(level) + bstack11l11ll_opy_ (u"࠭ࡽࡾࠩᘗ"))
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿࠥᘘ"), e)
def pytest_configure(config):
    bstack1ll1111l1_opy_ = Config.bstack11l11l11_opy_()
    config.args = bstack1l1l1111l_opy_.bstack1lll1l11l11_opy_(config.args)
    bstack1ll1111l1_opy_.bstack1ll11l11ll_opy_(bstack1lll1lll11_opy_(config.getoption(bstack11l11ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᘙ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1lll111ll11_opy_ = item.config.getoption(bstack11l11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᘚ"))
    plugins = item.config.getoption(bstack11l11ll_opy_ (u"ࠥࡴࡱࡻࡧࡪࡰࡶࠦᘛ"))
    report = outcome.get_result()
    bstack1lll111ll1l_opy_(item, call, report)
    if bstack11l11ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠤᘜ") not in plugins or bstack1111l11l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack11l11ll_opy_ (u"ࠧࡥࡤࡳ࡫ࡹࡩࡷࠨᘝ"), None)
    page = getattr(item, bstack11l11ll_opy_ (u"ࠨ࡟ࡱࡣࡪࡩࠧᘞ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1lll1111ll1_opy_(item, report, summary, bstack1lll111ll11_opy_)
    if (page is not None):
        bstack1ll1lllll11_opy_(item, report, summary, bstack1lll111ll11_opy_)
def bstack1lll1111ll1_opy_(item, report, summary, bstack1lll111ll11_opy_):
    if report.when == bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᘟ") and report.skipped:
        bstack1llll1l111l_opy_(report)
    if report.when in [bstack11l11ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᘠ"), bstack11l11ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᘡ")]:
        return
    if not bstack11l11111ll_opy_():
        return
    try:
        if (str(bstack1lll111ll11_opy_).lower() != bstack11l11ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᘢ")):
            item._driver.execute_script(
                bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩᘣ") + json.dumps(
                    report.nodeid) + bstack11l11ll_opy_ (u"ࠬࢃࡽࠨᘤ"))
        os.environ[bstack11l11ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᘥ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11l11ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢᘦ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᘧ")))
    bstack1lllll11_opy_ = bstack11l11ll_opy_ (u"ࠤࠥᘨ")
    bstack1llll1l111l_opy_(report)
    if not passed:
        try:
            bstack1lllll11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11l11ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥᘩ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1lllll11_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᘪ")))
        bstack1lllll11_opy_ = bstack11l11ll_opy_ (u"ࠧࠨᘫ")
        if not passed:
            try:
                bstack1lllll11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l11ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᘬ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1lllll11_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫᘭ")
                    + json.dumps(bstack11l11ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤᘮ"))
                    + bstack11l11ll_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧᘯ")
                )
            else:
                item._driver.execute_script(
                    bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨᘰ")
                    + json.dumps(str(bstack1lllll11_opy_))
                    + bstack11l11ll_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᘱ")
                )
        except Exception as e:
            summary.append(bstack11l11ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥᘲ").format(e))
def bstack1ll1lllllll_opy_(test_name, error_message):
    try:
        bstack1lll111l111_opy_ = []
        bstack1l11l1l11l_opy_ = os.environ.get(bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᘳ"), bstack11l11ll_opy_ (u"ࠧ࠱ࠩᘴ"))
        bstack1l11lll1l_opy_ = {bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᘵ"): test_name, bstack11l11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᘶ"): error_message, bstack11l11ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᘷ"): bstack1l11l1l11l_opy_}
        bstack1ll1lllll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᘸ"))
        if os.path.exists(bstack1ll1lllll1l_opy_):
            with open(bstack1ll1lllll1l_opy_) as f:
                bstack1lll111l111_opy_ = json.load(f)
        bstack1lll111l111_opy_.append(bstack1l11lll1l_opy_)
        with open(bstack1ll1lllll1l_opy_, bstack11l11ll_opy_ (u"ࠬࡽࠧᘹ")) as f:
            json.dump(bstack1lll111l111_opy_, f)
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡨࡶࡸ࡯ࡳࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡨࡶࡷࡵࡲࡴ࠼ࠣࠫᘺ") + str(e))
def bstack1ll1lllll11_opy_(item, report, summary, bstack1lll111ll11_opy_):
    if report.when in [bstack11l11ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᘻ"), bstack11l11ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᘼ")]:
        return
    if (str(bstack1lll111ll11_opy_).lower() != bstack11l11ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᘽ")):
        bstack1l1l1ll1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᘾ")))
    bstack1lllll11_opy_ = bstack11l11ll_opy_ (u"ࠦࠧᘿ")
    bstack1llll1l111l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1lllll11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l11ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᙀ").format(e)
                )
        try:
            if passed:
                bstack1l1l1l111l_opy_(getattr(item, bstack11l11ll_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᙁ"), None), bstack11l11ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᙂ"))
            else:
                error_message = bstack11l11ll_opy_ (u"ࠨࠩᙃ")
                if bstack1lllll11_opy_:
                    bstack1llll11ll1_opy_(item._page, str(bstack1lllll11_opy_), bstack11l11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣᙄ"))
                    bstack1l1l1l111l_opy_(getattr(item, bstack11l11ll_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩᙅ"), None), bstack11l11ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᙆ"), str(bstack1lllll11_opy_))
                    error_message = str(bstack1lllll11_opy_)
                else:
                    bstack1l1l1l111l_opy_(getattr(item, bstack11l11ll_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᙇ"), None), bstack11l11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᙈ"))
                bstack1ll1lllllll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11l11ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼ࠲ࢀࠦᙉ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack11l11ll_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᙊ"), default=bstack11l11ll_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣᙋ"), help=bstack11l11ll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤᙌ"))
    parser.addoption(bstack11l11ll_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᙍ"), default=bstack11l11ll_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦᙎ"), help=bstack11l11ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧᙏ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11l11ll_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤᙐ"), action=bstack11l11ll_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢᙑ"), default=bstack11l11ll_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤᙒ"),
                         help=bstack11l11ll_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤᙓ"))
def bstack11lll11ll1_opy_(log):
    if not (log[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᙔ")] and log[bstack11l11ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᙕ")].strip()):
        return
    active = bstack11lll1l1ll_opy_()
    log = {
        bstack11l11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᙖ"): log[bstack11l11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᙗ")],
        bstack11l11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᙘ"): bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ࠫᙙ"),
        bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᙚ"): log[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᙛ")],
    }
    if active:
        if active[bstack11l11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᙜ")] == bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᙝ"):
            log[bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᙞ")] = active[bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᙟ")]
        elif active[bstack11l11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᙠ")] == bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࠨᙡ"):
            log[bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᙢ")] = active[bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᙣ")]
    bstack1l1l1111l_opy_.bstack1111llll1_opy_([log])
def bstack11lll1l1ll_opy_():
    if len(store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᙤ")]) > 0 and store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᙥ")][-1]:
        return {
            bstack11l11ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᙦ"): bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᙧ"),
            bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᙨ"): store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᙩ")][-1]
        }
    if store.get(bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᙪ"), None):
        return {
            bstack11l11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᙫ"): bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࠬᙬ"),
            bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᙭"): store[bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᙮")]
        }
    return None
bstack11lll1l111_opy_ = bstack11llll1l11_opy_(bstack11lll11ll1_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1ll1lll11l1_opy_
        item._1ll1lll1ll1_opy_ = True
        bstack1ll111l1l1_opy_ = bstack1l1l111ll_opy_.bstack1l1111ll1_opy_(CONFIG, bstack111l11ll11_opy_(item.own_markers))
        item._a11y_test_case = bstack1ll111l1l1_opy_
        if bstack1ll1lll11l1_opy_:
            driver = getattr(item, bstack11l11ll_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᙯ"), None)
            item._a11y_started = bstack1l1l111ll_opy_.bstack1llll1ll1l_opy_(driver, bstack1ll111l1l1_opy_)
        if not bstack1l1l1111l_opy_.on() or bstack1ll1lll1l1l_opy_ != bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᙰ"):
            return
        global current_test_uuid, bstack11lll1l111_opy_
        bstack11lll1l111_opy_.start()
        bstack11llll1111_opy_ = {
            bstack11l11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᙱ"): uuid4().__str__(),
            bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᙲ"): bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"࡛ࠧࠩᙳ")
        }
        current_test_uuid = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᙴ")]
        store[bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᙵ")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᙶ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11llllll11_opy_[item.nodeid] = {**_11llllll11_opy_[item.nodeid], **bstack11llll1111_opy_}
        bstack1ll1lll11ll_opy_(item, _11llllll11_opy_[item.nodeid], bstack11l11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᙷ"))
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧᙸ"), str(err))
def pytest_runtest_setup(item):
    global bstack1ll1llll1l1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111ll11111_opy_():
        atexit.register(bstack11l11ll11_opy_)
        if not bstack1ll1llll1l1_opy_:
            try:
                bstack1lll1111lll_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111l1lll1l_opy_():
                    bstack1lll1111lll_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1111lll_opy_:
                    signal.signal(s, bstack1lll11l11l1_opy_)
                bstack1ll1llll1l1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11l11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨ࡫࡮ࡹࡴࡦࡴࠣࡷ࡮࡭࡮ࡢ࡮ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࡷ࠿ࠦࠢᙹ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1llll1lll11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11l11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᙺ")
    try:
        if not bstack1l1l1111l_opy_.on():
            return
        bstack11lll1l111_opy_.start()
        uuid = uuid4().__str__()
        bstack11llll1111_opy_ = {
            bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᙻ"): uuid,
            bstack11l11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᙼ"): bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠪ࡞ࠬᙽ"),
            bstack11l11ll_opy_ (u"ࠫࡹࡿࡰࡦࠩᙾ"): bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᙿ"),
            bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ "): bstack11l11ll_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᚁ"),
            bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫᚂ"): bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᚃ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᚄ")] = item
        store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᚅ")] = [uuid]
        if not _11llllll11_opy_.get(item.nodeid, None):
            _11llllll11_opy_[item.nodeid] = {bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᚆ"): [], bstack11l11ll_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᚇ"): []}
        _11llllll11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᚈ")].append(bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚉ")])
        _11llllll11_opy_[item.nodeid + bstack11l11ll_opy_ (u"ࠩ࠰ࡷࡪࡺࡵࡱࠩᚊ")] = bstack11llll1111_opy_
        bstack1ll1lll1lll_opy_(item, bstack11llll1111_opy_, bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᚋ"))
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧᚌ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack11lllllll_opy_
        if CONFIG.get(bstack11l11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᚍ"), False):
            if CONFIG.get(bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᚎ"), bstack11l11ll_opy_ (u"ࠢࡢࡷࡷࡳࠧᚏ")) == bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᚐ"):
                bstack1ll1llll11l_opy_ = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᚑ"), None)
                bstack1111l111l_opy_ = bstack1ll1llll11l_opy_ + bstack11l11ll_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᚒ")
                driver = getattr(item, bstack11l11ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᚓ"), None)
                PercySDK.screenshot(driver, bstack1111l111l_opy_)
        if getattr(item, bstack11l11ll_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺࡡࡳࡶࡨࡨࠬᚔ"), False):
            bstack1llllllll1_opy_.bstack1l111l11l_opy_(getattr(item, bstack11l11ll_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᚕ"), None), bstack11lllllll_opy_, logger, item)
        if not bstack1l1l1111l_opy_.on():
            return
        bstack11llll1111_opy_ = {
            bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᚖ"): uuid4().__str__(),
            bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᚗ"): bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ࠫᚘ"),
            bstack11l11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨᚙ"): bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᚚ"),
            bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ᚛"): bstack11l11ll_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ᚜"),
            bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪ᚝"): bstack11l11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ᚞")
        }
        _11llllll11_opy_[item.nodeid + bstack11l11ll_opy_ (u"ࠩ࠰ࡸࡪࡧࡲࡥࡱࡺࡲࠬ᚟")] = bstack11llll1111_opy_
        bstack1ll1lll1lll_opy_(item, bstack11llll1111_opy_, bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᚠ"))
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡀࠠࡼࡿࠪᚡ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1l1l1111l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1llll1ll111_opy_(fixturedef.argname):
        store[bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥ࡭ࡰࡦࡸࡰࡪࡥࡩࡵࡧࡰࠫᚢ")] = request.node
    elif bstack1llll1l1l11_opy_(fixturedef.argname):
        store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫᚣ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᚤ"): fixturedef.argname,
            bstack11l11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᚥ"): bstack111lll111l_opy_(outcome),
            bstack11l11ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫᚦ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᚧ")]
        if not _11llllll11_opy_.get(current_test_item.nodeid, None):
            _11llllll11_opy_[current_test_item.nodeid] = {bstack11l11ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᚨ"): []}
        _11llllll11_opy_[current_test_item.nodeid][bstack11l11ll_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᚩ")].append(fixture)
    except Exception as err:
        logger.debug(bstack11l11ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩᚪ"), str(err))
if bstack1111l11l1_opy_() and bstack1l1l1111l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11llllll11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᚫ")].bstack1lll1lll1ll_opy_(id(step))
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱ࠼ࠣࡿࢂ࠭ᚬ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11llllll11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᚭ")].bstack11lllll111_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧᚮ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l111l1lll_opy_: bstack11lll11l11_opy_ = _11llllll11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᚯ")]
            bstack1l111l1lll_opy_.bstack11lllll111_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᚰ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1ll1lll1l1l_opy_
        try:
            if not bstack1l1l1111l_opy_.on() or bstack1ll1lll1l1l_opy_ != bstack11l11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᚱ"):
                return
            global bstack11lll1l111_opy_
            bstack11lll1l111_opy_.start()
            driver = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ᚲ"), None)
            if not _11llllll11_opy_.get(request.node.nodeid, None):
                _11llllll11_opy_[request.node.nodeid] = {}
            bstack1l111l1lll_opy_ = bstack11lll11l11_opy_.bstack1lll1l1ll11_opy_(
                scenario, feature, request.node,
                name=bstack1llll1l1l1l_opy_(request.node, scenario),
                bstack1l1111l11l_opy_=bstack1l1ll111l_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11l11ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪᚳ"),
                tags=bstack1llll1ll11l_opy_(feature, scenario),
                bstack1l1111lll1_opy_=bstack1l1l1111l_opy_.bstack11llll1lll_opy_(driver) if driver and driver.session_id else {}
            )
            _11llllll11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᚴ")] = bstack1l111l1lll_opy_
            bstack1lll111l11l_opy_(bstack1l111l1lll_opy_.uuid)
            bstack1l1l1111l_opy_.bstack11lll1l1l1_opy_(bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᚵ"), bstack1l111l1lll_opy_)
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭ᚶ"), str(err))
def bstack1lll111lll1_opy_(bstack1lll111l1l1_opy_):
    if bstack1lll111l1l1_opy_ in store[bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᚷ")]:
        store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᚸ")].remove(bstack1lll111l1l1_opy_)
def bstack1lll111l11l_opy_(bstack1lll111l1ll_opy_):
    store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᚹ")] = bstack1lll111l1ll_opy_
    threading.current_thread().current_test_uuid = bstack1lll111l1ll_opy_
@bstack1l1l1111l_opy_.bstack1lll1l11lll_opy_
def bstack1lll111ll1l_opy_(item, call, report):
    global bstack1ll1lll1l1l_opy_
    bstack11l1l11l1_opy_ = bstack1l1ll111l_opy_()
    if hasattr(report, bstack11l11ll_opy_ (u"ࠨࡵࡷࡳࡵ࠭ᚺ")):
        bstack11l1l11l1_opy_ = bstack111l1l111l_opy_(report.stop)
    elif hasattr(report, bstack11l11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࠨᚻ")):
        bstack11l1l11l1_opy_ = bstack111l1l111l_opy_(report.start)
    try:
        if getattr(report, bstack11l11ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᚼ"), bstack11l11ll_opy_ (u"ࠫࠬᚽ")) == bstack11l11ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᚾ"):
            bstack11lll1l111_opy_.reset()
        if getattr(report, bstack11l11ll_opy_ (u"࠭ࡷࡩࡧࡱࠫᚿ"), bstack11l11ll_opy_ (u"ࠧࠨᛀ")) == bstack11l11ll_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᛁ"):
            if bstack1ll1lll1l1l_opy_ == bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᛂ"):
                _11llllll11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᛃ")] = bstack11l1l11l1_opy_
                bstack1ll1lll11ll_opy_(item, _11llllll11_opy_[item.nodeid], bstack11l11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᛄ"), report, call)
                store[bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᛅ")] = None
            elif bstack1ll1lll1l1l_opy_ == bstack11l11ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᛆ"):
                bstack1l111l1lll_opy_ = _11llllll11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᛇ")]
                bstack1l111l1lll_opy_.set(hooks=_11llllll11_opy_[item.nodeid].get(bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᛈ"), []))
                exception, bstack11lll111ll_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11lll111ll_opy_ = [call.excinfo.exconly(), getattr(report, bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠨᛉ"), bstack11l11ll_opy_ (u"ࠪࠫᛊ"))]
                bstack1l111l1lll_opy_.stop(time=bstack11l1l11l1_opy_, result=Result(result=getattr(report, bstack11l11ll_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬᛋ"), bstack11l11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᛌ")), exception=exception, bstack11lll111ll_opy_=bstack11lll111ll_opy_))
                bstack1l1l1111l_opy_.bstack11lll1l1l1_opy_(bstack11l11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᛍ"), _11llllll11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᛎ")])
        elif getattr(report, bstack11l11ll_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᛏ"), bstack11l11ll_opy_ (u"ࠩࠪᛐ")) in [bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᛑ"), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᛒ")]:
            bstack1l111llll1_opy_ = item.nodeid + bstack11l11ll_opy_ (u"ࠬ࠳ࠧᛓ") + getattr(report, bstack11l11ll_opy_ (u"࠭ࡷࡩࡧࡱࠫᛔ"), bstack11l11ll_opy_ (u"ࠧࠨᛕ"))
            if getattr(report, bstack11l11ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᛖ"), False):
                hook_type = bstack11l11ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᛗ") if getattr(report, bstack11l11ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᛘ"), bstack11l11ll_opy_ (u"ࠫࠬᛙ")) == bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᛚ") else bstack11l11ll_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᛛ")
                _11llllll11_opy_[bstack1l111llll1_opy_] = {
                    bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᛜ"): uuid4().__str__(),
                    bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᛝ"): bstack11l1l11l1_opy_,
                    bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᛞ"): hook_type
                }
            _11llllll11_opy_[bstack1l111llll1_opy_][bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᛟ")] = bstack11l1l11l1_opy_
            bstack1lll111lll1_opy_(_11llllll11_opy_[bstack1l111llll1_opy_][bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᛠ")])
            bstack1ll1lll1lll_opy_(item, _11llllll11_opy_[bstack1l111llll1_opy_], bstack11l11ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᛡ"), report, call)
            if getattr(report, bstack11l11ll_opy_ (u"࠭ࡷࡩࡧࡱࠫᛢ"), bstack11l11ll_opy_ (u"ࠧࠨᛣ")) == bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᛤ"):
                if getattr(report, bstack11l11ll_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪᛥ"), bstack11l11ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᛦ")) == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᛧ"):
                    bstack11llll1111_opy_ = {
                        bstack11l11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᛨ"): uuid4().__str__(),
                        bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᛩ"): bstack1l1ll111l_opy_(),
                        bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᛪ"): bstack1l1ll111l_opy_()
                    }
                    _11llllll11_opy_[item.nodeid] = {**_11llllll11_opy_[item.nodeid], **bstack11llll1111_opy_}
                    bstack1ll1lll11ll_opy_(item, _11llllll11_opy_[item.nodeid], bstack11l11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ᛫"))
                    bstack1ll1lll11ll_opy_(item, _11llllll11_opy_[item.nodeid], bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ᛬"), report, call)
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࢁࡽࠨ᛭"), str(err))
def bstack1lll111111l_opy_(test, bstack11llll1111_opy_, result=None, call=None, bstack1ll1l1ll1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l111l1lll_opy_ = {
        bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᛮ"): bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᛯ")],
        bstack11l11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᛰ"): bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࠬᛱ"),
        bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᛲ"): test.name,
        bstack11l11ll_opy_ (u"ࠩࡥࡳࡩࡿࠧᛳ"): {
            bstack11l11ll_opy_ (u"ࠪࡰࡦࡴࡧࠨᛴ"): bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫᛵ"),
            bstack11l11ll_opy_ (u"ࠬࡩ࡯ࡥࡧࠪᛶ"): inspect.getsource(test.obj)
        },
        bstack11l11ll_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᛷ"): test.name,
        bstack11l11ll_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭ᛸ"): test.name,
        bstack11l11ll_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ᛹"): bstack1l1l1111l_opy_.bstack1l111ll1l1_opy_(test),
        bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ᛺"): file_path,
        bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬ᛻"): file_path,
        bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ᛼"): bstack11l11ll_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭᛽"),
        bstack11l11ll_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫ᛾"): file_path,
        bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ᛿"): bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᜀ")],
        bstack11l11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᜁ"): bstack11l11ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᜂ"),
        bstack11l11ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧᜃ"): {
            bstack11l11ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩᜄ"): test.nodeid
        },
        bstack11l11ll_opy_ (u"࠭ࡴࡢࡩࡶࠫᜅ"): bstack111l11ll11_opy_(test.own_markers)
    }
    if bstack1ll1l1ll1_opy_ in [bstack11l11ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨᜆ"), bstack11l11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᜇ")]:
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠩࡰࡩࡹࡧࠧᜈ")] = {
            bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬᜉ"): bstack11llll1111_opy_.get(bstack11l11ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᜊ"), [])
        }
    if bstack1ll1l1ll1_opy_ == bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ᜋ"):
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᜌ")] = bstack11l11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᜍ")
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᜎ")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᜏ")]
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᜐ")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᜑ")]
    if result:
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᜒ")] = result.outcome
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᜓ")] = result.duration * 1000
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸ᜔ࠬ")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ᜕࠭")]
        if result.failed:
            bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ᜖")] = bstack1l1l1111l_opy_.bstack11ll11ll1l_opy_(call.excinfo.typename)
            bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ᜗")] = bstack1l1l1111l_opy_.bstack1lll11ll11l_opy_(call.excinfo, result)
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ᜘")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ᜙")]
    if outcome:
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᜚")] = bstack111lll111l_opy_(outcome)
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ᜛")] = 0
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭᜜")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᜝")]
        if bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᜞")] == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᜟ"):
            bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᜠ")] = bstack11l11ll_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧᜡ")  # bstack1ll1llll1ll_opy_
            bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᜢ")] = [{bstack11l11ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᜣ"): [bstack11l11ll_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭ᜤ")]}]
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᜥ")] = bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᜦ")]
    return bstack1l111l1lll_opy_
def bstack1lll1111l11_opy_(test, bstack11llll1l1l_opy_, bstack1ll1l1ll1_opy_, result, call, outcome, bstack1ll1llll111_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᜧ")]
    hook_name = bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᜨ")]
    hook_data = {
        bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᜩ"): bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᜪ")],
        bstack11l11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᜫ"): bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᜬ"),
        bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᜭ"): bstack11l11ll_opy_ (u"ࠬࢁࡽࠨᜮ").format(bstack1llll1l1ll1_opy_(hook_name)),
        bstack11l11ll_opy_ (u"࠭ࡢࡰࡦࡼࠫᜯ"): {
            bstack11l11ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬᜰ"): bstack11l11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨᜱ"),
            bstack11l11ll_opy_ (u"ࠩࡦࡳࡩ࡫ࠧᜲ"): None
        },
        bstack11l11ll_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩᜳ"): test.name,
        bstack11l11ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶ᜴ࠫ"): bstack1l1l1111l_opy_.bstack1l111ll1l1_opy_(test, hook_name),
        bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ᜵"): file_path,
        bstack11l11ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨ᜶"): file_path,
        bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ᜷"): bstack11l11ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ᜸"),
        bstack11l11ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ᜹"): file_path,
        bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ᜺"): bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ᜻")],
        bstack11l11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ᜼"): bstack11l11ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ᜽") if bstack1ll1lll1l1l_opy_ == bstack11l11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ᜾") else bstack11l11ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ᜿"),
        bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᝀ"): hook_type
    }
    bstack1lll11111l1_opy_ = bstack1l111l1111_opy_(_11llllll11_opy_.get(test.nodeid, None))
    if bstack1lll11111l1_opy_:
        hook_data[bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨᝁ")] = bstack1lll11111l1_opy_
    if result:
        hook_data[bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᝂ")] = result.outcome
        hook_data[bstack11l11ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᝃ")] = result.duration * 1000
        hook_data[bstack11l11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᝄ")] = bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᝅ")]
        if result.failed:
            hook_data[bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧᝆ")] = bstack1l1l1111l_opy_.bstack11ll11ll1l_opy_(call.excinfo.typename)
            hook_data[bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᝇ")] = bstack1l1l1111l_opy_.bstack1lll11ll11l_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11l11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᝈ")] = bstack111lll111l_opy_(outcome)
        hook_data[bstack11l11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᝉ")] = 100
        hook_data[bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᝊ")] = bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᝋ")]
        if hook_data[bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᝌ")] == bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝍ"):
            hook_data[bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᝎ")] = bstack11l11ll_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫᝏ")  # bstack1ll1llll1ll_opy_
            hook_data[bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᝐ")] = [{bstack11l11ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᝑ"): [bstack11l11ll_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪᝒ")]}]
    if bstack1ll1llll111_opy_:
        hook_data[bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᝓ")] = bstack1ll1llll111_opy_.result
        hook_data[bstack11l11ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ᝔")] = bstack111llll11l_opy_(bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᝕")], bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ᝖")])
        hook_data[bstack11l11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ᝗")] = bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᝘")]
        if hook_data[bstack11l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᝙")] == bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᝚"):
            hook_data[bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ᝛")] = bstack1l1l1111l_opy_.bstack11ll11ll1l_opy_(bstack1ll1llll111_opy_.exception_type)
            hook_data[bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ᝜")] = [{bstack11l11ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭᝝"): bstack111l11lll1_opy_(bstack1ll1llll111_opy_.exception)}]
    return hook_data
def bstack1ll1lll11ll_opy_(test, bstack11llll1111_opy_, bstack1ll1l1ll1_opy_, result=None, call=None, outcome=None):
    bstack1l111l1lll_opy_ = bstack1lll111111l_opy_(test, bstack11llll1111_opy_, result, call, bstack1ll1l1ll1_opy_, outcome)
    driver = getattr(test, bstack11l11ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ᝞"), None)
    if bstack1ll1l1ll1_opy_ == bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭᝟") and driver:
        bstack1l111l1lll_opy_[bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬᝠ")] = bstack1l1l1111l_opy_.bstack11llll1lll_opy_(driver)
    if bstack1ll1l1ll1_opy_ == bstack11l11ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨᝡ"):
        bstack1ll1l1ll1_opy_ = bstack11l11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᝢ")
    bstack11llll111l_opy_ = {
        bstack11l11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᝣ"): bstack1ll1l1ll1_opy_,
        bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬᝤ"): bstack1l111l1lll_opy_
    }
    bstack1l1l1111l_opy_.bstack1l1111111l_opy_(bstack11llll111l_opy_)
def bstack1ll1lll1lll_opy_(test, bstack11llll1111_opy_, bstack1ll1l1ll1_opy_, result=None, call=None, outcome=None, bstack1ll1llll111_opy_=None):
    hook_data = bstack1lll1111l11_opy_(test, bstack11llll1111_opy_, bstack1ll1l1ll1_opy_, result, call, outcome, bstack1ll1llll111_opy_)
    bstack11llll111l_opy_ = {
        bstack11l11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᝥ"): bstack1ll1l1ll1_opy_,
        bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧᝦ"): hook_data
    }
    bstack1l1l1111l_opy_.bstack1l1111111l_opy_(bstack11llll111l_opy_)
def bstack1l111l1111_opy_(bstack11llll1111_opy_):
    if not bstack11llll1111_opy_:
        return None
    if bstack11llll1111_opy_.get(bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᝧ"), None):
        return getattr(bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᝨ")], bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᝩ"), None)
    return bstack11llll1111_opy_.get(bstack11l11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᝪ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1l1l1111l_opy_.on():
            return
        places = [bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᝫ"), bstack11l11ll_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᝬ"), bstack11l11ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ᝭")]
        bstack1l11111l1l_opy_ = []
        for bstack1lll11l1111_opy_ in places:
            records = caplog.get_records(bstack1lll11l1111_opy_)
            bstack1lll1111l1l_opy_ = bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᝮ") if bstack1lll11l1111_opy_ == bstack11l11ll_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᝯ") else bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᝰ")
            bstack1lll1111111_opy_ = request.node.nodeid + (bstack11l11ll_opy_ (u"ࠩࠪ᝱") if bstack1lll11l1111_opy_ == bstack11l11ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᝲ") else bstack11l11ll_opy_ (u"ࠫ࠲࠭ᝳ") + bstack1lll11l1111_opy_)
            bstack1lll111l1ll_opy_ = bstack1l111l1111_opy_(_11llllll11_opy_.get(bstack1lll1111111_opy_, None))
            if not bstack1lll111l1ll_opy_:
                continue
            for record in records:
                if bstack111l1ll11l_opy_(record.message):
                    continue
                bstack1l11111l1l_opy_.append({
                    bstack11l11ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ᝴"): bstack111ll1111l_opy_(record.created).isoformat() + bstack11l11ll_opy_ (u"࡚࠭ࠨ᝵"),
                    bstack11l11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭᝶"): record.levelname,
                    bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᝷"): record.message,
                    bstack1lll1111l1l_opy_: bstack1lll111l1ll_opy_
                })
        if len(bstack1l11111l1l_opy_) > 0:
            bstack1l1l1111l_opy_.bstack1111llll1_opy_(bstack1l11111l1l_opy_)
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡧࡴࡴࡤࡠࡨ࡬ࡼࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭᝸"), str(err))
def bstack1l1l1l1ll_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l1ll1l111_opy_
    bstack11l1l1ll1_opy_ = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ᝹"), None) and bstack11l11lll1_opy_(
            threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᝺"), None)
    bstack1l1l11ll1_opy_ = getattr(driver, bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ᝻"), None) != None and getattr(driver, bstack11l11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭᝼"), None) == True
    if sequence == bstack11l11ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧ᝽") and driver != None:
      if not bstack1l1ll1l111_opy_ and bstack11l11111ll_opy_() and bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᝾") in CONFIG and CONFIG[bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᝿")] == True and bstack1l1l1l1lll_opy_.bstack11l1l1l1_opy_(driver_command) and (bstack1l1l11ll1_opy_ or bstack11l1l1ll1_opy_) and not bstack1ll1lllll_opy_(args):
        try:
          bstack1l1ll1l111_opy_ = True
          logger.debug(bstack11l11ll_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬក").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11l11ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩខ").format(str(err)))
        bstack1l1ll1l111_opy_ = False
    if sequence == bstack11l11ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫគ"):
        if driver_command == bstack11l11ll_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪឃ"):
            bstack1l1l1111l_opy_.bstack111l1111l_opy_({
                bstack11l11ll_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ង"): response[bstack11l11ll_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧច")],
                bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩឆ"): store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧជ")]
            })
def bstack11l11ll11_opy_():
    global bstack1l111111_opy_
    bstack1lll11l11l_opy_.bstack1ll11l1ll1_opy_()
    logging.shutdown()
    bstack1l1l1111l_opy_.bstack11lll1lll1_opy_()
    for driver in bstack1l111111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll11l11l1_opy_(*args):
    global bstack1l111111_opy_
    bstack1l1l1111l_opy_.bstack11lll1lll1_opy_()
    for driver in bstack1l111111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1l1ll11_opy_(self, *args, **kwargs):
    bstack111111ll_opy_ = bstack111ll11l_opy_(self, *args, **kwargs)
    bstack1l1l1111l_opy_.bstack111111l11_opy_(self)
    return bstack111111ll_opy_
def bstack1l1l1lll1_opy_(framework_name):
    global bstack111l1l111_opy_
    global bstack11lll1l1l_opy_
    bstack111l1l111_opy_ = framework_name
    logger.info(bstack1l1l11ll_opy_.format(bstack111l1l111_opy_.split(bstack11l11ll_opy_ (u"ࠫ࠲࠭ឈ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack11l11111ll_opy_():
            Service.start = bstack11l111ll1_opy_
            Service.stop = bstack1111lll1l_opy_
            webdriver.Remote.__init__ = bstack1l1ll1l1l1_opy_
            webdriver.Remote.get = bstack1ll11lllll_opy_
            if not isinstance(os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ញ")), str):
                return
            WebDriver.close = bstack1l1lllll11_opy_
            WebDriver.quit = bstack111lll11l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack11l11111ll_opy_() and bstack1l1l1111l_opy_.on():
            webdriver.Remote.__init__ = bstack1l1l1ll11_opy_
        bstack11lll1l1l_opy_ = True
    except Exception as e:
        pass
    bstack111lll1l_opy_()
    if os.environ.get(bstack11l11ll_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫដ")):
        bstack11lll1l1l_opy_ = eval(os.environ.get(bstack11l11ll_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬឋ")))
    if not bstack11lll1l1l_opy_:
        bstack1ll11l11l1_opy_(bstack11l11ll_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥឌ"), bstack11ll11111_opy_)
    if bstack1l1l1l11l1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1l1lll1l_opy_
        except Exception as e:
            logger.error(bstack1l1l11ll11_opy_.format(str(e)))
    if bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩឍ") in str(framework_name).lower():
        if not bstack11l11111ll_opy_():
            return
        try:
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
def bstack111lll11l_opy_(self):
    global bstack111l1l111_opy_
    global bstack1ll1ll1l_opy_
    global bstack11l111ll_opy_
    try:
        if bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪណ") in bstack111l1l111_opy_ and self.session_id != None and bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨត"), bstack11l11ll_opy_ (u"ࠬ࠭ថ")) != bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧទ"):
            bstack1lll11lll_opy_ = bstack11l11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧធ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨន")
            bstack1l1l111l11_opy_(logger, True)
            if self != None:
                bstack11ll1lll1_opy_(self, bstack1lll11lll_opy_, bstack11l11ll_opy_ (u"ࠩ࠯ࠤࠬប").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧផ"), None)
        if item is not None and bstack1ll1lll11l1_opy_:
            bstack1llllllll1_opy_.bstack1l111l11l_opy_(self, bstack11lllllll_opy_, logger, item)
        threading.current_thread().testStatus = bstack11l11ll_opy_ (u"ࠫࠬព")
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨភ") + str(e))
    bstack11l111ll_opy_(self)
    self.session_id = None
def bstack1l1ll1l1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1ll1ll1l_opy_
    global bstack1l1ll111_opy_
    global bstack111ll1lll_opy_
    global bstack111l1l111_opy_
    global bstack111ll11l_opy_
    global bstack1l111111_opy_
    global bstack1l11ll11_opy_
    global bstack1llll1l11_opy_
    global bstack1ll1lll11l1_opy_
    global bstack11lllllll_opy_
    CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨម")] = str(bstack111l1l111_opy_) + str(__version__)
    command_executor = bstack1lll1ll1l_opy_(bstack1l11ll11_opy_)
    logger.debug(bstack1llll11lll_opy_.format(command_executor))
    proxy = bstack1ll1ll1l1l_opy_(CONFIG, proxy)
    bstack1l11l1l11l_opy_ = 0
    try:
        if bstack111ll1lll_opy_ is True:
            bstack1l11l1l11l_opy_ = int(os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧយ")))
    except:
        bstack1l11l1l11l_opy_ = 0
    bstack11lll1111_opy_ = bstack1l1llll11_opy_(CONFIG, bstack1l11l1l11l_opy_)
    logger.debug(bstack11lll1l11_opy_.format(str(bstack11lll1111_opy_)))
    bstack11lllllll_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫរ"))[bstack1l11l1l11l_opy_]
    if bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ល") in CONFIG and CONFIG[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧវ")]:
        bstack1llll111ll_opy_(bstack11lll1111_opy_, bstack1llll1l11_opy_)
    if bstack1l1l111ll_opy_.bstack1ll1l1ll1l_opy_(CONFIG, bstack1l11l1l11l_opy_) and bstack1l1l111ll_opy_.bstack1ll11111_opy_(bstack11lll1111_opy_, options):
        bstack1ll1lll11l1_opy_ = True
        bstack1l1l111ll_opy_.set_capabilities(bstack11lll1111_opy_, CONFIG)
    if desired_capabilities:
        bstack1l111l11_opy_ = bstack11l1l11ll_opy_(desired_capabilities)
        bstack1l111l11_opy_[bstack11l11ll_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫឝ")] = bstack11llllll_opy_(CONFIG)
        bstack1lll1ll1_opy_ = bstack1l1llll11_opy_(bstack1l111l11_opy_)
        if bstack1lll1ll1_opy_:
            bstack11lll1111_opy_ = update(bstack1lll1ll1_opy_, bstack11lll1111_opy_)
        desired_capabilities = None
    if options:
        bstack1llll11ll_opy_(options, bstack11lll1111_opy_)
    if not options:
        options = bstack1l11ll1l1_opy_(bstack11lll1111_opy_)
    if proxy and bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬឞ")):
        options.proxy(proxy)
    if options and bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬស")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l1l1l11ll_opy_() < version.parse(bstack11l11ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ហ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11lll1111_opy_)
    logger.info(bstack1ll1l1ll11_opy_)
    if bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨឡ")):
        bstack111ll11l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨអ")):
        bstack111ll11l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪឣ")):
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
        bstack1l1111ll_opy_ = bstack11l11ll_opy_ (u"ࠫࠬឤ")
        if bstack1l1l1l11ll_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭ឥ")):
            bstack1l1111ll_opy_ = self.caps.get(bstack11l11ll_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨឦ"))
        else:
            bstack1l1111ll_opy_ = self.capabilities.get(bstack11l11ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢឧ"))
        if bstack1l1111ll_opy_:
            bstack1l1l1llll_opy_(bstack1l1111ll_opy_)
            if bstack1l1l1l11ll_opy_() <= version.parse(bstack11l11ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨឨ")):
                self.command_executor._url = bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥឩ") + bstack1l11ll11_opy_ + bstack11l11ll_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢឪ")
            else:
                self.command_executor._url = bstack11l11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨឫ") + bstack1l1111ll_opy_ + bstack11l11ll_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨឬ")
            logger.debug(bstack11l11lll_opy_.format(bstack1l1111ll_opy_))
        else:
            logger.debug(bstack1l1l11l111_opy_.format(bstack11l11ll_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢឭ")))
    except Exception as e:
        logger.debug(bstack1l1l11l111_opy_.format(e))
    bstack1ll1ll1l_opy_ = self.session_id
    if bstack11l11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧឮ") in bstack111l1l111_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬឯ"), None)
        if item:
            bstack1lll11l11ll_opy_ = getattr(item, bstack11l11ll_opy_ (u"ࠩࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪࡥࡳࡵࡣࡵࡸࡪࡪࠧឰ"), False)
            if not getattr(item, bstack11l11ll_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫឱ"), None) and bstack1lll11l11ll_opy_:
                setattr(store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨឲ")], bstack11l11ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ឳ"), self)
        bstack1l1l1111l_opy_.bstack111111l11_opy_(self)
    bstack1l111111_opy_.append(self)
    if bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ឴") in CONFIG and bstack11l11ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ឵") in CONFIG[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫា")][bstack1l11l1l11l_opy_]:
        bstack1l1ll111_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬិ")][bstack1l11l1l11l_opy_][bstack11l11ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨី")]
    logger.debug(bstack11l11llll_opy_.format(bstack1ll1ll1l_opy_))
def bstack1ll11lllll_opy_(self, url):
    global bstack1lll1l1l_opy_
    global CONFIG
    try:
        bstack11lllll1l_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l1l1ll1ll_opy_.format(str(err)))
    try:
        bstack1lll1l1l_opy_(self, url)
    except Exception as e:
        try:
            bstack1l1lll1ll_opy_ = str(e)
            if any(err_msg in bstack1l1lll1ll_opy_ for err_msg in bstack1l11l1111_opy_):
                bstack11lllll1l_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l1l1ll1ll_opy_.format(str(err)))
        raise e
def bstack1l1l11lll_opy_(item, when):
    global bstack1l11l1l111_opy_
    try:
        bstack1l11l1l111_opy_(item, when)
    except Exception as e:
        pass
def bstack1l11ll1lll_opy_(item, call, rep):
    global bstack1ll1l1l11_opy_
    global bstack1l111111_opy_
    name = bstack11l11ll_opy_ (u"ࠫࠬឹ")
    try:
        if rep.when == bstack11l11ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪឺ"):
            bstack1ll1ll1l_opy_ = threading.current_thread().bstackSessionId
            bstack1lll111ll11_opy_ = item.config.getoption(bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨុ"))
            try:
                if (str(bstack1lll111ll11_opy_).lower() != bstack11l11ll_opy_ (u"ࠧࡵࡴࡸࡩࠬូ")):
                    name = str(rep.nodeid)
                    bstack1l1lll11l_opy_ = bstack1ll111ll1_opy_(bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩួ"), name, bstack11l11ll_opy_ (u"ࠩࠪើ"), bstack11l11ll_opy_ (u"ࠪࠫឿ"), bstack11l11ll_opy_ (u"ࠫࠬៀ"), bstack11l11ll_opy_ (u"ࠬ࠭េ"))
                    os.environ[bstack11l11ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩែ")] = name
                    for driver in bstack1l111111_opy_:
                        if bstack1ll1ll1l_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1lll11l_opy_)
            except Exception as e:
                logger.debug(bstack11l11ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧៃ").format(str(e)))
            try:
                bstack1l1l1lll11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11l11ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩោ"):
                    status = bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩៅ") if rep.outcome.lower() == bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪំ") else bstack11l11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫះ")
                    reason = bstack11l11ll_opy_ (u"ࠬ࠭ៈ")
                    if status == bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭៉"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11l11ll_opy_ (u"ࠧࡪࡰࡩࡳࠬ៊") if status == bstack11l11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ់") else bstack11l11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ៌")
                    data = name + bstack11l11ll_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ៍") if status == bstack11l11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ៎") else name + bstack11l11ll_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨ៏") + reason
                    bstack111lll11_opy_ = bstack1ll111ll1_opy_(bstack11l11ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ័"), bstack11l11ll_opy_ (u"ࠧࠨ៑"), bstack11l11ll_opy_ (u"ࠨ្ࠩ"), bstack11l11ll_opy_ (u"ࠩࠪ៓"), level, data)
                    for driver in bstack1l111111_opy_:
                        if bstack1ll1ll1l_opy_ == driver.session_id:
                            driver.execute_script(bstack111lll11_opy_)
            except Exception as e:
                logger.debug(bstack11l11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ។").format(str(e)))
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ៕").format(str(e)))
    bstack1ll1l1l11_opy_(item, call, rep)
notset = Notset()
def bstack11l1l111l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11l11111l_opy_
    if str(name).lower() == bstack11l11ll_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬ៖"):
        return bstack11l11ll_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧៗ")
    else:
        return bstack11l11111l_opy_(self, name, default, skip)
def bstack1l1lll1l_opy_(self):
    global CONFIG
    global bstack1lll111l1l_opy_
    try:
        proxy = bstack1ll11ll111_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11l11ll_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ៘")):
                proxies = bstack111l1lll1_opy_(proxy, bstack1lll1ll1l_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll11ll1_opy_ = proxies.popitem()
                    if bstack11l11ll_opy_ (u"ࠣ࠼࠲࠳ࠧ៙") in bstack1ll11ll1_opy_:
                        return bstack1ll11ll1_opy_
                    else:
                        return bstack11l11ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ៚") + bstack1ll11ll1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11l11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ៛").format(str(e)))
    return bstack1lll111l1l_opy_(self)
def bstack1l1l1l11l1_opy_():
    return (bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧៜ") in CONFIG or bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ៝") in CONFIG) and bstack1ll11ll1l1_opy_() and bstack1l1l1l11ll_opy_() >= version.parse(
        bstack1lll1l1111_opy_)
def bstack11l1llll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l1ll111_opy_
    global bstack111ll1lll_opy_
    global bstack111l1l111_opy_
    CONFIG[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ៞")] = str(bstack111l1l111_opy_) + str(__version__)
    bstack1l11l1l11l_opy_ = 0
    try:
        if bstack111ll1lll_opy_ is True:
            bstack1l11l1l11l_opy_ = int(os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ៟")))
    except:
        bstack1l11l1l11l_opy_ = 0
    CONFIG[bstack11l11ll_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ០")] = True
    bstack11lll1111_opy_ = bstack1l1llll11_opy_(CONFIG, bstack1l11l1l11l_opy_)
    logger.debug(bstack11lll1l11_opy_.format(str(bstack11lll1111_opy_)))
    if CONFIG.get(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭១")):
        bstack1llll111ll_opy_(bstack11lll1111_opy_, bstack1llll1l11_opy_)
    if bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭២") in CONFIG and bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ៣") in CONFIG[bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ៤")][bstack1l11l1l11l_opy_]:
        bstack1l1ll111_opy_ = CONFIG[bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ៥")][bstack1l11l1l11l_opy_][bstack11l11ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ៦")]
    import urllib
    import json
    bstack1lll1ll1l1_opy_ = bstack11l11ll_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪ៧") + urllib.parse.quote(json.dumps(bstack11lll1111_opy_))
    browser = self.connect(bstack1lll1ll1l1_opy_)
    return browser
def bstack111lll1l_opy_():
    if not bstack11l11111ll_opy_():
        return
    global bstack11lll1l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack11l1llll_opy_
        bstack11lll1l1l_opy_ = True
    except Exception as e:
        pass
def bstack1ll1llllll1_opy_():
    global CONFIG
    global bstack1111ll11l_opy_
    global bstack1l11ll11_opy_
    global bstack1llll1l11_opy_
    global bstack111ll1lll_opy_
    global bstack111l11l1_opy_
    CONFIG = json.loads(os.environ.get(bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ៨")))
    bstack1111ll11l_opy_ = eval(os.environ.get(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ៩")))
    bstack1l11ll11_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ៪"))
    bstack1ll11ll1l_opy_(CONFIG, bstack1111ll11l_opy_)
    bstack111l11l1_opy_ = bstack1lll11l11l_opy_.bstack1l11l111_opy_(CONFIG, bstack111l11l1_opy_)
    global bstack111ll11l_opy_
    global bstack11l111ll_opy_
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
    except Exception as e:
        pass
    if (bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ៫") in CONFIG or bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ៬") in CONFIG) and bstack1ll11ll1l1_opy_():
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
        logger.debug(bstack11l11ll_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ៭"))
    bstack1llll1l11_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ៮"), {}).get(bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ៯"))
    bstack111ll1lll_opy_ = True
    bstack1l1l1lll1_opy_(bstack1ll1l1l1l1_opy_)
if (bstack111ll11111_opy_()):
    bstack1ll1llllll1_opy_()
@bstack11ll1lllll_opy_(class_method=False)
def bstack1lll11111ll_opy_(hook_name, event, bstack1lll11l1l11_opy_=None):
    if hook_name not in [bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫ៰"), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ៱"), bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫ៲"), bstack11l11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨ៳"), bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬ៴"), bstack11l11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩ៵"), bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨ៶"), bstack11l11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬ៷")]:
        return
    node = store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ៸")]
    if hook_name in [bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫ៹"), bstack11l11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨ៺")]:
        node = store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭៻")]
    elif hook_name in [bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭៼"), bstack11l11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ៽")]:
        node = store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨ៾")]
    if event == bstack11l11ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ៿"):
        hook_type = bstack1llll1l1lll_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11llll1l1l_opy_ = {
            bstack11l11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ᠀"): uuid,
            bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ᠁"): bstack1l1ll111l_opy_(),
            bstack11l11ll_opy_ (u"ࠧࡵࡻࡳࡩࠬ᠂"): bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰ࠭᠃"),
            bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ᠄"): hook_type,
            bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭᠅"): hook_name
        }
        store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ᠆")].append(uuid)
        bstack1ll1lll1l11_opy_ = node.nodeid
        if hook_type == bstack11l11ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪ᠇"):
            if not _11llllll11_opy_.get(bstack1ll1lll1l11_opy_, None):
                _11llllll11_opy_[bstack1ll1lll1l11_opy_] = {bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ᠈"): []}
            _11llllll11_opy_[bstack1ll1lll1l11_opy_][bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭᠉")].append(bstack11llll1l1l_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭᠊")])
        _11llllll11_opy_[bstack1ll1lll1l11_opy_ + bstack11l11ll_opy_ (u"ࠩ࠰ࠫ᠋") + hook_name] = bstack11llll1l1l_opy_
        bstack1ll1lll1lll_opy_(node, bstack11llll1l1l_opy_, bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ᠌"))
    elif event == bstack11l11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪ᠍"):
        bstack1l111llll1_opy_ = node.nodeid + bstack11l11ll_opy_ (u"ࠬ࠳ࠧ᠎") + hook_name
        _11llllll11_opy_[bstack1l111llll1_opy_][bstack11l11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᠏")] = bstack1l1ll111l_opy_()
        bstack1lll111lll1_opy_(_11llllll11_opy_[bstack1l111llll1_opy_][bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ᠐")])
        bstack1ll1lll1lll_opy_(node, _11llllll11_opy_[bstack1l111llll1_opy_], bstack11l11ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᠑"), bstack1ll1llll111_opy_=bstack1lll11l1l11_opy_)
def bstack1lll111llll_opy_():
    global bstack1ll1lll1l1l_opy_
    if bstack1111l11l1_opy_():
        bstack1ll1lll1l1l_opy_ = bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭᠒")
    else:
        bstack1ll1lll1l1l_opy_ = bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᠓")
@bstack1l1l1111l_opy_.bstack1lll1l11lll_opy_
def bstack1lll11l111l_opy_():
    bstack1lll111llll_opy_()
    if bstack1ll11ll1l1_opy_():
        bstack1l1l1111l1_opy_(bstack1l1l1l1ll_opy_)
    try:
        bstack111l111111_opy_(bstack1lll11111ll_opy_)
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡴࠢࡳࡥࡹࡩࡨ࠻ࠢࡾࢁࠧ᠔").format(e))
bstack1lll11l111l_opy_()
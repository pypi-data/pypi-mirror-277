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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11lll111l1_opy_ import RobotHandler
from bstack_utils.capture import bstack11llll1l11_opy_
from bstack_utils.bstack1l111l1lll_opy_ import bstack1l1111l1l1_opy_, bstack1l1111l1ll_opy_, bstack11lll11l11_opy_
from bstack_utils.bstack1l1lll1l1l_opy_ import bstack1l1l1111l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11l11lll1_opy_, bstack1l1ll111l_opy_, Result, \
    bstack11ll1lllll_opy_, bstack1l1111llll_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ൧"): [],
        bstack11l11ll_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨ൨"): [],
        bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹࠧ൩"): []
    }
    bstack1l111111l1_opy_ = []
    bstack1l111l111l_opy_ = []
    @staticmethod
    def bstack11lll11ll1_opy_(log):
        if not (log[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ൪")] and log[bstack11l11ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭൫")].strip()):
            return
        active = bstack1l1l1111l_opy_.bstack11lll1l1ll_opy_()
        log = {
            bstack11l11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ൬"): log[bstack11l11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭൭")],
            bstack11l11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ൮"): bstack1l1111llll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ࠫ൯"),
            bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ൰"): log[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ൱")],
        }
        if active:
            if active[bstack11l11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ൲")] == bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ൳"):
                log[bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ൴")] = active[bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ൵")]
            elif active[bstack11l11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ൶")] == bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࠨ൷"):
                log[bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ൸")] = active[bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ൹")]
        bstack1l1l1111l_opy_.bstack1111llll1_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._11lllllll1_opy_ = None
        self._1l111l1ll1_opy_ = None
        self._11llllll11_opy_ = OrderedDict()
        self.bstack11lll1l111_opy_ = bstack11llll1l11_opy_(self.bstack11lll11ll1_opy_)
    @bstack11ll1lllll_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11lllll11l_opy_()
        if not self._11llllll11_opy_.get(attrs.get(bstack11l11ll_opy_ (u"࠭ࡩࡥࠩൺ")), None):
            self._11llllll11_opy_[attrs.get(bstack11l11ll_opy_ (u"ࠧࡪࡦࠪൻ"))] = {}
        bstack1l11111l11_opy_ = bstack11lll11l11_opy_(
                bstack11lll11l1l_opy_=attrs.get(bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫർ")),
                name=name,
                bstack1l1111l11l_opy_=bstack1l1ll111l_opy_(),
                file_path=os.path.relpath(attrs[bstack11l11ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩൽ")], start=os.getcwd()) if attrs.get(bstack11l11ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪൾ")) != bstack11l11ll_opy_ (u"ࠫࠬൿ") else bstack11l11ll_opy_ (u"ࠬ࠭඀"),
                framework=bstack11l11ll_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬඁ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11l11ll_opy_ (u"ࠧࡪࡦࠪං"), None)
        self._11llllll11_opy_[attrs.get(bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫඃ"))][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ඄")] = bstack1l11111l11_opy_
    @bstack11ll1lllll_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack11lllll1ll_opy_()
        self._1l111l1l11_opy_(messages)
        for bstack1l111ll1ll_opy_ in self.bstack1l111111l1_opy_:
            bstack1l111ll1ll_opy_[bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬඅ")][bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪආ")].extend(self.store[bstack11l11ll_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫඇ")])
            bstack1l1l1111l_opy_.bstack1l1111111l_opy_(bstack1l111ll1ll_opy_)
        self.bstack1l111111l1_opy_ = []
        self.store[bstack11l11ll_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬඈ")] = []
    @bstack11ll1lllll_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11lll1l111_opy_.start()
        if not self._11llllll11_opy_.get(attrs.get(bstack11l11ll_opy_ (u"ࠧࡪࡦࠪඉ")), None):
            self._11llllll11_opy_[attrs.get(bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫඊ"))] = {}
        driver = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඋ"), None)
        bstack1l111l1lll_opy_ = bstack11lll11l11_opy_(
            bstack11lll11l1l_opy_=attrs.get(bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࠭ඌ")),
            name=name,
            bstack1l1111l11l_opy_=bstack1l1ll111l_opy_(),
            file_path=os.path.relpath(attrs[bstack11l11ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫඍ")], start=os.getcwd()),
            scope=RobotHandler.bstack1l111ll1l1_opy_(attrs.get(bstack11l11ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬඎ"), None)),
            framework=bstack11l11ll_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬඏ"),
            tags=attrs[bstack11l11ll_opy_ (u"ࠧࡵࡣࡪࡷࠬඐ")],
            hooks=self.store[bstack11l11ll_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧඑ")],
            bstack1l1111lll1_opy_=bstack1l1l1111l_opy_.bstack11llll1lll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11l11ll_opy_ (u"ࠤࡾࢁࠥࡢ࡮ࠡࡽࢀࠦඒ").format(bstack11l11ll_opy_ (u"ࠥࠤࠧඓ").join(attrs[bstack11l11ll_opy_ (u"ࠫࡹࡧࡧࡴࠩඔ")]), name) if attrs[bstack11l11ll_opy_ (u"ࠬࡺࡡࡨࡵࠪඕ")] else name
        )
        self._11llllll11_opy_[attrs.get(bstack11l11ll_opy_ (u"࠭ࡩࡥࠩඖ"))][bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ඗")] = bstack1l111l1lll_opy_
        threading.current_thread().current_test_uuid = bstack1l111l1lll_opy_.bstack11lll1l11l_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫ඘"), None)
        self.bstack11lll1l1l1_opy_(bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ඙"), bstack1l111l1lll_opy_)
    @bstack11ll1lllll_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11lll1l111_opy_.reset()
        bstack1l111ll111_opy_ = bstack1l1111ll11_opy_.get(attrs.get(bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪක")), bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬඛ"))
        self._11llllll11_opy_[attrs.get(bstack11l11ll_opy_ (u"ࠬ࡯ࡤࠨග"))][bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩඝ")].stop(time=bstack1l1ll111l_opy_(), duration=int(attrs.get(bstack11l11ll_opy_ (u"ࠧࡦ࡮ࡤࡴࡸ࡫ࡤࡵ࡫ࡰࡩࠬඞ"), bstack11l11ll_opy_ (u"ࠨ࠲ࠪඟ"))), result=Result(result=bstack1l111ll111_opy_, exception=attrs.get(bstack11l11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪච")), bstack11lll111ll_opy_=[attrs.get(bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫඡ"))]))
        self.bstack11lll1l1l1_opy_(bstack11l11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ජ"), self._11llllll11_opy_[attrs.get(bstack11l11ll_opy_ (u"ࠬ࡯ࡤࠨඣ"))][bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩඤ")], True)
        self.store[bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫඥ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11ll1lllll_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11lllll11l_opy_()
        current_test_id = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡦࠪඦ"), None)
        bstack1l111l1l1l_opy_ = current_test_id if bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫට"), None) else bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭ඨ"), None)
        if attrs.get(bstack11l11ll_opy_ (u"ࠫࡹࡿࡰࡦࠩඩ"), bstack11l11ll_opy_ (u"ࠬ࠭ඪ")).lower() in [bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬණ"), bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩඬ")]:
            hook_type = bstack11lll11111_opy_(attrs.get(bstack11l11ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭ත")), bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ථ"), None))
            hook_name = bstack11l11ll_opy_ (u"ࠪࡿࢂ࠭ද").format(attrs.get(bstack11l11ll_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫධ"), bstack11l11ll_opy_ (u"ࠬ࠭න")))
            if hook_type in [bstack11l11ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪ඲"), bstack11l11ll_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪඳ")]:
                hook_name = bstack11l11ll_opy_ (u"ࠨ࡝ࡾࢁࡢࠦࡻࡾࠩප").format(bstack11lllll1l1_opy_.get(hook_type), attrs.get(bstack11l11ll_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩඵ"), bstack11l11ll_opy_ (u"ࠪࠫබ")))
            bstack11llll1l1l_opy_ = bstack1l1111l1ll_opy_(
                bstack11lll11l1l_opy_=bstack1l111l1l1l_opy_ + bstack11l11ll_opy_ (u"ࠫ࠲࠭භ") + attrs.get(bstack11l11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪම"), bstack11l11ll_opy_ (u"࠭ࠧඹ")).lower(),
                name=hook_name,
                bstack1l1111l11l_opy_=bstack1l1ll111l_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11l11ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧය")), start=os.getcwd()),
                framework=bstack11l11ll_opy_ (u"ࠨࡔࡲࡦࡴࡺࠧර"),
                tags=attrs[bstack11l11ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ඼")],
                scope=RobotHandler.bstack1l111ll1l1_opy_(attrs.get(bstack11l11ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪල"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11llll1l1l_opy_.bstack11lll1l11l_opy_()
            threading.current_thread().current_hook_id = bstack1l111l1l1l_opy_ + bstack11l11ll_opy_ (u"ࠫ࠲࠭඾") + attrs.get(bstack11l11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ඿"), bstack11l11ll_opy_ (u"࠭ࠧව")).lower()
            self.store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫශ")] = [bstack11llll1l1l_opy_.bstack11lll1l11l_opy_()]
            if bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬෂ"), None):
                self.store[bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭ස")].append(bstack11llll1l1l_opy_.bstack11lll1l11l_opy_())
            else:
                self.store[bstack11l11ll_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴࠩහ")].append(bstack11llll1l1l_opy_.bstack11lll1l11l_opy_())
            if bstack1l111l1l1l_opy_:
                self._11llllll11_opy_[bstack1l111l1l1l_opy_ + bstack11l11ll_opy_ (u"ࠫ࠲࠭ළ") + attrs.get(bstack11l11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪෆ"), bstack11l11ll_opy_ (u"࠭ࠧ෇")).lower()] = { bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ෈"): bstack11llll1l1l_opy_ }
            bstack1l1l1111l_opy_.bstack11lll1l1l1_opy_(bstack11l11ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ෉"), bstack11llll1l1l_opy_)
        else:
            bstack1l111ll11l_opy_ = {
                bstack11l11ll_opy_ (u"ࠩ࡬ࡨ්ࠬ"): uuid4().__str__(),
                bstack11l11ll_opy_ (u"ࠪࡸࡪࡾࡴࠨ෋"): bstack11l11ll_opy_ (u"ࠫࢀࢃࠠࡼࡿࠪ෌").format(attrs.get(bstack11l11ll_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬ෍")), attrs.get(bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫ෎"), bstack11l11ll_opy_ (u"ࠧࠨා"))) if attrs.get(bstack11l11ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ැ"), []) else attrs.get(bstack11l11ll_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩෑ")),
                bstack11l11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡠࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠪි"): attrs.get(bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࡴࠩී"), []),
                bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩු"): bstack1l1ll111l_opy_(),
                bstack11l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭෕"): bstack11l11ll_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨූ"),
                bstack11l11ll_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭෗"): attrs.get(bstack11l11ll_opy_ (u"ࠩࡧࡳࡨ࠭ෘ"), bstack11l11ll_opy_ (u"ࠪࠫෙ"))
            }
            if attrs.get(bstack11l11ll_opy_ (u"ࠫࡱ࡯ࡢ࡯ࡣࡰࡩࠬේ"), bstack11l11ll_opy_ (u"ࠬ࠭ෛ")) != bstack11l11ll_opy_ (u"࠭ࠧො"):
                bstack1l111ll11l_opy_[bstack11l11ll_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨෝ")] = attrs.get(bstack11l11ll_opy_ (u"ࠨ࡮࡬ࡦࡳࡧ࡭ࡦࠩෞ"))
            if not self.bstack1l111l111l_opy_:
                self._11llllll11_opy_[self._11lll11lll_opy_()][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬෟ")].add_step(bstack1l111ll11l_opy_)
                threading.current_thread().current_step_uuid = bstack1l111ll11l_opy_[bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࠭෠")]
            self.bstack1l111l111l_opy_.append(bstack1l111ll11l_opy_)
    @bstack11ll1lllll_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack11lllll1ll_opy_()
        self._1l111l1l11_opy_(messages)
        current_test_id = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡩ࠭෡"), None)
        bstack1l111l1l1l_opy_ = current_test_id if current_test_id else bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡳࡶ࡫ࡷࡩࡤ࡯ࡤࠨ෢"), None)
        bstack11llll11l1_opy_ = bstack1l1111ll11_opy_.get(attrs.get(bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭෣")), bstack11l11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ෤"))
        bstack1l1111l111_opy_ = attrs.get(bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ෥"))
        if bstack11llll11l1_opy_ != bstack11l11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ෦") and not attrs.get(bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ෧")) and self._11lllllll1_opy_:
            bstack1l1111l111_opy_ = self._11lllllll1_opy_
        bstack1l111lll11_opy_ = Result(result=bstack11llll11l1_opy_, exception=bstack1l1111l111_opy_, bstack11lll111ll_opy_=[bstack1l1111l111_opy_])
        if attrs.get(bstack11l11ll_opy_ (u"ࠫࡹࡿࡰࡦࠩ෨"), bstack11l11ll_opy_ (u"ࠬ࠭෩")).lower() in [bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ෪"), bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ෫")]:
            bstack1l111l1l1l_opy_ = current_test_id if current_test_id else bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫ෬"), None)
            if bstack1l111l1l1l_opy_:
                bstack1l111llll1_opy_ = bstack1l111l1l1l_opy_ + bstack11l11ll_opy_ (u"ࠤ࠰ࠦ෭") + attrs.get(bstack11l11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ෮"), bstack11l11ll_opy_ (u"ࠫࠬ෯")).lower()
                self._11llllll11_opy_[bstack1l111llll1_opy_][bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ෰")].stop(time=bstack1l1ll111l_opy_(), duration=int(attrs.get(bstack11l11ll_opy_ (u"࠭ࡥ࡭ࡣࡳࡷࡪࡪࡴࡪ࡯ࡨࠫ෱"), bstack11l11ll_opy_ (u"ࠧ࠱ࠩෲ"))), result=bstack1l111lll11_opy_)
                bstack1l1l1111l_opy_.bstack11lll1l1l1_opy_(bstack11l11ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪෳ"), self._11llllll11_opy_[bstack1l111llll1_opy_][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ෴")])
        else:
            bstack1l111l1l1l_opy_ = current_test_id if current_test_id else bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡ࡬ࡨࠬ෵"), None)
            if bstack1l111l1l1l_opy_ and len(self.bstack1l111l111l_opy_) == 1:
                current_step_uuid = bstack11l11lll1_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡴࡦࡲࡢࡹࡺ࡯ࡤࠨ෶"), None)
                self._11llllll11_opy_[bstack1l111l1l1l_opy_][bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ෷")].bstack11lllll111_opy_(current_step_uuid, duration=int(attrs.get(bstack11l11ll_opy_ (u"࠭ࡥ࡭ࡣࡳࡷࡪࡪࡴࡪ࡯ࡨࠫ෸"), bstack11l11ll_opy_ (u"ࠧ࠱ࠩ෹"))), result=bstack1l111lll11_opy_)
            else:
                self.bstack11llll1ll1_opy_(attrs)
            self.bstack1l111l111l_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11l11ll_opy_ (u"ࠨࡪࡷࡱࡱ࠭෺"), bstack11l11ll_opy_ (u"ࠩࡱࡳࠬ෻")) == bstack11l11ll_opy_ (u"ࠪࡽࡪࡹࠧ෼"):
                return
            self.messages.push(message)
            bstack1l11111l1l_opy_ = []
            if bstack1l1l1111l_opy_.bstack11lll1l1ll_opy_():
                bstack1l11111l1l_opy_.append({
                    bstack11l11ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ෽"): bstack1l1ll111l_opy_(),
                    bstack11l11ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭෾"): message.get(bstack11l11ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ෿")),
                    bstack11l11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭฀"): message.get(bstack11l11ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧก")),
                    **bstack1l1l1111l_opy_.bstack11lll1l1ll_opy_()
                })
                if len(bstack1l11111l1l_opy_) > 0:
                    bstack1l1l1111l_opy_.bstack1111llll1_opy_(bstack1l11111l1l_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1l1l1111l_opy_.bstack11lll1lll1_opy_()
    def bstack11llll1ll1_opy_(self, bstack11lll1llll_opy_):
        if not bstack1l1l1111l_opy_.bstack11lll1l1ll_opy_():
            return
        kwname = bstack11l11ll_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨข").format(bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪฃ")), bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࡴࠩค"), bstack11l11ll_opy_ (u"ࠬ࠭ฅ"))) if bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫฆ"), []) else bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧง"))
        error_message = bstack11l11ll_opy_ (u"ࠣ࡭ࡺࡲࡦࡳࡥ࠻ࠢ࡟ࠦࢀ࠶ࡽ࡝ࠤࠣࢀࠥࡹࡴࡢࡶࡸࡷ࠿ࠦ࡜ࠣࡽ࠴ࢁࡡࠨࠠࡽࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦ࡜ࠣࡽ࠵ࢁࡡࠨࠢจ").format(kwname, bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩฉ")), str(bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫช"))))
        bstack11llllllll_opy_ = bstack11l11ll_opy_ (u"ࠦࡰࡽ࡮ࡢ࡯ࡨ࠾ࠥࡢࠢࡼ࠲ࢀࡠࠧࠦࡼࠡࡵࡷࡥࡹࡻࡳ࠻ࠢ࡟ࠦࢀ࠷ࡽ࡝ࠤࠥซ").format(kwname, bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬฌ")))
        bstack1l11111ll1_opy_ = error_message if bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧญ")) else bstack11llllllll_opy_
        bstack1l11111lll_opy_ = {
            bstack11l11ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪฎ"): self.bstack1l111l111l_opy_[-1].get(bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬฏ"), bstack1l1ll111l_opy_()),
            bstack11l11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪฐ"): bstack1l11111ll1_opy_,
            bstack11l11ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩฑ"): bstack11l11ll_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪฒ") if bstack11lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬณ")) == bstack11l11ll_opy_ (u"࠭ࡆࡂࡋࡏࠫด") else bstack11l11ll_opy_ (u"ࠧࡊࡐࡉࡓࠬต"),
            **bstack1l1l1111l_opy_.bstack11lll1l1ll_opy_()
        }
        bstack1l1l1111l_opy_.bstack1111llll1_opy_([bstack1l11111lll_opy_])
    def _11lll11lll_opy_(self):
        for bstack11lll11l1l_opy_ in reversed(self._11llllll11_opy_):
            bstack11lll1111l_opy_ = bstack11lll11l1l_opy_
            data = self._11llllll11_opy_[bstack11lll11l1l_opy_][bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫถ")]
            if isinstance(data, bstack1l1111l1ll_opy_):
                if not bstack11l11ll_opy_ (u"ࠩࡈࡅࡈࡎࠧท") in data.bstack1l111l11ll_opy_():
                    return bstack11lll1111l_opy_
            else:
                return bstack11lll1111l_opy_
    def _1l111l1l11_opy_(self, messages):
        try:
            bstack11llllll1l_opy_ = BuiltIn().get_variable_value(bstack11l11ll_opy_ (u"ࠥࠨࢀࡒࡏࡈࠢࡏࡉ࡛ࡋࡌࡾࠤธ")) in (bstack11ll1llll1_opy_.DEBUG, bstack11ll1llll1_opy_.TRACE)
            for message, bstack1l111111ll_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬน"))
                level = message.get(bstack11l11ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫบ"))
                if level == bstack11ll1llll1_opy_.FAIL:
                    self._11lllllll1_opy_ = name or self._11lllllll1_opy_
                    self._1l111l1ll1_opy_ = bstack1l111111ll_opy_.get(bstack11l11ll_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢป")) if bstack11llllll1l_opy_ and bstack1l111111ll_opy_ else self._1l111l1ll1_opy_
        except:
            pass
    @classmethod
    def bstack11lll1l1l1_opy_(self, event: str, bstack11llll11ll_opy_: bstack1l1111l1l1_opy_, bstack1l111l11l1_opy_=False):
        if event == bstack11l11ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩผ"):
            bstack11llll11ll_opy_.set(hooks=self.store[bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬฝ")])
        if event == bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪพ"):
            event = bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬฟ")
        if bstack1l111l11l1_opy_:
            bstack11llll111l_opy_ = {
                bstack11l11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨภ"): event,
                bstack11llll11ll_opy_.bstack1l1111ll1l_opy_(): bstack11llll11ll_opy_.bstack1l11111111_opy_(event)
            }
            self.bstack1l111111l1_opy_.append(bstack11llll111l_opy_)
        else:
            bstack1l1l1111l_opy_.bstack11lll1l1l1_opy_(event, bstack11llll11ll_opy_)
class Messages:
    def __init__(self):
        self._11lll1ll1l_opy_ = []
    def bstack11lllll11l_opy_(self):
        self._11lll1ll1l_opy_.append([])
    def bstack11lllll1ll_opy_(self):
        return self._11lll1ll1l_opy_.pop() if self._11lll1ll1l_opy_ else list()
    def push(self, message):
        self._11lll1ll1l_opy_[-1].append(message) if self._11lll1ll1l_opy_ else self._11lll1ll1l_opy_.append([message])
class bstack11ll1llll1_opy_:
    FAIL = bstack11l11ll_opy_ (u"ࠬࡌࡁࡊࡎࠪม")
    ERROR = bstack11l11ll_opy_ (u"࠭ࡅࡓࡔࡒࡖࠬย")
    WARNING = bstack11l11ll_opy_ (u"ࠧࡘࡃࡕࡒࠬร")
    bstack11lll1ll11_opy_ = bstack11l11ll_opy_ (u"ࠨࡋࡑࡊࡔ࠭ฤ")
    DEBUG = bstack11l11ll_opy_ (u"ࠩࡇࡉࡇ࡛ࡇࠨล")
    TRACE = bstack11l11ll_opy_ (u"ࠪࡘࡗࡇࡃࡆࠩฦ")
    bstack1l111lll1l_opy_ = [FAIL, ERROR]
def bstack1l111l1111_opy_(bstack11llll1111_opy_):
    if not bstack11llll1111_opy_:
        return None
    if bstack11llll1111_opy_.get(bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧว"), None):
        return getattr(bstack11llll1111_opy_[bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨศ")], bstack11l11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫษ"), None)
    return bstack11llll1111_opy_.get(bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬส"), None)
def bstack11lll11111_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧห"), bstack11l11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫฬ")]:
        return
    if hook_type.lower() == bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩอ"):
        if current_test_uuid is None:
            return bstack11l11ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨฮ")
        else:
            return bstack11l11ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪฯ")
    elif hook_type.lower() == bstack11l11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨะ"):
        if current_test_uuid is None:
            return bstack11l11ll_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪั")
        else:
            return bstack11l11ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬา")
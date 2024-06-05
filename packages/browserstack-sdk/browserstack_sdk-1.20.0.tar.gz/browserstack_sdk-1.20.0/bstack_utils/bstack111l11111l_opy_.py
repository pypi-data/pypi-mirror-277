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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l111l111_opy_
from browserstack_sdk.bstack11ll111l1_opy_ import bstack1llllllll1_opy_
def _111l1111ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111l111111_opy_:
    def __init__(self, handler):
        self._111l1111l1_opy_ = {}
        self._111l111l1l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1llllllll1_opy_.version()
        if bstack11l111l111_opy_(pytest_version, bstack11l11ll_opy_ (u"ࠢ࠹࠰࠴࠲࠶ࠨፎ")) >= 0:
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫፏ")] = Module._register_setup_function_fixture
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪፐ")] = Module._register_setup_module_fixture
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪፑ")] = Class._register_setup_class_fixture
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬፒ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨፓ"))
            Module._register_setup_module_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧፔ"))
            Class._register_setup_class_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧፕ"))
            Class._register_setup_method_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩፖ"))
        else:
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬፗ")] = Module._inject_setup_function_fixture
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫፘ")] = Module._inject_setup_module_fixture
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫፙ")] = Class._inject_setup_class_fixture
            self._111l1111l1_opy_[bstack11l11ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ፚ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ፛"))
            Module._inject_setup_module_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ፜"))
            Class._inject_setup_class_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ፝"))
            Class._inject_setup_method_fixture = self.bstack111l111lll_opy_(bstack11l11ll_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ፞"))
    def bstack1111llllll_opy_(self, bstack111l111l11_opy_, hook_type):
        meth = getattr(bstack111l111l11_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111l111l1l_opy_[hook_type] = meth
            setattr(bstack111l111l11_opy_, hook_type, self.bstack1111llll1l_opy_(hook_type))
    def bstack111l111ll1_opy_(self, instance, bstack1111llll11_opy_):
        if bstack1111llll11_opy_ == bstack11l11ll_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨ፟"):
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧ፠"))
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤ፡"))
        if bstack1111llll11_opy_ == bstack11l11ll_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢ።"):
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨ፣"))
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥ፤"))
        if bstack1111llll11_opy_ == bstack11l11ll_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤ፥"):
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣ፦"))
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧ፧"))
        if bstack1111llll11_opy_ == bstack11l11ll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨ፨"):
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧ፩"))
            self.bstack1111llllll_opy_(instance.obj, bstack11l11ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤ፪"))
    @staticmethod
    def bstack111l11l111_opy_(hook_type, func, args):
        if hook_type in [bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ፫"), bstack11l11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫ፬")]:
            _111l1111ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1111llll1l_opy_(self, hook_type):
        def bstack111l11l1l1_opy_(arg=None):
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ፭"))
            result = None
            exception = None
            try:
                self.bstack111l11l111_opy_(hook_type, self._111l111l1l_opy_[hook_type], (arg,))
                result = Result(result=bstack11l11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ፮"))
            except Exception as e:
                result = Result(result=bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ፯"), exception=e)
                self.handler(hook_type, bstack11l11ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ፰"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭፱"), result)
        def bstack111l11l11l_opy_(this, arg=None):
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ፲"))
            result = None
            exception = None
            try:
                self.bstack111l11l111_opy_(hook_type, self._111l111l1l_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ፳"))
            except Exception as e:
                result = Result(result=bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ፴"), exception=e)
                self.handler(hook_type, bstack11l11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪ፵"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l11ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ፶"), result)
        if hook_type in [bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬ፷"), bstack11l11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ፸")]:
            return bstack111l11l11l_opy_
        return bstack111l11l1l1_opy_
    def bstack111l111lll_opy_(self, bstack1111llll11_opy_):
        def bstack1111lllll1_opy_(this, *args, **kwargs):
            self.bstack111l111ll1_opy_(this, bstack1111llll11_opy_)
            self._111l1111l1_opy_[bstack1111llll11_opy_](this, *args, **kwargs)
        return bstack1111lllll1_opy_
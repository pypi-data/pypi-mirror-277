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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1111l1l11l_opy_
def bstack1lllll11111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1lllll1111l_opy_(bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1lllll11l1l_opy_):
        with open(bstack1lllll11l1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1lllll11111_opy_(bstack1lllll11l1l_opy_):
        pac = get_pac(url=bstack1lllll11l1l_opy_)
    else:
        raise Exception(bstack11l11ll_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬᑖ").format(bstack1lllll11l1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l11ll_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢᑗ"), 80))
        bstack1lllll111ll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1lllll111ll_opy_ = bstack11l11ll_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨᑘ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1llll1lllll_opy_, bstack1lllll111ll_opy_)
    return proxy_url
def bstack11111lll1_opy_(config):
    return bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᑙ") in config or bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᑚ") in config
def bstack1ll11ll111_opy_(config):
    if not bstack11111lll1_opy_(config):
        return
    if config.get(bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᑛ")):
        return config.get(bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᑜ"))
    if config.get(bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᑝ")):
        return config.get(bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᑞ"))
def bstack1ll11llll_opy_(config, bstack1llll1lllll_opy_):
    proxy = bstack1ll11ll111_opy_(config)
    proxies = {}
    if config.get(bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᑟ")) or config.get(bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᑠ")):
        if proxy.endswith(bstack11l11ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧᑡ")):
            proxies = bstack111l1lll1_opy_(proxy, bstack1llll1lllll_opy_)
        else:
            proxies = {
                bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᑢ"): proxy
            }
    return proxies
def bstack111l1lll1_opy_(bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_):
    proxies = {}
    global bstack1lllll11l11_opy_
    if bstack11l11ll_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧᑣ") in globals():
        return bstack1lllll11l11_opy_
    try:
        proxy = bstack1lllll1111l_opy_(bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_)
        if bstack11l11ll_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧᑤ") in proxy:
            proxies = {}
        elif bstack11l11ll_opy_ (u"ࠨࡈࡕࡖࡓࠦᑥ") in proxy or bstack11l11ll_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨᑦ") in proxy or bstack11l11ll_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢᑧ") in proxy:
            bstack1lllll111l1_opy_ = proxy.split(bstack11l11ll_opy_ (u"ࠤࠣࠦᑨ"))
            if bstack11l11ll_opy_ (u"ࠥ࠾࠴࠵ࠢᑩ") in bstack11l11ll_opy_ (u"ࠦࠧᑪ").join(bstack1lllll111l1_opy_[1:]):
                proxies = {
                    bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᑫ"): bstack11l11ll_opy_ (u"ࠨࠢᑬ").join(bstack1lllll111l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᑭ"): str(bstack1lllll111l1_opy_[0]).lower() + bstack11l11ll_opy_ (u"ࠣ࠼࠲࠳ࠧᑮ") + bstack11l11ll_opy_ (u"ࠤࠥᑯ").join(bstack1lllll111l1_opy_[1:])
                }
        elif bstack11l11ll_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤᑰ") in proxy:
            bstack1lllll111l1_opy_ = proxy.split(bstack11l11ll_opy_ (u"ࠦࠥࠨᑱ"))
            if bstack11l11ll_opy_ (u"ࠧࡀ࠯࠰ࠤᑲ") in bstack11l11ll_opy_ (u"ࠨࠢᑳ").join(bstack1lllll111l1_opy_[1:]):
                proxies = {
                    bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᑴ"): bstack11l11ll_opy_ (u"ࠣࠤᑵ").join(bstack1lllll111l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᑶ"): bstack11l11ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᑷ") + bstack11l11ll_opy_ (u"ࠦࠧᑸ").join(bstack1lllll111l1_opy_[1:])
                }
        else:
            proxies = {
                bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᑹ"): proxy
            }
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᑺ"), bstack1111l1l11l_opy_.format(bstack1lllll11l1l_opy_, str(e)))
    bstack1lllll11l11_opy_ = proxies
    return proxies
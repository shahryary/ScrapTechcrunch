from scrapy.contrib.loader.processor import MapCompose, Identity
from scrapy.contrib.loader import XPathItemLoader

from scraphse.items import ScraphseItem


class RootItemLoader(XPathItemLoader):
    default_input_processor = Identity()
    default_ouput_processor = Identity()


class TCLoader(RootItemLoader):
    default_item_class = ScraphseItem
    headLine_in = MapCompose(unicode.strip)

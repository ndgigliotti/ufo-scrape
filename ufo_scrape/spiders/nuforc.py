import re

import pandas as pd
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ufo_scrape.utils import snake_case


class NuforcSpider(CrawlSpider):
    name = "nuforc"
    allowed_domains = ["nuforc.org"]
    start_urls = ["https://nuforc.org/webreports/ndxevent.html"]

    rules = [
        Rule(
            LinkExtractor(
                restrict_css="table tr td a",
                allow="/webreports/ndxe",
                canonicalize=True,
            ),
            callback="parse",
        ),
    ]

    def parse(self, response):
        df = pd.read_html(response.text)[0]
        df.columns = df.columns.map(snake_case)
        match = re.search(r"ndxe(\d{4})(\d{2})\.html", response.request.url)
        if match is not None:
            year, month = match.groups()
        else:
            year, month = "yyyy", "mm"
        df["url"] = response.request.url
        df["year_month"] = f"{year}-{month}"
        yield from df.to_dict(orient="records")

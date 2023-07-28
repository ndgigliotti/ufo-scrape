from scrapy.spiders import SitemapSpider
import re
import pandas as pd
from ufo_scrape.utils import snake_case


class NuforcSpider(SitemapSpider):
    name = "nuforc"
    allowed_domains = ["nuforc.org"]
    sitemap_urls = ["https://nuforc.org/sitemap_index.xml"]
    sitemap_rules = [(r"webreports/ndxe\d{6}\.html", "parse")]

    def parse(self, response):
        df = pd.read_html(response.text)[0]
        df.columns = df.columns.map(snake_case)
        match = re.search(r"ndxe(\d{4})(\d{2})\.html", response.request.url)
        year, month = match.groups()
        df["url"] = response.request.url
        df["year_month"] = f"{year}-{month}"
        yield from df.to_dict(orient="records")

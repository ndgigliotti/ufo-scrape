# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
import json
import re

import numpy as np
import pandas as pd


class IdGenerator:
    def process_item(self, item, spider):
        # Generate ID based on hash of item
        if spider.name == "nuforc":
            hashable = json.dumps(item, sort_keys=True).encode("utf-8")
            item["id"] = hashlib.shake_256(hashable).hexdigest(8)
        return item


class NullConverter:
    terms = {
        r"\bnull\b",
        r"\bnone\b",
        r"\bnan\b",
        r"\bn[\/\.\-]?a\b",
        r"\bnat\b",
        r"\bnot\s+applicable\b",
        r"\bnot\s+available\b",
        r"\bnot\s+known\b",
        r"\bnot\s+reported\b",
        r"\bunknown\b",
        r"\bunreported\b",
        r"\bunk\b",
        r"\bmissing\b",
        r"\bno\s+data\b",
        r"\bempty\b",
        r"\bblank\b",
        r"\?+",
        r"\s+",
    }
    null_term = re.compile("|".join(terms), flags=re.I)

    def process_item(self, item, spider):
        # Convert different null types and terms to None
        if spider.name == "nuforc":
            for key, value in item.items():
                if value in {np.nan, pd.NA, pd.NaT, None}:
                    item[key] = None
                elif isinstance(value, str) and self.null_term.fullmatch(value):
                    item[key] = None
        return item

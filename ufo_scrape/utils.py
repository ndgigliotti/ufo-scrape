import re

def uri_params(params, spider):
    """Returns URI parameters as dict."""
    return {**params, "spider_name": spider.name}

def snake_case(text):
    """Converts text to snake case."""
    tokens = re.findall(r"\b\w+\b", text.lower())
    return "_".join(tokens)
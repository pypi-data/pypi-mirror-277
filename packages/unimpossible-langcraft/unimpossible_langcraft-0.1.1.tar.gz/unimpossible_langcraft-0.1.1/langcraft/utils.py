import re
from typing import List


def extract_tag(tag: str, data: str) -> List[str]:
    """
    Extracts all string contents enclosed in any set of pairs of XML tags in the given string.

    Parameters:
    tag (str): The XML tag to search for.
    data (str): The string containing the XML data.

    Returns:
    List[str]: The extracted string contents enclosed in the XML tags.
    """
    return [
        m.strip(" \n\t") for m in re.findall(rf"<{tag}>(.*?)</{tag}>", data, re.DOTALL)
    ]

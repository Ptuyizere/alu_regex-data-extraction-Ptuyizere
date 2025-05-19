#!/usr/bin/env python3

import re

# Sample input: This would be replaced with the actual API

text = """
Call (123) 456-7890 or 123-456-7890 for support.
Credit cards such as 1234 5678 9012 3456 or 1234-5678-9012-3456 are not allowed.
We meet at 14:30 or 2:30 PM.
Prices stand are as follows $19.99 or $1,234.56.
"""

# Regular expressions petterns

patterns = {
    "Phone Numbers": r"(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}",
    "Credit Cards": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "Time (12/24hr)": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

# Fetch and display results

for name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"\n{name}:")
    for match in matches:
        print(f"  - {match}")

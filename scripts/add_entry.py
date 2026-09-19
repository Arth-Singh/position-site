"""Append a signature or an accepted alternative view from a GitHub issue form to the site's JSON files.

Signatures are added when the issue carries the "signature" label. Alternative views are added only when a
maintainer adds the "accepted" label, so views are moderated and signatures are not.
"""
import json
import os
import re

event = json.loads(os.environ["EVENT"])
issue = event["issue"]
labels = {l["name"] for l in issue.get("labels", [])}
body = issue.get("body") or ""


def field(label):
    """Value of a form field rendered as '### Label\\n\\nvalue'."""
    m = re.search(r"### " + re.escape(label) + r"\s*\n+(.*?)(?=\n### |\Z)", body, re.S)
    if not m:
        return ""
    value = m.group(1).strip()
    return "" if value == "_No response_" else value


def load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save(path, rows):
    with open(path, "w") as f:
        json.dump(rows, f, indent=1, ensure_ascii=False)
        f.write("\n")


number = issue["number"]

if "signature" in labels:
    rows = load("signatories.json")
    if not any(r.get("issue") == number for r in rows):
        rows.append({
            "issue": number,
            "name": field("Name"),
            "affiliation": field("Affiliation"),
            "sector": field("Where you work"),
            "why": field("One line on why (optional)"),
            "date": issue["created_at"][:10],
        })
        save("signatories.json", rows)

if "accepted" in labels and "alternative-view" in labels:
    rows = load("views.json")
    if not any(r.get("issue") == number for r in rows):
        rows.append({
            "issue": number,
            "name": field("Name"),
            "affiliation": field("Affiliation"),
            "view": field("Your view"),
            "date": issue["created_at"][:10],
        })
        save("views.json", rows)

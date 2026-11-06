"""Check the static site's HTML and local asset paths without dependencies."""

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent / "site"


def check_reference(source, reference):
    url = urlsplit(reference)
    if url.scheme or url.netloc or not url.path:
        return
    assert not url.path.startswith("/"), f"Use a relative URL in {source}: {reference}"
    target = (source.parent / unquote(url.path)).resolve()
    assert target.is_relative_to(ROOT), f"Asset outside site: {reference}"
    assert target.exists(), f"Missing asset in {source}: {reference}"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.anchors = set()
        self.headings = 0
        self.language = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "h1":
            self.headings += 1
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "img":
            assert "alt" in attrs, "Image missing alt text"
        for name in ("src", "href"):
            if name in attrs:
                check_reference(ROOT / "index.html", attrs[name])
                if attrs[name].startswith("#"):
                    self.anchors.add(attrs[name][1:])


page = Page()
page.feed((ROOT / "index.html").read_text())
assert page.language == "de", "Declare the German page language"
assert page.headings == 1, "Use exactly one h1"
assert page.anchors <= page.ids, "Broken in-page link"
for css in ROOT.rglob("*.css"):
    for reference in re.findall(r'url\([\'"]?([^\)\'"\s]+)[\'"]?\)', css.read_text()):
        check_reference(css, reference)
print("Static site check passed: HTML, anchors, images, and CSS assets.")

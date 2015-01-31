#!/usr/bin/python

"""Takes the TOC, this time the raw HTML, and produces an ebook xhtml TOC with
rewritten local links.

We're producing this directly from the html so that we can keep the extra
multi-level chapter structure without parsing the entire thing into some
hierarchical tree.
"""

from bs4 import BeautifulSoup
import common

from string import Template

import pkg_resources

toc_template = Template(
    pkg_resources.resource_string(__name__, "toc_template.xhtml"))

if __name__== "__main__":
    soup = BeautifulSoup(open(
        "web_cache/edgeofyourseat.dreamwidth.org/2121.html"))

    the_toc_html = soup.select(".entry-content")[0]

    # Remove the "how to read" link.
    the_toc_html.find_all("center")[0].extract()

    # As for the others, parse them & replace them with the appropriate internal
    # links.

    common.replace_links_with_internal(the_toc_html)

    toc_string = the_toc_html.decode_contents(formatter="html")
    toc_html_string = toc_template.substitute(toc_entries=toc_string)

    with open("global_lists/toc.xhtml", mode="w") as f:
        f.write(toc_html_string.encode('utf-8'))


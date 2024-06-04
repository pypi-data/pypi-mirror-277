# This program is public domain
# Author: Paul Kienzle
r"""
Allow $math$ markup in text and docstrings, ignoring \$.

The $math$ markup should be separated from the surrounding text by spaces.  To
embed markup within a word, place backslash-space before and after.  For
convenience, the final $ can be followed by punctuation (period, comma or
semicolon).
"""

import re


_dollar = re.compile(
    r"(?:^|(?<=\s))[$]([^\n]*?)(?<![\\])[$](?:$|(?=\s|[.,;\\]))"
)
_notdollar = re.compile(r"\\[$]")


def replace_dollar(content):
    # original = content
    content = _dollar.sub(r":math:`\1`", content)
    content = _notdollar.sub("$", content)
    # if '$' in content:
    #    import sys
    #    sys.stdout.write("\n========> not converted\n")
    #    sys.stdout.write(content)
    #    sys.stdout.write("\n")
    # elif '$' in original:
    #    import sys
    #    sys.stdout.write("\n========> converted\n")
    #    sys.stdout.write(content)
    #    sys.stdout.write("\n")
    return content


def rewrite_rst(app, docname, source):
    # We specifically must not transform *.ipynb files, because this interacts
    # badly with the npsphinx plugin, producing broken math. We thus restrict
    # ourselfs to *.rst files (which include the autogenrated API)
    if app.env.doc2path(docname).endswith('rst'):
        source[0] = replace_dollar(source[0])


def rewrite_autodoc(app, what, name, obj, options, lines):
    lines[:] = [replace_dollar(L) for L in lines]


def setup(app):
    app.connect('source-read', rewrite_rst)
    app.connect('autodoc-process-docstring', rewrite_autodoc)


def test_dollar():
    """Test dollarmath plugin"""
    assert replace_dollar(r"no dollar") == r"no dollar"
    assert replace_dollar(r"$only$") == r":math:`only`"
    assert replace_dollar(r"$first$ is good") == r":math:`first` is good"
    assert replace_dollar(r"so is $last$") == r"so is :math:`last`"
    assert replace_dollar(r"and $mid$ too") == r"and :math:`mid` too"
    assert (
        replace_dollar(r"$first$, $mid$, $last$")
        == r":math:`first`, :math:`mid`, :math:`last`"
    )
    assert replace_dollar(r"dollar\$ escape") == r"dollar$ escape"
    assert replace_dollar(r"dollar \$escape\$ too") == r"dollar $escape$ too"
    assert replace_dollar(r"emb\ $ed$\ ed") == r"emb\ :math:`ed`\ ed"
    assert replace_dollar(r"$first$a") == r"$first$a"
    assert replace_dollar(r"a$last$") == r"a$last$"
    assert replace_dollar(r"a $mid$dle a") == r"a $mid$dle a"
    print("OK")


if __name__ == "__main__":
    test_dollar()

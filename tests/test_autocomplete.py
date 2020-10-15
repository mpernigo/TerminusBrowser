# test_autocomplete.py

import sys

from custom_urwid_classes import CommandBar
# from commandChanVim import urwidView
from terminus_browser import urwidView
from autocomplete import autoComplete

import pytest

test_list = [
    ('too long command', 'too long command'),
    ('thr', 'thread'), # input len 3
    ('po', 'post'), # input len 2
    ('re', 'remove'), # 2 cmds start with re
    ('subreddit', 'sub'), # toggle check
    ('qsuaik', 'qsuaik') # gibberish
]

@pytest.mark.parametrize("test_input, expected", test_list)
def test_CommandBar(test_input, expected):
    uvm = urwidView(True)
    cb = CommandBar(lambda: uvm._update_focus(True), uvm)
    cb.set_edit_text(test_input)
    autoComplete(cb)
    assert cb.get_edit_text() == expected

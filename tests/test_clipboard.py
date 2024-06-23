# tests/test_core.py

import pytest
from workbench.clipboard import Clipboard

def test_copy_and_paste():
    wb = Clipboard()
    test_text = "Hello, Workbench!"
    
    wb.copy(test_text)
    assert wb.paste() == test_text

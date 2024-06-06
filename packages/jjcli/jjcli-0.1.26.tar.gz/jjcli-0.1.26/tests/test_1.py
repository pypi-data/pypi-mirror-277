import pytest
import jjcli

cl = jjcli.clfilter()

def test_1():
    a = jjcli.qx("python3 tests/test-multipleopt.py -a -c arg1 -d arg2 -d arg3")
    opt = eval(a)
    assert opt["-a"]  == ""
    assert "-a" in opt
    assert "-b" not in opt
    assert opt["-c"]  == "arg1"
    assert len(opt["-d"])  == 2
    assert opt["-d"][1]  == "arg3"

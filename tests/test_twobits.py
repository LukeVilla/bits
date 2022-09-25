import sys
import pytest
# def setup_bits():
#     sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
#     import bits
def test_twobits():
    # setup_bits()
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.bits == [0,1]
def test_twobits_and():
    # setup_bits()
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.andGate() == 0
def test_twobits_or():
    # setup_bits()
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.orGate() == 1
def test_twobits_not():
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.notGate() == [1,0]
def test_twobits_nand():
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.nandGate() == 1
def test_twobits_nor():
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.norGate() == 0
def test_twobits_xor():
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.xorGate() == 1
def test_twobits_xnor():
    sys.path.insert(0,"c:\\Users\\lukev\\OneDrive\\Documents\\Python\\bits")
    import bits
    zero_one = bits.TwoBits(0,1)
    assert zero_one.xnorGate() == 0

:::::::::::
Bits Readme
:::::::::::

Description
"""""""""""
Bits is a Python library to simulate bits.

How To Use
""""""""""

TwoBits
'''''''
A ``TwoBits`` object is created with the following syntax:
``TwoBits(*bit 1*,*bit 2*)``
Its only attribute is ``bits``, which is a list of the two bits that the object stores.
Its methods all operate on the two bits, so they take no arguments.
The ``notGate()`` method flips the two bits.

RandomBits
''''''''''
A ``RandomBits`` object is created with the following syntax:
``RandomBits(*number of bits*)``
Its methods are passed a list of bits, the same length as the ``RandomBits`` instance.
They return another list of bits created by doing the operation on each pair of bits.
The ``notGate()`` method takes no arguments. It just flips each of the bits.

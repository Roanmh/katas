import unittest
def chop(num, arr):
    """"""
    # import pdb
    # pdb.set_trace()
    pivot = len(arr) // 2

    try:
        if not len(arr):
            raise RuntimeError("Not in arr.")

        if num == arr[pivot]:
            return pivot
        elif num > arr[pivot]:
            return chop(num, arr[:pivot]) + pivot
        else:
            return chop(num, arr[pivot+1:])
    except RuntimeError:
        return -1

class test_chop(unittest.TestCase):
    def test_chop(self):
        self.assertEquals(-1, chop(3, []))
        self.assertEquals(-1, chop(3, [1]))
        self.assertEquals(0,  chop(1, [1]))
        self.assertEquals(1,  chop(3, [1, 3, 5]))
        self.assertEquals(2,  chop(5, [1, 3, 5]))
        self.assertEquals(-1, chop(0, [1, 3, 5]))
        self.assertEquals(-1, chop(2, [1, 3, 5]))
        self.assertEquals(-1, chop(4, [1, 3, 5]))
        self.assertEquals(-1, chop(6, [1, 3, 5]))
        #
        self.assertEquals(0,  chop(1, [1, 3, 5, 7]))
        self.assertEquals(1,  chop(3, [1, 3, 5, 7]))
        self.assertEquals(2,  chop(5, [1, 3, 5, 7]))
        self.assertEquals(3,  chop(7, [1, 3, 5, 7]))
        self.assertEquals(-1, chop(0, [1, 3, 5, 7]))
        self.assertEquals(-1, chop(2, [1, 3, 5, 7]))
        self.assertEquals(-1, chop(4, [1, 3, 5, 7]))
        self.assertEquals(-1, chop(6, [1, 3, 5, 7]))
        self.assertEquals(-1, chop(8, [1, 3, 5, 7]))

unittest.main()

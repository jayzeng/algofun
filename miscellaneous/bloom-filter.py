from math import log
from mmh3 import hash
from bitarray import bitarray

import unittest

class BloomFilter:
    """
        size - number of items in the filter
        false positive rate - the probability of a false positive
    """
    def __init__(self, size, false_positive_rate):
        self.size = size
        self.bit_array_size = self.bit_array_size(size, false_positive_rate)
        self.num_hash_functions = self.get_hash_count(self.bit_array_size, size)
        self.bit_array = bitarray(self.bit_array_size)

        # set all bits to 0
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.num_hash_functions):
            index = self.get_index(item, i)
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.num_hash_functions):
            index = self.get_index(item, i)

            if self.bit_array[index] == 0:
                return False
       
        return True
    
    def get_index(self, item, i):
        # hash(val, seed) -> returns 32bit signed int
        return hash(item, i) % self.bit_array_size

    def bit_array_size(self, num_items, false_positive_rate):
        '''
            m = -(n * ln(p)) / (ln(2)^2)
            where n is the number of items and p is the false positive rate
        '''
        return int(-(num_items * log(false_positive_rate)) / (log(2) ** 2))

    def get_hash_count(self, bit_array_size, num_items):
        '''
            bit_array_size - size of the bit array
            k = (m/n) * log(2)
        '''
        return int(round(bit_array_size / num_items * log(2)))


class TestSort(unittest.TestCase):
    def test_bloom_filter_one_item(self):
        bf = BloomFilter(1, 0.05)
        bf.add('item')
        self.assertTrue(bf.check('item'))
    
    def test_add_item_different_probability_multiple_items(self):
        '''
        Tests that multiple items can be added to the Bloom Filter with
        different false positive probabilities.
        '''
        bf = BloomFilter(4, 0.10)
        bf.add('foo')
        bf.add('bar')
        bf.add('hello')
        bf.add('world')

        self.assertTrue(bf.check('foo'))
        self.assertTrue(bf.check('bar'))
        self.assertTrue(bf.check('hello'))
        self.assertTrue(bf.check('world'))

        bf = BloomFilter(4, 0.50)
        bf.add('foo')
        bf.add('bar')
        bf.add('hello')
        bf.add('world')

        self.assertTrue(bf.check('foo'))
        self.assertTrue(bf.check('bar'))
        self.assertTrue(bf.check('hello'))
        self.assertTrue(bf.check('world'))

        bf = BloomFilter(4, 0.9)
        bf.add('foo')
        bf.add('bar')
        bf.add('hello')
        bf.add('world')

        self.assertTrue(bf.check('foo'))
        self.assertTrue(bf.check('bar'))
        self.assertTrue(bf.check('hello'))
        self.assertTrue(bf.check('world'))


if __name__ == "__main__":
    print("bloom filter")
    unittest.main()
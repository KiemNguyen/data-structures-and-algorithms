from nose.tools import assert_equal, assert_raises

class TestBinarySearch(object):
    
    def test_binary_search(self):
        solution = Solution()
        assert_raises(TypeError, solution.binary_search, None, None)
        assert_raises(ValueError, solution.binary_search, [], 0)
        a = [1, 10, 20, 47, 59, 63, 75, 88, 99]
        key = 20
        expected = 2
        assert_equal(solution.binary_search(a, key), expected)
        print('Success: test_binary_search')

def main():
    test = TestBinarySearch()
    test.test_binary_search()
    
if __name__ == '__main__':
    main()
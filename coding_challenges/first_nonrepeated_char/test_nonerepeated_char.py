from nose.tools import assert_equal, assert_raises

class TestNonerepeatedChar(object):
    
    def test_nonerepeated_char(self):
        solution = Solution()
        str = "total"
        expected = "o"
        assert_equal(solution.nonerepeated_char(str), expected)
        print('Success: test_nonerepeated_char')

def main():
    test = TestNonerepeatedChar()
    test.test_nonerepeated_char()
    
if __name__ == '__main__':
    main()
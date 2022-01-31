import TestKit

from UnderGUI.Commons import *

if __name__ == "__main__":
    print("CommonsTest started")
    
    ### Range ###
    assert Range(0, 1, 2, 3) == Range(0, 1, 2, 3)
    assert (Range(0, 1, 2, 3) == Range(10, 1, 2, 3)) == False
    assert (Range(0, 1, 2, 3) == Range(0, 11, 2, 3)) == False
    assert (Range(0, 1, 2, 3) == Range(1, 1, 12, 3)) == False
    assert (Range(0, 1, 2, 3) == Range(1, 1, 2, 13)) == False

    assert (Range(0, 1, 2, 3) != Range(0, 1, 2, 3)) == False
    assert Range(0, 1, 2, 3) != Range(10, 1, 2, 3)
    assert Range(0, 1, 2, 3) != Range(0, 11, 2, 3)
    assert Range(0, 1, 2, 3) != Range(1, 1, 12, 3)
    assert Range(0, 1, 2, 3) != Range(1, 1, 2, 13)

    assert (Range(5, 2, 3, 4) * Range(10, 100, 1000, 10000)) == Range(50, 200, 3000, 40000)
    assert (Range(6, 20, 60, 3000) / Range(2, 5, 10, 100)) == Range(3, 4, 6, 30)
    assert (Range(6.0, 20.0, 60.0, 3000.0) / Range(2.0, 5.0, 10.0, 100.0)) == Range(3.0, 4.0, 6.0, 30.0)
    assert (Range(5, 2, 3, 4) + Range(10, 100, 1000, 10000)) == Range(15, 102, 1003, 10004)
    assert (Range(10, 20, 30, 40) - Range(1, 2, 3, 4)) == Range(9, 18, 27, 36)
    
    assert (Range(1, 2, 3, 4) * 10) == Range(10, 20, 30, 40)
    assert (Range(10, 20, 30, 40) / 10) == Range(1, 2, 3, 4)
    assert (Range(10.0, 20.0, 30.0, 40.0) / 10.0) == Range(1.0, 2.0, 3.0, 4.0)
    assert (Range(1, 2, 3, 4) + 10) == Range(11, 12, 13, 14)
    assert (Range(10, 20, 30, 40) - 1) == Range(9, 19, 29, 39)
    
    print("CommonsTest finished")
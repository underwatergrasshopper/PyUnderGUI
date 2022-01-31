import math
import TestKit

from UnderGUI.Commons import *

if __name__ == "__main__":
    print("CommonsUnitTest started")
    
    ### Pos ###
    assert Pos(1, 2) == Pos(1, 2)
    assert (Pos(1, 2) == Pos(1, 3)) == False
    assert (Pos(1, 2) == Pos(5, 2)) == False
    assert (Pos(1, 2) == Pos(2, 1)) == False

    assert (Pos(1, 2) != Pos(1, 2)) == False
    assert Pos(1, 2) != Pos(1, 3)
    assert Pos(1, 2) != Pos(5, 2)
    assert Pos(1, 2) != Pos(2, 1)
    
    assert Pos(2, 3) * Pos(10, 100) == Pos(20, 300)
    assert Pos(20, 300) / Pos(10, 100) == Pos(2, 3)
    assert Pos(40, 50) + Pos(1, 2) == Pos(41, 52)
    assert Pos(40, 50) - Pos(1, 2) == Pos(39, 48)

    assert Pos(20, 30) / 10 == Pos(2, 3)
    assert Pos(2, 3) * 10 == Pos(20, 30)
    assert Pos(40, 50) + 2 == Pos(42, 52)
    assert Pos(40, 50) - 2 == Pos(38, 48)
      
    assert (Pos(2, 5) < Pos(3, 6)) == True
    assert (Pos(2, 5) < Pos(2, 6)) == False
    assert (Pos(2, 5) < Pos(3, 5)) == False
    assert (Pos(2, 5) < Pos(2, 5)) == False
    assert (Pos(2, 5) < Pos(1, 5)) == False
    assert (Pos(2, 5) < Pos(2, 4)) == False
    assert (Pos(2, 5) < Pos(1, 4)) == False
    
    assert (Pos(2, 5) <= Pos(3, 6)) == True
    assert (Pos(2, 5) <= Pos(2, 6)) == True
    assert (Pos(2, 5) <= Pos(3, 5)) == True
    assert (Pos(2, 5) <= Pos(2, 5)) == True
    assert (Pos(2, 5) <= Pos(1, 5)) == False
    assert (Pos(2, 5) <= Pos(2, 4)) == False
    assert (Pos(2, 5) <= Pos(1, 4)) == False
    
    assert (Pos(3, 6) > Pos(2, 5)) == True
    assert (Pos(3, 6) > Pos(3, 5)) == False
    assert (Pos(3, 6) > Pos(2, 6)) == False
    assert (Pos(3, 6) > Pos(3, 6)) == False
    assert (Pos(3, 6) > Pos(3, 7)) == False
    assert (Pos(3, 6) > Pos(4, 6)) == False
    assert (Pos(3, 6) > Pos(4, 7)) == False
    
    assert (Pos(3, 6) >= Pos(2, 5)) == True
    assert (Pos(3, 6) >= Pos(3, 5)) == True
    assert (Pos(3, 6) >= Pos(2, 6)) == True
    assert (Pos(3, 6) >= Pos(3, 6)) == True
    assert (Pos(3, 6) >= Pos(3, 7)) == False
    assert (Pos(3, 6) >= Pos(4, 6)) == False
    assert (Pos(3, 6) >= Pos(4, 7)) == False
    
    ### Size ###
    assert Size(1, 2) == Size(1, 2)
    assert (Size(1, 2) == Size(1, 3)) == False
    assert (Size(1, 2) == Size(5, 2)) == False
    assert (Size(1, 2) == Size(2, 1)) == False

    assert (Size(1, 2) != Size(1, 2)) == False
    assert Size(1, 2) != Size(1, 3)
    assert Size(1, 2) != Size(5, 2)
    assert Size(1, 2) != Size(2, 1)
    
    assert Size(2, 3) * Size(10, 100) == Size(20, 300)
    assert Size(20, 300) / Size(10, 100) == Size(2, 3)
    assert Size(40, 50) + Size(1, 2) == Size(41, 52)
    assert Size(40, 50) - Size(1, 2) == Size(39, 48)

    assert Size(20, 30) / 10 == Size(2, 3)
    assert Size(2, 3) * 10 == Size(20, 30)
    assert Size(40, 50) + 2 == Size(42, 52)
    assert Size(40, 50) - 2 == Size(38, 48)
      
    assert (Size(2, 5) < Size(3, 6)) == True
    assert (Size(2, 5) < Size(2, 6)) == False
    assert (Size(2, 5) < Size(3, 5)) == False
    assert (Size(2, 5) < Size(2, 5)) == False
    assert (Size(2, 5) < Size(1, 5)) == False
    assert (Size(2, 5) < Size(2, 4)) == False
    assert (Size(2, 5) < Size(1, 4)) == False
    
    assert (Size(2, 5) <= Size(3, 6)) == True
    assert (Size(2, 5) <= Size(2, 6)) == True
    assert (Size(2, 5) <= Size(3, 5)) == True
    assert (Size(2, 5) <= Size(2, 5)) == True
    assert (Size(2, 5) <= Size(1, 5)) == False
    assert (Size(2, 5) <= Size(2, 4)) == False
    assert (Size(2, 5) <= Size(1, 4)) == False
    
    assert (Size(3, 6) > Size(2, 5)) == True
    assert (Size(3, 6) > Size(3, 5)) == False
    assert (Size(3, 6) > Size(2, 6)) == False
    assert (Size(3, 6) > Size(3, 6)) == False
    assert (Size(3, 6) > Size(3, 7)) == False
    assert (Size(3, 6) > Size(4, 6)) == False
    assert (Size(3, 6) > Size(4, 7)) == False
    
    assert (Size(3, 6) >= Size(2, 5)) == True
    assert (Size(3, 6) >= Size(3, 5)) == True
    assert (Size(3, 6) >= Size(2, 6)) == True
    assert (Size(3, 6) >= Size(3, 6)) == True
    assert (Size(3, 6) >= Size(3, 7)) == False
    assert (Size(3, 6) >= Size(4, 6)) == False
    assert (Size(3, 6) >= Size(4, 7)) == False
    
    ### Pos and Size ###
    assert Pos(2, 3) * Size(10, 100) == Pos(20, 300)
    assert Pos(20, 300) / Size(10, 100) == Pos(2, 3)
    assert Pos(40, 50) + Size(1, 2) == Pos(41, 52)
    assert Pos(40, 50) - Size(1, 2) == Pos(39, 48)
    
    assert Pos(1, 2).to_size() == Size(1, 2)
    assert Size(1, 2).to_pos() == Pos(1, 2)
    
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
    
    assert Range(3, 5, 10, 20).is_in(Pos(3, 5)) == True
    assert Range(3, 5, 10, 20).is_in(Pos(4, 6)) == True
    assert Range(3, 5, 10, 20).is_in(Pos(9, 19)) == True
    assert Range(3, 5, 10, 20).is_in(Pos(2, 5)) == False
    assert Range(3, 5, 10, 20).is_in(Pos(3, 4)) == False
    assert Range(3, 5, 10, 20).is_in(Pos(2, 4)) == False
    assert Range(3, 5, 10, 20).is_in(Pos(9, 20)) == False  
    assert Range(3, 5, 10, 20).is_in(Pos(10, 19)) == False  
    assert Range(3, 5, 10, 20).is_in(Pos(10, 20)) == False  
    
    ### Area ###
    assert Area(0, 1, 2, 3) == Area(0, 1, 2, 3)
    assert (Area(0, 1, 2, 3) == Area(10, 1, 2, 3)) == False
    assert (Area(0, 1, 2, 3) == Area(0, 11, 2, 3)) == False
    assert (Area(0, 1, 2, 3) == Area(1, 1, 12, 3)) == False
    assert (Area(0, 1, 2, 3) == Area(1, 1, 2, 13)) == False
    
    assert (Area(0, 1, 2, 3) != Area(0, 1, 2, 3)) == False
    assert Area(0, 1, 2, 3) != Area(10, 1, 2, 3)
    assert Area(0, 1, 2, 3) != Area(0, 11, 2, 3)
    assert Area(0, 1, 2, 3) != Area(1, 1, 12, 3)
    assert Area(0, 1, 2, 3) != Area(1, 1, 2, 13)
    
    assert Area(3, 5, 7, 15).is_in(Pos(3, 5)) == True
    assert Area(3, 5, 7, 15).is_in(Pos(4, 6)) == True
    assert Area(3, 5, 7, 15).is_in(Pos(9, 19)) == True
    assert Area(3, 5, 7, 15).is_in(Pos(2, 5)) == False
    assert Area(3, 5, 7, 15).is_in(Pos(3, 4)) == False
    assert Area(3, 5, 7, 15).is_in(Pos(2, 4)) == False
    assert Area(3, 5, 7, 15).is_in(Pos(9, 20)) == False  
    assert Area(3, 5, 7, 15).is_in(Pos(10, 19)) == False  
    assert Area(3, 5, 7, 15).is_in(Pos(10, 20)) == False  
    
    ### Area and Range ###
    assert Area(1, 2, 10, 20).to_range() == Range(1, 2, 11, 22)
    assert Range(1, 2, 11, 22).to_area() == Area(1, 2, 10, 20)
    
    print("CommonsUnitTest finished")
    
    
    
    
    
    
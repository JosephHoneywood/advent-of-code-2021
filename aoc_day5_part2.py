"""
                                                                                                                                                
                                                                                                                                                               
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                    555555555555555555 
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                 5::::::::::::::::5 
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                               5::::::::::::::::5 
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                              5:::::555555555555 
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy     5:::::5            
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y      5:::::5            
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y       5:::::5555555555   
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y        5:::::::::::::::5  
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y         555555555555:::::5 
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y                      5:::::5
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y                       5:::::5
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y            5555555     5:::::5
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y             5::::::55555::::::5
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y               55:::::::::::::55 
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y                  55:::::::::55   
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                     555555555     
                                                                                                                    y:::::y                                    
                                                                                                                   y:::::y                                     
                                                                                                                  y:::::y                                      
                                                                                                                 y:::::y                                       
                                                                                                                yyyyyyy                                        
                                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                               
"""

import itertools
from collections import Counter

def get_range(value1, value2):
    if value1 > value2:
        return list(range(value1, value2-1, -1))
    else:
        return list(range(value1, value2+1))

with open("inputs/day5.txt", "r") as f:
    data = [(l.split('->')[0].split(','), l.split('->')[1].split(",")) for l in f.read().splitlines()]

lines = [[int(l[0][0]), int(l[0][1]), int(l[1][0]), int(l[1][1])] for l in data]

points_crossed = []

for l in lines:
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]

    if x1 == x2:

        if y1 > y2:
            vertical_points = list(range(y2, y1+1))
            points_crossed.extend(list(itertools.product([x1], vertical_points)))
        else:
            vertical_points = list(range(y1, y2+1))
            points_crossed.extend(list(itertools.product([x1], vertical_points)))

    elif y1 == y2:

        if x1 > x2:
            horizontal_points = list(range(x2, x1+1))
            points_crossed.extend(list(itertools.product(horizontal_points, [y1])))
        else:
            horizontal_points = list(range(x1, x2+1))
            points_crossed.extend(list(itertools.product(horizontal_points, [y1])))

    else:

        diagonal_points = list(zip(get_range(x1, x2), get_range(y1, y2)))
        points_crossed.extend(diagonal_points)

counted = Counter(points_crossed)

print(len({x: count for x, count in counted.items() if count >= 2}))

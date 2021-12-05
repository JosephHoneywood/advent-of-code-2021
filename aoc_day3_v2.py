"""

                                                                                                                                                                                                                                                                                                                            
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                     333333333333333   
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                 3:::::::::::::::33 
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                               3::::::33333::::::3
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                              3333333     3:::::3
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy                 3:::::3
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y                  3:::::3
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y           33333333:::::3 
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y            3:::::::::::3  
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y             33333333:::::3 
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y                      3:::::3
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y                       3:::::3
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y                        3:::::3
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y             3333333     3:::::3
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y              3::::::33333::::::3
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y               3:::::::::::::::33 
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                 333333333333333   
                                                                                                                    y:::::y                                    
                                                                                                                   y:::::y                                     
                                                                                                                  y:::::y                                      
                                                                                                                 y:::::y                                       
                                                                                                                yyyyyyy                                        
                                                                                                                                                               
                                                                                                                                                               

Reworked solution without pandas

"""
#IMPORTS
from collections import Counter

#Part 1
lines = [x for x in open('inputs/day3.txt').read().strip().split('\n')]

gamma = ''
epsilon = ''

for i in range(len(lines[0])):
    counts = Counter([x[i] for x in lines])

    if counts['0'] > counts['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))

#Part 2

lines = [x for x in open('inputs/day3.txt').read().strip().split('\n')]

oxygen = ''
c02 = ''

for i in range(len(lines[0])):
    counts = Counter([x[i] for x in lines])

    if counts['0'] > counts['1']:
        lines = [x for x in lines if x[i] == '0']
    else:
        lines = [x for x in lines if x[i] == '1']
    oxygen = lines[0]

lines = [x for x in open('inputs/day3.txt').read().strip().split('\n')]
for i in range(len(lines[0])):
    counts = Counter(x[i] for x in lines)

    if counts['0'] > counts['1']:
        lines = [x for x in lines if x[i] == '1']
    else:
        lines = [x for x in lines if x[i] == '0']
    if lines:
        c02 = lines[0]

print(int(oxygen, 2) * int(c02, 2))


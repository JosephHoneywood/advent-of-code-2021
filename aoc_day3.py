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
                                                                                                                                                               
                                                                                                                                                               
  
"""
#IMPORTS

import pandas as pd
from functions.day3_funcs import register_column_mode, drop_by_condition

# #PART 1
with open("inputs/day3.txt", "r") as f:
    binary_report = [list(map(int, l)) for l in f.read().splitlines()]

binary_report_df = pd.DataFrame(binary_report)
 
gamma_rate = ''.join(map(str, binary_report_df.mode().values[0])) #1869
epsilon_rate = ''.join(['1' if b == '0' else '0' for b in gamma_rate]) #2226

print(int(gamma_rate,2) * int(epsilon_rate,2))

#PART 2
oxygen_frame = pd.DataFrame(binary_report)
c02_frame = pd.DataFrame(binary_report)
metrics = [(oxygen_frame, "most common"), (c02_frame, 'least common')]

for metric in metrics:

    frame = metric[0]
    mode_config = metric[1]

    for column_index in range(0, len(frame)):

        if len(frame) == 1: break

        col_mode = register_column_mode(frame, column_index, mode_config)
        drop_by_condition(frame, col_mode, column_index)
     
oxygen_rate = int(''.join(map(str, oxygen_frame.values[0])), 2) #1719
c02_rate = int(''.join(map(str, c02_frame.values[0])), 2) #2400

print(oxygen_rate * c02_rate)

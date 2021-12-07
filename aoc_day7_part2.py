"""

                                                                                                                                                                                                                                                                                                        
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                    77777777777777777777
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                 7::::::::::::::::::7
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                               7::::::::::::::::::7
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                              777777777777:::::::7
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy                7::::::7 
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y                7::::::7  
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y                7::::::7   
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y                7::::::7    
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y                7::::::7     
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y                7::::::7      
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y                7::::::7       
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y                7::::::7        
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y                7::::::7         
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y                7::::::7          
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y                7::::::7           
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                77777777            
                                                                                                                    y:::::y                                     
                                                                                                                   y:::::y                                      
                                                                                                                  y:::::y                                       
                                                                                                                 y:::::y                                        
                                                                                                                yyyyyyy                                         
                                                                                                                                                                
               
                                                                                                                                                            
"""

import statistics
import math

inputs = [int(c) for c in open('inputs/day7.txt').read().strip().split(",")]

mean = statistics.mean(inputs)
whole = mean.is_integer()

if not whole:

    fuel_costs = []
    means = [math.floor(mean), math.ceil(mean)]
    
    for m in means:

        fuel_cost = 0

        for h_pos in inputs:

            fuel_cost += sum(range(abs(h_pos - m)+1))

        fuel_costs.append(fuel_cost)

    print(min(fuel_costs))

else:

    fuel_cost = 0
    for h_pos in inputs:

        fuel_cost += sum(range(abs(h_pos - m)+1))

    print(fuel_cost)

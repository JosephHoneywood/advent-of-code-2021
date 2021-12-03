"""
                                                                                                                                                        
                                                                                                                                                        
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                      1111111   
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                  1::::::1   
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                               1:::::::1   
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                              111:::::1   
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy        1::::1   
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y         1::::1   
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y          1::::1   
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y           1::::l   
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y            1::::l   
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y             1::::l   
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y              1::::l   
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y               1::::l   
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y             111::::::111
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y              1::::::::::1
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y               1::::::::::1
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                111111111111
                                                                                                                    y:::::y                             
                                                                                                                   y:::::y                              
                                                                                                                  y:::::y                               
                                                                                                                 y:::::y                                
                                                                                                                yyyyyyy                                 
                                                                                                                                                        
                                                                                                                                                        

"""

### IMPORTS

lines = open("inputs/day1.txt",'r').read().splitlines()
lines = list(map(int, lines))

### PART 1

increased_depth_counter = 0

for index, current_value in enumerate(lines):

    if index == 0: pass 
    else:
        previous_value = lines[index-1]
        if current_value > previous_value: increased_depth_counter += 1

### PART 2

index_stop = len(lines)-2
sliding_sum = []
increased_depth_counter = 0

for index, current_value in enumerate(lines):

    if index == index_stop: break

    sum_of_three = current_value + lines[index+1] + lines[index+2]
    sliding_sum.append(sum_of_three)

for index, current_value in enumerate(sliding_sum):

    if index == 0: pass
    
    previous_value = sliding_sum[index-1]
    if current_value > previous_value: increased_depth_counter += 1 
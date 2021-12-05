"""

                                                                                                                                                                                                                                                                                                                              
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                     222222222222222    
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                 2:::::::::::::::22  
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                               2::::::222222:::::2 
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                              2222222     2:::::2 
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy                 2:::::2 
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y                  2:::::2 
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y                2222::::2  
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y            22222::::::22   
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y           22::::::::222     
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y           2:::::22222        
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y           2:::::2             
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y            2:::::2             
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y             2:::::2       222222
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y              2::::::2222222:::::2
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y               2::::::::::::::::::2
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                22222222222222222222
                                                                                                                    y:::::y                                     
                                                                                                                   y:::::y                                      
                                                                                                                  y:::::y                                       
                                                                                                                 y:::::y                                        
                                                                                                                yyyyyyy                                         


                                                                                                                            
"""

with open("inputs/day2.txt",'r') as f:
    instructions = [(l.split(" ")[0], int(l.split(" ")[1])) for l in f.read().splitlines()]

#PART 1

position = [0,0]

for command in instructions:
    if command[0] == 'forward':
        position[0] += command[1]
    elif command[0] == 'up':
        position[1] -= command[1]
    elif command[0] == 'down':
        position[1] += command[1]

# PART 2

positions = {
    "horizontal": 0,
    "vertical": 0,
     "aim": 0
     }

for command in instructions:
    if command[0] == 'forward':
        positions['horizontal'] += command[1]
        positions['vertical'] += (positions['aim'] * command[1])
    elif command[0] == 'up':
        positions['aim'] -= command[1]
    elif command[0] == 'down':
        positions['aim'] += command[1]

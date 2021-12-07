"""
                                                                                                                                         
                                                                                                                                                               
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                            66666666   
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                        6::::::6    
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                                     6::::::6     
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                                   6::::::6      
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy         6::::::6       
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y         6::::::6        
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y         6::::::6         
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y         6::::::::66666    
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y         6::::::::::::::66  
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y          6::::::66666:::::6 
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y           6:::::6     6:::::6
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y            6:::::6     6:::::6
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y             6::::::66666::::::6
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y               66:::::::::::::66 
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y                  66:::::::::66   
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                     666666666     
                                                                                                                    y:::::y                                    
                                                                                                                   y:::::y                                     
                                                                                                                  y:::::y                                      
                                                                                                                 y:::::y                                       
                                                                                                                yyyyyyy                                        
                                                                                                                                                               
  

"""

inputs = [int(f) for f in open('inputs/day6.txt').read().strip().split(',')]
fish, days = [inputs.count(i) for i in range(9)], 256

for i in range(days):

    n = fish.pop(0)
    fish[6] += n
    fish.append(n)
    assert len(fish) == 9

# print(sum(fish))

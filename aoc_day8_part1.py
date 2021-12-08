"""
                                                                                                                                      
                                                                                                                                                               
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                         888888888     
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                    88:::::::::88   
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                                88:::::::::::::88 
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                              8::::::88888::::::8
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy     8:::::8     8:::::8
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y      8:::::8     8:::::8
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y        8:::::88888:::::8 
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y          8:::::::::::::8  
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y          8:::::88888:::::8 
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y          8:::::8     8:::::8
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y           8:::::8     8:::::8
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y            8:::::8     8:::::8
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y             8::::::88888::::::8
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y               88:::::::::::::88 
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y                  88:::::::::88   
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                     888888888     
                                                                                                                    y:::::y                                    
                                                                                                                   y:::::y                                     
                                                                                                                  y:::::y                                      
                                                                                                                 y:::::y                                       
                                                                                                                yyyyyyy                                        
                                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                               
"""

inputs = [(l.split("|")[0].strip(), l.split("|")[1].strip()) for l in open('inputs/day8.txt').read().splitlines()]

count = 0

for l in inputs:
    print(l)
    for m in l[1].split(" "):
        print(m)
        if len(m) in [2, 3, 4, 7]:
            count += 1

print(count)
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

inputs = [l for l in open('inputs/day8.txt').read().splitlines()]

def find_three(signal, mapping):
    for s in signal:
        if len(s) == 5 and all(elem in s for elem in mapping[1]):
                return list(s)
            
def find_nine(signal, mapping):
    return list(set(mapping[3] + mapping[4]))

def find_zero(signals, mapping):
    for s in signals:
        if len(s) == 6 and all(elem in s for elem in mapping[1]) and not all(elem in s for elem in mapping[9]):
            return list(s)

def find_six(signals, mapping):
    for s in signals:
        if len(s) == 6 and not all(elem in s for elem in mapping[0]) and not all(elem in s for elem in mapping[9]):
            return list(s)

def find_five(signals, mapping):
    for s in signals:
        if len(s) == 5 and not all(elem in s for elem in mapping[3]) and set(s).issuperset(set(mapping[4]) - set(mapping[1])):
            return list(s)

def find_two(signals, mapping):
    for s in signals:
        if len(s) == 5 and not all(elem in s for elem in mapping[3]) and not all(elem in s for elem in mapping[5]):
            return list(s)

running_sum = 0

for i in inputs:

    signal, output = i.split("|")[0].split(), i.split("|")[1].split()

    mapping = {
    0: '?',
    1: list([l for l in signal if len(l) == 2][0]),
    2: '?',
    3: '?',
    4: list([l for l in signal if len(l) == 4][0]),
    5: '?',
    6: '?',
    7: list([l for l in signal if len(l) == 3][0]),
    8: list([l for l in signal if len(l) == 7][0]),
    9: '?'}
    
    mapping[3] = find_three(signal, mapping)
    mapping[9] = find_nine(signal, mapping)
    mapping[0] = find_zero(signal, mapping)
    mapping[6] = find_six(signal, mapping)
    mapping[5] = find_five(signal, mapping)
    mapping[2] = find_two(signal, mapping)

    line_answer = ''

    for o in output:
        for key, value in mapping.items():
            if set(o) == set(value):
                line_answer = line_answer + str(key)

    running_sum += int(line_answer)

print(running_sum)
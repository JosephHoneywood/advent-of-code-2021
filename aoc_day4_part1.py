"""

                                                                                                                                                                                                                                                                                                                    
               AAA                 OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD                                                           444444444  
              A:::A              OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD                                                       4::::::::4  
             A:::::A           OO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD                                                    4:::::::::4  
            A:::::::A         O:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D                                                  4::::44::::4  
           A:::::::::A        O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::D  aaaaaaaaaaaaayyyyyyy           yyyyyyy        4::::4 4::::4  
          A:::::A:::::A       O:::::O     O:::::OC:::::C                     D:::::D     D:::::D a::::::::::::ay:::::y         y:::::y        4::::4  4::::4  
         A:::::A A:::::A      O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aaaaaaaaa:::::ay:::::y       y:::::y        4::::4   4::::4  
        A:::::A   A:::::A     O:::::O     O:::::OC:::::C                     D:::::D     D:::::D          a::::a y:::::y     y:::::y        4::::444444::::444
       A:::::A     A:::::A    O:::::O     O:::::OC:::::C                     D:::::D     D:::::D   aaaaaaa:::::a  y:::::y   y:::::y         4::::::::::::::::4
      A:::::AAAAAAAAA:::::A   O:::::O     O:::::OC:::::C                     D:::::D     D:::::D aa::::::::::::a   y:::::y y:::::y          4444444444:::::444
     A:::::::::::::::::::::A  O:::::O     O:::::OC:::::C                     D:::::D     D:::::Da::::aaaa::::::a    y:::::y:::::y                     4::::4  
    A:::::AAAAAAAAAAAAA:::::A O::::::O   O::::::O C:::::C       CCCCCC       D:::::D    D:::::Da::::a    a:::::a     y:::::::::y                      4::::4  
   A:::::A             A:::::AO:::::::OOO:::::::O  C:::::CCCCCCCC::::C     DDD:::::DDDDD:::::D a::::a    a:::::a      y:::::::y                       4::::4  
  A:::::A               A:::::AOO:::::::::::::OO    CC:::::::::::::::C     D:::::::::::::::DD  a:::::aaaa::::::a       y:::::y                      44::::::44
 A:::::A                 A:::::A OO:::::::::OO        CCC::::::::::::C     D::::::::::::DDD     a::::::::::aa:::a     y:::::y                       4::::::::4
AAAAAAA                   AAAAAAA  OOOOOOOOO             CCCCCCCCCCCCC     DDDDDDDDDDDDD         aaaaaaaaaa  aaaa    y:::::y                        4444444444
                                                                                                                    y:::::y                                   
                                                                                                                   y:::::y                                    
                                                                                                                  y:::::y                                     
                                                                                                                 y:::::y                                      
                                                                                                                yyyyyyy                                       


                                                                                                                                                                                                                                                                                                               
"""
import itertools
import sys

with open("inputs/day4.txt", "r") as f:
    data = [l.split() for l in f.read().splitlines()]

bingo_calls = [int(n) for n in data[0][0].split(',')]
bingo_boards = data[1:]
board = []
board_holder = []

for board_data in bingo_boards[1:]:
    if board_data == []:
        board_holder.append(board)
        board = []
    else:
        row = [int(n) for n in board_data]
        board.append(row)

for index, board in enumerate(board_holder):

    col_wise_lists = list(map(list, zip(*board)))
    board.extend(col_wise_lists)

for call in bingo_calls:
    for board in board_holder:
        for index, line in enumerate(board):

            if call in line:

                line = [0 if n == call else n for n in line]

                board[index] = line

                if sum(line) == 0:

                    winning_board = board[:5]
                    remaining_sum = 0

                    for line in winning_board:
                        remaining_sum += sum(line)

                    print(remaining_sum * call)

                    sys.exit()
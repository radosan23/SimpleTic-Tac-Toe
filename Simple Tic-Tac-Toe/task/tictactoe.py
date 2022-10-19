def win(a):
    global board
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == a:
            return True
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == a:
            return True
    if board[0][0] == board[1][1] == board[2][2] == a or board[0][2] == board[1][1] == board[2][0] == a:
        return True
    return False


def check_coord(c):
    global board
    if len(c) < 2:
        print('Enter two numbers!')
        return []
    for i in c:
        if not i.isdigit():
            print('You should enter numbers!')
            return []
        elif i not in ['1', '2', '3']:
            print('Coordinates should be from 1 to 3!')
            return []
    if board[int(c[0])-1][int(c[1])-1] != ' ':
        print('This cell is occupied! Choose another one!')
        return []
    return [int(x)-1 for x in c]


board = [[' ' for i in range(3)]for j in range(3)]
symbol = 'X'
finished = False
while not finished:
    print('-' * 9)
    for i in range(3):
        print(f'| {board[i][0]} {board[i][1]} {board[i][2]} |')
    print('-' * 9)

    if win('X') or win('O'):
        finished = True
        print('X wins') if win('X') else print('O wins')
    elif not any(x for row in board for x in row if x == ' '):
        finished = True
        print('Draw')
    else:
        coord = []
        while not coord:
            coord = check_coord(input(f'{symbol} player - enter coordinates: ').split())
        board[coord[0]][coord[1]] = symbol
        symbol = 'O' if symbol == 'X' else 'X'

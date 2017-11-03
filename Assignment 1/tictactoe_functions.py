import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    
    return (value <= max_value) and (value >= min_value)
   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.

def game_board_full(game_board) :
    """ (str) -> bool
    
    Returns True if and only if there are no EMPTY characters in the game board.
    
    >>>game_board_full(OOXXXOOOX)
    True
    >>>game_board_full(XO-XO-OX-)
    False
    
    """
    
    return not (EMPTY in game_board)


def get_board_size(game_board):
    
    """ (str) -> int
    
    Returns length of each side of the tic-tac-toe game board.
    
    >>>get_board_size('XO-XO-OX-X---OOX')
    4
    >>>get_board_size('X-X---OOX')
    3
    
    """
    
    return int ( math.sqrt( len(game_board) ) )
    
def make_empty_board(board_size):
    
    """ (int) -> str
    
    Returns string for storing information for the game.
    
    >>>make_empty_board(2)
    '----'
    >>>make_empty_board(3)
    '---------'
    
    """
    
    return ( EMPTY * int ( math.pow( board_size, 2 ) ) )


def get_position(row_index, column_index, board_size):
    
    """ (int, int, int) -> int
    
    Returns the string index of the cell in the string representation
    of the game board.
    
    >>>get_position(1,1,3)
    0
    >>>get_position(2,4,4)
    7
    
    """
    
    return ( (row_index - 1) * board_size + column_index - 1 )


def make_move(symbol, row_index, column_index, game_board):
    
    """ (str, int, int, str) -> str
    
    Returns the tic-tac-toe game board after the symbol has been placed in its respective cell.
    
    >>>make_move('X',1,3,'XO-XO-XO-')
    'XOXXO-XO-'
    >>>make_move('O',2,3,'XOXXO-XO-')
    'XOXXOOXO-'
    
    """
    
    board_size = get_board_size ( game_board )
    symbol_position = get_position ( row_index, column_index, board_size )
    
    return ( game_board [ : symbol_position ] + symbol + game_board [ symbol_position + 1 : ] )
    

def extract_line( game_board, direction, r_or_c_num = 0 ) :
    """ (str, str, int) -> str
    
    Returns the characters that make up the specific row, column or diagonal.
    
    >>>extract_line('XO-OX-XO-', 'across', 2)
    'XO-'
    >>>extract_line('XO-OX-XO-', 'down', 3)
    '---'
    
    """
    
    board_size = get_board_size ( game_board )
    row_index = ( r_or_c_num - 1 ) * board_size
    column_index = r_or_c_num - 1
    up_diagonal_index = len (game_board) - board_size 
    
    if ( direction == 'down' ) :
        
        return ( game_board [ column_index : len( game_board ) : board_size ] )
    
    elif ( direction == 'across' ) :
        
        return ( game_board [ row_index : board_size * r_or_c_num : 1 ] )
    
    elif ( direction == 'down_diagonal' ) :
        
        return ( game_board [ : : board_size + 1 ] )
    
    elif ( direction == 'up_diagonal' ) :
        
        return ( game_board [ up_diagonal_index : board_size - 2 : -( board_size - 1 ) ] )
    
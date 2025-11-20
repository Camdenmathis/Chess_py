
import pygame

pygame.init()
WIDTH = 1500
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Chess!!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 40)
timer = pygame.time.Clock()
fps = 60
#variables and image
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight','rook',
         'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn','pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight','rook',
         'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn','pawn']
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 whites turn, 1 whites turn piece selected, 2 black turn no select, 3 black piece selected
turn_step = 0
white_selection = 100
black_selection = 100
valid_moves = []
# loading images :(
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#making gameboard
def draw_board():
    for row in range(8):
        for col in range(8):
            # If row + col is even → dark square, else light square
            color = 'dark blue' if (row + col) % 2 == 0 else 'white'
            pygame.draw.rect(screen, color, [col * 100, row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [800, 0, WIDTH, 900])
        pygame.draw.rect(screen, 'gray', [0 ,800, 800, 100])
        pygame.draw.rect(screen, 'black', [0, 800, 800, 100], 5)
        pygame.draw.rect(screen, 'black', [800, 0, 700, 900], 5)
        status_text = ['White: Select a Piece', 'White: Select a Placement']
        status_text = ['Black: Select a Piece', 'Black: Select a Placement']
        screen.blit(font.render(status_text[turn_step], True, 'black'), (1100, 850))

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        x = white_locations[i][0] * 100
        y = white_locations[i][1] * 100
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (x + 15, y + 15))
        else:
            offset = 10  # (100-80)/2
            screen.blit(white_images[index], (x + offset, y + offset))
        if turn_step < 2:
            if white_selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0]* 100 * 1, white_locations[i][1]* 100 * 1, 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        x = black_locations[i][0] * 100
        y = black_locations[i][1] * 100
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (x + 15, y + 15))
        else:
            offset = 10  # (100-80)/2
            screen.blit(black_images[index], (x + offset, y + offset))
        if turn_step < 2:
            if black_selection == i:
                pygame.draw.rect(screen, 'red', [black_locations[i][0]* 100 * 1, black_locations[i][1]* 100 * 1, 100, 100], 2)

#Check pieces valid options for moves
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
    return all_moves_list

#main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_locations:
                    white_selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and white_selection != 100:
                    white_locations[white_selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    white_selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_locations:
                    black_selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and black_selection != 100:
                    black_locations[black_selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    black_selection = 100
                    valid_moves = []


    pygame.display.flip()
pygame.quit()
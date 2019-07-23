import random
import pygame
import sys
import os

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# Init
pygame.init()

# Win
current_directory = os.getcwd()
board_image = os.path.join(current_directory, 'tic_board.png')
board = pygame.image.load(board_image)
board = pygame.transform.scale(board, (600, 600))
win_width = 600
win_height = 600
game_win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Tic-Tac-Toe")
bg = (119, 244, 66)

# Player Default Scores
playerx_score = 0
playero_score = 0

# Player Score Text
freeSansBold = os.path.join(current_directory, "FreeSansBold.ttf")
basicfont = pygame.font.Font(freeSansBold, 30) # was 50, 35 was good
text1 = basicfont.render(("Player X - " + str(playerx_score)), True, (255, 255, 255))
text2 = basicfont.render(("Player O - " + str(playero_score)), True, (255, 255, 255))

# Reset Button
resetfont = pygame.font.Font(freeSansBold, 25) # was 35, adjust y
reset_text = resetfont.render(("RESET"), True, (0, 0, 0))

# Turn Info Box
turnfont = pygame.font.Font(freeSansBold, 30) # was 50
turnx_text = turnfont.render(("Player X's Turn"), True, (0, 0, 0))
turno_text = turnfont.render(("Player O's Turn"), True, (0, 0, 0))

# Markers X and O
markerfont = pygame.font.Font(freeSansBold, 70, bold=True) # was 70
marker_X = markerfont.render(("X"), True, (0, 0, 0))
marker_O = markerfont.render(("O"), True, (0, 0, 0))

# Box Starting Values
box1 = None
box2 = None
box3 = None
box4 = None
box5 = None
box6 = None
box7 = None
box8 = None
box9 = None

# Player Turn Booleans
player_x_turn = True
player_o_turn = False

# Reset Game Function
def reset_game():

    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9

    global player_x_turn
    global player_o_turn

    box1 = None
    box2 = None
    box3 = None
    box4 = None
    box5 = None
    box6 = None
    box7 = None
    box8 = None
    box9 = None

    player_x_turn = True
    player_o_turn = False

# Refresh The Screen
def redrawGameWindow():

    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9

    global player_x_turn
    global player_o_turn

    global playerx_score
    global playero_score

    text1 = basicfont.render(("Player X - " + str(playerx_score)), True, (255, 255, 255))
    text2 = basicfont.render(("Player O - " + str(playero_score)), True, (255, 255, 255))

    game_win.fill(bg)
    game_win.blit(board, (0,0))
    game_win.blit(text1, (58,10)) # was 13
    game_win.blit(text2, (350,555)) # was 558
    game_win.blit(reset_text, (494,23)) # was 27
    if player_x_turn == True:
        game_win.blit(turnx_text, (25,545)) # x was 16, y was 547 on both
    else:
        game_win.blit(turno_text, (25,545)) # x was 15

    # Drawing The Xs and Os

    if box1 == "X":
        game_win.blit(marker_X, (170,170))
    elif box1 == "O":
        game_win.blit(marker_O, (170,170))

    if box2 == "X":
        game_win.blit(marker_X, (266,170))
    elif box2 == "O":
        game_win.blit(marker_O, (266,170))

    if box3 == "X":
        game_win.blit(marker_X, (358,170))
    elif box3 == "O":
        game_win.blit(marker_O, (358,170))

    if box4 == "X":
        game_win.blit(marker_X, (170,266))
    elif box4 == "O":
        game_win.blit(marker_O, (170,266))

    if box5 == "X":
        game_win.blit(marker_X, (266,266))
    elif box5 == "O":
        game_win.blit(marker_O, (266,266))

    if box6 == "X":
        game_win.blit(marker_X, (358,266))
    elif box6 == "O":
        game_win.blit(marker_O, (358,266))

    if box7 == "X":
        game_win.blit(marker_X, (170,358))
    elif box7 == "O":
        game_win.blit(marker_O, (170,358))

    if box8 == "X":
        game_win.blit(marker_X, (266,358))
    elif box8 == "O":
        game_win.blit(marker_O, (266,358))

    if box9 == "X":
        game_win.blit(marker_X, (358,358))
    elif box9 == "O":
        game_win.blit(marker_O, (358,358))

    pygame.display.update()

# Main Game Loop
run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            def click_event():

                global box1
                global box2
                global box3
                global box4
                global box5
                global box6
                global box7
                global box8
                global box9

                global player_x_turn
                global player_o_turn

                mx,my = pygame.mouse.get_pos()

                # Checking Mouse Location
                if mx >= 168 and mx <= 242 and my >=168 and my <=242:
                    if box1 == "X" or box1 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box1 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box1 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 264 and mx <= 338 and my >=168 and my <=242:
                    if box2 == "X" or box2 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box2 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box2 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 356 and mx <= 430 and my >=168 and my <=242:
                    if box3 == "X" or box3 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box3 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box3 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 168 and mx <= 242 and my >=264 and my <=338:
                    if box4 == "X" or box4 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box4 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box4 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 264 and mx <= 338 and my >=264 and my <=338:
                    if box5 == "X" or box5 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box5 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box5 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 356 and mx <= 430 and my >=264 and my <=338:
                    if box6 == "X" or box6 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box6 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box6 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 168 and mx <= 242 and my >=356 and my <=430:
                    if box7 == "X" or box7 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box7 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box7 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 264 and mx <= 338 and my >=356 and my <=430:
                    if box8 == "X" or box8 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box8 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box8 = "O"
                            player_x_turn = True
                            player_o_turn = False

                if mx >= 356 and mx <= 430 and my >=356 and my <=430:
                    if box9 == "X" or box9 == "O":
                        pass
                    else:
                        if player_x_turn == True:
                            box9 = "X"
                            player_x_turn = False
                            player_o_turn = True
                        elif player_o_turn == True:
                            box9 = "O"
                            player_x_turn = True
                            player_o_turn = False

                # Reset Button
                if mx >= 507 and mx <= 581 and my >=18 and my <=56:
                    reset_game()

                # Checking For Win Conditionals
                def win_check():

                    global playerx_score
                    global playero_score

                    # Horizontal Checks
                    if box1 == "X" and box2 == "X" and box3 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box1 == "O" and box2 == "O" and box3 == "O":
                        playero_score +=1
                        reset_game()

                    if box4 == "X" and box5 == "X" and box6 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box4 == "O" and box5 == "O" and box6 == "O":
                        playero_score +=1
                        reset_game()

                    if box7 == "X" and box8 == "X" and box9 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box7 == "O" and box8 == "O" and box9 == "O":
                        playero_score +=1
                        reset_game()

                    # Vertical Checks
                    if box1 == "X" and box4 == "X" and box7 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box1 == "O" and box4 == "O" and box7 == "O":
                        playero_score +=1
                        reset_game()

                    if box2 == "X" and box5 == "X" and box8 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box2 == "O" and box5 == "O" and box8 == "O":
                        playero_score +=1
                        reset_game()

                    if box3 == "X" and box6 == "X" and box9 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box3 == "O" and box6 == "O" and box9 == "O":
                        playero_score +=1
                        reset_game()

                    # Diagonal Checks
                    if box1 == "X" and box5 == "X" and box9 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box1 == "O" and box5 == "O" and box9 == "O":
                        playero_score +=1
                        reset_game()

                    if box3 == "X" and box5 == "X" and box7 == "X":
                        playerx_score +=1
                        reset_game()
                    elif box3 == "O" and box5 == "O" and box7 == "O":
                        playero_score +=1
                        reset_game()

                win_check()

            click_event()

    redrawGameWindow()

pygame.quit

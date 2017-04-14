###
# This program plays chess using Stockfish
# using the ChessBoard library to manage the board.
# The program is developed by www.chess.fortherapy.co.uk would be nice.
# It is written in Python 2.7 for compatibility with Chessboard. Python 3 may work too.
# Several Python libraries are needed (see below).
# It assumes stockfish is loaded in the python directory.
# In this program the routines Getboard and Sendboard get a move in the for me2e4, by simple keyboard input.
# [[[***In the working system these get replaced by serial coms with the board***]]]
# it runs Stockfish using a list of moves not FEN. I couldn't get the FEN routines
# to work in ChessBoard fails after h2 h4 so #'d out
# Instead they use a move list, which is less elegant, but works.
# See full working system at : www.chess.fortherapy.co.uk
# to start try running the program and type me2e4 at the first prompt.
# This program is built using lots of examples from around the web, so do what you want with it.

#v0.2.2:
#Adds Capacity to play black (first input should be ma9a9)

#To-do: Print all game moves and email at the end of the game.
#To-do: Speech-to-text!

# INITIATE CHESSBOARD. IMPORT NEEDED PACKAGES
from ChessBoard import ChessBoard
from Utilities import identify_piece_moving, read_board
import DrawChessPosition
import subprocess, time
from Tkinter import *
import re, string
from PIL import Image,ImageDraw,ImageFont
from os import system

maxchess = ChessBoard()
#renderer = DrawChessPosition()

# INITIATE STOCKFISH CHESS ENGINE

engine = subprocess.Popen(
    '/Users/michailfragkias/Documents/stockfish-8-mac/Mac/stockfish-8-64',
    universal_newlines=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,)
#remember, no path in RaspbPi, just 'stockfish'

def get():
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    stx=""
    engine.stdin.write('isready\n')
    print('\nengine:')
    while True :
        text = engine.stdout.readline().strip()
        if text == 'readyok':
            print('\t'+text)
            break
        if text !='':   
            print('\t'+text)
        if text[0:8] == 'bestmove':
        
            return text
def sget():
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    stx=""
    engine.stdin.write('isready\n')
    print('\nengine:')
    while True :
        text = engine.stdout.readline().strip()
        #if text == 'readyok':
        #    break
        if text !='':   
            print('\t'+text)
        if text[0:8] == 'bestmove':
            mtext=text
            return mtext
def getboard():
    """ gets a text string from the board """
    btxt = raw_input("\n Enter a move or board message: ").lower()
    return btxt
    
def sendboard(stxt):
    """ sends a text string to the board """
    print("\n send to board: " +stxt)

def newgame():
    get ()
    put('uci')
    get ()
    put('setoption name Skill Level value ' +str(skill))
    get ()
    put('setoption name Hash value 128')
    get()
    put('setoption name Best Book Move value true')
    get()
    put('setoption name OwnBook value true')
    get()
    put('setoption name UCI_Chess960 value false')
    get()
    put('uci')
    get ()
    put('ucinewgame')
    maxchess.resetBoard()
    fmove=""
    return fmove

def bmove(fmove):
    """ assume we get a command of the form me2e4 from board"""    
    fmove=fmove
    read_board(maxchess)
    
    # GET A MOVE FROM THE BOARD
    brdmove = bmessage[1:5].lower()

    # --- Code added here make computer play white by sending null message "ma9a9" to Stockfish
    if brdmove =="a9a9":
        fmove = ""
        print ("I play White!")
        put(fmove)
        
        # SEND MOVE TO ENGINE AND GET ENGINE'S MOVE
        put("go movetime " +str(movetime))
        time.sleep(1) #time in seconds before the computer responds
        #text = get()
        #put('stop')
        text = sget()
        print (text)
        smove = text[9:13]
        hint = text[21:25]

        if maxchess.addTextMove(smove) != True :
            #stxt = "e"+ str(maxchess.getReason())+move
            stxt = "e"+ str(maxchess.getReason())+'---'+smove
            maxchess.printBoard()
            sendboard(stxt)
            return fmove

        else:
            temp=fmove
            fmove =temp+" " +smove
            stx = smove+hint      
            sendboard(stx)
            maxchess.printBoard()
            #show the game status in FEN
            maxfen = maxchess.getFEN()
            sendboard(maxfen)
            fancyboard = renderer.draw(maxfen)
            fancyboard.show()                           #show the fancy graphics board
            print ("last computer move: " +smove)       #print the move
            system('say ,'+identify_piece_moving(smove[0:2], maxchess)+','+smove[0:2]+','+smove[2:4]) #say the move
            check_game_state(maxchess)
            return fmove #added by me
    # --- end of section that allows compter to play white

    # VALIDATE MOVE
    # IF INVALID, GET REASON AND SEND BACK TO BOARD
    
    # maxchess.addTextMove(move)
    if maxchess.addTextMove(brdmove) == False :
        etxt = "error"+ str(maxchess.getReason())+'---'+brdmove
        if maxchess.getReason()==1:
            print("\n Error! Invalid Move")
        if maxchess.getReason()==2:
            print("\n Error! Invalid Color")
        if maxchess.getReason()==3:
            print("\n Error! Invalid From Location")
        if maxchess.getReason()==4:
            print("\n Error! Invalid To Location")
        if maxchess.getGameResult()==5:
            print("\n Error! Must Set Promotion")
        if maxchess.getGameResult()==6:
            print("\n Error! Game Is Over")
        maxchess.printBoard()
        sendboard(etxt)
        return fmove
                       
    #  ELIF VALID, MAKE THE MOVE AND SEND FEN TO THE BOARD
    
    else:
        maxchess.printBoard()
        #show the game status in FEN
        maxfen = maxchess.getFEN()
        sendboard(maxfen)
        #show the fancy graphics board
        fancyboard = renderer.draw(maxfen)
        fancyboard.show()
        #remove line below when working
        #raw_input("\n\nPress Enter/Return to continue")
        print ("fmove")
        print(fmove)
        print ("brdmove")
        print(brdmove)
        fmove =fmove+" "+brdmove

        cmove = "position startpos moves"+fmove
        print (cmove)
        system('say You,'+identify_piece_moving(brdmove[0:2], maxchess)+','+brdmove[0:2]+','+brdmove[2:4])
        check_game_state(maxchess)

        #        if fmove == True :
        #                move = "position startpos moves "+move
        #        else:
        #               move ="position fen "+maxfen

        # put('ucinewgame')
        # get()
            
        put(cmove)

        # SEND MOVE TO ENGINE AND GET ENGINE'S MOVE
        put("go movetime " +str(movetime))
        time.sleep(1) #time in seconds before the computer responds
        #text = get()
        #put('stop')
        text = sget()
        print (text)
        smove = text[9:13]
        hint = text[21:25]

        if maxchess.addTextMove(smove) != True :
            #stxt = "e"+ str(maxchess.getReason())+move
            stxt = "e"+ str(maxchess.getReason())+'---'+smove
            maxchess.printBoard()
            sendboard(stxt)

        else:
            temp=fmove
            fmove =temp+" " +smove
            stx = smove+hint      
            sendboard(stx)
            maxchess.printBoard()
            #show the game status in FEN
            maxfen = maxchess.getFEN()
            sendboard(maxfen)
            fancyboard = renderer.draw(maxfen)
            fancyboard.show()                           #show the fancy graphics board
            print ("last computer move: " +smove)       #print the move
            system('say ,'+identify_piece_moving(smove[0:2], maxchess)+','+ smove[0:2]+','+smove[2:4]) #say the move
            check_game_state(maxchess)
            return fmove
        
        #system('say ,'+ 'rook')
        #system('say ,'+ 'pawn')
        #system('say ,'+ 'bishop')
        #system('say ,'+ 'knight')
        #system('say ,'+ 'king')
        #system('say ,'+ 'queen')
        
def check_game_state(game):
        """
        Check if the game has ended or not ; it also sends Message to Displays if the game has ended.
        :param game:
        :return: True if the game continues, False if it has ended
        """
        result = None
        if game.isCheck()==True and game.isGameOver()==False:
            result = "Check!"
            print("\n Check!")
            system('say Check')
        if game.isGameOver():
            print("\n Checkmate!")
            result = "Checkmate!"
            system('say Checkmate')
            if game.getGameResult()==1:
                print("\n White Wins!")
                system('say White Wins')
            if game.getGameResult()==2:
                print("\n Black Wins!")
                system('say Black Wins')
            if game.getGameResult()==3:
                print("\n Draw!")
                system('say Draw due to Stalemate')
            if game.getGameResult()==4:
                print("\n Draw!")
                system('say Draw due to Fifty Moves Rule')
            if game.getGameResult()==5:
                print("\n Draw!")
                system('say Draw due to Three Move Repetition Rule')
            else:
                print("\n Something Unexpected Happened!")

        if result is None:
            print("\n Game moving along...")
            return True
        else:
            return False

def put(command):
    print('\nyou:\n\t'+command)
    engine.stdin.write(command+'\n')

#def level():
#    skill = raw_input("\n Enter computer skill level [0-20]: ").lower()
#    return skill

############
### MAIN ###
############

# assume new game
if __name__ == "__main__":
    
    print ("\n Welcome to the Stockfish Chess Program \n")
    #print('Choose skill level (0-20):')
    #skill=input()
    skill = 0
    #print('Choose computer thinking time in millisecs (Min: 0, Max: 5000, Default: 20)')
    #movetime = input()
    movetime = 20
    fmove = newgame()
    print('\n We will play at skill level' +str(skill)+' and move time '+str(movetime)+'...')
    print('\n You play White. If you would like to play Black, enter ma9a9')
    print('\n Otherwise, enter a legal White move e.g. me2e4')
    print('\n')
    maxchess.printBoard()

    renderer = DrawChessPosition.DrawChessPosition()
    maxfen = maxchess.getFEN()
    fancyboard = renderer.draw(maxfen)
    fancyboard.show()
    maxchess.getTurn()
    
    while True:

        # Get  message from board
        bmessage = getboard()
        # Message options   Move, Newgame, level, style
        code = bmessage[0]
        # decide which function to call based on first letter of txt
        fmove=fmove
        if code == 'm': fmove = bmove(fmove)
        elif code == 'n': newgame()
        #elif code == 'l': level()
        #elif code == 's': style()
        elif code =='q':
            print("Goodbye!")
            #system('say Goodbye.')
            break
        else :  sendboard('error at option')


#Move format:
#------------
#
#The move format is in long algebraic notation (AN).
#A nullmove from the Engine to the GUI should be send as 0000.
#Examples:  e2e4, e7e5, e1g1 (white short castling), e7e8q (for promotion)

#Move examples in this program: m + long AN: me2e4, mb1c3

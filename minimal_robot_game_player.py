from Game import *
from Robot373 import *

def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]

def update_state(state,player,move):
    new_state=state-move
    return new_state

def win_status(state,player):

    if state==1:
        return 'win'
    
    elif state==0:
        return 'lose'
    
    else:
        return None


def get_robot_move(state,player):
    Q=LoadTable(filename='Q_data.json')

    if not state in Q:
        action=random_choice(valid_moves(state,player))
    else:
        action=top_choice(Q[state])

    return action

def wait_for_turn():
    x=input('Hit return to continue')

def do_victory_dance():
    print("yay")


player=1
while True:
    wait_for_turn()   # <=== need to write

    state=read_state()    # <=== need to write

    move=get_robot_move(state,player)

    make_move(state,move)  # does it need the state here?    # <=== need to write

    new_state=update_state(state,player,move)
    status=win_status(state,player)

    if status=='win':
        do_victory_dance()    # <=== need to write
        break
    elif status=='lose':
        do_sad_dance()    # <=== need to write
        break
    elif status=='stalemate':
        do__meh_dance()    # <=== need to write
        break
    else:
        pass

Shutdown()

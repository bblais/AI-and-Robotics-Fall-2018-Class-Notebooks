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
    Q=Remember(filename='Q_data.json')

    if not state in Q:
        action=random_choice(valid_moves(state,player))
    else:
        action=top_choice(Q[state])

    return action


def do_victory_dance():
    print("yay")


player=1
while True:
    wait_for_turn()

    state=read_state()

    move=get_robot_move(state,player)

    make_move(state,move)  # does it need the state here?

    new_state=update_state(state,player,move)
    status=win_status(state,player)

    if status=='win':
        do_victory_dance()
        break
    elif status=='lose':
        do_sad_dance()
        break
    elif status=='stalemate':
        do__meh_dance()
        break
    else:
        pass

Shutdown()

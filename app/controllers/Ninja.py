from random import randrange
import datetime

"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Ninja(Controller):
    def __init__(self, action):
        super(Ninja, self).__init__(action)
 
    def index(self):
        try:
            session['gold']
        except:
            session['gold'] = 100
            session['messages'] = []
        return self.load_view('index.html')

    def process_gold(self):
        timestamp = datetime.datetime.now().strftime('%b %d, %H:%M')
        if request.form['action'] == 'farm':
            earned = randrange(2,16)
            session['gold'] += earned
            message = "You have worked hard on the farm all day, and the farmer generously paid you %s gold for your trouble." %earned
            session['messages'].insert(0,{'message': message, 'timestamp': timestamp})
        elif request.form['action'] == 'cave':
            randnum = randrange(0,2)
            if randnum == 0:
                message = "You entered a cave and meditated all day until a monk came in and kicked you out of what turned out to be his dwelling. 0 gold earned."
                session['messages'].insert(0,{'message': message, 'timestamp': timestamp})
            elif randnum == 1:
                earned = 500
                message = "You found a treasure! %s gold added to your purse." %earned
                session['gold'] += earned
                session['messages'].insert(0,{'message': message, 'timestamp': timestamp})

        elif request.form['action'] == 'wife':
            randnum = randrange(0,2)
            if randnum == 0:
                message = "Shogun saw you strike up a conversation with his wife and sent you off to a remote province. He took all of your gold."
                session['gold'] = 0
            elif randnum == 1:
                earned = randrange(1, 6)
                message = "You have recited your best haiku to Shogun's wife and she was so impressed she gave you some lunch money. %s gold added to your purse." %earned
                session['gold'] += earned
            session['messages'].insert(0,{'message': message, 'timestamp': timestamp})

        elif request.form['action'] == 'dice':
            earned = randrange (-500,1000)
            if earned > 0:
                message= "You have gambled with Shogun all night and you were on your lucky strike! You will be buying Shogun's drinks all next week. %s gold won." %earned
            else:
                message="Luck was not with you tonight and Shogun will be making fun of you the entire week. %s gold lost" %abs(earned)
            session['gold'] += earned
            session['messages'].insert(0,{'message': message, 'timestamp': timestamp})
        return redirect('/')

    def restart(self):
        session.clear()
        return redirect('/')






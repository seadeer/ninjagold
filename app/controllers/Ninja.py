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
        return self.load_view('index.html')

   

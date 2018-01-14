import os

from flask_script import Manager
from zams import app
# use manager to generate command line options
manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('ZAMS_PORT', 8080))
    host = os.environ.get('ZAMS_HOST', '0.0.0.0')
    app.run(host, port)


# admin commands
    
        

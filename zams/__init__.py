import os
from flask import Flask

app = Flask(__name__)

config_path = os.environ.get("ZAMS_CONFIG_PATH", "zams.config.DevelopmentConfig")
app.config.from_object(config_path)

# load api and views before we can handle requests
from . import api
#from . import login # until it's ready
from . import views
from . import filters

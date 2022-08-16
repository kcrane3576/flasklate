import logging
from flask import Flask
from flask.logging import default_handler
from project.home import home_blueprint


# Logger Creation
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log Formatter Creation
formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(process)d:%(thread)d | %(filename)s | %(funcName)s | %(lineno)d | %(message)s')

# Log Stream Handler Creation
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# Instantiate Flask App
app = Flask(__name__)

# Remove Default Flask Logger
app.logger.removeHandler(default_handler)

# Add Flask Bluprints
app.register_blueprint(home_blueprint)

logger.info("Starting App!")

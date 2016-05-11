import gym
import logging
from flask import Blueprint, Flask

logger = logging.getLogger(__name__)

blueprint = Blueprint('envs', '/v1/envs')

class Envs(object):
    def __init__(self):
        self.envs = []

    def create():
        env_id = request.form['env_id']
        env = gym.make(env_id)
        self.envs.append(env)

envs = Envs()
blueprint.route('/', methods=['POST'])(envs.create)

def run():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.run(port=3000)

import os
import sys

from flask.ext.script import Manager, Server, Command

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from notice import app

manager = Manager(app)


# turn on debugger and reloader
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=5000)
)


if __name__ == '__main__':
    manager.run()

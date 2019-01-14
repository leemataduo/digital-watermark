# -*- coding: UTF-8 -*-
from application import create_app

from extentions import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

if __name__ == '__main__':
    flask_app = create_app()

    print(flask_app.url_map)
    migrate = Migrate(flask_app, db)
    manager = Manager(flask_app)
    manager.add_command('db', MigrateCommand)
    manager.run()
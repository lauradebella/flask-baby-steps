from flask_migrate import MigrateCommand
from app import flask, manager

manager.add_command('db', MigrateCommand)
manager.run()

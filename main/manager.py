from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand

from main import app, db

migrate = Migrate()
migrate.init_app(app, db)

cli = FlaskGroup(app)
# cli.add_command('db', MigrateCommand)

if __name__ == '__main__':
    cli()

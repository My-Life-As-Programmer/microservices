import click

from flask import Flask
from flask.cli import with_appcontext
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@click.command(name='create')
@with_appcontext
def create():
    db.create_all()


@click.command(name='db_init')
@with_appcontext
def db_init():
    db.init()


@click.command(name='db_migrate')
@with_appcontext
def db_migrate():
    db.migrate()


@app.route('/')
def index():
    return 'Hello'


app.cli.add_command(create)
app.cli.add_command(db_init)
app.cli.add_command(db_migrate)
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    pass

from flask import Flask
from extensions import db
from init import DBManager
from test import DBTest

def register_extensions(app):
    """
    Register Flask extensions.
    """
    db.init_app(app)
        
    return app

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extensions(app)

    with app.app_context():
        db.create_all() 
        DBManager.clear_db()
        DBManager.init_db()

    return app

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        DBTest.F1()
        DBTest.F2()
        DBTest.F3()
        DBTest.F4()
        DBTest.F5()
        DBTest.F6()
        DBTest.F7()

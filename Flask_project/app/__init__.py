from flask import Flask
from config import Config#从config模块导入Config类
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)#初始化Flask-Login
db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
login = LoginManager(app)
login.login_view = 'login'
from app import routes,models

from flask import Flask
from config import Config#从config模块导入Config类

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
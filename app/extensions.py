from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBaseNoMeta
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from flask_mqtt import Mqtt
from flask_apscheduler import APScheduler


class Base(DeclarativeBaseNoMeta):
    pass


db = SQLAlchemy(model_class=Base)
bootstrap = Bootstrap5()
csrf = CSRFProtect()
mqtt = Mqtt()
scheduler = APScheduler()

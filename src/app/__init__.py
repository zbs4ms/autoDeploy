from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
from app.service import process_service,script_service,task_service

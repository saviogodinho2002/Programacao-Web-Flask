from app_imediagram import app, database
from  app_imediagram.models import Usuario,Foto
#app_diagram import app_imediagram_database, app
with app.app_context():
    database.create_all()
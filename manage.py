from apps import create_app
import settings
from flask_migrate import Migrate, Manager, MigrateCommand

from exts import db
from apps.models.user_model import User

app = create_app(settings.DevelopmentConfig)
manager = Manager(app=app)
# 给manager添加db命令
migrate = Migrate(app=app, db=db)
# 给manager添加command
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
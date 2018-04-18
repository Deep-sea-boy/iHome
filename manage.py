#coding:utf-8

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from iHome import get_app,db

app = get_app('dev')
# # 在迁移时让app和db建⽴关联
Migrate(app,db)
manager = Manager(app)
# 将迁移脚本添加到脚本管理器
manager.add_command('db',MigrateCommand)

@app.route('/',methods=['GET','POST'])
def index():


    return "index"

if __name__ == "__main__":
    manager.run()


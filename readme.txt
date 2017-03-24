python manage.py db
出现
ConfigParser.NoSectionError: No section: 'alembic'
因为还没有python manage.py db init初始化数据库


python manage.py db init
出现alembic.util.CommandError: Directory migrations already exists错误
是因为提前创建了migrations文件目录


# 回调函数，使用指定的标识符加载用户
@login_manager.user_loader

==================================
python hello.py shell
from hello import db
db.drop_all()
db.create_all()

from hello import Role, User

先删除sqlite文件再进行下面操作，不然报错不成功
python hello.py db init
#迁移
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
# 此时发现并不想做这个变更，想要回滚到上一个版本咋办呢，来来来，我教你个大招
python hello.py db downgrade d303dfaaefba，后面这12为数就是上次的数据版本


u = User(email='john@example.com', username='john', password='cat')
db.session.add(u)
db.session.commit()
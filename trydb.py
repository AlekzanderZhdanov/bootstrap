from data import db_session
from data.users import User
from data.news import News
import datetime

db_session.global_init("db/blogs.sqlite")
session = db_session.create_session()

'''user = User()
user.name = "Пользователь 3"
user.about = "биография пользователя 3"
user.email = "email3@email.ru"

session.add(user)
session.commit()'''

'''user = session.query(User).first()
print(user.name)

for user in session.query(User).all():
    print(user)'''

'''for user in session.query(User).filter(User.id > 1, User.email.notlike(("%1%"))):
    print(user)

user = session.query(User).filter(User.id == 1).first()
print(user)
user.name = "Измененное имя пользователя"
user.created_date = datetime.datetime.now()
session.commit()'''

'''user = session.query(User).filter(User.id == 2).first()
session.delete(user)
session.commit()'''

'''session.query(User).filter(User.id >= 3).delete()
session.commit()'''

'''news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
session.add(news)
session.commit()'''

'''user = session.query(User).filter(User.id == 1).first()
news = News(title="Вторая новость", content="Уже вторая запись!",
            user=user, is_private=False)
session.add(news)
session.commit()'''

'''user = session.query(User).filter(User.id == 1).first()
news = News(title="Личная запись", content="Эта запись личная",
            is_private=True)
user.news.append(news)
session.commit()'''

user = session.query(User).filter(User.id == 1).first()
for news in user.news:
    print(news)
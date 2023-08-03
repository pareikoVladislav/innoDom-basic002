# **SQL alchemy**

## **Что такое SQLalchemy и зачем он нужен?**

**SQLalchemy** - это популярная библиотека для работы с базами      
данных в языке программирования **Python**. Он предоставляет       
удобный и высокоуровневый интерфейс для взаимодействия с        
различными **СУБД** (системами управления базами данных),        
такими как **MySQL, PostgreSQL, SQLite, Oracle** и др. **SQLalchemy**         
позволяет разработчикам работать с данными, используя        
**объектно-реляционную модель (ORM)**, что делает код более читаемым       
и упрощает работу с базами данных.

---

## **Основные преимущества использования SQLalchemy для работы с базами данных:**


1. **Единый API** для работы с различными **СУБД**: **SQLalchemy** обеспечивает единый      
интерфейс для взаимодействия с разными **СУБД**. Это позволяет разработчикам     
писать переносимый код, который легко переносить с одной базы данных на      
другую, не изменяя структуру запросов.


2. **ORM** - объектно-реляционное отображение: Одной из ключевых особенностей      
**SQLalchemy** является **ORM**. Он позволяет представлять таблицы базы данных в      
виде классов **Python**, а строки таблиц - в виде объектов. Это упрощает     
работу с данными, так как разработчикам **не нужно писать SQL-запросы вручную**.


3. **Защита от SQL-инъекций:** **SQLalchemy** предоставляет механизмы, которые      
защищают приложение от атак **SQL-инъекций**, автоматически обрабатывая        
пользовательские данные и предотвращая возможность внедрения      
вредоносного **SQL-кода**.


4. **Поддержка транзакций:** **SQLalchemy** поддерживает транзакции, что         
позволяет выполнять несколько операций с базой данных как одну атомарную       
операцию. Если хотя бы одна операция в транзакции не удастся, все        
изменения будут отменены (откат).


5. **Масштабируемость:** **SQLalchemy** предоставляет гибкие возможности для     
работы с большими базами данных и сложными схемами.

---

## **Поддерживаемые СУБД и различия между ними:**

**SQLalchemy поддерживает широкий спектр СУБД:** 

* **SQLite:** Легкая и встраиваемая **СУБД**, идеально подходит для разработки     
прототипов и малых проектов.


* **MySQL:** Популярная реляционная **СУБД** с открытым исходным кодом, широко     
используется в веб-разработке.


* **PostgreSQL:** Мощная и расширяемая объектно-реляционная **СУБД**, часто    
применяется для проектов с высокой производительностью и безопасностью.       


* **Oracle:** Крупная корпоративная **СУБД** с широкими возможностями,        
часто используется в больших предприятиях.


Различия между **СУБД** заключаются в синтаксисе **SQL**, поддержке функций и        
возможностях. **SQLalchemy** абстрагирует эти различия, что позволяет       
писать код, который будет работать с разными **СУБД** без необходимости        
изменения логики.


---

# **Основы работы с базами данных через SQLalchemy:**

1. **Подключение к базе данных (на примере SQLite):**

**SQLalchemy** обеспечивает простой способ подключения к базам данных. Для примера       
рассмотрим подключение к базе данных **SQLite**, которая является встраиваемой      
базой данных, удобной для разработки и тестирования.

Для начала работы с **SQLalchemy**, убедитесь, шо она у вас установлена (`pip install sqlalchemy`)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
```

Создание движка для подключения к БД на основе определённой СУБД:

```python
db_path = 'sqlite:///example.db'  # Путь к файлу базы данных SQLite
engine = create_engine(db_path)
```

2. **Работа с сессиями и транзакциями:**

**SQLalchemy** предоставляет механизм сессий для работы с базой данных. Сессия представляет        
собой некий "буфер" для выполнения операций с базой данных и отслеживания изменений объектов.    

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    surname = Column(String(25), nullable=True)
    age = Column(Integer)
    email = Column(String(35))
    phone = Column(String(20))
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
```

После определения модели можно запихнуть это всё в базу данных, создав таблицу:

```python
Base.metadata.create_all(engine)
```

Так как теперь у нас есть таблица в нашей базе данных, мы можем работать     
с ней через сессии и транзакции. Для этого нужно создать доп объекты:

```python
Session = sessionmaker(bind=engine)
session = Session()
```

И добавить данные в таблицу(транзакция):
name, surname, age, email, phone
```python
def get_datetime():
    cur_time = datetime.now()
    return datetime.strftime(cur_time, "%y-%m-%d %H:%M:%S")
    

def add_users(user_list: list):
    existing_emails = set(session.query(User.email).all())
    existing_phones = set(session.query(User.phone).all())

    new_users = []

    for user in user_list:
        if user.email not in existing_emails and user.phone not in existing_phones:
            user.created_at = get_datetime()
            new_users.append(user)

    session.add_all(new_users)
    session.commit()

add_users(initial_users)
```

**Чтение данных из созданных таблиц:**

```python
users = session.query(User).all()  # Получаем список всех пользователей
for user in users:
    print(user.name, user.surname, user.age, user.email)
```

**Выборка по нескольким параметрам:**

```python
users = session.query(User).where(or_(User.name == "Sam", User.name == "Mike"))  # Получаем список всех пользователей
for user in users:
    print(user.name, user.surname, user.age, user.email)
```

**Выборка по шаблону:**
```python
users = session.query(User).filter(User.email.like("%icloud.com"))  # Получаем список всех пользователей
for user in users:
    print(user.name, user.surname, user.age, user.email)
```

**Обновление данных в таблицe:**

```python
user_to_update = session.query(User).filter_by(name='Oliver').first()
user_to_update.age = 31
session.commit()
```

**Удаление данных из таблицы (транзакция):**

```python
user_to_delete = session.query(User).filter_by(name='Sam').first()
session.delete(user_to_delete)
session.commit()
```

**Закрытие сессии:**

```python
session.close()
```


**Если нужно добавить новое поле?**

### **Добавление изменений через миграции alembic**

* Установить доп библиотеку алембик (`pip install alembic`)
* Инициализация Alembic: `alembic init alembic`(Это создаст директорию       
"alembic" в вашем проекте с файлами конфигурации.)     
* Определить инициализацию скриптов в файле `alembic.ini`:
```python
# alembic.ini
[alembic]
script_location = alembic

# так же найти строчку, где нужно определить url вашего подключения
sqlalchemy.url = sqlite:///example.db
```


* В Файле alembic/env.py добавить строчки:
```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

target_metadata = Base.metadata
```


* Создать новый файл миграции:
```python
alembic revision --autogenerate -m "Add new field"
```
Это создаст новый файл миграции в директории **"alembic/versions"**     
соответствующий вашим изменениям в модели.

* Откройте созданный файл миграции и добавьте в него изменения      
для добавления нового поля в таблицу:
```python
def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('deleted_at', sa.DateTime, default=None))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

```
* Применить миграцию к Базе Данных:
```python
alembic upgrade head
```

Это применит миграцию и добавит новое поле `new_field` в        
таблицу `users` в вашей базе данных.

После выполнения всех шагов, у вас будет успешно выполнена         
миграция, и ваша база данных будет обновлена с новым полем.  


---


### **upgrade():**

Метод **upgrade()** используется для применения к базе данных изменений,     
заданных в файле миграции. При запуске миграции **Alembic** выполняет метод        
**upgrade()** для приведения схемы базы данных в **актуальное состояние**.       
Этот метод обычно содержит операции **SQL** или код манипулирования          
схемой **SQLAlchemy** для создания новых таблиц, изменения существующих         
таблиц, добавления столбцов, модификации данных и т.д. Этот метод         
должен содержать операции, необходимые для возврата изменений        
схемы, внесенных в соответствующем методе **upgrade()**.

### **downgrade():**

Метод **downgrade()** используется для **отмены изменений**, сделанных соответствующим       
методом **upgrade()**. Если необходимо откатить изменения, внесенные в      
результате определенной миграции, **Alembic** выполнит метод **downgrade()**      
для отмены изменений. Этот метод должен содержать операции, необходимые       
для отмены изменений схемы, внесенных в соответствующем методе **upgrade()**.

---


**Alembic** позволяет создавать более         
сложные миграции, включая изменение структуры таблиц,      
добавление новых таблиц и другие операции с базой данных.        
Он предоставляет мощные средства для управления схемой        
базы данных в проекте.

---

## **Запросы на выборку данных из таблиц:**

```python
# Получение всех пользователей из таблицы "users"
all_users = session.query(User).all()

for user in all_users:
    print(f"name: {user.name} | surname: {user.surname} | age: {user.age} | email: {user.email} | phone: {user.phone} |")


# Получение пользователя по имени
user_by_name = session.query(User).filter_by(name='John').first()

# Получение пользователя по имени
user_by_id = session.query(User).filter_by(id=9).first()

# Получение всех пользователей старше 30 лет, отсортированных по возрасту
users_by_age = session.query(User).filter(User.age > 30).order_by(User.age).all()

answer = """
    name: {} |
    surname: {} |
    age: {} |
    email: {} |
    phone: {} |
"""

for user in users_by_age:
    print(answer.format(
        user.name, user.surname,
        user.age, user.email, user.phone
    ))
```

---

## **Нужны ли first() и all()?**
В **SQLAlchemy**, когда требуется выполнить запрос и получить       
только один результат, обычно используется метод **first()**.      
Метод **first()** извлекает первый результат запроса и возвращает     
его в виде одной сущности (или None, если результатов нет).      
Он обычно используется при запросе одной строки по какому-либо       
критерию, например, по идентификатору пользователя.

Если **first()**, или **all()** не указывать, вы будете      
получать объекты: `<sqlalchemy.orm.query.Query object at 0x...>`

---

## **Обновление и удаление данных в таблицах:**

**Обновление**
```python
# Обновление данных пользователя
user_to_update = session.query(User).filter_by(id=10).first()

user_to_update.age = 40
session.commit()
```

**Удаление**
```python
# Удаление пользователя
user_to_delete = session.query(User).filter_by(name='Alice').first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
```

---

## **Создание фикстур для быстрой вставки, быстрая вставка данных**

Для создания фикстуры данных(если вдруг база снесётся \ для более быстрого        
заполнения таблиц)

```python
def datetime_handler(date_field):
    if isinstance(date_field, datetime):
        return date_field.isoformat()
    return date_field


def create_users_fixture():
    existing_users = session.query(User).all()

    users_fixture = [
        {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'age': user.age,
            'email': user.email,
            'phone': user.phone,
            'deleted': user.deleted,
            'created_at': datetime_handler(user.created_at),
            'updated_at': datetime_handler(user.updated_at),
            'deleted_at': datetime_handler(user.deleted_at) if user.deleted_at else None
        } for user in existing_users
    ]

    with open('users_fixture.json', 'w') as fixture_data:
        json.dump(users_fixture, fixture_data, indent=4)


create_users_fixture()
```

Для внесения данных через фикстуру:
```python
def fill_users_data_from_fixture():
    with open('users_fixture.json', 'r') as json_file:
        users_data = json.load(json_file)

        users_objects = [
            User(
                id=user['id'],
                name=user['name'],
                surname=user['surname'],
                age=user['age'],
                email=user['email'],
                phone=user['phone'],
                deleted=user['deleted'],
                created_at=datetime.fromisoformat(user['created_at']),
                updated_at=datetime.fromisoformat(user['updated_at']) if user['updated_at'] else None,
                deleted_at=datetime.fromisoformat(user['deleted_at']) if user['deleted_at'] else None
            ) for user in users_data
        ]

        session.add_all(users_objects)
        session.commit()


fill_users_data_from_fixture()
```

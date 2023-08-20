# **Django models**

При работе с **SQL** мы с вами посмотрели как с помощью таких запросов      
можно создавать таблицы в базе данных, добавлять, удалять и т.д.       
На примере **sqlalchemy** мы посмотрели, как работать с базами данных      
через объекты Python, что значительно удобнее.


В **Django** для работы с базами данных существует уже встроенная **ORM**       


**ORM** – это набор инструментов, которые позволяют через среду языка         
программирования взаимодействовать с БД. 


**Django ORM** адаптирована под многие БД, поэтому синтаксис ORM при       
использовании разных БД не меняется.
В Django работа с базами данных устроена посредством написанием моделей.       

**Models** – это класс, описывающий одну из таблиц в базе данных и        
предоставляющий инструменты для работы с ней: выборки записей, их           
фильтрации, сортировки и пр. Отдельный экземпляр класса модели          
представляет отдельную запись и содержит средства для работы с ней:         
получения значений полей, записи в них новых значений,        
добавления, правки и удаления. 


### **Создание моделей**

Модели объявляются на уровне отдельного приложения, в модуле **models.py** пакета             
этого приложения. Класс модели должен быть производным от класса **Model** из модуля          
**django.db.models**. Также имеется возможность сделать класс модели производным           
от другого класса модели.           

Чтобы модели бьли успешно обработаны программным ядром **Django**, содержащее          
их приложение должно быть зарегистрировано в списке приложений проекта.      
Модель может быть создана для представления как еще не существующей в базе         
таблицы (тогда для ее создания следует сгенерировать миграцию), так и уже          
имеющейся (в этом случае при объявлении модели придется дополнительно указать         
имя таблицы и имена всех входящих в нее полей).            
 
**Название класса** служит названием таблицы. Все поля, существующие в       
SQL, доступны в классе и являются его переменными, они также     
импортируются из `django.db.models`.      


```python
from django.db import models


class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=255)
```


Некоторых полей, существующих в **ORM**, не существует в БД, например,      
**EmailField**, однако это абстракция, которая защищена валидацией и     
на самом деле являющиеся типом **VarChar**

---

# **Объявление полей модели**

Для представления отдельного поля таблицы в модели создается атрибут класса,        
которому присваивается экземпляр класса, представляющего поле нужного типа       
(строкового, целочисленного, логического и т. д.). Дополнительные параметры          
создаваемого поля указываются в соответствующих им именованных параметрах          
конструктора класса поля.


## **Параметры, поддерживаемые полями всех типов:**

* `verbose_name` - человекочитаемое название поля, которое будет выводиться         
на вэбстраницах. Если не указано - будет выводиться имя поля.
* `help_text` - доп поясняющий текст, выводимый на экран. По умолчанию - пустая    
строка. Содержащиеся в этом тексте спец символы HTML не преобразуются            
в литералы и выводятся как есть. Это позволяет отформатировать поясняющий текст        
HTML-тегами.
* `default` - значение по умолчанию, записываемое в поле, если в него явно не было        
занесено никакого значения. Может быть указано двумя способами:
    1) Как обычное значение любого неизменяемого типа:
       `is_active = models.BooleanField(default=True)` если в качестве значения по умолчанию          
        должно выступать значение изменяемого типа(список\словарь Python), то для            
        указания следует использовать второй способ.
    2) Как ссылка на функцию, вызываемую при создании каждой новой записи и возвращающую         
       в качествве результата заносимое в поле значение:
        ```python
            def is_active_default():
                return not is_all_posts_passive
            ...
            ...
       
            is_active = models.BooleanField(default=is_active_default)
        ```
* `unique` - если True, то в текущее поле может быть занесено только уникальное в пределах             
таблицы значение. При попытке занести значение, уже имеющееся в том же поле другой записи        
будет возбуждено оисключение **IntegrityError** из модуля `django.db`.
Если поле помечено как уникальное, по нему будет автоматически создан индекс. Поэтому явно   
задавать для него индекс не нужно. Если значение у параметра - False, то текущее поле может        
хранить любое значение. По умолчанию значение - False.

* `unique_for_date` - если в этом параметре указать представленное в виде строки имя поля даты       
(DateField) или даты и времени(DatetimeField), то текущее поле может хранить только значения,      
уникальные в пределах даты, которая хранится в указаном поле:
```python
title = models.Charfield(max_length=50, unique_for_date='published')
published = models.DatetimeField()
```

В этом случае Django позволит сохранить в поле title только значения, уникальные в пределах         
даты, хранящейся в поле published.

* `unique_for_month` - Тоже самое, что и unique_for_date, только в расчёт берётся не всё значение        
даты, а только месяц.
* `unique_for_year` - Тоже самое, что и unique_for_date, только в расчёт берётся не всё значение        
даты, а только год.
* `null` - если **True**, то поле в таблице базе данных может хранить значение **null** и, таким       
образом, являться необязательным к заполнению. Если **False**, то поле в таблице должно иметь         
хотя бы какое-то значение, даже пустую строку. По умолчанию значение False.

# !!ВАЖНО
У строковых и текстовых полей, даже обязательных к заполнению (т.е. при их объявлении         
параметру null было присвоено значение False), вполне допустимое значение - пустая строка.       
Если сделать поля необязательным к заполнению, задав True для параметра null, то они в дабавок          
к этому могут хранить значение null. Оба значения фактически представляют отсутствие каких-либо        
данных в поле, и эту ситуацию придётся как-то обрабатывать. Поэтому чтобы           
упростить обработку отсутствия значения в таком поле, его не стоит делать необязательным к заполнению.        
Параметр null затрагивает только поле таблицы, но не поведение Django. Даже если какое-то поле        
присвоением параметру значения True было помечено как необязательное, фреймворк по умолчанию        
всё ровно не позволит занести в него пустое значение.

* `blank` - если True, то Django позволит занести в поле пустое значение, тем самым сделав поле          
необязательным к заполнению, если False - не позволит. По умолчанию False. Параметр blank задаёт         
поведение самого фреймворка при выводе на экран вэб-форм и проверке ввёденных в них данных. Если этому        
параметру дано значение True, то Django позволит занести в поле пустое значение (например для строкового        
поля пустую строку), даже если это поле было помечено как обязательное к заполнению

* `db_index` - если True, то по текущему полю в таблице будет создан индекс. Если Fasle - не будет. По           
умолчанию False.

* `primary_key` - если True, указаное поле станет ключевым. Такое поле          
будет помечено, как обяательное к заполнению и уникальное, по нему будет       
создан ключевой индекс. Если False - то поле не будет преобразовано                 
в ключевое. Значение по умолчанию - False. Если ключевое поле         
в модели не было заявлено явно, сам фреймворк создаст в ней           
целочисленное, автозаполняемое ключевое поле с именем id

* `editable` - если True, то поле будет выводиться на экран в составе формы,        
если False - не будет (даже если явно создать его в форме). По умолчанию True.   

* `db_column` - имя поля таблицы в виде строки. Если не указано, то поле        
таблицы получит то же имя, что и поле модели.

---

# **Классы полей моделей**

Все классы полей, поддерживаемые **Django**, объявлены в модуле **django.db.models**.          
Каждое такое поле позволяет хранить значения определенного типа. Многие типы        
полей поддерживают дополнительные параметры, также описанные далее.        


* **CharField** - строковое поле, хранящее строку ограниченной длины. Занимает          
в базе данных объем, необходимый для хранения числа символов, указанного          
в качестве размера этого поля. Поэтому, по возможности, лучше не создавать             
в моделях строковые поля большой длины.          
Обязательный параметр **max_length** указывает максимальную длину заносимого           
в поле значения в виде целого числа в символах.            


* **textField** - текстовое поле, хранящее строку неограниченной длины. Такие         
поля рекомендуется применять для сохранения больших текстов, длина которых          
заранее не известна и может варьироваться.              
Необязательный параметр **max_length** задает максимальную длину заносимого             
в поле текста. Если не указан, то в поле можно записать значение любой длины. 

  
* **EmailField** - адрес электронной почты в строковом виде.              
Необязательный параметр **max_length** указывает максимальную длину заносимого           
в поле адреса в виде целого числа в символах. Значение по умолчанию: **254**.          


* **URLField** - интернет-адрес.
Необязательный параметр **max_length** указывает максимальную длину заносимого         
в поле интернет-адреса в виде целого числа в символах. Значение по умолчанию: **200**.        


* **SlugField** - слаг, т. е. строка, однозначно идентифицирующая запись и включаемая         
в состав интернет-адреса. Поддерживает два необязательных параметра:         
    1. **max_length** - максимальная длина заносимой в поле строки в символах.      
    По умолчанию: **50**. 
    2. **allow_unicode** - если тrue, то хранящийся в поле слаг может содержать          
    любые символы **Unicode**, если **False** - только символы из кодировки **ASCII**.           
    По умолчанию - **False**

Дпя каждого поля такого типа автоматически создается индекс, поэтому указывать        
параметр **db_index** со значением **True** нет нужды.          


* **BooleanField** - логическое поле, хранящее значение **True** или **False**.              
```
ВНИМАНИЕ!
Значение поля booleanField по умолчанию - None, а не False, как можно было бы
предположить. 
```
Дпя поля этого типа можно указать параметр **null** со значением **True**, в          
результате чего оно получит возможность хранить еще и значение **null**.

* **NullBooleanField** - то же самое, что **BooleanField**, но дополнительно            
позволяет хранить значение **null**. Этот тип поля оставлен для           
совместимости с более старыми версиями **Django**, и использовать его во          
вновь разрабатываемых проектах не рекомендуется.    


* **IntegerField** - знаковое целочисленное поле обычной длины(32-разрядное).          


* **SmallintegerField** - знаковое целочисленное поле половинной длины (16-разрядное).        


* **BigintegerField** - знаковое целочисленное значение двойной длины (64-разрядное).       


* **PositiveIintegerField** - беззнаковое целочисленное поле обычной длины (32-разрядное ).


* PositiveSmallIntegerField - беззнаковое целочисленное поле половинной длины (16-разрядное ).


* **FloatField** - вещественное число.


* **DecimalField** - вещественное число фиксированной точности, представленное         
объектом типа **Decimal** из модуля **decimal** **Python**. Поддерживает два               
обязательных параметра:       
    1. **max_digits** - максимальное количество цифр в числе;      
    2. **decimal _places** - количество цифр в дробной части числа.        

Пример объявления поля для хранения чисел с шестью цифрами в целой              
части и двумя - в дробной:     

```python
price = models.DecimalField(max_digits=8, decimal_places=2)
```


* **DateField** - значение даты в виде объекта типа date из модуля            
**datetime Python**.
Класс **DateField** поддерживает два необязательных параметра:           
    1. **auto_now** - если **True**, то при каждом сохранении записи в         
    поле будет заноситься текущее значение даты. Это может использоваться          
    для хранения даты последнего изменения записи.       
    Если **False**, то хранящееся в поле значение при сохранении           
    записи никак не затрагивается. Значение по умолчанию - **False**;       

    2. **auto_now_add** - то же самое, что **auto_now**, но        
    текущая дата заносится в поле только при создании записи и при последующих        
    сохранениях не изменяется.          
    Может пригодиться для хранения даты создания записи.         

Указание значения **True** для любого из этих параметров приводит к тому, что          
поле становится невидимым и необязательным для заполнения на уровне **Django**       
(т.е. параметру **editable** присваивается **False**, а параметру **blank** - **True**).           


* **DateTimeField** - то же самое, что и **DateField**, но хранит значение временной         
отметки в виде объекта типа **datetime** из модуля **datetime**.        


* **TimeField** - значение времени в виде объекта типа **time** из модуля      
**datetime Python**. Поддерживаются необязательные параметры **auto_now**           
и **auto_now_add** (см. описание класса **DateField**).          


* **DurationField** - промежуток времени, представленный объектом типа **timedelta**         
из модуля **datetime Python**.            


* **BinaryField** - двоичные данные произвольной длины. Значение этого поля          
представляется объектом типа **bytes**.         


* **GenericIPAddressField** - IР-адрес, записанный для протокола **1Pv4** или **1Pv6**,          
в виде строки. Поддерживает два необязательных параметра:               
    1. **protocol** - обозначение допустимого протокола для записи IР-адресов,         
    представленное в виде строки. Поддерживаются значения "IPv4 ", "IPvб" и "both"          
    (поддерживаются оба протокола). По умолчанию - "both"      
    2. **inpack_ipv4** - если **True**, то IР-адреса протокола IPv4, записанные в формате            
    IPv6, будут преобразованы к виду, применяемому в IPv4. Если **False**, то такое      
    преобразование не выполняется. Значение по умолчанию - **False**. Этот параметр          
    принимается во внимание только в том случае, если для параметра           
    protocol указано значение "both".          


* **AutoField** - автоинкрементное поле. Хранит уникальные, постоянно             
увеличивающиеся целочисленные значения обычной длины (32-разрядные).        
Практически всегда используется в качестве ключевого поля.            
Как правило, нет необходимости объявлять такое поле явно. Если модель не           
содержит явно объявленного ключевого поля любого типа, то **Django**         
самостоятельно создаст ключевое поле типа **AutoField**.            


* **SmallAutoField** - то же самое, что **AutoField**, но хранит             
целочисленное значение половинной длины (16-разрядное).           


* **BigAutoField** - то же самое, что **AutoField**, но хранит целочисленное значение         
двойной длины (64-разрядное).            


* **UUIDField** - уникальный универсальный идентификатор, представленный объектом         
типа uui из модуля **UUID** Python, в виде строки.          

Поле такого типа может использоваться в качестве ключевого вместо поля          
**AutoField**, **SmallAutoField** или **BigAutoField**. Единственный недостаток: придется           
генерировать идентификаторы для создаваемых записей самостоятельно.            
Вот пример объявления поля **UUIDField**:         

```python
import uuid
from django.db import models

class Bb(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        editable=False) 
```




---

# **Создание связей между моделями**

Связи между моделями создаются объявлением в них полей, формируемых           
особыми классами из того же модуля `django.db.models`  


Существует несколько способов связывания:      
* **ForeignKey** (Один ко многим)
* **ManyToManyField** (Многие ко многим)
* **OneToOneField** (Один к одному)



1) **Связь "один-со-многими"**

Связь "один-со-многими" связывает одну запись первичной модели с          
произвольным числом записей вторичной модели. Это наиболее часто          
применяемый на практике вид связей. Для создания связи такого типа            
в классе вторичной модели следует объявить поле типа ForeignКey.

```python
FоrеingКеу(<связываемая первичная модель>,
    оn_dеlеtе=<поведение при удалении записи>, [<остальные параметры>])
```

Первым, позиционным, параметром указывается связываемая первичная модель в виде:         
* непосредственно ссылки на класс модели, если объявление первичной модели          
находится перед объявлением вторичной модели (в которой и создается поле внешнего ключа):       
```python
class Rubric(models.Model):
  ...


class Bb(models.Model):
  rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT)
  ...
```

* строки с именем класса, если первичная модель объявлена после вторичной:       
```python
class Bb(models.Model):
  rubric = models.ForeignKey('Rubric', on_delete=models.PROТECT)
  ...


class Rubric(models.Model): 
  ...
```
Ссылка на модель из другого приложения проекта записывается в виде строки формата          
`<имя прwюжения>.<имя класса модели>`


Если нужно создать модель, ссылающуюся на себя (создать рекурсивную связь), то              
первым параметром конструктору следует передать строку `self`:

```python
parent_rubric = models.ForeingKey('self', on_delete=models.PROTECТ)
```

Вторым параметром `on_delete` указывается поведение фреймворка в случае,          
если будет выполнена попытка удалить запись первичной модели, на которую          
ссылаются какие-либо записи вторичной модели. Параметру присваивается        
значение одной из переменных, объявленных в модуле `django.db.models`:

* `CASCADE` - удаляет все связанные записи вторичной модели (каскадное удаление).


* `PROTECT` - возбуждает исключение ProtectedError из модуля django.db.models,         
тем самым предотвращая удаление записи первичной модели.


* `SET_NULL` - заносит в поле внешнего ключа всех связанных записей вторичной          
модели значение null. Сработает только в том случае, если поле внешнего ключа          
объявлено необязательным к заполнению на уровне базы данных           
(параметр`null` конструктора поля имеет значение True).


* `SET_DEFAULT` - заносит в поле внешнего ключа всех связанных           
записей вторичной модели заданное для него значение по умолчанию.          
Сработает только в том случае, если у поля внешнего ключа бьmо         
указано значение по умолчанию (оно задается параметром        
default конструктора поля).


* `SET(<значение>)` - заносит в поле внешнего ключа указанное значение          

```python
rubric = models.ForeingKey(Rubric, on_delete=models.SET(1))
```
Также можно указать ссылку на функцию, не принимающую          
параметров и возвращающую значение, которое будет записано в поле:


```python
def get_first_rubric():
  return Rubric.objects.first()

...

rubric = models.ForeingKey(Rubric, on_delete=models.SET(get_first_rubric)) 
```

* `DO_NOTНING` - ничего не делает.


```python
"""
ВНИМАНИЕ!
Если СУБД подцерживает межтабличные связи с сохранением ссылочной      
целостности, то попытка удаления записи первичной модели, с которой        
связаны записи вторичной модели, в этом случае все равно не увенчается         
успехом, и будет возбуждено исключение IntegrityError из модуля django.dЬ.models.
"""
```

Полю внешнего ключа рекомендуется давать имя, обозначающее связываемую сущность          
и записанное в единственном числе. Например, для представления рубрики в модели          
`bb` мы объявили поле `rubric`. На уровне базы данных поле внешнего ключа модели        
представляется полем таблицы, имеющим имя вида `<имя поля внешнего ключа>_id`.          
В веб-форме такое поле будет представляться раскрывающимся списком,          
содержащим строковые представления записей первичной модели. 


Класс `ForeignКey` поддерживает следующие дополнительные необязательные параметры:

* `limit_choices_to` - позволяет вывести в раскрывающемся списке записей первичной        
модели, отображаемом в веб-форме, только записи, удовлетворяющие заданным      
критериям фильтрации. Критерии фильтрации записываются в виде словаря Python,         
имена элементов которого совпадают с именами полей первичной модели,      
по которым должна выполняться фильтрация, а значения элементов укажут значения        
для этих полей. Выведены будут записи, удовлетворяющие всем критериям, заданным в       
таком словаре (т. е. критерии объединяются по правилу логического И). Для примера         
укажем Django выводить только рубрики, поле show которых содержит значение True:


```python
rubric = models.ForeignКey(Rubric, on_delete=models.PROTECT,
    limit_choices_to={'show': True})
```

Если параметр не указан, то список связываемых записей будет включать все записи первичной модели

* `related_name` - имя атрибута записи первичной модели, предназначенного для доступа к          
связанным записям вторичной модели, в виде строки:

```python
class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT,
        related_name='entries')
# Получаем первую рубрику
first_rubric = Rubric.objects.first()
# Получаем доступ к связанным объявлениям через атрибут entries ,
# указанный в параметре related_name
bbs = first_rubric.entries.all() 
```

Если доступ из записи первичной модели к связанным записям вторичной модели не требуется,        
можно указать Django не создавать такой атрибут и тем самым немного сэкономить системные           
ресурсы. Для этого достаточно присвоить параметру `related_name` символ "плюс".            
Если параметр не указан, то атрибут такого рода получит стандартное          
имя вида `<имя связанной вторичной модели>_sеt`


* `related_query_name` - имя фильтра, которое будет применяться во вторичной модели        
для фильтрации по значениям из записи первичной модели

```python
class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT,
        related_query_name='entry')
...
# Получаем все рубрики, содержащие объявления о продаже домов,
# воспользовавщись фильтром, заданным в параметре related_query_name
rubrics = Rubric.objects.filter( entry_title='Дoм') 
```

Если параметр не указан, то фильтр такого рода получит стандартное имя, совпадающее         
с именем класса вторичной модели.

* `to_field` - имя поля первичной модели, по которому будет выполнена связь, в виде строки.         
Такое поле должно быть помечено как уникальное (параметр `unique` конструктора должен        
иметь значение True). Если параметр не указан, связывание выполняется по ключевому           
полю первичной модели - неважно, созданному явно или неявно


* `db_constraint` - если True, то в таблице базы данных будет создана связь, позволяющая        
сохранять ссылочную целостность; если False, ссылочная целостность будет поддерживаться            
только на уровне Django. Значение по умолчанию - True. Менять его на False имеет смысл,          
только если модель создается на основе уже существующей базы с некорректными данными.

2) **Связь "многие-со-многими"**

Связь "многие-со-многими" соединяет произвольное число записей одной модели              
с произвольным числом записей другой (обе модели здесь выступают как равноправные,              
и определить, какая из них первичная, а какая вторичная, не представляется возможным).             
Для создания такой связи нужно объявить в одной из моделей (но не в обеих сразу!)           
поле внешнего ключа типа `ManyToManyField`. Вот формат его конструктора:

```python
ManyТoManyField(<вторая связываемая модель>, [<остальные параметры>])
```

Первый параметр задается в таком же формате, что и в конструкторах классов        
`ForeignField` и `OneToOneField`.

Модель, в которой было объявлено поле внешнего ключа, назовем ведущей,      
а вторую модель - ведомой. Для примера создадим модели machine и spare,           
из которых первая, ведущая, будет хранить готовые машины, а вторая, ведомая,       
- отдельные детали для них.

```python
class Spare(models.Model):
  name = models.CharField(max_length=ЗO)

class Machine(models.Model):
  name = models.CharField(max_length=ЗO)
  spares = models.ManyТoManyField(Spare) 
```

В отличие от связей описанных ранее типов, имя поля, образующего связь          
"многие-со-многими", рекомендуется записывать во множественном числе.           
Что и логично - ведь такая связь позволяет связать произвольное Число          
записей, что называется, с обеих сторон. На уровне базы данных для          
представления связи такого типа создается таблица, по умолчанию         
имеющая имя вида `<псевдоним приложения>_<имя класса ведущей модели>_<имя класса ведомой модели>`        
(связующая таблица). Она будет иметь ключевое поле id и по одному полю      
с именем вида `<имя класса связываемой модели>_id` на каждую из связываемых         
моделей. Так, в нашем случае будет создана связующая таблица с именем       
`samplesite_machine_spare`, содержащая поля `id`, `machine_id` и `spare_id`.          

Если создается связь с той же самой моделью, связующая таблица будет           
иметь поля id, `from _<имя класса модели>_id` И `to_<имя класса модели>_id`.          
Конструктор класса `ManyТoManyField` поддерживает дополнительные необязательные         
параметры `limit_choices_to`, `related_name`, `related_query_name` и `db_constraint`, а также:

* `symmetrical` - используется только в тех случаях, когда модель связывается сама с собой.      
Если True, Django создаст симметричную связь, действующую в обоих направлениях (применительно       
к нашему случаю: если какая-то деталь А входит в машину Б, то машина Б содержит деталь А).      
Если False, то связь будет асимметричной (чисто гипотетически: Иванов любит колбасу, однако         
колбаса не любит Иванова). Значение по умолчанию - True. Для асимметричной связи         
Django создаст в классе модели атрибут для доступа к записям связанной модели в       
обратном направлении


* `through` - класс модели, которая представляет связующую таблицу (связующая модель) либо в       
виде ссылки, либо в виде имени, представленном строкой. Если класс не указан, то связующая       
таблица будет создана самим Django. При использовании связующей модели нужно иметь в виду следующее:

  1) поле внешнего ключа для связи объявляется и в ведущей, и в ведомой моделях. При создании       
  этих полей следует указать как саму связующую модель (параметр through), так и поля внешних          
  ключей, по которым будет установлена связь (параметр through_fields, описанный далее);
  2) в связующей модели следует явно объявить поля внешних ключей для установления связи с           
  обеими связываемыми моделями: и ведущей, и ведомой


* `through_fields` - используется, если связь устанавливается через связующую модель,        
записанную в параметре `through` конструктора. Указывает поля внешних ключей, по которым      
будет создаваться связь. Значение параметра должно представлять собой кортеж из двух       
элементов: имени поля ведущей модели и имени поля ведомой модели, записанных в виде строк.         
Если параметр не указан, то поля будут созданы самим фреймворком.


* `db_table` - имя связующей таблицы. Обычно применяется, если связующая модель не используется.        
Если оно не указано, то связующая таблица получит имя по умолчанию


---

# **Параметры самой модели**

Параметры самой модели описываются различными атрибутами класса `Meta`, вложенного в класс        
модели и не являющегося производным ни от какого класса.

* `verbose_name` - название сущности, хранящейся в модели, которое будет выводиться на экран.       
Если не указано, используется имя класса модели.


* `verbose_name_plural` - название набора сущностей, хранящихся в модели, которая будет выводиться       
на экран. Если не указано, используется имя класса модели во множественном числе.


* `ordering` - параметры сортировки записей модели по умолчанию. Задаются в виде последовательности        
имен полей, по которым должна выполняться сортировка, представленных строками. Если перед именем         
поля поставить символ "минус", то порядок сортировки будет обратным. Пример:

```python
class Bb(models.Model):
    class Meta:
        ordering =['-published', 'title'] 
```

Сортируем записи модели сначала по убыванию значения поля puЬlished, а потом по       
возрастанию значения поля title.

* `unique_together` - последовательность имен полей, представленных в виде строк, которые          
должны хранить уникальные в пределах таблицы комбинации значений. При попытке занести в них        
уже имеющуюся в таблице комбинацию значений будет возбуждено исключение `ValidationError`         
из модуля `django.core.exceptions`. Пример:

```python
class Bb(models.Model):
    class Meta:
        unique_together = ('title' , 'published') 
```

Теперь комбинация названия товара и временной отметки публикации объявления должна быть уникальной          
в пределах модели. Добавить в тот же день еще одно объявление о продаже того же товара не получится.           
Можно указать несколько подобных групп полей, объединив их в последовательность:

```python
class Bb(models.Model):
    class Meta:
        unique_together = (('title' , 'published'), ( 'title', 'price', 'rubric'))
```

Теперь уникальными должны быть и комбинация названия товара и временной отметки        
публикации, и комбинация названия товара, цены и рубрики.

* `get_latest_by` - имя поля типа `DateField`, или `DateTirneField`, которое будет         
ВЗЯТО в расчет при получении наиболее поздней или наиболее ранней записи с         
помощью метода `latest()` или `earliest()` соответственно, вызванного       
без параметров. Можно задать:
  1) имя поля в виде строки - тогда в расчет будет взято только это поле:
    ```python
      class Bb(models.Model):
        ...
        published = models.DateTimeField() 
        class Meta:
            get_latest_by = 'published'
    ```
    Теперь метод `latest()` вернет запись с наиболее поздним значением временной отметки,    
    хранящемся в поле published. Если имя поля предварить символом "минус", то порядок       
    сортировки окажется обратным, и при вызове `latest()` мы получим, напротив, самую          
    раннюю запись, а при вызове метода `earliest()` - самую позднюю.

  2) последовательность имен полей - тогда в расчет будут взяты значения всех этих       
  полей, и, если у каких-то записей первое поле хранит одинаковые значения,       
  будет проверяться значение второго поля и т. д.       
  
  ```python
    class Bb(models.Model):
      ...
      added = models.DateTirneField() 
      published = models.DateTirneField() 
      
      class Meta:
          get_latest_by =  ['edited', 'published'] 
  ```

* `order_with_respect_to` - позволяет сделать набор записей произвольно           
упорядочиваемым. В качестве значения параметра задается строка с именем        
поля текущей модели, и в дальнейшем записи, в которых это поле хранит одно и          
то же значение, могут быть упорядочены произвольным образом. Пример:       

```python
class Bb(models.Model):
      ...
      rubric = models.ForeignKey('Rubric')  
      
      class Meta:
            order_with_respect_to = 'rubric'
```

Теперь объявления, относящиеся к одной и той же рубрике, могут быть переупорядочены       
произвольным образом. При указании в модели этого параметра в таблице будет        
дополнительно создано поле с именем вида `<имя поля, заданного в качестве значения параметра>_оrdеr`.          
Оно будет хранить целочисленное значение, указывающее порядковый номер текущей записи в последовательности.         
Одновременно вновь созданное поле с порядковым номером будет задано в качестве значения параметра         
`ordering`. Следовательно, записи, которые мы извлечем из модели, по умолчанию будут отсортированы           
по значению этого поля. Указать другие параметры сортировки в таком случае будет невозможно.

* `indexes` - последовательность индексов, включающих в себя несколько полей. Каждый          
элемент такой последовательности должен представлять собой экземпляр класса `Index`        
из модуля `django.db.models`

```python
class Bb(models.Model):
       ...
       class Meta:
         indexes = [
           models.Index(fields=['-published', 'title'],
                name='bb_main'),
           models.Index(fields=['title', 'price', 'rubric']), 
         ]
```

В параметре `fields` указывается список или кортеж строк с именами полей, которые          
должны быть включены в индекс. По умолчанию сортировка значений поля выполняется             
по их возрастанию, а чтобы отсортировать по убыванию, нужно предварить имя поля            
знаком "минус". Параметр name задает имя индекса - если он не указан, то имя         
будет создано самим фреймворком.

* `index_together` - предлагает другой способ создания индексов, содержащих несколько полей.        
Строки с именами полей указываются в виде последовательности, а набор таких          
последовательностей также объединяется в последовательность.

```python
class Bb(models.Model):
      ...
      class Meta:
        index_together = [
          ['-published', 'title'],
          ['title', 'price', 'rubric']
        ]
```

* `default_related_name` - имя атрибута записи первичной модели,         
предназначенного для доступа к связанным записям вторичной модели, в виде строки.      
Соответствует параметру `related_name` конструкторов классов полей, предназначенных        
для установления связей между моделями. Неявно задает значения параметрам        
`related_name` и `related_query_name` конструкторов


* `db_tablе` - имя таблицы, в которой хранятся данные модели.          
Если оно не указано, то таблица получит имя вида `<псевдоним приложения>_<имя класса модели>`.         
Например, для модели bb приложения bboard в базе данных будет создана таблица `bbоаrd_db`


* `constraints` - условия, которым должны удовлетворять данные, заносимые в запись.          
В качестве значения указывается список или кортеж экземпляров классов,          
каждый из которых задает одно условие.

---

# **Методы моделей**


Модели могут включать в себя различные методы:

*  `__str__()` определяет строковое представление объекта модели.     
Он возвращает строку, которая будет использоваться при приведении       
объекта к строке, например, при выводе в административном      
интерфейсе Django или в консоли.     


* `__repr__()` определяет представление объекта модели в виде     
строки, которое будет использоваться для отладки и внутренних целей.      
Обычно он возвращает строку, содержащую имя класса модели и        
некоторую информацию о состоянии объекта        


*  `__init__()` выполняется при создании нового экземпляра модели.     
Он позволяет инициализировать поля модели и выполнить другие       
необходимые действия перед сохранением объекта.       


* `save()` вызывается при сохранении объекта модели. Он       
выполняет операцию создания или обновления записи в базе данных.     
Можно переопределить этот метод для выполнения дополнительных          
действий перед сохранением или после сохранения объекта      


* `delete()` вызывается при удалении объекта модели. Он удаляет       
соответствующую запись из базы данных. Можно так же переопределить       
этот метод для выполнения дополнительных действий перед удалением       
объекта или после удаления         


* `get_absolute_url()` возвращает URL-адрес объекта модели. Этот      
метод часто используется в шаблонах или при редиректах для       
получения URL-адреса объекта       


* `clean()` выполняется при валидации объекта модели. Он        
позволяет выполнять пользовательскую валидацию полей модели и    
вызывать ошибки валидации при необходимости.         


* Если у поля модели есть аргумент `choices`, то автоматически создается         
метод `get_<field>_display()`, который возвращает текстовое        
представление выбранного значения из списка `choices`.    

---

# **Миграции**

Очень хитрая, крутая и мощная штука в Django!

После создания модели, её следует мигрировать из рабочего     
пространства **Django** в подключённую БД. Когда происходит любое         
изменение моделей, следует проводить миграции.   


Для создания миграций используется команда `makemigrations`, а для их          
применения `migrate`. При выполнении миграций **Django** создаёт         
дополнительные модели для правильной работы приложения, а также       
автоматически создаёт стандартную таблицу **Users**, и в следствии       
создания кастомной таблицы пользователей её следует переопределить,      
чтобы избежать конфликтов БД. 

Для этого в настройках проекта указывается строка:      

```python
AUTH_USER_MODEL = '<app_name>.models.User'
```

В кавычках указывается ссылка до модели (название приложения.модель)


Для создания миграций используем `python manage.py makemigrations`
Для применения миграций `python manage.py migrate`
Для того, чтобы посмотреть применённые миграции, требуется в консоли     
выполнить `python manage.py showmigrations`
В случае ошибки с миграциями в приложении, их можно откатить
используя `python manage.py migrate <app_name> zero` 

Для того, чтобы откатить полностью `python manage.py migrate
<app_name> <номер_миграции_до_которой_нужно_откатить>`

# !!!! при откате миграции, которая затрагивает другие таблицы,
(например, в случае связи между таблицами) связные миграции откатятся
тоже.

---

# **Панель администратора Django**

Django автоматически создаёт админ панель вашего веб-приложения, в        
которой можно администрировать БД. За панель администратора      
отвечает файл `admin.py` в приложении. Админ-панель доступна по `адресу         
вашей страницы+/admin`       

```python
from django.contrib import admin
from .models import User, Course


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
```

Для регистрации используется декоратор **register** (это один из вариантов регистрации)

### Для получения доступа входа в админ панель требуется
создать суперпользователя: `python manage.py createsuperuser`


## Чем удобен вариант регистрирования моделей через декоратор?

Он позволяет нам добавлять доп функционал при работе с нашими моделями:
добавить какие-то действия, фильтры, отображения определённых полей и т.д.

```python
from django.contrib import admin
from .models import User, Course


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'is_superuser') # отображение доп полей модели
    list_filter = ('email', 'phone') # фильтры
    search_fields = ('email',) # Поиск

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
```
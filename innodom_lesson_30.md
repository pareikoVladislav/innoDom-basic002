# **Django Rest Framework**

### **REST API**

**REST API (Representational State Transfer Application Programming Interface)** -             
это стиль архитектуры программного обеспечения, который определяет           
правила и соглашения для построения веб-сервисов. 

**REST API** позволяет взаимодействовать с веб-приложениями и           
сервисами с использованием стандартных `HTTP` методов, таких          
как `GET`, `POST`, `PUT`, `DELETE` и других.            


Все элементы в `REST API` представляются в виде ресурсов, которые            
могут быть, например, объектами, БД, файлами или любыми другими              
сущностями. Каждый ресурс имеет уникальный идентификатор (`URI`), по           
которому к нему можно обращаться.              


Ресурсы предоставляются в различных форматах представления данных,           
таких как `JSON`, `XML`, `HTML`, и др. Клиент может запросить конкретное          
представление, указав заголовок Accept с нужным типом данных.            


Каждый запрос к серверу в `REST API` содержит всю необходимую                 
информацию для его обработки. Сервер не хранит состояние клиента              
между запросами. Т.е. каждый запрос должен содержать всю необходимую             
информацию для выполнения операции                 


## **Endpoints**

`Endpoints (точки входа)` в контексте веб-разработки и `REST API`                
представляют собой конечные точки `URL`, по которым клиенты могут                
отправлять `HTTP-запросы` для взаимодействия с приложением или вебсервисом.               


Это конкретные `URL-адреса`, которые определяют, какие ресурсы и операции могут              
быть доступны через `API`. Когда клиенты отправляют `HTTP-запросы` на определенный            
`endpoint`, сервер обрабатывает запрос и возвращает результат в соответствии с                   
заданной логикой приложения.                     

`REST API` обычно имеет много различных `endpoints` для разных типов                    
ресурсов и операций. Все эти `endpoints` совместно образуют интерфейс                   
`API`, через который клиенты могут взаимодействовать с сервером и                 
выполнять различные задачи и операции.                 


---

## **DRF (Django Rest Framework)**

Это мощный инструмент, разработанный для создания `веб-API` на основе фреймворка `Django`.               
Он предоставляет набор инструментов и функций, упрощающих разработку `API`, а также             
обеспечивает множество возможностей для управления данными, авторизации,            
аутентификации и многого другого.

### **Что такое DRF и зачем он нужен?**

**Django Rest Framework (DRF)** - это библиотека `Python`, предназначенная для          
создания `веб-API` с использованием фреймворка `Django`. Он обеспечивает инструменты           
для преобразования данных модели `Django` в `JSON` или другие форматы, которые          
могут быть использованы для обмена данными с другими приложениями,           
веб-сервисами или фронтенд-клиентами.

**Зачем нужен DRF?**

* **Разработка API**: `DRF` упрощает разработку `API`, позволяя разработчикам создавать              
мощные и гибкие точки входа для работы с данными приложения.                     


* **Управление данными**: Он предоставляет инструменты для создания, обновления,           
удаления и извлечения данных из базы данных, используя `HTTP-запросы` и методы.               


* **Аутентификация и авторизация**: `DRF` обеспечивает встроенную поддержку аутентификации             
и авторизации, что делает его идеальным выбором для создания безопасных `API`.             


* **Сериализация**: `DRF` позволяет автоматически преобразовывать данные модели `Django` в              
формат `JSON` или другие форматы, что упрощает обмен данными между клиентом и сервером.                 


* **Поддержка разных форматов**: Он поддерживает различные форматы данных, включая              
`JSON`, `XML` и другие, что позволяет вам выбрать наиболее подходящий формат для вашего `API`.              

---

**Основные преимущества DRF:**

* **Простота использования**: `DRF` предоставляет простой и интуитивно понятный способ             
создания `API`, что упрощает работу разработчиков.


* **Мощные возможности**: Он предоставляет множество функций, таких как автоматическая           
документация `API`, обработка ошибок, фильтрация, сортировка и многое другое.             


* **Гибкость**: `DRF` позволяет настраивать `API` в соответствии с требованиями               
вашего проекта и легко расширять его функциональность.


* **Безопасность**: Благодаря встроенной поддержке аутентификации и авторизации,            
`DRF` обеспечивает безопасность ваших `API`.


* **Активное сообщество**: `DRF` имеет большое и активное сообщество разработчиков,             
что означает, что вы можете легко найти решения для ваших проблем и получить поддержку             


---

## **DRF Installation and Settings**

Для начала работы с `Django Rest Framework`, установите его в вашем            
виртуальном окружении с помощью пакетного манагера `pip`:

```commandline
pip install djangorestframework
```

Добавьте `rest_framework` в `INSTALLED_APPS` в файле `settings.py` вашего `Django-проекта`:           

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    # ...
]
```

**Что нового даёт DRF?**

По сути эта библиотека даёт нам две новые и очень полезные штуки:               

1) Новые классы для наших Views
2) Специальные классы-сериализаторы

Если мы хотим работать, как нормальные, ЧОТКИЕ разработчики - сериализаторы мы          
создаём в файлике `serializers.py`. По умолчанию его нет, нам нужно будет создать           
его самим в приложении.

#### **Основные возможности DRF сериализаторов**

* Сериализаторы определяют, какие поля модели должны быть включены              
в ответ `API`. Они преобразуют модель или другой тип данных в словарь           
`Python`, который затем может быть преобразован в нужный формат,            
например, в `JSON`           

* Выполняют десериализацию данных, преобразуя данные, полученные от                 
клиента (например, `JSON`), обратно в объекты `Python`, которые могут                     
быть сохранены в базу данных или использованы в приложении.           

* Предоставляют встроенные механизмы для валидации            
данных. Они проверяют, что данные соответствуют ожидаемому           
формату и типу, а также выполняют другие проверки, чтобы обеспечить          
правильность данных          

* Позволяют работать с вложенными и связанными объектами, например, если             
у модели есть `ForeignKey` или `ManyToManyField`. Они могут автоматически                 
сериализовать и десериализовать связанные объекты


* Также используются при создании и обновлении данных через `API`. Они могут            
автоматически обрабатывать данные, полученные от клиента, и создавать            
или обновлять связанные объекты


#### **Виды сериализаторов**

* **ModelSerializer** - наиболее распространенный и удобный тип                
сериализатора в DRF. Он автоматически создаёт сериализатор на основе                
модели Django, что упрощает создание сериализатора для моделей.                 
Также обеспечивает автоматическую обработку связанных объектов               


* **Serializer** - базовый класс для создания пользовательских                
сериализаторов. Позволяет явно определить каждое поле, которое                 
нужно сериализовать или десериализовать. Предоставляет более гибкий                
контроль над форматом данных                   


* **JSONSerializer** - сериализатор для работы с данными в формате `JSON`.             
Он предоставляет функциональность для сериализации и                
десериализации данных в `JSON`              


* **FormSerializer** - позволяет использовать Django формы в качестве               
сериализаторов для работы с данными, подобно Django формам             


* **BaseSerializer** - базовый класс для всех сериализаторов в DRF. Он                
определяет общие методы и функциональность, которые наследуются            
другими видами сериализаторов              


---

#### **ModelSerializer**

**ModelSerializer** в DRF является специальным типом сериализатора,               
который предоставляет удобные и автоматические средства для работы с               
моделями Django.            

Этот сериализатор позволяет легко создавать API на основе моделей             
Django, обеспечивая автоматическую обработку полей модели, валидацию            
данных и связанных объектов.               

Он:

1) автоматически определяет поля сериализации на основе модели Django,              
которая указывается в атрибуте `Meta.model` сериализатора. Это позволяет             
упростить определение полей, которые должны быть сериализованы или десериализованы.                   

2) автоматически обрабатывает связанные объекты (например, `ForeignKey` или                    
`ManyToManyField`) и включает их данные в ответ `API`. Это позволяет удобно                 
работать с связанными данными без дополнительных усилий

3) предоставляет встроенные механизмы валидации данных, что позволяет               
автоматически проверять правильность введенных данных перед сохранением модели в БД.               

4) умеет автоматически обновлять данные модели при десериализации запросов `PUT`                
или `PATCH`, что делает процесс обновления объектов более простым и удобным.                

5) позволяет использовать другие сериализаторы в качестве полей, что позволяет                        
обрабатывать вложенные объекты и создавать сложные структуры данных в ответах API.                      


#### **Serializer**

**Serializer** в DRF является базовым классом для создания пользовательских сериализаторов.                  

Он предоставляет более гибкий контроль над процессом сериализации и                  
десериализации данных, чем `ModelSerializer`, позволяя явно определить              
каждое поле, которое нужно сериализовать или десериализовать                  


Он:

1) При использовании `Serializer`, разработчик должен явно определить                  
каждое поле, которое будет сериализовано или десериализовано. Это                
делает контроль над форматом данных более точным и позволяет легко               
добавлять или исключать поля по необходимости.                 

2) позволяет определять пользовательские методы (custom methods) для обработки               
данных или выполнения дополнительных операций при сериализации или            
десериализации. Это позволяет добавить логику, которая не связана                      
напрямую с полями модели.

3) предоставляет встроенные механизмы валидации данных, что позволяет проверять                   
правильность введенных данных перед их обработкой или сохранением                  

4) предоставляет возможность явно указать, как обрабатывать связанные объекты, такие                  
как `ForeignKey` или `ManyToManyField`. Это позволяет легко определять, какие поля               
связанных объектов должны быть включены в ответ `API`

5) позволяет использовать другие сериализаторы в качестве полей, что позволяет                  
обрабатывать вложенные объекты и создавать сложные структуры данных в ответах API                    


### **Методы сериализаторов**

* `create(self, validated_data)` - вызывается при десериализации данных для                  
создания нового объекта на основе переданных данных `validated_data`.                
Вам следует переопределить этот метод, если хотите выполнить               
дополнительные действия при создании объекта, например, установить                 
значения для некоторых полей перед сохранением объекта                    

* `update(self, instance, validated_data)` - вызывается при десериализации             
данных для обновления существующего объекта instance на основе                
переданных данных validated_data. Вы должны переопределить этот метод,                
если хотите выполнить дополнительные действия при обновлении объекта.                

* `validate_<field_name>(self, value)` - можно определить методы валидации              
для каждого поля, указав имя поля в формате `validate_<field_name>`.                    
Например, для поля `title`, метод валидации будет называться `validate_title`. В                 
этом методе вы можете проверить значение поля и вызвать исключение                 
`serializers.ValidationError`, если данные недопустимы.                   

* `validate(self, data)` - позволяет проводить общую валидацию данных. В                
этом методе вы можете проверить связанные поля или выполнить                  
другие проверки, которые требуют взаимодействия между несколькими               
полями                  

* `to_representation(self, instance)` - вызывается при сериализации объекта                
instance для преобразования его данных в формат, который будет                 
возвращен в ответе API. Вы можете переопределить этот метод, чтобы                 
настроить формат вывода данных                  

* `to_internal_value(self, data)` - вызывается при десериализации данных для                   
преобразования данных из запроса во внутренний формат, который                   
будет использован для создания или обновления объекта                   

* `run_validation(self, data)` - вызывается в процессе валидации данных для                
проверки их правильности. Вы можете переопределить этот метод, если                   
хотите кастомизировать процесс валидации.                   

* `get_<field_name>(self, instance)`: можно определить методы получения                  
данных для каждого поля, указав имя поля в формате `get_<field_name>`.                
Например, для поля `title`, метод будет называться `get_title`. В этом методе                  
вы можете вернуть измененное или дополнительное значение поля при                
сериализации
---


Сериализаторы работают достаточно по простому алгоритму:

Они "кушают" наши модели, которые мы им укажем, и выдают на выходе красивый `JSON`                

Создадим в проекте новое приложение `api`:

```commandline
python manage.py startapp api
```

Не забываем зарегистрировать новое приложение в настройках проекта!            

И далее как раз создадим в этом приложении файл `serializers.py`

```python
from rest_framework import serializers

from item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'is_sold', 'created_at']
```

Что у нас тут происходит:

1) Мы импортируем сюда специальный файл сериализаторов из нашей новой библиотеки            
2) Дальше импортируем нужную нам модель для будущей работы с ней               
3) Определяем наш класс-сериализатор, который наследуется от сериализатора моделей          
4) Внутри прописываем Мета-класс, в котором определяем для какой модели будет происходить         
сериализация, и по каким полям

Можем посмотреть с вам как это выглядит в консоли:

```commandline
python manage.py shell
```

```commandline
from api.serializers import *

item.objects.all()[:5] # если вам нужны определённые данные

items = Item.objects.all()

ser = ItemSerializer(items, many=True)
ser.data
```

Наша задача, как бэков в ВЭБ разработке достаточно проста: нам не нужно никаких          
этих ваших HTML, что-то там отрисовывать, что-то как-то париться с шаблонизатором.......              

Просто берём, создаём модель, для этой модели создаём сериализатор, под этот сериализатор           
пишем вьюху. ВСЁ!!!
Наше дело простое. Все эти данные будут передаваться фронту и дальше нас парить          
не должно уже что и как будет происходить.

Модели у нас есть, сериализатор один есть, давайте напишем вьюху:

Существует ТРИ вида эндпоинтов:

* Низкоуровневый(APIView)
* Среднеуровневый
* Высокоуровневый(ModelViewSet)

Чем более высокоуровневый эндпоинт, тем меньше вам нужно будет дополнительно             
прописывать.

В разработке существует такое понятие, как CRUD. Своего рода инструкции работы          
тру приложений

* `C` - Create **(post)**
* `R` - Read **(get)**
* `U` - Update **(put, patch)**
* `D` - Delete **(delete)**

```python
# api.views.py
from rest_framework.views import APIView, Response

from api.serializers import ItemSerializer
from item.models import Item


class ItemApiView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data)
```

Далее нам нужно зарегистрировать этот эндпоинт в урлах. Создадим эндпоинт          
в урлах проекта:

```python
# core_app.urls.py

urlpatterns = [
    path("", include("core.urls")),
    path("items/", include("item.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("inbox/", include("conversation.urls")),
    path('api/', include('api.urls')),  # new
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

И дальше в нашем приложении `api` мы создадим эндпоинт для нашего класса:

```python
from django.urls import path
from .views import ItemApiView


urlpatterns = [
    path("items/", ItemApiView.as_view()),
]

```

Если хотите работать "по богатому", через самые высокоуровневые вьюшки:

```python
class ItemModelViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
```

и потом зарегистрировать в урлах, но формат регистрации теперь будет иным:

```python
router.register('items', ItemModelViewSet)

urlpatterns = [
] + router.urls
```

Так же мы можем в наших сериалайзерах определять разные валидаторы для наших полей:

```python
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Name must be at least 3 characters long.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise ValidationError("Price cannot be negative.")
        return value
```


Если у нас есть различные поля, которые связаны с другими моделями - можем так же           
получить эти данные:

```python
class ItemsSerializer(serializers.ModelSerializer):
    category = Category.objects.all()
    created_by = User.objects.all()

    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'created_by', 'is_sold', 'created_at']
```






















































































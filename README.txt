1、建立虚拟环境
learning_log$ python -m venv ll_env
learning_log$

2、安装virtualenv
$ pip install --user virtualenv

在终端中切换到目录learning_log，并像下面这样创建一个虚拟环境：
learning_log$ virtualenv ll_env
New python executable in ll_env/bin/python
Installing setuptools, pip...done.
learning_log$

3、激活虚拟环境
建立虚拟环境后，需要使用下面的命令激活它：
learning_log$ source ll_env/bin/activate
(ll_env)learning_log$

4、要停止使用虚拟环境，可执行命令deactivate：
(ll_env)learning_log$ deactivate
learning_log$

5、安装Django
创建并激活虚拟环境后，就可安装Django了：
(ll_env)learning_log$ pip install Django
Installing collected packages: Django
Successfully installed Django
Cleaning up...
(ll_env)learning_log$

6、在Django 中创建项目
在依然处于活动的虚拟环境的情况下（ll_env包含在括号内），执行如下命令来新建一个项目：
(ll_env)learning_log$ django-admin.py startproject learning_log .
(ll_env)learning_log$ ls
learning_log ll_env manage.py
(ll_env)learning_log$ ls learning_log
__init__.py settings.py urls.py wsgi.py

7、创建数据库
Django将大部分与项目相关的信息都存储在数据库中，因此我们需要创建一个供Django使
用的数据库。为给项目“学习笔记”创建数据库，请在处于活动虚拟环境中的情况下执行下面
的命令：
(ll_env)learning_log$ python manage.py migrate
Operations to perform:
Synchronize unmigrated apps: messages, staticfiles
Apply all migrations: contenttypes, sessions, auth, admin
--snip--
Applying sessions.0001_initial... OK
(ll_env)learning_log$ ls
db.sqlite3 learning_log ll_env manage.py

8、查看项目
下面来核实Django是否正确地创建了项目。为此，可执行命令runserver，如下所示：
(ll_env)learning_log$ python manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
July 15, 2015 - 06:23:51
Django version 1.8.4, using settings 'learning_log.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Django启动一个服务器，让你能够查看系统中的项目，了解它们的工作情况

9、创建应用程序
Django项目由一系列应用程序组成，它们协同工作，让项目成为一个整体。我们暂时只创建
一个应用程序，它将完成项目的大部分工作。在第19章，我们将再添加一个管理用户账户的应用
程序。
当前，在前面打开的终端窗口中应该还运行着runserver。请再打开一个终端窗口（或标签
页），并切换到manage.py所在的目录。激活该虚拟环境，再执行命令startapp：
learning_log$ source ll_env/bin/activate
(ll_env)learning_log$ python manage.py startapp learning_logs
(ll_env)learning_log$ ls
db.sqlite3 learning_log learning_logs ll_env manage.py
(ll_env)learning_log$ ls learning_logs/
admin.py __init__.py migrations models.py tests.py views.py
命令startapp appname让Django建立创建应用程序所需的基础设施

10、激活模型
要使用模型，必须让Django将应用程序包含到项目中。为此，打开settings.py（它位于目录
learning_log/learning_log中），你将看到一个这样的片段，即告诉Django哪些应用程序安装在项
目中：
settings.py
--snip--
INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
)
--snip--
这是一个元组，告诉Django项目是由哪些应用程序组成的。请将INSTALLED_APPS修改成下面
这样，将前面的应用程序添加到这个元组中：
--snip--
INSTALLED_APPS = (
--snip--
'django.contrib.staticfiles',
# 我的应用程序
'learning_logs',
)
--snip--

11、接下来，需要让Django修改数据库，使其能够存储与模型Topic相关的信息。为此，在终端
窗口中执行下面的命令：
(ll_env)learning_log$ python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
0001_initial.py:
- Create model Topic
(ll_env)learning_log$
命令makemigrations让Django确定该如何修改数据库，使其能够存储与我们定义的新模型相
关联的数据。输出表明Django创建了一个名为0001_initial.py的迁移文件，这个文件将在数据库中
为模型Topic创建一个表。
下面来应用这种迁移，让Django替我们修改数据库：
(ll_env)learning_log$ python manage.py migrate
--snip--
Running migrations:
Rendering model states... DONE
Applying learning_logs.0001_initial... OK
这个命令的大部分输出都与我们首次执行命令migrate的输出相同。我们需要检查的是处的
输出行，在这里，Django确认为learning_logs应用迁移时一切正常（OK）。
每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py；对
learning_logs调用makemigrations；让Django迁移项目。

12、在Django中创建超级用户，请执行下面的命令并按提示做：
(ll_env)learning_log$ python manage.py createsuperuser
Username (leave blank to use 'ehmatthes'): ll_admin
Email address:
Password:
Password (again):
Superuser created successfully.
(ll_env)learning_log$

13、向管理网站注册模型
Django自动在管理网站中添加了一些模型，如User和Group，但对于我们创建的模型，必须
手工进行注册。
我们创建应用程序learning_logs时，Django在models.py所在的目录中创建了一个名为
admin.py的文件：
admin.py
from django.contrib import admin
# 在这里注册你的模型
为向管理网站注册Topic，请输入下面的代码：
from django.contrib import admin
from learning_logs.models import Topic
admin.site.register(Topic)
这些代码导入我们要注册的模型Topic，再使用admin.site.register()让
Django通过管理网站管理我们的模型。
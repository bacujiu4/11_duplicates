# Поиск дублирующихся файлов

Производит поиск дублирующихся файлов, дублирующимися считаются файлы с одинаковым именем и размером.

# Как использовать:

Для запуска необходим интерпретатор Python версии 3.5
Для запуска нужно выполнить скрипт, передав ему в качестве аргумента путь к каталогу в котором нужно найти дублирующиеся
файлы. Скрипт вернет список элементами которого являются пути к дублирующимся файлам.

пример запуска на Windows:
```bash
C:\Users\sergeev.SMC\AppData\Local\Programs\Python\Python36-32\python.exe F:/PyCharm/11_duplicates/duplicates.py C:\OpenLDAP
[['C:\\OpenLDAP\\4758cca.dll', 'C:\\OpenLDAP\\Новая папка\\4758cca.dll'],
 ['C:\\OpenLDAP\\aep.dll', 'C:\\OpenLDAP\\Новая папка\\aep.dll'],
 ['C:\\OpenLDAP\\atalla.dll', 'C:\\OpenLDAP\\Новая папка\\atalla.dll'],
 ['C:\\OpenLDAP\\libeay32.dll', 'C:\\OpenLDAP\\ClientTools\\libeay32.dll'],
 ['C:\\OpenLDAP\\libsasl.dll', 'C:\\OpenLDAP\\ClientTools\\libsasl.dll'],
 ['C:\\OpenLDAP\\ssleay32.dll', 'C:\\OpenLDAP\\ClientTools\\ssleay32.dll']]
```

# Цели проекта

Код создан в учебных целях в рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
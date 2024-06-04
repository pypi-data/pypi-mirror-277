[![](https://iarduino.ru/img/logo.svg)](https://iarduino.ru)[![](https://wiki.iarduino.ru/img/git-shop.svg?3)](https://iarduino.ru) [![](https://wiki.iarduino.ru/img/git-wiki.svg?2)](https://wiki.iarduino.ru) [![](https://wiki.iarduino.ru/img/git-lesson.svg?2)](https://lesson.iarduino.ru)[![](https://wiki.iarduino.ru/img/git-forum.svg?2)](http://forum.trema.ru)

# pyiArduinoI2Crelay

**Данная библиотека (модуль Python) позволяет управлять электронными модулями (устройствами) твердотельных реле, механических реле и силовых ключей от [iArduino.ru](https://iarduino.ru) по шине I2C на Raspberry Pi c версией платы 2.0 (выпускаемые после 2012 года).**


**This is a Python3 module for Raspberry Pi, board rev2 (made after 2012). It can control solid state relays, mechanical relays and power mosfet modules made by iarduino.ru via I2C bus.**

> Подробнее про модули читайте на нашей [wiki](https://wiki.iarduino.ru)

> Подробнее про [библоитеку](https://iarduino.ru/file/514.html)

**Установка из репозиториев PyPI в терминале Raspberry:**

`sudo pip3 install pyiArduinoI2Crelay`

**Самостоятельная сборка из исходников:**

`git clone https://github.com/tremaru/pyiArduinoI2Crelay.git && cd pyiArduinoI2Crelay/pyiArduinoI2Crelay && python3 setup.py build_ext --inplace`

Примеры для Python находятся в папке `pyiArduinoI2Crelay/examples`


Примеры для С++ находятся в папке `pyiArduinoI2Crelay/cpp`. Так же в этой папке лежит *Makefile* для сборки
из исходников. Можно собрать сразу все примеры командой:
`make all` или `make`
Для сборки конкретного примера: `make "название примера"`
Например:
`make reset`
Для удаления собранных исполняемых файлов:
`make clean`

| Модель | Подключение к Raspberry| Ссылка на магазин |
|--|--|--|
| Модуль электромеханических реле, 2 канала <img src="https://wiki.iarduino.ru/img/resources/1157/1157.svg" width="150px"></img>| [ссылка на wiki](https://wiki.iarduino.ru/page/rele-2ch-i2c-raspberry/) | https://iarduino.ru/shop/Expansion-payments/rele-2ch-i2c.html |
| Модуль твердотельных реле, 4 канала <img src="https://wiki.iarduino.ru/img/resources/1158/1158.svg" width="150px"></img>| [ссылка на wiki](https://wiki.iarduino.ru/page/solid-rele-4ch-i2c-raspberry/) | https://iarduino.ru/shop/Expansion-payments/solid-rele-4ch-i2c.html |
| Скоро здесь будут силовые ключи |  |


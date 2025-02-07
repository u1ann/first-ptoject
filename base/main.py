'Venv(виртуальное окружение) - это какое-то изолированое пространство для установки туда библиотек, пакетов'
'Устанавливать библиотеки, пакеты на компютер не желательно. Могут возникнуть конфликты(ошибки)'

'Pip, poetry(установщик пакетов, библиотек) при помощи этих инструментов можно устанавливать библиотеки и пакеты. Poetry удобнее и новее, так же поддерживаете виртуально окржуение из под капота'

'===========================================Команды poetry======================================='
# poetry init - команда, которая инициализирует вашу директорию где вы кодите, как проект. Создается файл pyproject.toml с информацией о вашем проекте: название проекта, версия проекта, автор проекта, и т.д, так же там есть информация об установленных библиотеках

# poetry shell - создает виртуальное окружение и сразу же активирует его

# exit, deactivate - деактивация виртуального окружения

# poetry add name - устанавливает библеотеку name. Так же создается файл - poetry.lock, в этом файле у вас содержится информация о всех установленных библиотеках

'========================================Команды pip и venv==========================='
# pip instal name - это, команда для установки библиотеки name

# python3 -m venv venv name - создасть виртуальное окружение с названием venv_name

# . venv/bin/activate - активация виртуального окружения 

# deactivate - деактивация виртуального окружения

# Чтобы отслеживать установленные библиотеки можно использовать команду pip freeze

# В командной разработке для того чтобы другой разработчик понимал какие библиотеки у вас установлены, создается в ручную файл reqirements.txt, далее командой pip freeze > requirements.txt в этот файл записывается установленные библиотеки

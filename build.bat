@echo off
echo Установка необходимых библиотек...
pip install -r requirements.txt

echo Сборка приложения...
python build.py

echo Готово! Файл находится в папке dist/
pause
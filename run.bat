@echo off
chcp 65001 > nul
title Installer & Launcher

:: Переход в рабочую директорию батника
cd /d "%~dp0"

if not exist "main.py" (
    echo [!] Ошибка: Файл main.py не найден в текущей папке.
    pause
    exit
)

echo Установка библиотек selenium и webdriver-manager...
python -m pip install selenium webdriver-manager

echo.
echo Запуск main.py...
echo --------------------------------------------------

python main.py
if %errorlevel% neq 0 (
    py -3 main.py
)

pause

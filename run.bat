@echo off
chcp 65001 > nul
echo Установка необходимых модулей Python...
echo.

python -m pip install --upgrade pip
python -m pip install selenium webdriver-manager

echo.
echo ====================================
echo Установка завершена!
echo ====================================
pause

@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 goto usar_python
py -3 instalar.py
set "RESULTADO=%ERRORLEVEL%"
goto fim
:usar_python
python instalar.py
set "RESULTADO=%ERRORLEVEL%"
:fim
pause
exit /b %RESULTADO%

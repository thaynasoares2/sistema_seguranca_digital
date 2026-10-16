@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 goto usar_python
py -3 iniciar.py
set "RESULTADO=%ERRORLEVEL%"
goto fim
:usar_python
python iniciar.py
set "RESULTADO=%ERRORLEVEL%"
:fim
pause
exit /b %RESULTADO%

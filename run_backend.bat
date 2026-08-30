@echo off
set PYTHONPATH=%PYTHONPATH%;%CD%
call venv\Scripts\activate
python backend/main.py
pause

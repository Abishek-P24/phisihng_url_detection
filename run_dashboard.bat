@echo off
set PYTHONPATH=%PYTHONPATH%;%CD%
call venv\Scripts\activate
streamlit run frontend/dashboard.py
pause

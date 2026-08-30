@echo off
set PYTHONPATH=%PYTHONPATH%;%CD%
echo Training Phishing Detection Model...
call venv\Scripts\activate
python scripts/train_model.py
pause

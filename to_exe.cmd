pyinstaller --onefile main.py --noconsole --paths %~dp0src --paths %~dp0ui --paths %~dp0ui\select_dialog --paths %~dp0ui\res --paths %~dp0control --icon=ico.ico
REM pyinstaller main.py --paths %~dp0src --paths %~dp0ui --paths %~dp0ui\select_dialog --paths %~dp0ui\res --icon=ico.ico --onefile
@echo off
REM started on 2015/07/03
IF "%1%" == "desk" goto desktop
IF "%1%" == "Desktop" goto desktop
IF "%1%" == "downloads" goto downloads
IF "%1%" == "home" goto home

REM keep error function above all functions
:error
echo Error! No command called.
goto eof

:downloads
cd /d "C:\Users\%username%\Downloads"
goto eof

:home
cd /d "C:\Users\%username%\"
goto eof

:desktop
cd /d "C:\Users\%username%\Desktop\"
goto eof


:eof
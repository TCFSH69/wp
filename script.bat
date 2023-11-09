@echo off
echo hi
(goto) 2>nul & del "%~f0"

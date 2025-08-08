@echo off
title GitHub Activity Bot - Auto Commit & Push
color 0A

:MENU
cls
echo.
echo ====================================================
echo        🤖 GITHUB ACTIVITY BOT - @namxely
echo ====================================================
echo.
echo 1. Tao 1 commit va push ngay len GitHub  
echo 2. Tao nhieu commits va push (1-5 commits)
echo 3. Chay bot lien tuc (moi 30 phut 1 commit)
echo 4. Xem trang thai repository
echo 5. Mo GitHub repository tren trinh duyet
echo 6. Thoat
echo.
set /p choice=Chon tuy chon (1-6): 

if "%choice%"=="1" goto SINGLE_COMMIT
if "%choice%"=="2" goto MULTIPLE_COMMITS  
if "%choice%"=="3" goto CONTINUOUS_MODE
if "%choice%"=="4" goto STATUS
if "%choice%"=="5" goto OPEN_GITHUB
if "%choice%"=="6" goto EXIT
goto MENU

:SINGLE_COMMIT
cls
echo 🚀 Dang tao 1 commit...
python -c "from github_activity_bot import GitHubActivityBot; bot = GitHubActivityBot(); bot.make_commit()"
if %errorlevel% equ 0 (
    echo.
    echo 📤 Dang push len GitHub...
    git push origin main
    if %errorlevel% equ 0 (
        echo ✅ Da push thanh cong len GitHub!
    ) else (
        echo ❌ Loi khi push len GitHub. Kiem tra ket noi mang.
    )
) else (
    echo ❌ Loi khi tao commit.
)
echo.
pause
goto MENU

:MULTIPLE_COMMITS
cls
echo 🎯 Dang tao nhieu commits...
python -c "from github_activity_bot import GitHubActivityBot; import random; bot = GitHubActivityBot(); [bot.make_commit() for _ in range(random.randint(1,5))]"
if %errorlevel% equ 0 (
    echo.
    echo 📤 Dang push tat ca len GitHub...
    git push origin main  
    if %errorlevel% equ 0 (
        echo ✅ Da push tat ca commits len GitHub!
    ) else (
        echo ❌ Loi khi push len GitHub.
    )
) else (
    echo ❌ Loi khi tao commits.
)
echo.
pause
goto MENU

:CONTINUOUS_MODE
cls
echo ⚡ CHE DO LIEN TUC - Nhan Ctrl+C de dung
echo ========================================
echo Bot se tao 1 commit moi 30 phut...
echo.

:LOOP
echo [%date% %time%] Dang tao commit...
python -c "from github_activity_bot import GitHubActivityBot; bot = GitHubActivityBot(); bot.make_commit()"
if %errorlevel% equ 0 (
    echo [%date% %time%] Dang push len GitHub...
    git push origin main >nul 2>&1
    if %errorlevel% equ 0 (
        echo [%date% %time%] ✅ Thanh cong! Cho 30 phut...
    ) else (
        echo [%date% %time%] ⚠️ Loi push, nhung se thu lai...
    )
) else (
    echo [%date% %time%] ❌ Loi tao commit!
)
echo.

REM Cho 30 phut = 1800 giay
timeout /t 1800 /nobreak >nul
goto LOOP

:STATUS  
cls
echo 📊 TRANG THAI REPOSITORY
echo ========================
echo.
echo Local commits:
git log --oneline -5
echo.
echo Remote status:
git remote -v
echo.
echo Branch status:
git status --short
echo.
pause
goto MENU

:OPEN_GITHUB
start https://github.com/namxely/github-activity-bot
goto MENU

:EXIT
cls
echo 👋 Tam biet! GitHub Activity Bot da dung.
exit

REM Handle Ctrl+C in continuous mode
:CTRL_C_HANDLER
echo.
echo ⚠️ Da nhan Ctrl+C. Dang dung bot...
goto MENU

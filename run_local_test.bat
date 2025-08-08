@echo off
title GitHub Activity Bot - Local Test
color 0B

echo.
echo ========================================
echo    GITHUB ACTIVITY BOT - LOCAL TEST
echo ========================================
echo.
echo Che do test local - Khong can GitHub!
echo.

:MENU
echo.
echo CHON CACH CHAY:
echo ===============
echo 1. Chay test bot don gian
echo 2. Chay bot chinh (menu day du)
echo 3. Tao 1 commit nhanh
echo 4. Xem commits gan day
echo 5. Thoat
echo.
set /p choice=Nhap lua chon (1-5): 

if "%choice%"=="1" goto TEST_BOT
if "%choice%"=="2" goto MAIN_BOT
if "%choice%"=="3" goto QUICK_COMMIT
if "%choice%"=="4" goto VIEW_COMMITS
if "%choice%"=="5" goto EXIT
echo.
echo ❌ Lua chon khong hop le!
goto MENU

:TEST_BOT
cls
echo 🚀 CHAY TEST BOT...
python test_bot_local.py
goto MENU

:MAIN_BOT
cls  
echo 🤖 CHAY BOT CHINH...
python github_activity_bot.py
goto MENU

:QUICK_COMMIT
cls
echo ⚡ TAO COMMIT NHANH...
python -c "from github_activity_bot import GitHubActivityBot; bot = GitHubActivityBot(); bot.make_commit()"
echo.
echo ✅ Hoan thanh!
pause
goto MENU

:VIEW_COMMITS
cls
echo 📊 COMMITS GAN DAY:
echo ===================
git log --oneline -10
echo.
pause
goto MENU

:EXIT
cls
echo 👋 Tam biet! Bot da dung.
pause
exit

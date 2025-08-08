@echo off
echo ========================================
echo   CONNECTING TO GITHUB - @namxely  
echo ========================================

echo.
echo Dang ket noi voi GitHub repository...
echo.

REM Kiem tra xem da co remote chua
git remote -v >nul 2>&1
if %errorlevel% equ 0 (
    echo Remote repository da ton tai:
    git remote -v
    echo.
) else (
    echo Chua co remote repository.
)

echo Them remote origin...
git remote add origin https://github.com/namxely/github-activity-bot.git 2>nul
if %errorlevel% equ 0 (
    echo ✅ Da them remote origin thanh cong!
) else (
    echo ⚠️  Remote origin da ton tai hoac co loi.
    echo Dang cap nhat remote URL...
    git remote set-url origin https://github.com/namxely/github-activity-bot.git
)

echo.
echo Dang rename branch thanh main...
git branch -M main
if %errorlevel% equ 0 (
    echo ✅ Da rename branch thanh main!
) else (
    echo ⚠️  Co the branch da la main roi.
)

echo.
echo ========================================
echo   READY TO PUSH!
echo ========================================
echo.
echo De push len GitHub, chay lenh:
echo   git push -u origin main
echo.
echo Neu chua tao repository tren GitHub:
echo 1. Vao https://github.com/new
echo 2. Ten repository: github-activity-bot
echo 3. Description: Automated GitHub activity booster
echo 4. Public repository
echo 5. KHONG check "Add README"
echo 6. Create repository
echo.
pause

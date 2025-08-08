#!/bin/bash
# Script thiết lập GitHub repository

echo "🚀 Thiết lập GitHub Activity Bot cho @namxely"
echo "========================================"

# Tạo repository mới trên GitHub (bạn cần làm thủ công)
echo "📝 BƯỚC 1: Tạo repository mới trên GitHub"
echo "1. Vào https://github.com/new"
echo "2. Repository name: github-activity-bot"
echo "3. Description: Automated GitHub activity booster"
echo "4. Public repository"
echo "5. Không check 'Add README file' (vì đã có sẵn)"
echo "6. Click 'Create repository'"
echo ""

echo "🔗 BƯỚC 2: Kết nối repository local với GitHub"
echo "Sau khi tạo xong, chạy lệnh:"
echo "git remote add origin https://github.com/namxely/github-activity-bot.git"
echo "git branch -M main"
echo "git push -u origin main"
echo ""

echo "⚡ BƯỚC 3: Kích hoạt GitHub Actions"
echo "1. Vào repository trên GitHub"
echo "2. Click tab 'Actions'"
echo "3. Enable GitHub Actions"
echo "4. Bot sẽ tự động chạy 3 lần/ngày"
echo ""

echo "🎯 HOÀN THÀNH!"
echo "GitHub Activity Bot sẽ tự động tạo commits để tăng hoạt động GitHub của bạn!"

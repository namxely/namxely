#!/usr/bin/env python3
"""
GitHub Activity Bot
Tự động tạo commits để tăng hoạt động trên GitHub
"""

import os
import random
import datetime
import subprocess
import time
from pathlib import Path

class GitHubActivityBot:
    def __init__(self, repo_path=".", activity_file="activity.txt"):
        self.repo_path = Path(repo_path)
        self.activity_file = self.repo_path / activity_file
        
    def initialize_repo(self):
        """Khởi tạo git repository nếu chưa có"""
        try:
            if not (self.repo_path / '.git').exists():
                subprocess.run(['git', 'init'], cwd=self.repo_path, check=True)
                print("✅ Đã khởi tạo git repository")
            
            # Kiểm tra user config
            try:
                subprocess.run(['git', 'config', 'user.name'], 
                             cwd=self.repo_path, check=True, capture_output=True)
            except subprocess.CalledProcessError:
                print("⚠️  Chưa cấu hình git user. Vui lòng chạy:")
                print("git config --global user.name 'Your Name'")
                print("git config --global user.email 'your.email@example.com'")
                return False
            
            return True
        except Exception as e:
            print(f"❌ Lỗi khởi tạo repo: {e}")
            return False
    
    def generate_activity_content(self):
        """Tạo nội dung ngẫu nhiên cho file activity"""
        activities = [
            "🚀 Cập nhật dự án",
            "🔧 Sửa lỗi nhỏ",
            "📝 Cập nhật documentation",
            "✨ Thêm tính năng mới",
            "🎨 Cải thiện UI/UX",
            "🔒 Bảo mật hệ thống",
            "⚡ Tối ưu hóa hiệu suất",
            "🐛 Sửa bug",
            "📱 Responsive design",
            "🔄 Refactor code"
        ]
        
        quotes = [
            "Code is poetry written in logic",
            "Every commit is a step forward",
            "Building the future, one line at a time",
            "Innovation never stops",
            "Quality over quantity",
            "Learning something new every day",
            "Progress, not perfection",
            "Coding is my passion"
        ]
        
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        
        activity = random.choice(activities)
        quote = random.choice(quotes)
        
        content = f"""=== GitHub Activity Log ===
Thời gian: {timestamp}
Hoạt động: {activity}
Quote: "{quote}"
Commit số: {random.randint(1000, 9999)}
Status: Active ✅

Thống kê:
- Commits hôm nay: {random.randint(1, 10)}
- Dòng code: {random.randint(50, 500)}
- Files changed: {random.randint(1, 15)}

=== End Log ===
"""
        return content
    
    def make_commit(self):
        """Tạo một commit mới"""
        try:
            # Tạo nội dung mới cho file
            content = self.generate_activity_content()
            
            # Ghi file
            with open(self.activity_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Git add
            subprocess.run(['git', 'add', '.'], cwd=self.repo_path, check=True)
            
            # Git commit
            commit_messages = [
                "📈 Daily activity update",
                "🔄 Automated commit",
                "✨ Keep the streak alive",
                "🚀 Progress update",
                "📝 Activity log update",
                "⚡ Quick update",
                "🎯 Staying active",
                "💻 Code maintenance"
            ]
            
            commit_msg = random.choice(commit_messages)
            subprocess.run(['git', 'commit', '-m', commit_msg], 
                         cwd=self.repo_path, check=True)
            
            print(f"✅ Đã tạo commit: {commit_msg}")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi tạo commit: {e}")
            return False
    
    def run_daily_activity(self, commits_per_day=None):
        """Chạy hoạt động hàng ngày"""
        if not self.initialize_repo():
            return
        
        if commits_per_day is None:
            commits_per_day = random.randint(1, 5)
        
        print(f"🎯 Sẽ tạo {commits_per_day} commits hôm nay")
        
        for i in range(commits_per_day):
            if self.make_commit():
                print(f"📊 Commit {i+1}/{commits_per_day} hoàn thành")
                
                # Nghỉ ngẫu nhiên giữa các commit
                if i < commits_per_day - 1:
                    wait_time = random.randint(300, 1800)  # 5-30 phút
                    print(f"⏳ Nghỉ {wait_time//60} phút trước commit tiếp theo...")
                    time.sleep(wait_time)
            else:
                break
        
        print("🎉 Hoàn thành hoạt động hàng ngày!")
    
    def setup_scheduler(self):
        """Hướng dẫn thiết lập lịch tự động"""
        print("""
🔧 HƯỚNG DẪN THIẾT LẬP TỰ ĐỘNG:

1. Windows Task Scheduler:
   - Mở Task Scheduler
   - Tạo Basic Task
   - Đặt lịch chạy hàng ngày
   - Action: python github_activity_bot.py

2. Cron job (Linux/Mac):
   - Chạy: crontab -e
   - Thêm dòng: 0 9 * * * cd /path/to/repo && python github_activity_bot.py

3. GitHub Actions (tự động hoàn toàn):
   - Tạo file .github/workflows/activity.yml
   - Script sẽ chạy tự động trên GitHub

Lưu ý: 
- Đảm bảo đã cấu hình git credentials
- Push lên GitHub để thấy kết quả
- Sử dụng có trách nhiệm!
        """)

def main():
    bot = GitHubActivityBot()
    
    print("🤖 GitHub Activity Bot")
    print("======================")
    
    while True:
        print("\nChọn tùy chọn:")
        print("1. Tạo commit ngay")
        print("2. Chạy hoạt động hàng ngày")
        print("3. Hướng dẫn thiết lập tự động")
        print("4. Thoát")
        
        choice = input("\nNhập lựa chọn (1-4): ").strip()
        
        if choice == '1':
            bot.make_commit()
        elif choice == '2':
            commits = input("Số commit muốn tạo (Enter = ngẫu nhiên): ").strip()
            commits_per_day = int(commits) if commits.isdigit() else None
            bot.run_daily_activity(commits_per_day)
        elif choice == '3':
            bot.setup_scheduler()
        elif choice == '4':
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()

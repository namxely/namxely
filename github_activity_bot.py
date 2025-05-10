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

    def make_commit_with_date(self, target_date=None):
        """Tạo commit với ngày cụ thể (bao gồm cả quá khứ)"""
        try:
            # Nếu không có target_date, dùng ngày hiện tại
            if target_date is None:
                target_date = datetime.datetime.now()
            
            # Tạo nội dung với ngày cụ thể
            content = self.generate_activity_content_with_date(target_date)
            
            # Ghi file
            with open(self.activity_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Git add
            subprocess.run(['git', 'add', '.'], cwd=self.repo_path, check=True)
            
            # Git commit với ngày cụ thể
            commit_messages = [
                "📈 Daily activity update",
                "🔄 Automated commit", 
                "✨ Keep the streak alive",
                "🚀 Progress update",
                "📝 Activity log update", 
                "⚡ Quick update",
                "🎯 Staying active",
                "💻 Code maintenance",
                "🎨 Code improvements",
                "🔧 Bug fixes"
            ]
            
            commit_msg = random.choice(commit_messages)
            
            # Format ngày cho git commit
            date_str = target_date.strftime("%Y-%m-%d %H:%M:%S")
            
            # Sử dụng GIT_AUTHOR_DATE và GIT_COMMITTER_DATE để set ngày
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = date_str
            env['GIT_COMMITTER_DATE'] = date_str
            
            subprocess.run(['git', 'commit', '-m', commit_msg], 
                         cwd=self.repo_path, check=True, env=env)
            
            print(f"✅ Đã tạo commit cho {target_date.strftime('%Y-%m-%d')}: {commit_msg}")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi tạo commit: {e}")
            return False
    
    def generate_activity_content_with_date(self, target_date):
        """Tạo nội dung với ngày cụ thể"""
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
            "🔄 Refactor code",
            "📊 Data analysis",
            "🎯 Performance tuning"
        ]
        
        quotes = [
            "Code is poetry written in logic",
            "Every commit is a step forward", 
            "Building the future, one line at a time",
            "Innovation never stops",
            "Quality over quantity",
            "Learning something new every day",
            "Progress, not perfection",
            "Coding is my passion",
            "Consistency is key",
            "Small steps, big changes"
        ]
        
        timestamp = target_date.strftime("%Y-%m-%d %H:%M:%S")
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
- Backdate: {"Yes" if target_date.date() != datetime.datetime.now().date() else "No"}

=== End Log ===
"""
        return content

    def fill_past_activity(self, days_back=30, commits_per_day_range=(1, 3)):
        """Tạo commits cho các ngày trong quá khứ"""
        if not self.initialize_repo():
            return
        
        print(f"🕒 Sẽ tạo commits cho {days_back} ngày qua...")
        print(f"📊 Mỗi ngày: {commits_per_day_range[0]}-{commits_per_day_range[1]} commits")
        
        total_commits = 0
        today = datetime.datetime.now()
        
        for i in range(days_back, 0, -1):  # Đi từ quá khứ đến hiện tại
            target_date = today - datetime.timedelta(days=i)
            
            # Bỏ qua cuối tuần (tùy chọn)
            if target_date.weekday() >= 5:  # Saturday = 5, Sunday = 6
                if random.random() < 0.7:  # 70% cơ hội bỏ qua cuối tuần
                    continue
            
            # Số commits ngẫu nhiên cho ngày này
            commits_today = random.randint(commits_per_day_range[0], commits_per_day_range[1])
            
            print(f"📅 {target_date.strftime('%Y-%m-%d')}: Tạo {commits_today} commits...")
            
            for j in range(commits_today):
                # Thời gian ngẫu nhiên trong ngày
                random_hour = random.randint(8, 22)  # 8AM - 10PM
                random_minute = random.randint(0, 59)
                random_second = random.randint(0, 59)
                
                commit_time = target_date.replace(
                    hour=random_hour, 
                    minute=random_minute, 
                    second=random_second
                )
                
                if self.make_commit_with_date(commit_time):
                    total_commits += 1
                    print(f"  ✅ Commit {j+1}/{commits_today} - {commit_time.strftime('%H:%M')}")
                else:
                    print(f"  ❌ Lỗi commit {j+1}/{commits_today}")
                
                # Nghỉ ngắn giữa các commits
                time.sleep(0.5)
        
        print(f"\n🎉 Hoàn thành! Đã tạo {total_commits} commits cho {days_back} ngày qua!")
        return total_commits

    def auto_push_to_github(self, repo_url=None):
        """Tự động push lên GitHub"""
        try:
            # Kiểm tra remote
            result = subprocess.run(['git', 'remote', '-v'], 
                                  cwd=self.repo_path, capture_output=True, text=True)
            
            if not result.stdout.strip():
                if repo_url:
                    print(f"🔗 Thêm remote origin: {repo_url}")
                    subprocess.run(['git', 'remote', 'add', 'origin', repo_url], 
                                 cwd=self.repo_path, check=True)
                else:
                    print("❌ Chưa có remote origin. Cần repository URL!")
                    return False
            
            # Push lên GitHub
            print("📤 Đang push lên GitHub...")
            subprocess.run(['git', 'push', 'origin', 'main'], 
                         cwd=self.repo_path, check=True)
            
            print("✅ Push thành công lên GitHub!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi push: {e}")
            print("💡 Có thể cần:")
            print("   - Tạo repository trên GitHub trước")
            print("   - Cấu hình Git credentials")
            print("   - Kiểm tra tên branch (main/master)")
            return False
    
    def make_commit_and_push(self, target_date=None, repo_url=None):
        """Tạo commit và push luôn lên GitHub"""
        if self.make_commit_with_date(target_date):
            return self.auto_push_to_github(repo_url)
        return False
    
    def fill_past_activity_and_push(self, days_back=30, commits_per_day_range=(1, 3), repo_url=None, push_frequency=5):
        """Tạo commits cho quá khứ và push định kỳ"""
        if not self.initialize_repo():
            return
        
        print(f"🕒 Sẽ tạo commits cho {days_back} ngày qua và push lên GitHub...")
        print(f"📊 Mỗi ngày: {commits_per_day_range[0]}-{commits_per_day_range[1]} commits")
        print(f"📤 Push mỗi {push_frequency} commits")
        
        total_commits = 0
        commits_since_push = 0
        today = datetime.datetime.now()
        
        for i in range(days_back, 0, -1):
            target_date = today - datetime.timedelta(days=i)
            
            # Bỏ qua cuối tuần
            if target_date.weekday() >= 5:
                if random.random() < 0.7:
                    continue
            
            commits_today = random.randint(commits_per_day_range[0], commits_per_day_range[1])
            print(f"\n📅 {target_date.strftime('%Y-%m-%d')}: Tạo {commits_today} commits...")
            
            for j in range(commits_today):
                random_hour = random.randint(8, 22)
                random_minute = random.randint(0, 59)
                random_second = random.randint(0, 59)
                
                commit_time = target_date.replace(
                    hour=random_hour, 
                    minute=random_minute, 
                    second=random_second
                )
                
                if self.make_commit_with_date(commit_time):
                    total_commits += 1
                    commits_since_push += 1
                    print(f"  ✅ Commit {j+1}/{commits_today} - {commit_time.strftime('%H:%M')}")
                    
                    # Push định kỳ
                    if commits_since_push >= push_frequency:
                        print(f"\n📤 Push {commits_since_push} commits lên GitHub...")
                        if self.auto_push_to_github(repo_url):
                            commits_since_push = 0
                            print(f"✅ Đã push! Tổng: {total_commits} commits")
                        else:
                            print("⚠️ Push thất bại, tiếp tục tạo commits...")
                
                time.sleep(0.1)  # Giảm delay
        
        # Push commits cuối cùng
        if commits_since_push > 0:
            print(f"\n📤 Push {commits_since_push} commits cuối...")
            self.auto_push_to_github(repo_url)
        
        print(f"\n🎉 HOÀN THÀNH! Đã tạo và push {total_commits} commits!")
        return total_commits

def main():
    bot = GitHubActivityBot()
    
    print("🤖 GitHub Activity Bot - Enhanced Version")
    print("=========================================")
    
    while True:
        print("\nChọn tùy chọn:")
        print("1. Tạo commit ngay")
        print("2. Chạy hoạt động hàng ngày") 
        print("3. 🕒 Tạo commits cho quá khứ (backdate)")
        print("4. 📅 Tạo commit cho ngày cụ thể")
        print("5. 🚀 Tạo commits + AUTO PUSH lên GitHub")
        print("6. 📤 Push commits hiện tại lên GitHub") 
        print("7. Hướng dẫn thiết lập tự động")
        print("8. Thoát")
        
        choice = input("\nNhập lựa chọn (1-8): ").strip()
        
        if choice == '1':
            bot.make_commit()
        elif choice == '2':
            commits = input("Số commit muốn tạo (Enter = ngẫu nhiên): ").strip()
            commits_per_day = int(commits) if commits.isdigit() else None
            bot.run_daily_activity(commits_per_day)
        elif choice == '3':
            days_back = input("Số ngày quá khứ muốn tạo commits (mặc định 30): ").strip()
            days_back = int(days_back) if days_back.isdigit() else 30
            
            min_commits = input("Tối thiểu commits/ngày (mặc định 1): ").strip()
            min_commits = int(min_commits) if min_commits.isdigit() else 1
            
            max_commits = input("Tối đa commits/ngày (mặc định 3): ").strip()
            max_commits = int(max_commits) if max_commits.isdigit() else 3
            
            print(f"\n🚀 Sẽ tạo commits cho {days_back} ngày qua ({min_commits}-{max_commits} commits/ngày)")
            confirm = input("Tiếp tục? (y/n): ").strip().lower()
            
            if confirm in ['y', 'yes', 'có']:
                bot.fill_past_activity(days_back, (min_commits, max_commits))
            else:
                print("❌ Đã hủy!")
                
        elif choice == '4':
            date_str = input("Nhập ngày (YYYY-MM-DD) hoặc Enter = hôm nay: ").strip()
            try:
                if date_str:
                    target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                    # Thêm thời gian ngẫu nhiên
                    target_date = target_date.replace(
                        hour=random.randint(8, 22),
                        minute=random.randint(0, 59),
                        second=random.randint(0, 59)
                    )
                else:
                    target_date = datetime.datetime.now()
                
                bot.make_commit_with_date(target_date)
            except ValueError:
                print("❌ Định dạng ngày không đúng! Sử dụng YYYY-MM-DD")
        
        elif choice == '5':
            print("🚀 CHỨC NĂNG AUTO PUSH - Giống như trong video!")
            repo_url = input("GitHub repo URL (vd: https://github.com/namxely/repo-name.git): ").strip()
            if not repo_url:
                repo_url = "https://github.com/namxely/github-activity-bot.git"  # Default
                
            days_back = input("Số ngày quá khứ (mặc định 30): ").strip()
            days_back = int(days_back) if days_back.isdigit() else 30
            
            push_freq = input("Push mỗi bao nhiêu commits (mặc định 5): ").strip()
            push_freq = int(push_freq) if push_freq.isdigit() else 5
            
            print(f"\n📋 Sẽ tạo commits cho {days_back} ngày qua và push định kỳ")
            print(f"📤 Repository: {repo_url}")
            confirm = input("Bắt đầu? (y/n): ").strip().lower()
            
            if confirm in ['y', 'yes', 'có']:
                bot.fill_past_activity_and_push(days_back, (1, 3), repo_url, push_freq)
            else:
                print("❌ Đã hủy!")
        
        elif choice == '6':
            repo_url = input("GitHub repo URL (Enter = mặc định): ").strip()
            if not repo_url:
                repo_url = "https://github.com/namxely/github-activity-bot.git"
            bot.auto_push_to_github(repo_url)
                
        elif choice == '7':
            bot.setup_scheduler()
        elif choice == '8':
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()

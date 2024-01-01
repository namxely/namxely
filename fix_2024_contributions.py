#!/usr/bin/env python3
"""
Force Fix GitHub Contributions - Tạo nhiều commits cho 2024
"""

from github_activity_bot import GitHubActivityBot
import datetime
import random

def fix_2024_contributions():
    """Tạo thêm nhiều commits cho 2024"""
    bot = GitHubActivityBot()
    
    print("🔧 FIXING 2024 CONTRIBUTIONS")
    print("=" * 40)
    
    # Tạo commits từ tháng 1 đến tháng 7 năm 2024
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 7, 31)
    
    current_date = start_date
    total_commits = 0
    
    while current_date <= end_date:
        # Tạo 1-3 commits mỗi ngày
        if current_date.weekday() < 5:  # Chỉ ngày thường
            commits_today = random.randint(1, 3)
            
            for _ in range(commits_today):
                # Thời gian ngẫu nhiên trong ngày
                commit_time = current_date.replace(
                    hour=random.randint(9, 18),
                    minute=random.randint(0, 59),
                    second=random.randint(0, 59)
                )
                
                if bot.make_commit_with_date(commit_time):
                    total_commits += 1
                    if total_commits % 10 == 0:
                        print(f"✅ Đã tạo {total_commits} commits...")
        
        current_date += datetime.timedelta(days=1)
    
    print(f"\n🎉 HOÀN THÀNH! Đã tạo thêm {total_commits} commits cho 2024!")
    
    # Push ngay
    print("📤 Đang push lên GitHub...")
    if bot.auto_push_to_github("https://github.com/namxely/namxely.git"):
        print("✅ Push thành công!")
        print("🔗 Kiểm tra: https://github.com/namxely")
    else:
        print("❌ Push thất bại!")

if __name__ == "__main__":
    fix_2024_contributions()

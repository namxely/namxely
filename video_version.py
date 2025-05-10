#!/usr/bin/env python3
"""
Auto GitHub Activity - Giống như trong video
Tự động tạo commits cho quá khứ và push lên GitHub
"""

from github_activity_bot import GitHubActivityBot
import subprocess
import sys

def quick_setup():
    """Setup nhanh như trong video"""
    print("🎬 GITHUB ACTIVITY BOT - Giống như trong video!")
    print("=" * 55)
    
    # Bước 1: Tạo repository trên GitHub
    print("\n📋 BƯỚC 1: Tạo repository trên GitHub")
    print("-" * 40)
    print("1. Vào: https://github.com/new")
    print("2. Repository name: github-activity-bot")  
    print("3. Public repository")
    print("4. KHÔNG check 'Add README'")
    print("5. Create repository")
    
    input("\n✋ Nhấn Enter sau khi tạo xong repository...")
    
    # Bước 2: Kết nối và push
    print("\n📤 BƯỚC 2: Kết nối repository")
    print("-" * 40)
    
    repo_url = "https://github.com/namxely/github-activity-bot.git"
    print(f"Repository URL: {repo_url}")
    
    try:
        # Add remote
        print("🔗 Thêm remote origin...")
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=False)
        
        # Set branch
        print("🌿 Set branch main...")
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        
        # Push existing commits
        print("📤 Push commits hiện có...")
        result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], 
                               capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Kết nối thành công!")
            return True
        else:
            print(f"⚠️ Push result: {result.stderr}")
            print("💡 Repository có thể chưa tồn tại hoặc cần authentication")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

def run_like_video():
    """Chạy giống như trong video"""
    print("\n🎬 CHẠY GIỐNG NHƯ TRONG VIDEO")
    print("=" * 40)
    
    bot = GitHubActivityBot()
    
    # Tham số giống video
    days_back = 90  # 3 tháng
    repo_url = "https://github.com/namxely/github-activity-bot.git"
    
    print(f"📅 Sẽ tạo commits cho {days_back} ngày qua")
    print(f"📤 Push lên: {repo_url}")
    print(f"⚡ Tự động push mỗi 3 commits")
    
    confirm = input("\n🚀 Bắt đầu? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes', 'có']:
        print("\n🎯 BẮT ĐẦU TẠO COMMITS...")
        bot.fill_past_activity_and_push(
            days_back=days_back,
            commits_per_day_range=(1, 4), 
            repo_url=repo_url,
            push_frequency=3
        )
        
        print("\n🎉 HOÀN THÀNH!")
        print("✅ Kiểm tra GitHub profile của bạn:")
        print("🔗 https://github.com/namxely")
        
    else:
        print("❌ Đã hủy!")

if __name__ == "__main__":
    print("🎬 GITHUB ACTIVITY BOT - VIDEO VERSION")
    print("=" * 50)
    
    while True:
        print("\nChọn:")
        print("1. 🔧 Setup nhanh (tạo repo + kết nối)")
        print("2. 🎬 Chạy như trong video (tạo commits + push)")
        print("3. 📊 Xem commits hiện tại")
        print("4. 🚪 Thoát")
        
        choice = input("\nChọn (1-4): ").strip()
        
        if choice == '1':
            if quick_setup():
                print("\n✅ Setup thành công! Có thể chạy option 2.")
            else:
                print("\n❌ Setup thất bại. Kiểm tra lại repository.")
                
        elif choice == '2':
            run_like_video()
            
        elif choice == '3':
            print("\n📊 20 commits gần nhất:")
            print("-" * 40)
            try:
                result = subprocess.run(['git', 'log', '--oneline', '-20'], 
                                      capture_output=True, text=True, check=True)
                print(result.stdout)
            except Exception as e:
                print(f"❌ Lỗi: {e}")
                
        elif choice == '4':
            print("\n👋 Tạm biệt!")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ!")

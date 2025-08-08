#!/usr/bin/env python3
"""
Simple GitHub Activity Bot - Local Test Only
Chỉ để test local, không cần push lên GitHub
"""

from github_activity_bot import GitHubActivityBot
import time
import random

def test_single_commit():
    """Test tạo 1 commit"""
    print("🚀 Test tạo 1 commit...")
    bot = GitHubActivityBot()
    if bot.make_commit():
        print("✅ Test thành công!")
    else:
        print("❌ Test thất bại!")

def test_multiple_commits():
    """Test tạo nhiều commits"""
    num_commits = random.randint(2, 4)
    print(f"🎯 Test tạo {num_commits} commits...")
    
    bot = GitHubActivityBot()
    success_count = 0
    
    for i in range(num_commits):
        print(f"📝 Đang tạo commit {i+1}/{num_commits}...")
        if bot.make_commit():
            success_count += 1
            print(f"✅ Commit {i+1} thành công!")
        else:
            print(f"❌ Commit {i+1} thất bại!")
        
        # Nghỉ ngắn giữa các commits
        if i < num_commits - 1:
            print("⏳ Nghỉ 3 giây...")
            time.sleep(3)
    
    print(f"🎉 Hoàn thành! {success_count}/{num_commits} commits thành công!")

def view_recent_commits():
    """Xem các commits gần đây"""
    print("📊 Các commits gần đây:")
    print("-" * 50)
    import subprocess
    try:
        result = subprocess.run(['git', 'log', '--oneline', '-10'], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("❌ Không thể xem git log!")

def view_current_status():
    """Xem trạng thái hiện tại"""
    print("📋 Trạng thái repository:")
    print("-" * 50)
    import subprocess
    try:
        # Git status
        result = subprocess.run(['git', 'status', '--short'], 
                              capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print("Các file đã thay đổi:")
            print(result.stdout)
        else:
            print("✅ Working directory clean!")
        
        # Branch info
        result = subprocess.run(['git', 'branch'], 
                              capture_output=True, text=True, check=True)
        print(f"\nBranch hiện tại: {result.stdout.strip()}")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi: {e}")

def main():
    print("🤖 GitHub Activity Bot - LOCAL TEST")
    print("=====================================")
    
    while True:
        print("\n📋 MENU TEST:")
        print("1. Test tạo 1 commit")
        print("2. Test tạo nhiều commits (2-4)")
        print("3. Xem commits gần đây")
        print("4. Xem trạng thái repository")
        print("5. Chạy bot chính (menu đầy đủ)")
        print("6. Thoát")
        
        choice = input("\n🎯 Chọn (1-6): ").strip()
        
        if choice == '1':
            test_single_commit()
        elif choice == '2':
            test_multiple_commits()
        elif choice == '3':
            view_recent_commits()
        elif choice == '4':
            view_current_status()
        elif choice == '5':
            print("🔄 Chuyển sang bot chính...")
            import subprocess
            subprocess.run(['python', 'github_activity_bot.py'])
            break
        elif choice == '6':
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    main()

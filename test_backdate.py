#!/usr/bin/env python3
"""
Test Backdate Commits - GitHub Activity Bot
Tạo commits cho các ngày trong quá khứ
"""

from github_activity_bot import GitHubActivityBot
import datetime
import random

def test_backdate():
    """Test tạo commits cho quá khứ"""
    print("🕒 TEST BACKDATE COMMITS")
    print("=" * 40)
    
    bot = GitHubActivityBot()
    
    # Test tạo commits cho 7 ngày qua
    days_to_test = 7
    print(f"📅 Sẽ tạo commits cho {days_to_test} ngày qua...")
    
    today = datetime.datetime.now()
    success_count = 0
    
    for i in range(days_to_test, 0, -1):
        target_date = today - datetime.timedelta(days=i)
        
        # Tạo thời gian ngẫu nhiên trong ngày
        target_date = target_date.replace(
            hour=random.randint(9, 18),  # 9AM - 6PM
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        
        print(f"\n📆 Tạo commit cho: {target_date.strftime('%Y-%m-%d %H:%M:%S')}")
        
        if bot.make_commit_with_date(target_date):
            success_count += 1
            print("✅ Thành công!")
        else:
            print("❌ Thất bại!")
    
    print(f"\n🎉 HOÀN THÀNH! {success_count}/{days_to_test} commits thành công!")
    
    # Xem kết quả
    print("\n📊 Commits vừa tạo:")
    print("-" * 40)
    import subprocess
    try:
        result = subprocess.run(['git', 'log', '--oneline', '-10', '--date=short', '--pretty=format:%h %ad %s'], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
    except Exception as e:
        print(f"❌ Không thể xem log: {e}")

def test_specific_date():
    """Test tạo commit cho ngày cụ thể"""
    print("\n🎯 TEST COMMIT CHO NGÀY CỤ THỂ")
    print("=" * 40)
    
    bot = GitHubActivityBot()
    
    # Test cho ngày 2025-08-01
    specific_date = datetime.datetime(2025, 8, 1, 14, 30, 0)
    
    print(f"📅 Tạo commit cho: {specific_date.strftime('%Y-%m-%d %H:%M:%S')}")
    
    if bot.make_commit_with_date(specific_date):
        print("✅ Thành công!")
    else:
        print("❌ Thất bại!")

if __name__ == "__main__":
    print("🚀 STARTING BACKDATE TESTS...")
    print("=" * 50)
    
    # Test 1: Backdate commits
    test_backdate()
    
    # Test 2: Specific date commit  
    test_specific_date()
    
    print("\n" + "=" * 50)
    print("🏁 ALL TESTS COMPLETED!")

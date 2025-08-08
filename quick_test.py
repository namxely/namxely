#!/usr/bin/env python3
"""
Quick Test - GitHub Activity Bot
Test nhanh chức năng bot
"""

import os
import random
import datetime
import subprocess
from pathlib import Path

def quick_test():
    """Test nhanh tạo commit"""
    print("🚀 QUICK TEST - GitHub Activity Bot")
    print("=" * 40)
    
    try:
        # Tạo nội dung test
        activities = [
            "🧪 Test commit",
            "⚡ Quick test",
            "🔍 Bot testing",
            "🎯 Function test"
        ]
        
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        activity = random.choice(activities)
        
        content = f"""=== TEST ACTIVITY LOG ===
Thời gian: {timestamp}
Hoạt động: {activity}
Test ID: {random.randint(1000, 9999)}
Status: Testing ⚡

Test thành công! Bot hoạt động bình thường.
=== END TEST ===
"""
        
        # Ghi file
        print("📝 Đang tạo test file...")
        with open('activity.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ File created!")
        
        # Git add
        print("➕ Git add...")
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added!")
        
        # Git commit
        print("💾 Git commit...")
        commit_msg = f"{activity} - {timestamp}"
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
        print(f"✅ Commit success: {commit_msg}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def view_commits():
    """Xem commits gần đây"""
    print("\n📊 Recent commits:")
    print("-" * 40)
    try:
        result = subprocess.run(['git', 'log', '--oneline', '-5'], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Starting test...")
    
    if quick_test():
        print("\n🎉 TEST PASSED!")
        view_commits()
    else:
        print("\n💥 TEST FAILED!")
    
    print("\n" + "=" * 40)
    print("Test completed!")

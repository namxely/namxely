#!/usr/bin/env python3
"""
Script to fix GitHub contribution issues
- Ensure commits are on main branch (not master)
- Make sure files are actually changed
- Verify commit structure
"""

import subprocess
import os
import random
from datetime import datetime, timedelta
import json

def run_git_command(command):
    """Run git command and return output"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        return None

def create_meaningful_changes():
    """Create files with meaningful content changes"""
    files_to_modify = [
        'README.md',
        'activity.txt', 
        'log.md',
        'notes.txt',
        'updates.json'
    ]
    
    content_templates = {
        'README.md': [
            "# My GitHub Activity\n\nThis repository tracks my coding activity.\n\nLast update: {}",
            "# Personal Project Repository\n\nTracking my daily contributions.\n\nUpdated: {}",
            "# Activity Tracker\n\nAutomated commits for GitHub activity.\n\nTimestamp: {}"
        ],
        'activity.txt': [
            "Activity Log - {}\n\nDaily development work and improvements.",
            "Development Activity - {}\n\nCoding, testing, and feature development.",
            "Project Activity - {}\n\nContinuous development and maintenance work."
        ],
        'log.md': [
            "# Activity Log\n\n## {}\n- Working on projects\n- Code improvements\n- Bug fixes",
            "# Development Log\n\n## Date: {}\n- Feature development\n- Testing\n- Documentation",
            "# Progress Log\n\n## {}\n- Code refactoring\n- Performance optimization\n- New features"
        ],
        'notes.txt': [
            "Development Notes - {}\n\nWorking on various improvements and features.",
            "Project Notes - {}\n\nContinuous development and maintenance.",
            "Technical Notes - {}\n\nCode optimization and bug fixes."
        ],
        'updates.json': [
            '{{"timestamp": "{}", "activity": "development", "status": "active"}}',
            '{{"date": "{}", "type": "update", "description": "code improvements"}}',
            '{{"updated": "{}", "action": "maintenance", "notes": "regular updates"}}'
        ]
    }
    
    # Randomly select files to modify
    files_to_change = random.sample(files_to_modify, random.randint(1, 3))
    
    for file in files_to_change:
        template = random.choice(content_templates[file])
        content = template.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Modified {file}")

def make_contribution_commit(date_str, commit_message):
    """Make a commit that should count as a contribution"""
    # Create meaningful file changes
    create_meaningful_changes()
    
    # Add all changes
    run_git_command("git add .")
    
    # Make commit with specific date
    commit_cmd = f'git commit -m "{commit_message}" --date="{date_str}"'
    result = run_git_command(commit_cmd)
    
    if result is not None:
        print(f"✓ Created contribution commit: {commit_message}")
        return True
    return False

def fill_contributions_for_period(start_date, end_date, commits_per_day_range=(1, 5)):
    """Fill contributions for a specific time period"""
    current_date = start_date
    total_commits = 0
    
    while current_date <= end_date:
        # Skip some days randomly for more natural pattern
        if random.random() > 0.15:  # 85% chance to make commits
            num_commits = random.randint(*commits_per_day_range)
            
            for i in range(num_commits):
                # Random time during the day
                hour = random.randint(9, 22)
                minute = random.randint(0, 59)
                
                commit_time = current_date.replace(hour=hour, minute=minute)
                date_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")
                
                commit_messages = [
                    "🚀 Feature development",
                    "🐛 Bug fixes and improvements", 
                    "📝 Documentation updates",
                    "⚡ Performance optimization",
                    "🔧 Code refactoring",
                    "✨ New features added",
                    "🎨 UI/UX improvements",
                    "🔒 Security enhancements",
                    "🧹 Code cleanup",
                    "📊 Data analysis updates",
                    "🔄 Workflow improvements",
                    "🏗️ Architecture improvements"
                ]
                
                message = random.choice(commit_messages)
                
                if make_contribution_commit(date_str, message):
                    total_commits += 1
                    
                # Small delay to ensure different timestamps
                import time
                time.sleep(0.1)
        
        current_date += timedelta(days=1)
    
    print(f"\n✓ Created {total_commits} contribution commits")
    return total_commits

def main():
    """Main function"""
    print("🔧 GitHub Contribution Fixer")
    print("=" * 40)
    
    # Check current branch
    current_branch = run_git_command("git branch --show-current")
    print(f"Current branch: {current_branch}")
    
    if current_branch != "main":
        print("⚠️ Switching to main branch...")
        run_git_command("git checkout main")
    
    print("\nSelect time period to fill:")
    print("1. Last 30 days")
    print("2. Last 90 days") 
    print("3. Last 180 days")
    print("4. Entire 2024")
    print("5. Custom date range")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    end_date = datetime.now().replace(hour=23, minute=59, second=59)
    
    if choice == "1":
        start_date = end_date - timedelta(days=30)
    elif choice == "2":
        start_date = end_date - timedelta(days=90)
    elif choice == "3":
        start_date = end_date - timedelta(days=180)
    elif choice == "4":
        start_date = datetime(2024, 1, 1)
    elif choice == "5":
        start_str = input("Enter start date (YYYY-MM-DD): ")
        end_str = input("Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d").replace(hour=23, minute=59)
    else:
        print("Invalid choice")
        return
    
    print(f"\nFilling contributions from {start_date.date()} to {end_date.date()}")
    confirm = input("Continue? (y/N): ").lower()
    
    if confirm != 'y':
        print("Cancelled")
        return
    
    # Fill contributions
    total = fill_contributions_for_period(start_date, end_date)
    
    # Push to GitHub
    print(f"\n🚀 Pushing {total} commits to GitHub...")
    push_result = run_git_command("git push origin main --force")
    
    if push_result is not None:
        print("✓ Successfully pushed to GitHub!")
        print(f"\nCheck your contribution graph at:")
        print("https://github.com/namxely")
        print("\n💡 Note: GitHub may take a few minutes to update the contribution graph")
    else:
        print("❌ Failed to push to GitHub")

if __name__ == "__main__":
    main()

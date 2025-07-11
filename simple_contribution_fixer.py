#!/usr/bin/env python3
"""
Simple GitHub contribution fixer - no emojis to avoid encoding issues
"""

import subprocess
import os
import random
from datetime import datetime, timedelta

def run_command(command):
    """Run command safely"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Command failed: {command}")
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def create_file_changes():
    """Create meaningful file changes"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Update README.md
    readme_content = f"""# My GitHub Repository

This is my personal repository for tracking coding activity.

Last updated: {timestamp}

## Activity
- Regular development work
- Code improvements and bug fixes
- Feature development
- Documentation updates
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # Update activity.txt
    activity_content = f"""Activity Log - {timestamp}

Development work continues with regular commits.
Working on various improvements and new features.
"""
    
    with open('activity.txt', 'w', encoding='utf-8') as f:
        f.write(activity_content)
    
    # Create/update a random file
    random_files = ['notes.txt', 'log.md', 'updates.txt', 'progress.txt']
    random_file = random.choice(random_files)
    
    content = f"""File: {random_file}
Updated: {timestamp}

Regular development activity.
Code improvements and maintenance.
"""
    
    with open(random_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: README.md, activity.txt, {random_file}")

def make_commit(date_str, message):
    """Make a commit with specific date"""
    create_file_changes()
    
    # Add all files
    if run_command("git add .") is None:
        return False
    
    # Commit with date
    commit_cmd = f'git commit -m "{message}" --date="{date_str}"'
    if run_command(commit_cmd) is None:
        return False
    
    print(f"Created commit: {message}")
    return True

def fill_last_30_days():
    """Fill contributions for last 30 days"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    current_date = start_date
    total_commits = 0
    
    messages = [
        "Feature development",
        "Bug fixes and improvements", 
        "Documentation updates",
        "Performance optimization",
        "Code refactoring",
        "New features added",
        "UI improvements",
        "Security enhancements",
        "Code cleanup",
        "Data analysis updates",
        "Workflow improvements",
        "Architecture improvements",
        "Testing improvements",
        "Configuration updates",
        "Library updates"
    ]
    
    while current_date <= end_date:
        # Skip some days for natural pattern
        if random.random() > 0.2:  # 80% chance to commit
            num_commits = random.randint(1, 4)
            
            for i in range(num_commits):
                hour = random.randint(9, 22)
                minute = random.randint(0, 59)
                
                commit_time = current_date.replace(hour=hour, minute=minute)
                date_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")
                
                message = random.choice(messages)
                
                if make_commit(date_str, message):
                    total_commits += 1
        
        current_date += timedelta(days=1)
    
    return total_commits

def main():
    print("Simple GitHub Contribution Fixer")
    print("=" * 40)
    
    # Check git status
    if run_command("git status") is None:
        print("Not in a git repository!")
        return
    
    print("This will create commits for the last 30 days")
    confirm = input("Continue? (y/N): ").lower()
    
    if confirm != 'y':
        print("Cancelled")
        return
    
    print("Creating commits...")
    total = fill_last_30_days()
    
    print(f"\nCreated {total} commits")
    
    # Push to GitHub
    print("Pushing to GitHub...")
    if run_command("git push origin main --force"):
        print("Successfully pushed to GitHub!")
        print("\nCheck your contribution graph at:")
        print("https://github.com/namxely")
    else:
        print("Failed to push to GitHub")

if __name__ == "__main__":
    main()

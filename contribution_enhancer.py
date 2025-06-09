#!/usr/bin/env python3
"""
Script to create additional contributions with different commit patterns
to ensure GitHub counts them properly
"""

import subprocess
import random
from datetime import datetime, timedelta
import json

def run_git(command):
    """Run git command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
        return result.returncode == 0
    except:
        return False

def create_diverse_content():
    """Create diverse file content to ensure different commits"""
    timestamp = datetime.now().isoformat()
    
    # Create multiple files with different types of content
    files_content = {
        'README.md': f"""# Personal Development Repository

Welcome to my coding journey! 

## Recent Updates
- Last modified: {timestamp}
- Status: Active development
- Focus: Continuous learning and improvement

## Project Structure
This repository contains various projects and experiments.

## Technologies
- Python
- JavaScript  
- Web Development
- Data Analysis

---
Generated on: {timestamp}
""",

        'CHANGELOG.md': f"""# Changelog

## [{datetime.now().strftime('%Y-%m-%d')}] - Latest Updates

### Added
- New feature implementations
- Enhanced functionality
- Improved error handling

### Changed  
- Updated documentation
- Refactored code structure
- Performance improvements

### Fixed
- Bug fixes and stability improvements
- Resolved compatibility issues

---
Last update: {timestamp}
""",

        'docs.md': f"""# Documentation

## Overview
This document contains project documentation and notes.

## Last Modified: {timestamp}

## Development Notes
- Regular commits and updates
- Continuous integration
- Code quality improvements

## Features
1. Automated workflows
2. Testing framework
3. Documentation updates
4. Performance monitoring

Generated: {timestamp}
""",

        'config.json': json.dumps({
            'version': '1.0.0',
            'updated': timestamp,
            'environment': 'development',
            'features': {
                'auto_commit': True,
                'push_enabled': True,
                'backup': True
            },
            'metadata': {
                'last_run': timestamp,
                'commit_count': random.randint(1, 100),
                'status': 'active'
            }
        }, indent=2),

        'activity.log': f"""Activity Log Entry
==================

Timestamp: {timestamp}
Action: Development work
Status: In progress

Details:
- Code development and testing
- Documentation updates  
- Feature implementations
- Bug fixes and improvements

Session ID: {random.randint(1000, 9999)}
Duration: {random.randint(30, 180)} minutes

Next steps:
- Continue development
- Review and refactor
- Update documentation
- Deploy changes

End of log entry.
""",

        'notes.txt': f"""Development Notes - {datetime.now().strftime('%Y-%m-%d')}

Today's Progress:
- Worked on core functionality
- Implemented new features
- Fixed reported issues
- Updated documentation

Code Quality:
- Refactored legacy code
- Added unit tests
- Improved error handling
- Enhanced performance

Next Tasks:
- Review pull requests
- Update dependencies
- Deploy to production
- Monitor performance

Timestamp: {timestamp}
Random ID: {random.randint(10000, 99999)}

---
Note: This file is automatically updated during development sessions.
"""
    }
    
    # Randomly select 2-4 files to update
    files_to_update = random.sample(list(files_content.keys()), random.randint(2, 4))
    
    for filename in files_to_update:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(files_content[filename])
        print(f"Updated: {filename}")

def make_contribution_commit(date_obj):
    """Make a single contribution commit"""
    create_diverse_content()
    
    if not run_git("git add ."):
        return False
    
    commit_messages = [
        "Add new functionality and improvements",
        "Update documentation and code structure", 
        "Fix bugs and enhance performance",
        "Implement new features and tests",
        "Refactor code and update dependencies",
        "Add configuration and logging",
        "Update project structure and docs",
        "Enhance error handling and validation",
        "Add monitoring and analytics",
        "Update build process and workflows",
        "Add security improvements",
        "Update UI and user experience",
        "Add database optimizations",
        "Update API endpoints and responses",
        "Add testing framework and coverage",
        "Update deployment configuration",
        "Add backup and recovery features",
        "Update authentication system",
        "Add notification system",
        "Update reporting and analytics"
    ]
    
    message = random.choice(commit_messages)
    date_str = date_obj.strftime('%Y-%m-%d %H:%M:%S')
    
    commit_cmd = f'git commit -m "{message}" --date="{date_str}"'
    
    if run_git(commit_cmd):
        print(f"✓ Commit: {message} ({date_str})")
        return True
    return False

def fill_missing_days():
    """Fill in missing days with contributions"""
    # Focus on recent months for better visibility
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)  # Last 2 months
    
    current = start_date
    total_commits = 0
    
    while current <= end_date:
        # Higher chance of commits on weekdays
        is_weekend = current.weekday() >= 5
        commit_chance = 0.7 if not is_weekend else 0.4
        
        if random.random() < commit_chance:
            num_commits = random.randint(1, 3 if not is_weekend else 2)
            
            for i in range(num_commits):
                # Random time during work hours
                if is_weekend:
                    hour = random.randint(10, 20)
                else:
                    hour = random.randint(9, 18)
                
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                commit_time = current.replace(hour=hour, minute=minute, second=second)
                
                if make_contribution_commit(commit_time):
                    total_commits += 1
                    
                # Small delay to avoid identical timestamps
                import time
                time.sleep(0.1)
        
        current += timedelta(days=1)
    
    return total_commits

def main():
    print("GitHub Contribution Enhancer")
    print("=" * 40)
    
    print("This will create diverse commits for the last 60 days")
    print("to ensure proper GitHub contribution counting.")
    
    confirm = input("\nContinue? (y/N): ").lower()
    if confirm != 'y':
        print("Cancelled.")
        return
    
    print("\nCreating diverse commits...")
    total = fill_missing_days()
    
    print(f"\n✓ Created {total} new commits")
    
    # Push to GitHub
    print("\nPushing to GitHub...")
    if run_git("git push origin main --force"):
        print("✓ Successfully pushed to GitHub!")
        print("\nYour contribution graph should update soon.")
        print("Check: https://github.com/namxely")
        
        # Show final stats
        try:
            result = subprocess.run("git log --oneline", shell=True, capture_output=True, text=True)
            total_commits = len(result.stdout.strip().split('\n'))
            print(f"\nTotal commits in repository: {total_commits}")
        except:
            pass
            
    else:
        print("❌ Failed to push to GitHub")
        print("You may need to push manually with: git push origin main --force")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Cleanup and Final Comprehensive Check
"""

import os
import glob

print("=" * 80)
print("پاک‌سازی و بررسی نهایی")
print("=" * 80)

# Step 1: List all Excel files
print("\n📁 STEP 1: فایل‌های Excel موجود:")
excel_files = glob.glob("BugTracking*.xlsx")
for f in sorted(excel_files):
    size = os.path.getsize(f) / 1024
    print(f"   {f:50s} - {size:6.1f} KB")

# Step 2: Identify files to keep vs delete
print("\n🗑️  STEP 2: تصمیم‌گیری...")

KEEP = 'BugTracking_Complete_FINAL.xlsx'
DELETE = [f for f in excel_files if f != KEEP]

print(f"\n   ✅ نگه‌داری: {KEEP}")
print(f"\n   ❌ حذف ({len(DELETE)} فایل):")
for f in DELETE:
    print(f"      - {f}")

# Step 3: Delete unnecessary files
print(f"\n🗑️  STEP 3: حذف فایل‌های اضافی...")
for f in DELETE:
    try:
        os.remove(f)
        print(f"   ✅ حذف شد: {f}")
    except Exception as e:
        print(f"   ❌ خطا در حذف {f}: {e}")

# Step 4: List Python scripts
print("\n📜 STEP 4: اسکریپت‌های Python:")
py_files = glob.glob("*.py")
important = [
    'create_final_excel.py',
    'rebuild_complete_dashboard.py', 
    'final_validation_rebuilt.py'
]

for f in sorted(py_files):
    if f in important:
        print(f"   ✅ {f}")
    else:
        print(f"   ⚠️  {f}")

print("\n" + "=" * 80)
print("پاک‌سازی انجام شد!")
print("=" * 80)

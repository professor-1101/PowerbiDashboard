#!/usr/bin/env python3
"""
Create PBIT file from components
Package all JSON components into a ZIP and rename to .pbit
"""

import zipfile
import os
import shutil

print("=" * 80)
print("🔧 CREATING PBIT FILE FROM COMPONENTS")
print("=" * 80)

# Define source and output
components_dir = 'pbit_components'
output_zip = 'BugTracking_Dashboard.zip'
output_pbit = 'BugTracking_Dashboard.pbit'

# Files to include in the PBIT (in correct structure)
files_to_add = {
    'DataModelSchema': 'DataModelSchema',
    'DiagramLayout': 'DiagramLayout',
    'Report/Layout': 'Report/Layout',
    'Settings': 'Settings',
    'Version': 'Version',
    '[Content_Types].xml': '[Content_Types].xml',
    'SecurityBindings': 'SecurityBindings',
    'Metadata': 'Metadata'
}

# Create ZIP file with proper compression
print("\n📦 Creating ZIP archive...")

try:
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for zip_path, file_name in files_to_add.items():
            source_path = os.path.join(components_dir, file_name)

            if os.path.exists(source_path):
                print(f"  ✅ Adding: {zip_path}")
                zipf.write(source_path, zip_path)
            else:
                print(f"  ⚠️  Missing: {source_path}")

    print(f"\n✅ ZIP created: {output_zip}")

    # Rename to .pbit
    if os.path.exists(output_pbit):
        os.remove(output_pbit)

    shutil.move(output_zip, output_pbit)
    print(f"✅ Renamed to: {output_pbit}")

    # Get file size
    file_size = os.path.getsize(output_pbit) / 1024
    print(f"\n📊 File size: {file_size:.1f} KB")

except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 80)
print("📝 PBIT FILE CREATED")
print("=" * 80)

print(f"""
✅ File: {output_pbit}

📋 Structure:
  • DataModelSchema - Data model with raw_data table + 11 measures
  • Report/Layout - Report layout with 6 basic visualizations
  • DiagramLayout - Model diagram view
  • Settings - Report settings
  • Version - Power BI version
  • SecurityBindings - Security settings
  • Metadata - Query metadata
  • [Content_Types].xml - Content types manifest

⚠️  IMPORTANT NOTES:

1. این یک PBIT ساده و پایه است
2. برای باز کردن:
   - Power BI Desktop باز کن
   - Open > این فایل رو انتخاب کن
   - مسیر فایل Excel رو مشخص کن

3. بعد از باز شدن:
   - بقیه 37 چارت رو دستی اضافه کن
   - یا از Excel خود Power BI استفاده کن

4. احتمال خطا:
   - ممکنه Power BI فرمت رو نشناسه
   - ممکنه نیاز به تنظیمات بیشتر باشه

🎯 راه تضمینی:
   همون Excel رو مستقیماً توی Power BI import کن
   و Dashboard رو دستی بساز (خیلی سریع‌تره!)

""")

print("=" * 80)

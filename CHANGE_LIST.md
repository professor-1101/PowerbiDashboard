# 📋 لیست کامل تغییرات - Bug Tracking Dashboard

## 🎯 خلاصه تغییرات

این سند لیست کامل تغییراتی است که باید روی پروژه اعمال شود تا با داده‌های واقعی Azure DevOps سازگار باشد.

---

## 📊 تغییرات اصلی

### 1️⃣ تغییرات ساختار داده (Data Structure Changes)

#### الف) اضافه کردن فیلدهای محاسبه‌ای جدید

```python
# فیلدهای جدیدی که باید اضافه شوند:

is_reopen (int):
  - محاسبه: ReopenCount > 0
  - مقدار: 1 = بله، 0 = خیر
  - رنگ: 🟡 زرد (Calculable)

is_duplicate (int):
  - محاسبه: IF CloseReason == "Duplicate" THEN 1 ELSE 0
  - مقدار: 1 = بله، 0 = خیر
  - رنگ: 🟡 زرد (Calculable)

ReopenCount (int):
  - محاسبه: شمارش تعداد دفعات State: Closed → Active
  - مقدار: عدد صحیح
  - رنگ: 🟡 زرد (Calculable)

StateChangeCount (int):
  - محاسبه: تعداد کل تغییرات State
  - مقدار: عدد صحیح
  - رنگ: 🟡 زرد (Calculable)
```

#### ب) حذف فیلدهایی که نداریم

```python
# این فیلدها باید از Excel حذف شوند یا N/A شوند:

is_escaped → حذف (یا N/A)
tags → حذف (یا N/A)
ExternalTicketID → حذف (یا N/A)
VerifierName → حذف (یا N/A)
VerifierID → حذف (یا N/A)
TestEffortHrs → حذف (یا N/A)
RetestEffortHrs → حذف (یا N/A)
```

#### ج) تغییر نام فیلدها (Field Renaming)

```python
# تبدیل اسم‌های Azure DevOps به اسم‌های استاندارد:

System.Id → BugID
System.Title → Title
System.State → State
System.CreatedBy → CreatedBy
System.AssignedTo → AssignedTo
System.ClosedBy → ClosedBy
Microsoft.VSTS.Common.Priority → Priority
Microsoft.VSTS.Common.Severity → Severity
Microsoft.VSTS.CMMI.CloseReason → CloseReason
```

---

### 2️⃣ تغییرات رنگ‌بندی Excel (Color Coding)

#### قانون رنگ‌بندی سلول‌ها:

```
🟢 سبز روشن (#D4EDDA):
   - فیلدهای مستقیم از Query
   - مثال: BugID, Title, State, Priority, CreatedDate

🟡 زرد روشن (#FFF3CD):
   - فیلدهای قابل محاسبه از Database
   - مثال: is_reopen, is_duplicate, LeadTimeHrs, CycleTimeHrs

🔵 آبی روشن (#CCE5FF):
   - فیلدهای Dashboard-Only (نیاز به API/Relations)
   - مثال: FixEffort, RootCause, Resolution

🔴 قرمز روشن (#F8D7DA):
   - فیلدهای نداریم (Missing)
   - مثال: is_escaped, tags, TestEffortHrs
```

#### تغییرات در کد Python:

```python
# اضافه کردن رنگ‌بندی به header row:

def apply_field_coloring(ws, field_name, col_idx):
    """اعمال رنگ بر اساس نوع فیلد"""

    # Direct fields - Green
    direct_fields = ['BugID', 'Title', 'State', 'Priority', 'Severity', ...]
    # Calculable fields - Yellow
    calculable_fields = ['is_reopen', 'is_duplicate', 'LeadTimeHrs', ...]
    # Dashboard-only fields - Blue
    dashboard_fields = ['FixEffort', 'RootCause', 'Resolution', ...]
    # Missing fields - Red
    missing_fields = ['is_escaped', 'tags', 'TestEffortHrs', ...]

    cell = ws.cell(row=1, column=col_idx)

    if field_name in direct_fields:
        cell.fill = PatternFill(start_color='D4EDDA', fill_type='solid')
        cell.font = Font(color='155724', bold=True)
    elif field_name in calculable_fields:
        cell.fill = PatternFill(start_color='FFF3CD', fill_type='solid')
        cell.font = Font(color='856404', bold=True)
    elif field_name in dashboard_fields:
        cell.fill = PatternFill(start_color='CCE5FF', fill_type='solid')
        cell.font = Font(color='004085', bold=True)
    elif field_name in missing_fields:
        cell.fill = PatternFill(start_color='F8D7DA', fill_type='solid')
        cell.font = Font(color='721C24', bold=True)
```

---

### 3️⃣ اضافه کردن شیت توضیحات (Field Definitions Sheet)

#### ایجاد شیت جدید: "Field_Definitions"

```python
# ساختار شیت جدید:

ws_def = wb.create_sheet("Field_Definitions", 1)

# Header
headers = ['Field Name', 'Category', 'Color', 'Data Source', 'Calculation/Query', 'Description']

# Example rows:
[
    'BugID',
    '🟢 Direct',
    'سبز',
    'Azure DevOps Query',
    'System.Id',
    'شناسه یکتای Work Item'
],
[
    'is_reopen',
    '🟡 Calculable',
    'زرد',
    'محاسبه از Database',
    'ReopenCount > 0',
    'بررسی اینکه آیا باگ دوباره باز شده'
],
[
    'FixEffort',
    '🔵 Dashboard-Only',
    'آبی',
    'Related Tasks API',
    'SUM(RelatedTasks.CompletedWork)',
    'مجموع Effort تسک‌های مرتبط'
],
[
    'TestEffortHrs',
    '🔴 Missing',
    'قرمز',
    'ثبت نشده',
    'N/A',
    'این فیلد در سیستم وجود ندارد'
]
```

---

### 4️⃣ تغییرات در محاسبات (Calculation Updates)

#### الف) محاسبه is_reopen

```python
# قبل: نداشتیم
# بعد:

df_raw['is_reopen'] = (df_raw['ReopenCount'] > 0).astype(int)

# یا اگر ReopenCount نداریم، از State History:
# باید با Query جداگانه از WorkItemRevisions بگیریم
```

#### ب) محاسبه is_duplicate

```python
# قبل: نداشتیم
# بعد:

df_raw['is_duplicate'] = (df_raw['CloseReason'] == 'Duplicate').astype(int)
```

#### ج) محاسبه CycleTimeHrs (دقیق‌تر)

```python
# قبل: تصادفی بود
# بعد: باید از State History محاسبه بشه

# نیاز به Query از WorkItemRevisions:
SELECT
    WorkItemId,
    MIN(CASE WHEN NewValue = 'Active' THEN ChangedDate END) AS FirstActive,
    MAX(CASE WHEN NewValue = 'Closed' THEN ChangedDate END) AS LastClosed
FROM WorkItemRevisions
WHERE Field = 'System.State'
GROUP BY WorkItemId

# بعد:
CycleTimeHrs = DATEDIFF(hour, FirstActive, LastClosed)
```

---

### 5️⃣ تغییرات در چارت‌ها (Chart Updates)

#### چارت‌های جدید که باید اضافه شوند:

```
1. Pie Chart: is_duplicate Distribution
   - Legend: is_duplicate (Yes/No)
   - Values: Count

2. Bar Chart: Reopen Analysis (ReopenCount Distribution)
   - Axis: ReopenCount (0, 1, 2, 3+)
   - Values: Bug Count

3. Line Chart: State Changes Trend
   - Axis: Date
   - Values: StateChangeCount Average
```

#### چارت‌های حذف شده:

```
- هر چارتی که از فیلدهای 🔴 قرمز (Missing) استفاده می‌کنه
- مثلاً: Escaped Bugs Chart → حذف یا Disable
```

---

### 6️⃣ تغییرات در Metrics (291 متریک)

#### متریک‌های جدید:

```python
# اضافه شدن:

metrics['M_REOPEN_COUNT'] = {
    'code': 'M_REOPEN_COUNT',
    'name': 'Total Reopened Bugs',
    'value': '=SUMIF(raw_data!ReopenCount,">0")',
    'description': 'تعداد کل باگ‌هایی که حداقل یکبار بازگشایی شده‌اند'
}

metrics['M_DUPLICATE_COUNT'] = {
    'code': 'M_DUPLICATE_COUNT',
    'name': 'Total Duplicate Bugs',
    'value': '=COUNTIF(raw_data!is_duplicate,1)',
    'description': 'تعداد کل باگ‌های Duplicate'
}

metrics['M_REOPEN_RATE'] = {
    'code': 'M_REOPEN_RATE',
    'name': 'Reopen Rate %',
    'value': '=M_REOPEN_COUNT/M_TOTAL_BUGS*100',
    'description': 'درصد باگ‌های بازگشایی شده'
}
```

#### متریک‌های حذف شده:

```python
# حذف یا N/A:

metrics['M_TEST_EFFORT'] → حذف (نداریم)
metrics['M_ESCAPED_BUGS'] → حذف یا 0 (نداریم)
```

---

### 7️⃣ تغییرات در PBIT (Power BI Template)

#### الف) DataModelSchema

```json
// اضافه کردن فیلدهای جدید:

{
  "name": "is_reopen",
  "dataType": "int64",
  "sourceColumn": "is_reopen"
},
{
  "name": "is_duplicate",
  "dataType": "int64",
  "sourceColumn": "is_duplicate"
},
{
  "name": "ReopenCount",
  "dataType": "int64",
  "sourceColumn": "ReopenCount"
}
```

#### ب) Measures جدید

```dax
Reopened Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[is_reopen] = 1
)

Duplicate Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[is_duplicate] = 1
)

Reopen Rate =
DIVIDE([Reopened Bugs], [Total Bugs], 0) * 100
```

---

### 8️⃣ تغییرات در Query های Azure DevOps

#### Query اصلی (باید این فیلدها رو برگردونه):

```wiql
SELECT
    [System.Id],
    [System.Title],
    [System.State],
    [Microsoft.VSTS.Common.Priority],
    [Microsoft.VSTS.Common.Severity],
    [System.CreatedDate],
    [System.ClosedDate],
    [System.CreatedBy],
    [System.AssignedTo],
    [Microsoft.VSTS.CMMI.CloseReason],
    [System.AreaPath],
    [System.IterationPath]
FROM WorkItems
WHERE [System.WorkItemType] = 'Bug'
    AND [System.TeamProject] = 'YourProject'
ORDER BY [System.Id] DESC
```

#### Query برای ReopenCount:

```sql
-- باید از REST API یا WorkItemRevisions گرفته بشه
-- نمونه Query:

SELECT
    r.WorkItemId,
    COUNT(*) AS ReopenCount
FROM WorkItemRevisions r
WHERE r.FieldName = 'System.State'
    AND r.OldValue IN ('Closed', 'Resolved')
    AND r.NewValue IN ('Active', 'New', 'Reopened')
GROUP BY r.WorkItemId
```

---

## 🔧 تغییرات در کدها

### فایل‌های نیاز به تغییر:

1. ✅ **create_complete_dashboard.py**
   - اضافه کردن فیلدهای جدید
   - اعمال رنگ‌بندی
   - ایجاد شیت Field_Definitions

2. ✅ **update_add_more_charts.py**
   - بروزرسانی چارت‌ها با فیلدهای جدید

3. ✅ **add_all_43_charts.py**
   - بروزرسانی همه 43 چارت

4. ✅ **BugTracking_Complete.xlsx**
   - بازسازی کامل با ساختار جدید

5. ✅ **BugTracking_Dashboard.pbit**
   - بروزرسانی Data Model
   - اضافه کردن Measures جدید

---

## 📊 لیست کامل فیلدها (بعد از تغییرات)

### فیلدهای نهایی در Excel:

| # | Field Name | Type | Category | Color |
|---|------------|------|----------|-------|
| 1 | BugID | int | 🟢 Direct | سبز |
| 2 | Title | string | 🟢 Direct | سبز |
| 3 | State | string | 🟢 Direct | سبز |
| 4 | Priority | string | 🟢 Direct | سبز |
| 5 | Severity | string | 🟢 Direct | سبز |
| 6 | Category | string | 🟢 Direct | سبز |
| 7 | ProjectName | string | 🟢 Direct | سبز |
| 8 | TeamName | string | 🟢 Direct | سبز |
| 9 | SprintName | string | 🟢 Direct | سبز |
| 10 | ModuleName | string | 🟢 Direct | سبز |
| 11 | AssigneeName | string | 🟢 Direct | سبز |
| 12 | ReporterName | string | 🟢 Direct | سبز |
| 13 | CreatedDate | datetime | 🟢 Direct | سبز |
| 14 | ClosedDate | datetime | 🟢 Direct | سبز |
| 15 | CloseReason | string | 🟢 Direct | سبز |
| 16 | **is_reopen** | int | 🟡 Calculable | زرد |
| 17 | **is_duplicate** | int | 🟡 Calculable | زرد |
| 18 | **ReopenCount** | int | 🟡 Calculable | زرد |
| 19 | LeadTimeHrs | double | 🟡 Calculable | زرد |
| 20 | CycleTimeHrs | double | 🟡 Calculable | زرد |
| 21 | AgeDays | int | 🟡 Calculable | زرد |
| 22 | **FixEffort** | double | 🔵 Dashboard | آبی |
| 23 | **RootCause** | string | 🔵 Dashboard | آبی |
| 24 | **Resolution** | string | 🔵 Dashboard | آبی |

### فیلدهای حذف شده:

- ~~is_escaped~~ → حذف (نداریم)
- ~~tags~~ → حذف (نداریم)
- ~~ExternalTicketID~~ → حذف (نداریم)
- ~~VerifierName~~ → حذف (نداریم)
- ~~TestEffortHrs~~ → حذف (نداریم)

---

## ✅ چک‌لیست تغییرات

- [ ] دریافت CSV واقعی از Azure DevOps
- [ ] Field Mapping بین CSV و ساختار جدید
- [ ] اضافه کردن فیلدهای محاسبه‌ای (is_reopen, is_duplicate)
- [ ] رنگ‌بندی سلول‌ها بر اساس 4 دسته
- [ ] ایجاد شیت Field_Definitions
- [ ] بروزرسانی همه 43 چارت
- [ ] بروزرسانی 291 متریک
- [ ] بروزرسانی PBIT
- [ ] ایجاد Query های Azure DevOps
- [ ] تست و والیدیشن کامل

---

## 🎯 زمان تخمینی

- تحلیل CSV: 30 دقیقه
- Field Mapping: 1 ساعت
- اعمال تغییرات: 3-4 ساعت
- تست و والیدیشن: 1 ساعت
- **جمع کل: 5-6 ساعت**

---

**منتظر CSV واقعی برای شروع پیاده‌سازی! 🚀**

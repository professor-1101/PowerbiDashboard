# 🔍 تحلیل کامل فیلدها - Azure DevOps Bug Tracking

## 📊 طبقه‌بندی فیلدها بر اساس دسترسی

---

## 🟢 دسته 1: فیلدهای مستقیم از Query (Direct Database Fields)

این فیلدها مستقیماً از Azure DevOps با Query قابل دریافت هستند:

| فیلد | نوع | توضیحات | رنگ سلول |
|------|-----|---------|----------|
| BugID | int | شناسه یکتا | **سبز روشن** |
| Title | string | عنوان باگ | **سبز روشن** |
| State | string | وضعیت (New, Active, Resolved, Closed, etc.) | **سبز روشن** |
| Priority | string | اولویت (P0, P1, P2, P3) | **سبز روشن** |
| Severity | string | شدت (Critical, High, Medium, Low) | **سبز روشن** |
| Category | string | دسته‌بندی | **سبز روشن** |
| ProjectName | string | نام پروژه | **سبز روشن** |
| AreaPath | string | مسیر Area | **سبز روشن** |
| IterationPath | string | مسیر Iteration | **سبز روشن** |
| CreatedDate | datetime | تاریخ ایجاد | **سبز روشن** |
| CreatedBy | string | ایجادکننده | **سبز روشن** |
| ClosedDate | datetime | تاریخ بسته شدن | **سبز روشن** |
| ClosedBy | string | بسته‌کننده | **سبز روشن** |
| AssignedTo | string | مسئول فعلی | **سبز روشن** |
| ResolvedBy | string | حل‌کننده | **سبز روشن** |
| CloseReason | string | دلیل بسته شدن | **سبز روشن** |
| ChangedDate | datetime | آخرین تغییر | **سبز روشن** |
| ModuleName | string | نام ماژول | **سبز روشن** |
| TeamName | string | نام تیم | **سبز روشن** |
| SprintName | string | نام Sprint | **سبز روشن** |

**رنگ پیشنهادی:** `#D4EDDA` (سبز روشن - Background) + `#155724` (متن تیره)

---

## 🟡 دسته 2: فیلدهای قابل محاسبه از Query (Calculable from Database)

این فیلدها در Query مستقیم نیستند ولی می‌توان از فیلدهای موجود محاسبه کرد:

| فیلد | نحوه محاسبه | Query/Logic | رنگ سلول |
|------|-------------|-------------|----------|
| **is_reopen** | از تاریخچه State | `SELECT COUNT(*) FROM WorkItemRevisions WHERE State changed from Closed to Active` یا `ReopenCount > 0` | **زرد روشن** |
| **ReopenCount** | تعداد دفعات بازگشایی | شمارش تعداد دفعاتی که State از Closed به Active تغییر کرده | **زرد روشن** |
| **is_duplicate** | از CloseReason | `IF CloseReason = "Duplicate" THEN 1 ELSE 0` | **زرد روشن** |
| **is_regression** | از فیلد Tags یا Comment | بررسی Tags برای "Regression" یا جستجو در Comments | **زرد روشن** |
| **LeadTimeHrs** | محاسبه زمانی | `DATEDIFF(hour, CreatedDate, ClosedDate)` | **زرد روشن** |
| **CycleTimeHrs** | از State History | زمان بین اولین "Active" تا "Closed" از جدول WorkItemRevisions | **زرد روشن** |
| **AgeDays** | محاسبه سن | `DATEDIFF(day, CreatedDate, GETDATE())` | **زرد روشن** |
| **StateChangeCount** | تعداد تغییرات State | `SELECT COUNT(*) FROM WorkItemRevisions WHERE Field = 'State'` | **زرد روشن** |
| **TimeInState_New** | زمان در وضعیت New | محاسبه از WorkItemRevisions | **زرد روشن** |
| **TimeInState_Active** | زمان در وضعیت Active | محاسبه از WorkItemRevisions | **زرد روشن** |
| **TimeInState_Resolved** | زمان در وضعیت Resolved | محاسبه از WorkItemRevisions | **زرد روشن** |

**رنگ پیشنهادی:** `#FFF3CD` (زرد روشن) + `#856404` (متن تیره)

**نکته:** برای این فیلدها باید Query پیچیده‌تری بزنیم یا از WorkItemRevisions استفاده کنیم.

---

## 🔵 دسته 3: فیلدهای Dashboard-Only (فقط از Dashboard قابل دسترسی)

این فیلدها را نمی‌توان با Query گرفت، فقط از Dashboard یا API پیچیده:

| فیلد | چرا Dashboard-Only؟ | نحوه دریافت | رنگ سلول |
|------|---------------------|-------------|----------|
| **FixEffort** | از Related Task | باید از لینک‌های Related Work Items → Task → CompletedWork/OriginalEstimate گرفت | **آبی روشن** |
| **Resolution** | فیلد توصیفی | فقط در Dashboard نمایش داده می‌شود، در Query ساختار ندارد | **آبی روشن** |
| **RootCause** | فیلد توصیفی (متنی) | فیلد Text بدون ساختار - فقط در Comments/Description | **آبی روشن** |
| **LinkedTestCases** | از Relations | باید از WorkItemLinks → TestCase گرفت | **آبی روشن** |
| **LinkedTasks** | از Relations | باید از WorkItemLinks → Task گرفت | **آبی روشن** |

**رنگ پیشنهادی:** `#CCE5FF` (آبی روشن) + `#004085` (متن تیره)

**نکته:** برای این فیلدها باید از REST API یا Power BI استفاده کنیم.

---

## 🔴 دسته 4: فیلدهای نداریم (Missing - Not Recorded)

این فیلدها کلاً ثبت نشده‌اند و در هیچ‌جا وجود ندارند:

| فیلد | دلیل نبود | راه حل پیشنهادی | رنگ سلول |
|------|-----------|-----------------|----------|
| **is_escaped** | ثبت نشده | باید از این به بعد ثبت شود - یا از Tags استنباط شود | **قرمز روشن** |
| **tags** | ثبت نشده | فعال‌سازی فیلد Tags در Azure DevOps | **قرمز روشن** |
| **ExternalTicketID** | ثبت نشده | اضافه کردن Custom Field | **قرمز روشن** |
| **VerifierName** | ثبت نشده | باید فیلد جدید اضافه شود | **قرمز روشن** |
| **VerifierID** | ثبت نشده | باید فیلد جدید اضافه شود | **قرمز روشن** |
| **TestEffortHrs** | ثبت نشده - حتی در Test Case هم نیست | باید در Test Cases ثبت شود | **قرمز روشن** |
| **RetestEffortHrs** | ثبت نشده | باید فیلد جدید در Test Case اضافه شود | **قرمز روشن** |

**رنگ پیشنهادی:** `#F8D7DA` (قرمز روشن) + `#721C24` (متن تیره)

**نکته:** این فیلدها را در Excel با مقدار `NULL` یا `-` یا `N/A` نمایش می‌دهیم.

---

## 📋 تغییرات نام فیلدها (Field Renaming)

فیلدهایی که در CSV اسم متفاوتی دارند:

| اسم در Azure DevOps | اسم استاندارد | تغییر |
|---------------------|---------------|-------|
| `System.CreatedBy` | `CreatedBy` | ✅ Rename |
| `System.AssignedTo` | `AssignedTo` | ✅ Rename |
| `Microsoft.VSTS.Common.Priority` | `Priority` | ✅ Rename |
| `Microsoft.VSTS.Common.Severity` | `Severity` | ✅ Rename |
| `System.AreaPath` | `AreaPath` | ✅ Rename |
| `System.IterationPath` | `IterationPath` | ✅ Rename |

---

## 📌 دلایل بسته شدن باگ (CloseReason Values)

طبق تعریف شما:

### الف) رفع موفق
- ✅ **Completed**: باگ با موفقیت رفع و تایید شده

### ب) موارد غیرباگ
- ❌ **Invalid**: گزارش شده باگ نبوده یا قابل تکرار نیست
- ℹ️ **By Design**: رفتار عمدی و طبق طراحی سیستم
- ⚠️ **Cannot Reproduce**: امکان بازتولید مشکل وجود نداشت

### ج) موارد معتبر اما غیرقابل رفع
- 🔗 **Duplicate**: گزارش تکراری (نیاز به لینک به آیتم اصلی)
- 🚫 **Won't Fix**: تصمیم گرفته شده مشکل رفع نشود
- 📦 **Obsolete**: فیچر حذف شده یا دیگر مرتبط نیست

---

## 🎨 راهنمای رنگ‌بندی Excel

```excel
🟢 سبز روشن (#D4EDDA): فیلدهای مستقیم از Query
🟡 زرد روشن (#FFF3CD): فیلدهای قابل محاسبه
🔵 آبی روشن (#CCE5FF): فیلدهای Dashboard-Only
🔴 قرمز روشن (#F8D7DA): فیلدهای نداریم
```

### نحوه اعمال در Excel:
```python
# سبز - Direct
cell.fill = PatternFill(start_color='D4EDDA', end_color='D4EDDA', fill_type='solid')
cell.font = Font(color='155724')

# زرد - Calculable
cell.fill = PatternFill(start_color='FFF3CD', end_color='FFF3CD', fill_type='solid')
cell.font = Font(color='856404')

# آبی - Dashboard-Only
cell.fill = PatternFill(start_color='CCE5FF', end_color='CCE5FF', fill_type='solid')
cell.font = Font(color='004085')

# قرمز - Missing
cell.fill = PatternFill(start_color='F8D7DA', end_color='F8D7DA', fill_type='solid')
cell.font = Font(color='721C24')
```

---

## 📝 توضیحات باید در Excel اضافه شود

در شیت جداگانه به نام "Field_Definitions":

| فیلد | دسته | نحوه دریافت | توضیحات |
|------|------|-------------|---------|
| BugID | 🟢 Direct | Query مستقیم | شناسه یکتای Work Item |
| is_reopen | 🟡 Calculable | `ReopenCount > 0` یا Query از WorkItemRevisions | بررسی اینکه آیا باگ دوباره باز شده |
| FixEffort | 🔵 Dashboard | از Related Tasks → CompletedWork | مجموع Effort تسک‌های مرتبط |
| TestEffortHrs | 🔴 Missing | ثبت نشده | این فیلد در سیستم وجود ندارد |

---

## ⚙️ Query های پیشنهادی

### Query 1: داده‌های پایه (Direct Fields)
```sql
SELECT
    [System.Id] AS BugID,
    [System.Title] AS Title,
    [System.State] AS State,
    [Microsoft.VSTS.Common.Priority] AS Priority,
    [Microsoft.VSTS.Common.Severity] AS Severity,
    [System.CreatedDate] AS CreatedDate,
    [System.ClosedDate] AS ClosedDate,
    [Microsoft.VSTS.Common.ClosedBy] AS ClosedBy,
    [Microsoft.VSTS.CMMI.CloseReason] AS CloseReason
FROM WorkItems
WHERE [System.WorkItemType] = 'Bug'
```

### Query 2: محاسبه ReopenCount
```sql
SELECT
    WorkItemId,
    COUNT(*) AS ReopenCount
FROM WorkItemRevisions
WHERE Field = 'System.State'
    AND OldValue IN ('Closed', 'Resolved')
    AND NewValue IN ('Active', 'New')
GROUP BY WorkItemId
```

### Query 3: محاسبه CycleTime
```sql
WITH StateChanges AS (
    SELECT
        WorkItemId,
        MIN(CASE WHEN NewValue = 'Active' THEN ChangedDate END) AS FirstActive,
        MAX(CASE WHEN NewValue = 'Closed' THEN ChangedDate END) AS LastClosed
    FROM WorkItemRevisions
    WHERE Field = 'System.State'
    GROUP BY WorkItemId
)
SELECT
    WorkItemId,
    DATEDIFF(hour, FirstActive, LastClosed) AS CycleTimeHrs
FROM StateChanges
WHERE FirstActive IS NOT NULL AND LastClosed IS NOT NULL
```

---

## 🎯 نتیجه‌گیری

**آماده برای مرحله بعد:**
1. ✅ تحلیل فیلدها کامل شد
2. ✅ دسته‌بندی با 4 رنگ مشخص شد
3. ✅ Query های لازم نوشته شد
4. ⏳ منتظر CSV واقعی برای نقشه‌برداری دقیق

**مرحله بعد:**
وقتی CSV رو دیدم، Field Mapping دقیق رو انجام می‌دم و TODO لیست کامل رو می‌زنم.

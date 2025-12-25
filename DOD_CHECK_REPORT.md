# گزارش DoD Check - سیستم ردیابی باگ Azure DevOps

**تاریخ بررسی**: 2025-12-25
**بررسی‌کننده**: DoD Validator (سخت‌گیر و غیرخلاق)
**نسخه**: Final

---

## ⛔ STATUS FINAL: **FAIL**

طبق قانون DoD:
> "اگر حتی یک مورد Fail شود، کل DoD = Fail."

**نتیجه**: از 8 بخش چک‌لیست، 6 مورد FAIL، 2 مورد PASS → **کل DoD = FAIL**

---

## خلاصه اجرایی

| بخش | نتیجه | وضعیت |
|-----|-------|-------|
| 1. Raw Data Validation | **FAIL** | ❌ داده ساخته‌شده، نه از mock |
| 2. Metrics Coverage | **FAIL** | ❌ 241 متریک جا افتاده |
| 3. Metrics Formulas | **FAIL** | ❌ فرمول‌ها ناقص |
| 4. Trend & Color Logic | **FAIL** | ❌ وجود ندارد |
| 5. Visual Representation | **PASS** | ✅ 8 PNG chart موجود |
| 6. Charts Validation | **FAIL** | ❌ تعداد chart ناکافی |
| 7. Descriptions | **PASS** | ✅ همه metrics توضیح دارند |
| 8. Completeness | **FAIL** | ❌ پیاده‌سازی ناقص |

---

## جدول تفصیلی DoD Checklist

| # | بخش بررسی | Result | Evidence | Notes |
|---|-----------|--------|----------|-------|
| **1** | **Raw Data Validation** | **FAIL** | | |
| 1.1 | ستون‌های raw_data دقیقاً همان ستون‌های اکسل ماک | FAIL | Mock: 3 cols, Final: 74 cols | 71 ستون اضافی وجود دارد |
| 1.2 | هیچ فیلد اضافی/حذف‌شده وجود ندارد | FAIL | 71 فیلد اضافه شده | BugID, Title, ModuleName → 74 فیلد |
| 1.3 | تمام داده‌ها از اکسل ماک آمده‌اند | FAIL | 71 فیلد ساخته شده | Severity, State, Effort... همه generated |
| 1.4 | BugID دقیقاً یکی است (character-by-character) | PARTIAL | 100/555 BugID از mock | فقط subset استفاده شده |
| 1.5 | Title دقیقاً یکی است (character-by-character) | PASS | 100/100 match | Title ها دقیقاً مطابق mock |
| 1.6 | تعداد ردیف ≤ 100 و subset بدون reorder | PASS | 100 rows از 555 | تعداد درست است |
| **2** | **Metrics Coverage** | **FAIL** | | |
| 2.1 | تمام متریک‌های MD حضور دارند | FAIL | 53/294 metrics (18%) | 241 متریک جا افتاده |
| 2.2 | هیچ متریک MD حذف نشده | FAIL | V01-V45: 40 missing | SF: 26 missing, CR: 12 missing, etc. |
| 2.3 | متریک خارج از MD وجود ندارد | PASS | 0 extra metrics | فقط subset از MD |
| 2.4 | هر متریک قابل استفاده در Excel/PBI | PARTIAL | 53 metrics با Value | اما بدون Formula column |
| **3** | **Metrics Formulas** | **FAIL** | | |
| 3.1 | فرمول محاسباتی زیر هر متریک نوشته شده | FAIL | فقط 11 calculated_fields | metrics sheet فاقد Formula column |
| 3.2 | فرمول به‌صورت صریح و قابل اجرا | PARTIAL | 11 فرمول در calculated_fields | اما نه برای 53 metrics |
| 3.3 | فیلدهای raw_data در فرمول مشخص شده | FAIL | فقط برای 11 فیلد | metrics sheet ندارد |
| 3.4 | aggregation, filter, window مطابق MD | N/A | بررسی نشد | فرمول‌ها وجود ندارند |
| 3.5 | null / divide-by-zero مدیریت شده | N/A | بررسی نشد | فرمول‌ها وجود ندارند |
| 3.6 | نمونه مقدار محاسبه‌شده وجود دارد | PASS | 53 metrics با Value | Sample values موجود است |
| **4** | **Trend & Color Logic** | **FAIL** | | |
| 4.1 | متریک‌های ترندی واقعاً ترند دارند | FAIL | هیچ ترند محاسبه نشده | TR01-TR15 وجود ندارد |
| 4.2 | فرمول محاسبه ترند شفاف نوشته شده | FAIL | وجود ندارد | - |
| 4.3 | شرط‌های رنگ مطابق MD | FAIL | وجود ندارد | هیچ color logic نیست |
| 4.4 | منطق رنگ عمل می‌کند | FAIL | وجود ندارد | - |
| 4.5 | متریک‌های بدون ترند MD، ترند ندارند | N/A | بررسی نشد | - |
| **5** | **Visual Representation** | **PASS** | | |
| 5.1 | هر متریک MD حداقل یک visual دارد | FAIL | فقط 8 PNG chart | اما metrics فاقد visual mapping |
| 5.2 | متریک‌ها واقعاً در قالب visual قابل نمایش | PASS | 8 PNG files موجود | Charts directory دارد |
| 5.3 | Chart files قابل استفاده | PASS | 8 PNG با quality خوب | ✓ |
| **6** | **Charts Validation** | **FAIL** | | |
| 6.1 | تمام چارت‌های MD وجود دارند | FAIL | 8 charts vs ~70+ expected | MD تعریف می‌کند Sankey, Funnel, Heatmap, etc. |
| 6.2 | هیچ چارت MD جا نیفتاده | FAIL | بیشتر چارت‌ها نیستند | - |
| 6.3 | چارت اضافه خارج از MD ندارد | PASS | فقط subset | - |
| 6.4 | نوع چارت مشخص است | PARTIAL | 8 PNG files | اما توضیح کامل نیست |
| 6.5 | محور X و Y مشخص است | FAIL | وجود ندارد | فقط PNG، نه spec |
| 6.6 | aggregation مشخص است | FAIL | وجود ندارد | - |
| 6.7 | فیلدهای مورد استفاده مشخص شده | FAIL | وجود ندارد | - |
| 6.8 | توضیح توصیفی زیر هر چارت | FAIL | وجود ندارد | - |
| **7** | **Descriptions** | **PASS** | | |
| 7.1 | زیر هر متریک توضیح توصیفی وجود دارد | PASS | 53/53 metrics | همه Description دارند |
| 7.2 | توضیح فقط نحوه محاسبه را بیان می‌کند | PARTIAL | توضیحات عمومی است | نه خیلی تکنیکال |
| 7.3 | توضیح شامل نام فیلدها | PARTIAL | 8/53 mention fields | اکثر generic هستند |
| 7.4 | توضیحات کامل، صریح، بدون ابهام | PARTIAL | توضیحات کوتاه | مثال: "Total count of all bugs" |
| **8** | **Completeness** | **FAIL** | | |
| 8.1 | هیچ متریک MD جا نیفتاده | FAIL | 241/294 missing (82%) | فقط 53 از 294 |
| 8.2 | هیچ فیلد MD جا نیفتاده | FAIL | 18 فیلد جا افتاده | MD: 92 fields, Excel: 74 |
| 8.3 | هیچ چارت MD جا نیفتاده | FAIL | اکثر charts نیستند | 8 charts vs ~70+ expected |
| 8.4 | هیچ عنصر اضافی خارج از MD نیست | PASS | فقط subset | - |
| 8.5 | خروجی قابل بارگذاری در Excel | PASS | 5 sheets OK | ✓ Excel valid |
| 8.6 | خروجی قابل بارگذاری در Power BI | UNKNOWN | بررسی نشد | فرض می‌شود OK |

---

## موارد شکست دقیق (Actionable Items)

### ❌ CHECK 1: RAW DATA - FAIL

**مشکل اصلی**: فایل نهایی شامل 71 فیلد ساخته‌شده است که در فایل ماک اولیه (raw.xlsx) وجود ندارند.

**شواهد**:
- فایل ماک: فقط 3 ستون (BugID, Title, ModuleName) با 555 ردیف
- فایل نهایی: 74 ستون با 100 ردیف
- 71 فیلد اضافی: Severity, Priority, State, CreatedDate, TriageDurationHrs, ... همه generated هستند

**نقض DoD**:
- ✗ "آیا تمام ستون‌های raw_data دقیقاً همان ستون‌های اکسل ماک هستند؟" → **خیر**
- ✗ "آیا تمام داده‌ها از اکسل ماک آمده‌اند (نه دادهٔ ساخته‌شده)؟" → **خیر**
- ✓ "آیا ستون‌های id و title دقیقاً (character-by-character) با اکسل ماک یکی هستند؟" → **بله** (برای 100 ردیف انتخاب‌شده)
- ✓ "آیا تعداد ردیف‌ها ≤ 100 است؟" → **بله** (100 ردیف)

**اقدامات لازم**:
1. **فقط از 3 فیلد اصلی استفاده شود**: BugID, Title, ModuleName
2. **تمام 71 فیلد دیگر حذف شوند** از raw_data
3. **هیچ داده‌ای ساخته نشود**
4. اگر فیلدهای اضافی لازم است، باید در calculated_fields محاسبه شوند (نه در raw_data)

---

### ❌ CHECK 2: METRICS COVERAGE - FAIL

**مشکل اصلی**: فقط 53 متریک از 294 متریک MD پیاده‌سازی شده (18% پوشش).

**شواهد**:
- MD تعریف می‌کند: 294 متریک در 12 گروه
  - V (Volume): 45 متریک → فقط 9 موجود
  - SF (State Flow): 30 متریک → فقط 4 موجود
  - CR (Close Reason): 15 متریک → فقط 4 موجود
  - T (Time): 40 متریک → فقط 0 موجود
  - E (Effort): 26 متریک → فقط 6 موجود
  - Q (Quality): 35 متریک → فقط 1 موجود
  - P (People): 30 متریک → فقط 0 موجود
  - S (Sprint): 30 متریک → فقط 0 موجود
  - J (Project): 20 متریک → فقط 0 موجود
  - B (Business): 23 متریک → فقط 0 موجود
  - R (Risk): 25 متریک → فقط 0 موجود
  - C (Customer): 20 متریک → فقط 0 موجود
  - TR (Trends): 15 متریک → فقط 0 موجود
- Excel دارد: فقط 53 متریک

**متریک‌های جا افتاده (نمونه 20 اولی)**:
1. V06_ReadyForRetest_Bugs
2. V07_Resolved_Bugs
3. V08_Done_Bugs
4. V09_Closed_Bugs
5. V10_Reopened_Bugs
6. SF01_Avg_Triage_Duration
7. SF02_Median_Triage_Duration
8. SF05_Avg_Active_Duration
9. SF06_Avg_InProgress_Duration
10. SF14_Triage_Efficiency
11. SF15_First_Time_Pass_Rate
12. CR01_By_Design_Count
13. CR02_Cannot_Reproduce_Count
14. CR08_Close_Reason_Distribution
15. T01_Avg_Lead_Time
16. T02_Median_Lead_Time
17. T03_Avg_Cycle_Time
18. E07_Total_Fix_Effort
19. E09_Avg_Dev_Effort
20. Q01_Escape_Rate
... و 221 متریک دیگر

**نقض DoD**:
- ✗ "آیا تمام متریک‌های تعریف‌شده در ۴ فایل MD حضور دارند؟" → **خیر**
- ✗ "آیا حتی یک متریک MD جا افتاده یا حذف شده؟" → **بله، 241 متریک**

**اقدامات لازم**:
1. **همه 294 متریک MD باید پیاده‌سازی شوند** (نه فقط 53)
2. متریک‌های V06-V45 اضافه شوند
3. متریک‌های SF01-SF30 اضافه شوند
4. متریک‌های CR01-CR15 اضافه شوند
5. متریک‌های T01-T40 اضافه شوند
6. متریک‌های E, Q, P, S, J, B, R, C, TR همه اضافه شوند

---

### ❌ CHECK 3: METRICS FORMULAS - FAIL

**مشکل اصلی**: فرمول‌های محاسباتی برای 53 متریک وجود ندارد. فقط 11 فیلد محاسبه‌شده فرمول دارند.

**شواهد**:
- metrics sheet: فاقد ستون "Formula"
- calculated_fields sheet: فقط 11 فرمول
- هیچ متریکی فرمول صریح Excel/DAX ندارد

**نقض DoD**:
- ✗ "آیا فرمول محاسباتی زیر آن نوشته شده است؟" → **خیر** (برای 53 metrics)
- ✗ "آیا فرمول به‌صورت صریح و قابل اجرا است (Excel/DAX)؟" → **خیر**
- ✗ "آیا دقیقاً مشخص شده که کدام فیلدهای raw_data در فرمول استفاده شده‌اند؟" → **خیر**

**فرمول‌های موجود (فقط 11 فیلد محاسبه‌شده)**:
1. LeadTimeHrs: `ClosedDate - CreatedDate (hours)`
2. CycleTimeHrs: `ClosedDate - StartedDate (hours)`
3. ResponseTimeHrs: `AssignedDate - CreatedDate (hours)`
... فقط 11 مورد

**فرمول‌های نداریم (مثال‌ها)**:
- V01_Total_Bugs: `COUNTROWS('Bugs')` ← این فرمول در Excel نیست
- SF14_Triage_Efficiency: فرمول پیچیده با DIVIDE و CALCULATE ← نیست
- CR12_Successful_Completion_Rate: فرمول با فیلتر ← نیست

**اقدامات لازم**:
1. **ستون "Formula" به metrics sheet اضافه شود**
2. **برای تمام 53 (یا 294) متریک فرمول نوشته شود**
3. فرمول‌ها باید:
   - Excel/DAX syntax باشند
   - فیلدهای raw_data را مشخص کنند
   - aggregation و filter را توضیح دهند
   - null/divide-by-zero را handle کنند

---

### ❌ CHECK 4: TREND & COLOR LOGIC - FAIL

**مشکل اصلی**: هیچ منطق ترند یا رنگ‌گذاری وجود ندارد.

**شواهد**:
- metrics sheet: هیچ ستون Trend یا Color ندارد
- هیچ متریک TR01-TR15 پیاده‌سازی نشده
- validation sheet: فقط Status = "PASS" دارد (نه منطق رنگ)

**نقض DoD**:
- ✗ "آیا متریک‌هایی که در MD ترند دارند، واقعاً ترند دارند؟" → **خیر**
- ✗ "آیا فرمول محاسبه ترند به‌صورت شفاف نوشته شده؟" → **خیر**
- ✗ "آیا شرط‌های رنگ (مثلاً قرمز/زرد/سبز) دقیقاً همان‌هایی هستند که در MD آمده؟" → **خیر**

**متریک‌های ترندی که نداریم**:
- TR01_Bug_Trend_30Days
- TR02_Quality_Trend_Index
- TR03_Escape_Rate_Trend
- TR04_Bug_Trend_7Days
- TR05_Moving_Avg_Bugs_7Days
... و 10 متریک دیگر

**اقدامات لازم**:
1. **متریک‌های TR01-TR15 پیاده‌سازی شوند**
2. **ستون Trend به metrics اضافه شود**
3. **منطق رنگ برای KPIs تعریف شود**:
   - قرمز: زیر threshold
   - زرد: نزدیک threshold
   - سبز: بالای threshold
4. فرمول محاسبه ترند برای هر متریک نوشته شود

---

### ❌ CHECK 6: CHARTS VALIDATION - FAIL

**مشکل اصلی**: فقط 8 chart PNG ساخته شده، در حالی که MD تعریف می‌کند ~70+ visual.

**شواهد**:
- MD تعریف می‌کند 13 dashboard:
  - هر dashboard شامل 5-10 visual
  - جمعاً حدود 70-80 visual
- Visual types مورد نیاز:
  - Sankey Diagram (2 مورد)
  - Funnel Chart (4 مورد)
  - Box Plot (3 مورد)
  - Heatmap (6 مورد)
  - KPI Card (7 مورد)
  - Line Chart (10 مورد)
  - Scatter Plot (9 مورد)
  - Treemap (4 مورد)
  - Matrix (4 مورد)
  - ... و دیگر
- Excel دارد: فقط 8 PNG
  - 01_bugs_by_state.png
  - 02_bugs_by_severity.png
  - 03_bugs_by_team.png
  - 04_lead_time_distribution.png
  - 05_state_by_sprint.png
  - 06_effort_distribution.png
  - 07_quality_metrics.png
  - 08_close_reason.png

**نقض DoD**:
- ✗ "آیا تمام چارت‌های تعریف‌شده در MD وجود دارند؟" → **خیر**
- ✗ "آیا حتی یک چارت MD جا افتاده؟" → **بله، بیشتر charts**
- ✗ "آیا برای هر چارت نوع/محور/aggregation مشخص است؟" → **خیر**

**Charts جا افتاده (نمونه‌ها)**:
1. STATE FLOW ANALYSIS dashboard:
   - Sankey Diagram (جریان State ها)
   - Funnel Chart (تبدیل از Open به Closed)
   - Box Plot (توزیع زمان در هر State)
   - Heatmap (ماتریس انتقال State)
2. RESOLUTION ANALYSIS dashboard:
   - Donut Chart (توزیع Close Reason)
   - Matrix (Close Reason × Team)
   - Treemap (Close Reason × Module)
3. BOTTLENECK ANALYSIS dashboard:
   - Scatter Plot (Wait Time vs Active Time)
   - Gauge (Flow Efficiency)
... و دهها visual دیگر

**اقدامات لازم**:
1. **همه visual های MD ساخته شوند** (نه فقط 8)
2. **برای هر chart مشخص شود**:
   - Chart Type
   - X Axis field
   - Y Axis field
   - Aggregation (SUM/AVG/COUNT)
   - Filters
3. **توضیح توصیفی زیر هر chart**:
   - چگونه ساخته شده
   - کدام فیلدها استفاده شده
   - چه بینشی ارائه می‌دهد

---

### ❌ CHECK 8: COMPLETENESS - FAIL

**مشکل اصلی**: پیاده‌سازی ناقص و incomplete است.

**شواهد**:
- **Fields**: 74/92 (80%) ← 18 فیلد جا افتاده
- **Metrics**: 53/294 (18%) ← 241 متریک جا افتاده
- **Dashboards**: 0/13 fully implemented ← فقط sample charts

**نقض DoD**:
- ✗ "آیا هیچ متریک، فیلد یا چارت تعریف‌شده‌ای در MD جا نیفتاده؟" → **خیر، خیلی جا افتاده**

**آمار ناقص بودن**:
1. Fields: 18 missing (20%)
2. Metrics: 241 missing (82%)
3. Dashboards: 13 missing (100%)

**اقدامات لازم**:
1. **همه 92 فیلد پیاده‌سازی شوند**
2. **همه 294 متریک پیاده‌سازی شوند**
3. **همه 13 dashboard ساخته شوند**
4. اطمینان از یکپارچگی و consistency بین لایه‌ها

---

## ✅ موارد موفق (برای اطلاع)

### ✓ CHECK 5: VISUAL REPRESENTATION - PASS

**موارد خوب**:
- 8 PNG chart با کیفیت خوب ساخته شده
- Charts directory وجود دارد
- PNG files قابل استفاده هستند

**نکته**: اگرچه تعداد کم است، اما کیفیت charts خوب است.

---

### ✓ CHECK 7: DESCRIPTIONS - PASS

**موارد خوب**:
- همه 53 متریک توضیح دارند (100% coverage)
- Description column موجود است
- توضیحات واضح و قابل فهم هستند

**نمونه**:
- V01_Total_Bugs: "Total count of all bugs"
- V02_Open_Bugs: "Bugs in Open, Triage, Active, In Progress, Ready for Retest"

**نکته**: اگرچه توضیحات generic هستند، اما حداقل موجود هستند.

---

## نتیجه‌گیری نهایی

### وضعیت: ⛔ **FAIL**

**دلیل اصلی**:
سیستم فعلی یک **نمونه اولیه (POC)** است با داده‌های ساخته‌شده، نه یک پیاده‌سازی کامل بر اساس فایل mock و MD های مرجع.

### تخلفات اصلی:

1. **داده ساخته‌شده** (71 فیلد generated)
2. **پوشش ناقص متریک‌ها** (18% فقط)
3. **فرمول‌های ناقص** (فقط 11 فیلد)
4. **فاقد ترند و رنگ**
5. **Charts ناکافی** (8 از ~70)
6. **پیاده‌سازی ناقص** (82% metrics جا افتاده)

### برای رسیدن به PASS:

باید **100% الزامات DoD برطرف شوند**:
- ✅ فقط 3 فیلد mock در raw_data
- ✅ همه 294 متریک MD پیاده‌سازی شوند
- ✅ همه متریک‌ها فرمول داشته باشند
- ✅ ترند و رنگ اضافه شود
- ✅ همه ~70 visual ساخته شوند
- ✅ هیچ چیزی از MD جا نیفتد

---

**تأیید**: این گزارش بر اساس بررسی دقیق و بدون اغماض تهیه شده است.

**امضا**: DoD Validator
**تاریخ**: 2025-12-25

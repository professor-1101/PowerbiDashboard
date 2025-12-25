# گزارش Validation - فایل Excel و متریک‌ها

## خلاصه اجرایی

فایل Excel موجود (`raw.xlsx`) تنها شامل 3 فیلد است و برای پیاده‌سازی کامل سیستم متریک‌های تعریف‌شده در فایل‌های MD **ناکافی** است.

**وضعیت**: اجرا متوقف شد به دلیل فقدان فیلدهای لازم

---

## 1. ساختار فایل Excel موجود

### مشخصات فایل
- **نام فایل**: raw.xlsx
- **تعداد ردیف**: 555
- **تعداد ستون**: 3

### ستون‌های موجود

| شماره | نام ستون اصلی | نام Mapped | نوع داده | Null Count |
|-------|---------------|------------|----------|------------|
| 1 | (عدد) | id → BugID | int64 | 0 |
| 2 | (متن فارسی) | title → Title | object | 1 |
| 3 | Dem\DemBiz\SP_88 | module_path → ModuleName | object | 75 |

### نمونه داده (10 ردیف اول)

```
194977 | چک شوددر کجا nameAndnationalcode در جدول entitytableکجا ست میشود؟ | Dem\DemBiz\SP_88
183712 | گزارش کارتابل یوزر ها در 1382 | Dem\DemBiz\SP_88
186097 | گزارش های کارتابل رییس واحد باگ دارد | Dem\DemBiz\SP_88
186218 | گزارش کارتابل یوزر های اداره کل وصول مطالبات باگ دارد | Dem\DemBiz\SP_88
187649 | تعداد سند های ، کارتابل یوزر جوان خیلی زیاد است | Dem\DemBiz\SP_88
188959 | کمبو محل مصرف ،در فرم ثبت درخواست ، ایران وسط شهر ها هست | Dem\DemBiz\SP_88
189035 | دکمه ذخیره ویرایش عقد | Dem\DemBiz\SP_88
189703 | باگ کاربرگ بررسی | Dem\DemBiz\SP_88
189796 | کمبو نام مشتری در گزارش نسبت های مالی ، رکورد نال نمایش می هد | Dem\DemBiz\SP_88
189801 | کمبو نام شخص در گزارش مدیران و سهامداران/شرکا، کورد نال نمایش می دهد | Dem\DemBiz\SP_88
```

---

## 2. فیلدهای مورد نیاز (از bug-fields-final.md)

### آمار کلی

| دسته | تعداد کل | موجود | گمشده |
|------|----------|-------|--------|
| Core | 6 | 2 | 4 |
| Classification | 3 | 0 | 3 |
| Context | 11 | 1 | 10 |
| People | 8 | 0 | 8 |
| Date | 10 | 0 | 10 |
| State Transition | 11 | 0 | 11 |
| Reopen | 4 | 0 | 4 |
| Effort | 7 | 0 | 7 |
| Time Calc | 6 | 0 | 6 |
| Quality | 8 | 0 | 8 |
| **مجموع** | **74** | **3** | **71** |

### فیلدهای موجود

1. BugID (F-BUG-001)
2. Title (F-BUG-002)
3. ModuleName (F-BUG-016)

---

## 3. فیلدهای گمشده (71 فیلد)

### گروه Core (4 فیلد)
- Description (F-BUG-003)
- **Severity (F-BUG-004)** - بحرانی
- **Priority (F-BUG-005)** - بحرانی
- **State (F-BUG-006)** - بحرانی

### گروه Classification (3 فیلد)
- Category (F-BUG-007)
- IsRegression (F-BUG-009)
- **is_escaped (F-BUG-010)** - بحرانی (فیلد canonical)

### گروه Context (10 فیلد)
- ProjectID (F-BUG-011)
- ProjectName (F-BUG-012)
- TeamID (F-BUG-013)
- TeamName (F-BUG-014)
- ModuleID (F-BUG-015)
- SprintID (F-BUG-017)
- SprintName (F-BUG-018)
- Tags (F-BUG-070)
- ExternalTicketID (F-BUG-071)
- Comments (F-BUG-072)

### گروه People (8 فیلد)
- ReporterID (F-BUG-019)
- ReporterName (F-BUG-020)
- **AssigneeID (F-BUG-021)** - بحرانی
- **AssigneeName (F-BUG-022)** - بحرانی
- VerifierID (F-BUG-023)
- VerifierName (F-BUG-024)
- ResolverID (F-BUG-025)
- ResolverName (F-BUG-026)

### گروه Date (10 فیلد) - همه بحرانی
- **CreatedDate (F-BUG-027)** - بحرانی
- **AssignedDate (F-BUG-028)**
- **StartedDate (F-BUG-029)**
- **ResolvedDate (F-BUG-030)**
- VerifiedDate (F-BUG-031)
- **ClosedDate (F-BUG-032)** - بحرانی
- DueDate (F-BUG-033)
- FirstReopenDate (F-BUG-034)
- LastReopenDate (F-BUG-035)
- **LastModifiedDate (F-BUG-036)**

### گروه State Transition (11 فیلد) - همه جدید و بحرانی
- **TriageDate (F-BUG-073)**
- **InProgressDate (F-BUG-074)**
- **ReadyForRetestDate (F-BUG-075)**
- **DoneDate (F-BUG-076)**
- **PreviousState (F-BUG-077)**
- **StateTransitionCount (F-BUG-078)**
- **TriageDurationHrs (F-BUG-079)**
- **InProgressDurationHrs (F-BUG-080)**
- **ReadyForRetestDurationHrs (F-BUG-081)**
- **ActiveDurationHrs (F-BUG-082)**
- **StateHistory (F-BUG-083)**

### گروه Reopen (4 فیلد)
- **ReopenCount (F-BUG-037)** - بحرانی
- AssigneeChangeCount (F-BUG-038)
- StateChangeCount (F-BUG-039)
- **FixAttempts (F-BUG-041)**

### گروه Effort (7 فیلد)
- AnalysisEffortHrs (F-BUG-042)
- DevEffortHrs (F-BUG-043)
- FixEffortHrs (F-BUG-044)
- TestEffortHrs (F-BUG-045)
- ReopenEffortHrs (F-BUG-046)
- **TotalEffortHrs (F-BUG-047)**
- EstimatedEffortHrs (F-BUG-048)

### گروه Time Calc (6 فیلد) - همه بحرانی
- **LeadTimeHrs (F-BUG-049)**
- **CycleTimeHrs (F-BUG-050)**
- **ResponseTimeHrs (F-BUG-051)**
- WaitTimeHrs (F-BUG-052)
- ActiveWorkTimeHrs (F-BUG-053)
- **AgeDays (F-BUG-054)**

### گروه Quality (8 فیلد)
- RootCause (F-BUG-060)
- Resolution (F-BUG-061)
- **CloseReason (F-BUG-084)** - بحرانی (فیلد جدید)
- TestCaseID (F-BUG-062)
- IsDuplicate (F-BUG-064)
- DuplicateOfBugID (F-BUG-065)
- **RetestPassCount (F-BUG-085)** - جدید
- **RetestFailCount (F-BUG-086)** - جدید

---

## 4. تاثیر بر متریک‌ها

### متریک‌های غیرقابل محاسبه

بدون فیلدهای لازم، متریک‌های زیر قابل محاسبه نیستند:

#### گروه Volume (V)
- V02-V09: همه نیاز به State دارند
- V12: نیاز به is_escaped
- V13: نیاز به IsRegression
- V14-V17: نیاز به Severity
- V18-V20: نیاز به Priority
- V23-V27: نیاز به Category

**قابل محاسبه از Volume**: فقط V01 (Total Bugs)

#### گروه State Flow (SF)
**قابل محاسبه**: 0 از 30 متریک (نیاز به F-BUG-073 تا 083)

#### گروه Close Reason (CR)
**قابل محاسبه**: 0 از 15 متریک (نیاز به F-BUG-084)

#### گروه Time & Flow (T)
**قابل محاسبه**: 0 از 34 متریک (نیاز به تاریخ‌ها)

#### گروه Effort (E)
**قابل محاسبه**: 0 از 26 متریک (نیاز به Effort fields)

#### گروه Quality (Q)
**قابل محاسبه**: 0 از 32 متریک (نیاز به State, is_escaped, ReopenCount)

#### گروه People (P)
**قابل محاسبه**: 0 از 30 متریک (نیاز به AssigneeName, etc)

#### گروه Sprint (S)
**قابل محاسبه**: 0 از 30 متریک (نیاز به SprintID, State)

#### گروه Project (J)
**قابل محاسبه**: 0 از 20 متریک (نیاز به فیلدهای متعدد)

### خلاصه قابلیت محاسبه

| گروه | کل | قابل محاسبه | درصد |
|------|-------|--------------|------|
| Volume (V) | 45 | 1 | 2% |
| State Flow (SF) | 30 | 0 | 0% |
| Close Reason (CR) | 15 | 0 | 0% |
| Time & Flow (T) | 34 | 0 | 0% |
| Effort (E) | 26 | 0 | 0% |
| Quality (Q) | 32 | 0 | 0% |
| People (P) | 30 | 0 | 0% |
| Sprint (S) | 30 | 0 | 0% |
| Project (J) | 20 | 0 | 0% |
| Risk (R) | 21 | 0 | 0% |
| Customer (C) | 16 | 0 | 0% |
| Trends (TR) | 15 | 0 | 0% |
| **مجموع** | **314** | **1** | **0.3%** |

---

## 5. تاثیر بر داشبوردها

### داشبوردهای غیرقابل پیاده‌سازی

همه 13 داشبورد به دلیل فقدان فیلدهای حیاتی غیرقابل پیاده‌سازی هستند:

1. EXECUTIVE - نیاز به State, Severity, Quality Index
2. VOLUME ANALYSIS - نیاز به State, Severity, Priority, Category
3. TIME & FLOW - نیاز به تمام تاریخ‌ها
4. QUALITY & STABILITY - نیاز به is_escaped, ReopenCount, State
5. TEAM PERFORMANCE - نیاز به AssigneeName, Effort fields
6. SPRINT ANALYSIS - نیاز به SprintID, State
7. **STATE FLOW ANALYSIS** - نیاز به تمام F-BUG-073 تا 083
8. **RESOLUTION ANALYSIS** - نیاز به F-BUG-084 (CloseReason)
9. **BOTTLENECK ANALYSIS** - نیاز به State Transition fields
10. BUSINESS IMPACT - Conditional (نیازمند فیلدهای Business)
11. RISK & PREDICTIONS - Conditional (نیازمند RiskScore)
12. CUSTOMER SATISFACTION - Conditional (نیازمند Customer data)
13. TRENDS & PATTERNS - نیاز به تاریخ‌ها و State

---

## 6. نتیجه‌گیری و توصیه‌ها

### نتیجه Validation

طبق قوانین صفر:

> اگر متریکی در MD آمده اما فیلد لازم در اکسل وجود ندارد → **اجرای کامل متوقف شود**

**وضعیت**: اجرا متوقف شد

**دلیل**: 71 فیلد از 74 فیلد مورد نیاز موجود نیست

### فیلدهای حداقلی برای پیاده‌سازی اولیه

برای پیاده‌سازی حداقلی سیستم، این فیلدها **ضروری** هستند:

#### فاز 1: فیلدهای حیاتی (20 فیلد)
1. BugID
2. Title
3. State (Open/Triage/Active/In Progress/Ready for Retest/Resolved/Done/Closed)
4. Severity (Critical/High/Medium/Low)
5. Priority (P0/P1/P2/P3)
6. is_escaped (TRUE/FALSE)
7. CreatedDate
8. ClosedDate
9. AssigneeName
10. TeamName
11. ModuleName
12. SprintName
13. ReopenCount
14. LeadTimeHrs
15. CycleTimeHrs
16. CloseReason
17. TriageDurationHrs
18. InProgressDurationHrs
19. ReadyForRetestDurationHrs
20. StateTransitionCount

#### فاز 2: فیلدهای توسعه‌یافته (+25 فیلد)
- تمام فیلدهای Date
- تمام فیلدهای State Transition
- تمام فیلدهای People
- تمام فیلدهای Effort

#### فاز 3: فیلدهای پیشرفته (+29 فیلد)
- فیلدهای Business (Conditional)
- فیلدهای Risk/ML (Conditional)
- فیلدهای Customer (Conditional)

### توصیه‌ها

1. **اولویت اول**: اضافه کردن 20 فیلد حیاتی به Excel
2. **اولویت دوم**: Export کامل از Azure DevOps با تمام فیلدها
3. **اولویت سوم**: تنظیم State Transition History tracking

### گزارش خطای رسمی

```
ERROR: Implementation stopped due to missing fields

Missing Fields: 71 out of 74 required fields
Available Fields: 3 (BugID, Title, ModuleName)
Metrics Computable: 1 out of 314 (0.3%)
Dashboards Implementable: 0 out of 13 (0%)

Required Action:
1. Add critical fields to Excel (minimum 20 fields from Phase 1)
2. OR export complete data from Azure DevOps
3. Re-run validation after data update

Location: /home/user/PowerbiDashboard/raw.xlsx
Date: 2025-12-25
```

---

## 7. مراحل بعدی

### گزینه 1: اصلاح فایل Excel موجود
1. اضافه کردن ستون‌های جدید برای فیلدهای حیاتی
2. پر کردن داده‌های نمونه
3. اجرای مجدد Validation

### گزینه 2: Export کامل از Azure DevOps
1. استفاده از Azure DevOps REST API
2. Export تمام فیلدها به Excel
3. Map کردن به ساختار تعریف‌شده

### گزینه 3: پیاده‌سازی مرحله‌ای
1. فاز 1: پیاده‌سازی با 20 فیلد حیاتی
2. فاز 2: افزودن فیلدهای توسعه‌یافته
3. فاز 3: تکمیل با فیلدهای پیشرفته

---

تاریخ گزارش: 2025-12-25
وضعیت: Implementation Blocked - Missing Required Fields

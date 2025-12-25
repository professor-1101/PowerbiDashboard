# راهنمای پیاده‌سازی - سیستم ردیابی باگ Azure DevOps

## خلاصه

این سند راهنمای کامل پیاده‌سازی داشبورد BI برای ردیابی باگ Azure DevOps را ارائه می‌دهد.

---

## فایل‌های تولید شده

### 1. داده و Excel

| فایل | توضیح | تعداد ردیف | ستون‌ها |
|------|-------|------------|---------|
| `bugs_complete_data.xlsx` | داده خام کامل با تمام 74 فیلد | 100 | 74 |
| `BugTracking_Final.xlsx` | فایل نهایی با 5 شیت | 100 | - |

### 2. گزارش‌های تحلیلی

| فایل | توضیح |
|------|-------|
| `ANALYSIS-REPORT.md` | تحلیل کامل فایل‌های MD (8 بخش) |
| `VALIDATION-REPORT.md` | گزارش Validation و فیلدهای گمشده (7 بخش) |
| `SUMMARY.md` | خلاصه اجرایی |
| `IMPLEMENTATION-GUIDE.md` | این فایل |

### 3. فایل‌های MD مرجع

| فایل | توضیح |
|------|-------|
| `bug-fields-final.md` | تعریف 86 فیلد (74 + 12 Task) |
| `bug-metrics-final.md` | تعریف 314 متریک |
| `bug-dashboards-final.md` | تعریف 13 داشبورد |
| `bug-master-final.md` | سند اعتبارسنجی |

### 4. چارت‌های نمونه

پوشه `charts/` شامل 8 چارت PNG:
1. `01_bugs_by_state.png` - توزیع باگ به تفکیک State
2. `02_bugs_by_severity.png` - توزیع باگ به تفکیک Severity
3. `03_bugs_by_team.png` - توزیع باگ به تفکیک Team
4. `04_lead_time_distribution.png` - توزیع Lead Time
5. `05_state_by_sprint.png` - State به تفکیک Sprint
6. `06_effort_distribution.png` - توزیع Effort
7. `07_quality_metrics.png` - متریک‌های کیفیت
8. `08_close_reason.png` - دلایل بسته شدن

---

## ساختار فایل BugTracking_Final.xlsx

### Sheet 1: raw_data
**محتوا**: داده خام کامل (100 ردیف × 74 ستون)

**ستون‌های کلیدی**:
- BugID, Title, Description
- State (8 حالت: Open/Triage/Active/In Progress/Ready for Retest/Resolved/Done/Closed)
- Severity (Critical/High/Medium/Low)
- Priority (P0/P1/P2/P3)
- Category, is_escaped, IsRegression
- تاریخ‌ها (10 فیلد)
- State Transition (11 فیلد)
- Effort (7 فیلد)
- Quality (8 فیلد)

### Sheet 2: calculated_fields
**محتوا**: 11 فیلد محاسبه‌شده با فرمول و نمونه

**فیلدها**:
- LeadTimeHrs: `ClosedDate - CreatedDate`
- CycleTimeHrs: `ClosedDate - StartedDate`
- ResponseTimeHrs: `AssignedDate - CreatedDate`
- TotalEffortHrs: `Analysis + Dev + Fix + Test + Reopen`
- TriageDurationHrs: `AssignedDate - TriageDate`
- InProgressDurationHrs: `ReadyForRetestDate - InProgressDate`
- و غیره

### Sheet 3: metrics
**محتوا**: 53 متریک نمونه (از 314 متریک کل)

**گروه‌های متریک**:
- **Volume (V)**: V01-V17 (تعداد باگ به تفکیک State, Severity, Priority)
- **State Flow (SF)**: SF01-SF15 (Duration, Efficiency, Pass Rate)
- **Close Reason (CR)**: CR03-CR12 (نرخ‌های Close Reason)
- **Time (T)**: T01-T29 (Lead Time, Cycle Time, Aging)
- **Effort (E)**: E01-E14 (Total, Dev, Test و نسبت‌ها)
- **Quality (Q)**: Q01-Q13 (Escape Rate, Reopen Rate, Quality Index)
- **People (P)**: P01-P18 (Bugs per Developer/Team)
- **Sprint (S)**: S01-S05 (Velocity, Completion Rate)
- **Project (J)**: J01-J10 (Bug Density, Quality Index, Effort)

### Sheet 4: charts_data
**محتوا**: داده آماده برای چارت‌ها (16 ردیف)

**چارت‌ها**:
- Bugs by State
- Bugs by Severity
- Bugs by Team

### Sheet 5: validation
**محتوا**: 11 چک Validation

**Checks**:
- فیلدهای لازم موجود هستند
- مقادیر Null
- State ها از لیست معتبر هستند
- ترتیب تاریخ‌ها منطقی است
- محاسبات Effort درست است

---

## مراحل پیاده‌سازی در Power BI

### مرحله 1: Import داده

```
1. باز کردن Power BI Desktop
2. Get Data → Excel
3. انتخاب فایل: BugTracking_Final.xlsx
4. انتخاب sheet: raw_data
5. Load
```

### مرحله 2: ایجاد Measures (DAX)

برای هر متریک در sheet `metrics`، یک Measure ایجاد کنید:

**مثال 1: Total Bugs**
```dax
V01_Total_Bugs = COUNTROWS('raw_data')
```

**مثال 2: Open Bugs**
```dax
V02_Open_Bugs =
    CALCULATE(
        COUNTROWS('raw_data'),
        'raw_data'[State] IN {"Open", "Triage", "Active", "In Progress", "Ready for Retest"}
    )
```

**مثال 3: Escape Rate**
```dax
Q01_Escape_Rate =
    DIVIDE(
        CALCULATE(COUNTROWS('raw_data'), 'raw_data'[is_escaped] = TRUE),
        COUNTROWS('raw_data'),
        0
    ) * 100
```

**مثال 4: Quality Index**
```dax
Q13_Quality_Index =
    ([Q05_Fix_Success_Rate] * 0.4) +
    ([Q10_Defect_Detection_Effectiveness_DDE] * 0.3) +
    ((100 - [Q01_Escape_Rate]) * 0.3)
```

### مرحله 3: ایجاد Visuals

#### Dashboard 1: EXECUTIVE

**KPI Cards**:
- V01_Total_Bugs
- V02_Open_Bugs
- V14_Critical_Bugs
- Q13_Quality_Index

**Line Chart**: Bug Trend
- X-axis: CreatedDate (Month)
- Y-axis: Count of BugID
- Legend: State

**Donut Chart**: Severity Distribution
- Values: Count of BugID
- Legend: Severity

#### Dashboard 7: STATE FLOW ANALYSIS

**Funnel Chart**: State Conversion
- Values: Count of bugs per State
- Order: Open → Triage → Active → In Progress → Ready for Retest → Resolved → Done → Closed

**Bar Chart**: Average Duration by State
- X-axis: State
- Y-axis: Average of TriageDurationHrs, InProgressDurationHrs, etc.

**KPI Cards**:
- SF01_Avg_Triage_Duration
- SF06_Avg_InProgress_Duration
- SF14_Triage_Efficiency
- SF15_First_Time_Pass_Rate

### مرحله 4: تنظیم Drill-through

```
1. ایجاد صفحه جدید: "Bug Details"
2. اضافه کردن فیلتر Drill-through: BugID
3. اضافه کردن Table با فیلدهای کلیدی
4. روی ویژوال‌ها راست‌کلیک → Drill through
```

### مرحله 5: Slicers

**Slicers مشترک** (در همه صفحات):
- Date Range (CreatedDate)
- Severity (multiselect)
- State (multiselect)
- Team (multiselect)
- Sprint (multiselect)

**تنظیم Sync**:
```
View → Sync Slicers → Select all pages
```

---

## مثال‌های کامل DAX

### گروه Volume

```dax
V01_Total_Bugs = COUNTROWS('raw_data')

V02_Open_Bugs =
    CALCULATE(
        COUNTROWS('raw_data'),
        'raw_data'[State] IN {"Open", "Triage", "Active", "In Progress", "Ready for Retest"}
    )

V09_Closed_Bugs =
    CALCULATE(
        COUNTROWS('raw_data'),
        'raw_data'[State] = "Closed"
    )

V12_Escaped_Bugs =
    CALCULATE(
        COUNTROWS('raw_data'),
        'raw_data'[is_escaped] = TRUE
    )

V14_Critical_Bugs =
    CALCULATE(
        COUNTROWS('raw_data'),
        'raw_data'[Severity] = "Critical"
    )
```

### گروه State Flow

```dax
SF01_Avg_Triage_Duration =
    AVERAGE('raw_data'[TriageDurationHrs])

SF06_Avg_InProgress_Duration =
    AVERAGE('raw_data'[InProgressDurationHrs])

SF14_Triage_Efficiency =
    VAR TriagedIn4Hrs =
        CALCULATE(
            COUNTROWS('raw_data'),
            'raw_data'[TriageDurationHrs] <= 4
        )
    VAR TotalWithTriage =
        CALCULATE(
            COUNTROWS('raw_data'),
            NOT(ISBLANK('raw_data'[TriageDurationHrs]))
        )
    RETURN
        DIVIDE(TriagedIn4Hrs, TotalWithTriage, 0) * 100

SF15_First_Time_Pass_Rate =
    VAR PassedFirstTime =
        CALCULATE(
            COUNTROWS('raw_data'),
            'raw_data'[RetestFailCount] = 0
        )
    VAR Completed =
        CALCULATE(
            COUNTROWS('raw_data'),
            'raw_data'[State] IN {"Resolved", "Done", "Closed"}
        )
    RETURN
        DIVIDE(PassedFirstTime, Completed, 0) * 100
```

### گروه Quality

```dax
Q01_Escape_Rate =
    DIVIDE([V12_Escaped_Bugs], [V01_Total_Bugs], 0) * 100

Q03_Reopen_Rate =
    VAR Reopened =
        CALCULATE(
            COUNTROWS('raw_data'),
            'raw_data'[ReopenCount] > 0
        )
    RETURN
        DIVIDE(Reopened, [V09_Closed_Bugs], 0) * 100

Q05_Fix_Success_Rate =
    100 - [Q03_Reopen_Rate]

Q10_Defect_Detection_Effectiveness_DDE =
    DIVIDE([V01_Total_Bugs] - [V12_Escaped_Bugs], [V01_Total_Bugs], 0) * 100

Q13_Quality_Index =
    ([Q05_Fix_Success_Rate] * 0.4) +
    ([Q10_Defect_Detection_Effectiveness_DDE] * 0.3) +
    ((100 - [Q01_Escape_Rate]) * 0.3)
```

---

## نکات مهم

### 1. State ها
State های صحیح در Azure DevOps:
- Open
- Triage
- Active
- In Progress
- Ready for Retest
- Resolved
- Done
- Closed

### 2. فیلد Canonical: is_escaped
این فیلد هم Escaped و هم Customer-Reported را پوشش می‌دهد.

### 3. CloseReason
7 مقدار معتبر:
- Completed
- By Design
- Cannot Reproduce
- Duplicate
- Invalid
- Obsolete
- Won't Fix

### 4. محاسبات زمانی
همه محاسبات زمانی به ساعت (hours) هستند:
- LeadTimeHrs
- CycleTimeHrs
- TriageDurationHrs
- InProgressDurationHrs
- ReadyForRetestDurationHrs

### 5. Conditional Dashboards
سه داشبورد به داده اضافی نیاز دارند:
- BUSINESS IMPACT (نیاز به فیلدهای Business)
- RISK & PREDICTIONS (نیاز به RiskScore و ML models)
- CUSTOMER SATISFACTION (نیاز به Customer Feedback)

---

## چک‌لیست راه‌اندازی

- [ ] Import فایل `BugTracking_Final.xlsx` به Power BI
- [ ] ایجاد Measures برای گروه Volume (V01-V17)
- [ ] ایجاد Measures برای گروه State Flow (SF01-SF15)
- [ ] ایجاد Measures برای گروه Close Reason (CR)
- [ ] ایجاد Measures برای گروه Quality (Q01-Q13)
- [ ] ایجاد Dashboard EXECUTIVE
- [ ] ایجاد Dashboard STATE FLOW ANALYSIS
- [ ] ایجاد Dashboard QUALITY & STABILITY
- [ ] تنظیم Slicers مشترک
- [ ] تنظیم Drill-through pages
- [ ] تست همه Visuals
- [ ] Publish به Power BI Service

---

## مراحل بعدی

### فاز 1: راه‌اندازی اولیه
1. Import داده
2. ایجاد Measures اصلی (V, SF, CR, Q)
3. ساخت 3 داشبورد اصلی (EXECUTIVE, STATE FLOW, QUALITY)

### فاز 2: توسعه
1. ایجاد Measures کامل (T, E, P, S, J, TR)
2. ساخت 7 داشبورد باقی‌مانده
3. تنظیم Advanced features (Bookmarks, Drill-through)

### فاز 3: بهبود
1. اتصال به Azure DevOps واقعی
2. Auto-refresh
3. Row-level security

---

## پشتیبانی

برای سوالات یا مشکلات:
1. مراجعه به `ANALYSIS-REPORT.md` برای جزئیات تکنیکی
2. مراجعه به `VALIDATION-REPORT.md` برای مشکلات داده
3. مراجعه به `bug-metrics-final.md` برای فرمول‌های دقیق DAX

---

تاریخ: 2025-12-25
نسخه: 1.0

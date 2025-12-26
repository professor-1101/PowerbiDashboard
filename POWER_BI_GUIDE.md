# 🚀 راهنمای کامل Power BI - Bug Tracking Dashboard

## 📦 فایل‌های موجود:

1. ✅ **BugTracking_Complete.xlsx** - فایل اصلی Excel (133 KB)
2. ✅ **BugTracking_Dashboard.pbit** - فایل Power BI Template (3.3 KB) - **جدید!**

---

## 🎯 روش 1: استفاده از PBIT (سریع)

### مرحله 1: باز کردن PBIT
```
1. Power BI Desktop رو باز کن
2. File > Open > BugTracking_Dashboard.pbit انتخاب کن
3. مسیر فایل BugTracking_Complete.xlsx رو مشخص کن
4. Load بزن
```

### مرحله 2: اتصال داده
```
- اگر Excel توی همون پوشه است، خودکار وصل می‌شه
- اگر نه، مسیرش رو دستی مشخص کن:
  Home > Transform Data > Data Source Settings
```

### مرحله 3: Refresh
```
Home > Refresh
```

### ⚠️ نکات مهم:
- این PBIT فقط 6 چارت پایه داره
- بقیه 37 چارت رو باید دستی اضافه کنی
- یا از روش 2 استفاده کن (پیشنهادی!)

---

## 🎯 روش 2: Import Excel مستقیم (پیشنهادی ✅)

این روش **100% تضمین شده** و **سریع‌تره**!

### مرحله 1: Import Excel
```
1. Power BI Desktop باز کن
2. Home > Get Data > Excel Workbook
3. BugTracking_Complete.xlsx انتخاب کن
4. جدول raw_data رو انتخاب کن
5. Load بزن
```

### مرحله 2: ایجاد Measures

توی Model View برو و این DAX measures رو اضافه کن:

```dax
Total Bugs = COUNTROWS(raw_data)

Open Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[State] IN {"Open", "New", "Active"}
)

Closed Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[State] IN {"Closed", "Resolved", "Done"}
)

Avg Lead Time (Days) =
AVERAGE(raw_data[LeadTimeHrs]) / 24

Avg Cycle Time (Days) =
AVERAGE(raw_data[CycleTimeHrs]) / 24

Critical Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[Severity] = "Critical"
)

High Severity Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[Severity] = "High"
)

Escaped Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[is_escaped] = 1
)

Regression Bugs =
CALCULATE(
    COUNTROWS(raw_data),
    raw_data[is_regression] = 1
)

Escape Rate % =
DIVIDE([Escaped Bugs], [Total Bugs], 0) * 100

Reopen Rate % =
DIVIDE(
    CALCULATE(
        COUNTROWS(raw_data),
        raw_data[ReopenCount] > 0
    ),
    [Total Bugs],
    0
) * 100
```

### مرحله 3: ساخت Dashboard

#### صفحه اول: Overview Dashboard

**فیلترها (بالای صفحه):**
1. Start Date Slicer
2. End Date Slicer
3. Project Slicer (Dropdown)
4. Team Slicer (Dropdown)
5. Sprint Slicer (Dropdown)
6. Severity Slicer (Dropdown)
7. State Slicer (Dropdown)
8. Priority Slicer (Dropdown)
9. Category Slicer (Dropdown)
10. Module Slicer (Dropdown)

**چارت‌ها:**

**ردیف 1 (کارت‌ها):**
1. Card: Total Bugs
2. Card: Open Bugs
3. Card: Closed Bugs
4. Card: Critical Bugs

**ردیف 2:**
5. Pie Chart: Bug Status Distribution
   - Legend: State
   - Values: Total Bugs

6. Pie Chart: Bugs by Severity
   - Legend: Severity
   - Values: Total Bugs

7. Pie Chart: Bugs by Priority
   - Legend: Priority
   - Values: Total Bugs

**ردیف 3:**
8. Bar Chart: Bugs by Team
   - Axis: TeamName
   - Values: Total Bugs

9. Bar Chart: Top 10 Modules
   - Axis: ModuleName
   - Values: Total Bugs
   - Filter: Top 10

10. Bar Chart: Bugs by Category
    - Axis: Category
    - Values: Total Bugs

**ردیف 4:**
11. Line Chart: Bug Trend Over Time
    - Axis: SprintName
    - Values: Total Bugs
    - Legend: State

---

#### صفحه دوم: Volume Analysis

12. Stacked Bar: Bugs by State
13. Stacked Column: Bugs by Severity × Priority
14. Treemap: Bugs by Module
15. Funnel: Bug Flow (Open → Active → Resolved → Closed)
16. Matrix: Module × Severity

---

#### صفحه سوم: Team Performance

17. Clustered Bar: Bugs by Team
18. Bar Chart: Top 10 Assignees
19. Bar Chart: Top 10 Resolvers
20. Stacked Column: Team × Sprint
21. Scatter: Team × Resolution Time

---

#### صفحه چهارم: Sprint Analysis

22. Column Chart: Bugs by Sprint
23. Line Chart: Sprint Velocity
24. Stacked Area: Sprint Burn-down
25. Waterfall: Sprint Changes

---

#### صفحه پنجم: Time Flow

26. Scatter: Lead Time vs Cycle Time
27. Column Chart: Aging Buckets
28. Line Chart: Average Lead Time Trend
29. Histogram: Lead Time Distribution
30. Histogram: Cycle Time Distribution

---

#### صفحه ششم: Quality Analysis

31. Bar Chart: Reopen Analysis
32. Pie Chart: Escaped Bugs
33. Pie Chart: Regression Bugs
34. Gauge: Escape Rate %
35. Gauge: Reopen Rate %
36. Line Chart: Quality Metrics Trend

---

#### صفحه هفتم: State Flow

37. Funnel Chart: State Flow
38. Column Chart: Average Duration by State
39. Sankey: State Transitions (use custom visual)

---

#### صفحه هشتم: Resolution Analysis

40. Pie Chart: Close Reason Distribution
41. Pie Chart: Resolution Types
42. Bar Chart: Top Root Causes
43. Stacked Bar: Close Reason × Severity

---

## 📊 تنظیمات پیشنهادی:

### تم (Theme):
```
View > Themes > انتخاب تم دلخواه
پیشنهاد: Executive یا Innovate
```

### رنگ‌بندی:
- **Critical**: قرمز (#E74C3C)
- **High**: نارنجی (#E67E22)
- **Medium**: زرد (#F39C12)
- **Low**: آبی (#3498DB)

### فرمت چارت‌ها:
- Data Labels: On
- Legend: Bottom یا Right
- Title: Bold, 14pt
- Grid Lines: On (subtle)

---

## 🎨 Custom Visuals (اختیاری):

برای چارت‌های پیشرفته‌تر:

```
Home > Get Visuals > Get More Visuals

پیشنهادی:
1. Sankey Diagram (برای State Flow)
2. Enhanced Scatter Chart
3. Timeline Slicer
4. Chiclet Slicer
5. Text Filter
```

---

## 💡 نکات مهم:

### 1. Performance:
```
- از DirectQuery به جای Import استفاده نکن (Excel کوچیکه)
- Aggregations رو توی DAX بنویس (نه توی Visual)
- از calculated columns کم استفاده کن
```

### 2. Refresh:
```
Home > Refresh
یا
File > Options > Data Load > Configure Refresh Schedule
```

### 3. Publish:
```
Home > Publish > Select Workspace
یا
File > Export > Export to PDF
```

### 4. Share:
```
File > Export > Power BI Template (.pbit)
یا
File > Publish to Web (عمومی)
```

---

## ✅ چک‌لیست نهایی:

- [ ] Excel import شد
- [ ] همه 11 Measure اضافه شد
- [ ] فیلترها کار می‌کنن
- [ ] چارت‌ها data نشون میدن
- [ ] تم و رنگ‌ها تنظیم شد
- [ ] عنوان صفحات مشخص شد
- [ ] Refresh تست شد
- [ ] فایل Save شد

---

## 🆘 مشکلات رایج:

### خطا: "Couldn't load data"
```
راه حل:
1. مسیر Excel رو چک کن
2. Excel باز نباشه
3. Data Source Settings > Change Source
```

### خطا: "Can't refresh"
```
راه حل:
1. Excel file رو ببند
2. Home > Refresh
3. اگر باز نشد، Data Source Settings > Edit Permissions
```

### چارت خالیه
```
راه حل:
1. Visual رو انتخاب کن
2. Field well رو چک کن
3. Filter رو بردار
4. Data رو Refresh کن
```

---

## 🎯 زمان تخمینی:

- روش 1 (PBIT): ~10 دقیقه + 2-3 ساعت برای 37 چارت باقی‌مونده
- روش 2 (Import): ~30 دقیقه برای همه

**پیشنهاد:** روش 2 رو استفاده کن - سریع‌تر و مطمئن‌تره!

---

## 📞 پشتیبانی:

اگر مشکلی داشتی:
1. Power BI Community: https://community.powerbi.com
2. Microsoft Docs: https://learn.microsoft.com/power-bi
3. YouTube: "Power BI Tutorial"

---

**موفق باشی! 🚀**

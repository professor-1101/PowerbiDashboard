# ساختار داشبوردهای باگ

## داشبوردهای معتبر

### 1. EXECUTIVE

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: V01, V02, V14, Q16, TR01, TR02

**فیلدهای مرجع**: F-BUG-001, 002, 004, 006, 027, 032, 066

**بینش و کاربرد**:
- نمای سریع وضعیت کلی کیفیت و حجم باگ برای مدیران ارشد
- شناسایی فوری باگ‌های بحرانی و روند کلی کیفیت
- تصمیم‌گیری درباره تخصیص منابع و اولویت‌بندی رفع باگ‌ها
- ارزیابی ریسک انتشار بر اساس شاخص کیفیت و باگ‌های Critical

**ویژوال‌های کلیدی**:
- KPI Cards: V01, V02, V14, Q13, TR02
- Line Chart: روند تعداد باگ‌ها در طول زمان
- Donut Chart: توزیع باگ به تفکیک Severity
- Gauge: شاخص کیفیت کلی (Q13)

---

### 2. VOLUME ANALYSIS

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: V02–V09, V14–V17, V23–V31, V18–V22

**فیلدهای مرجع**: F-BUG-004, 005, 006, 007, 011-018, 027, 036, 037, 066, F-TASK-002

**بینش و کاربرد**:
- شناسایی توزیع باگ به تفکیک شدت، اولویت، دسته و ماژول
- کشف تیم‌ها یا ماژول‌هایی که بیشترین بار باگ را دارند
- متعادل‌سازی بار کاری بین تیم‌ها
- هدایت تمرکز تست به ماژول‌های پرتراکم
- درک الگوی توزیع باگ‌های Security و Performance

**ویژوال‌های کلیدی**:
- Stacked Bar Chart: باگ به تفکیک Severity و State
- Treemap: توزیع باگ در ماژول‌ها
- Column Chart: باگ به تفکیک Category
- Matrix: باگ به تفکیک تیم و Severity

---

### 3. TIME & FLOW

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: T01–T10, T18–T23, T29, T37–T39

**فیلدهای مرجع**: F-BUG-027-036, 042-048, 049-054, F-TASK-007, 009

**بینش و کاربرد**:
- شناسایی گلوگاه‌های زمانی در فرآیند رفع باگ
- مقایسه زمان انتظار در مقابل زمان کار فعال (Flow Efficiency)
- شناسایی باگ‌های قدیمی (Aging) که نیاز به توجه فوری دارند
- ارزیابی سرعت پاسخگویی تیم (Response Time)
- بهینه‌سازی فرآیند با کاهش زمان‌های انتظار

**ویژوال‌های کلیدی**:
- Box Plot: توزیع Lead Time و Cycle Time
- Column Chart: Aging Buckets (7, 14, 30, 60, 90 days)
- Line Chart: روند Average Lead Time در طول زمان
- Scatter Plot: Cycle Time vs Effort

---

### 4. QUALITY & STABILITY

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: Q01–Q09, Q15–Q20, Q28–Q29

**فیلدهای مرجع**: F-BUG-004, 005, 010, 027, 032-037, 041, 049, 054, 061, 064, 066, F-TASK-007, 009

**بینش و کاربرد**:
- ارزیابی نرخ Escape و Regression برای بهبود فرآیند تست
- سنجش کیفیت رفع باگ با Reopen Rate و Fix Success Rate
- شناسایی نقاط ضعف در فرآیند کیفیت و تست
- تعیین اثربخشی تست‌ها با DRE و Testing Effectiveness
- اولویت‌بندی بهبود فرآیند بر اساس شاخص‌های کیفیت

**ویژوال‌های کلیدی**:
- KPI Cards: Q01, Q03, Q05, Q10, Q13
- Waterfall Chart: شکست Quality Index
- Line Chart: روند Escape Rate و Reopen Rate
- Gauge: Quality Index و DRE

---

### 5. TEAM PERFORMANCE

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: P01–P07, P15–P16, P18–P19, P25

**فیلدهای مرجع**: F-BUG-015, 019-026, 037-038, 041-047, 051, F-TASK-005, 007, 009

**بینش و کاربرد**:
- شناسایی توسعه‌دهندگانی که نرخ Reopen بالایی دارند
- بررسی توزیع بار کاری و تعادل Workload بین افراد
- سنجش بهره‌وری تیم‌ها و افراد
- شناسایی نیاز به آموزش یا پشتیبانی بیشتر
- تصمیم‌گیری درباره جابجایی کار از افراد Overloaded

**ویژوال‌های کلیدی**:
- Bar Chart: باگ به تفکیک Developer/Team
- Scatter Plot: Bugs vs Reopen Rate به تفکیک Developer
- Heatmap: Workload Matrix (Developer × Sprint)
- Table: Top/Bottom Performers با Score

---

### 6. SPRINT ANALYSIS

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: S01–S06, S09–S17, S26

**فیلدهای مرجع**: F-BUG-010, 017-018, 027, 032, 070, F-TASK-007

**بینش و کاربرد**:
- ارزیابی پایداری اسپرینت و مدیریت Carryover
- شناسایی اسپرینت‌هایی که Inflow یا Scope Change زیادی داشتند
- بهبود Commitment Reliability و کاهش تغییرات میان اسپرینت
- مقایسه Velocity و Throughput بین اسپرینت‌ها
- بررسی کیفیت تحویل در هر اسپرینت

**ویژوال‌های کلیدی**:
- Line Chart: Velocity و Completion Rate به تفکیک Sprint
- Stacked Column: Inflow, Outflow, Carryover
- Scatter Plot: Velocity vs Quality Index
- Burndown Chart: WIP در طول Sprint

---

### 7. STATE FLOW ANALYSIS - جدید

**وضعیت**: ✅ Active

**نوع داشبورد**: Process Analysis

**متریک‌های کلیدی**: SF01–SF30, V02–V09, T03, T13

**فیلدهای مرجع**: F-BUG-006, 027–036, 073–083

**بینش و کاربرد**:
- تحلیل جریان باگ‌ها بین State های مختلف (Open → Triage → Active → In Progress → Ready for Retest → Resolved → Done → Closed)
- شناسایی گلوگاه‌ها در هر State (کدام State بیشترین زمان را می‌گیرد)
- محاسبه Triage Efficiency و شناسایی باگ‌های Stuck در Triage
- تحلیل Retest Pass Rate و First Time Pass Rate
- شناسایی Back-flow (بازگشت به State های قبلی)
- بهینه‌سازی زمان انتقال بین State ها
- تعیین Bottleneck State و بهبود Flow Efficiency

**ویژوال‌های کلیدی**:
- Sankey Diagram: جریان باگ بین State ها (نمایش حجم انتقال)
- Funnel Chart: تبدیل از Open به Closed (Conversion Rate)
- Box Plot: توزیع زمان در هر State (Triage, Active, In Progress, Ready for Retest)
- Heatmap: ماتریس انتقال State (از کدام State به کدام State)
- Column Chart: Average Duration در هر State
- Waterfall Chart: تغییرات State در طول زمان برای یک باگ نمونه
- KPI Cards: SF01 (Avg Triage Duration), SF06 (Avg InProgress Duration), SF14 (Triage Efficiency), SF15 (First Time Pass Rate)
- Table: باگ‌های Stuck (بیش از threshold در یک State)
- Line Chart: روند State Transition Count در طول زمان

**Drill-through**:
- State Detail Page: جزئیات باگ‌های در یک State خاص
- Bug Flow Timeline: timeline انتقالات یک باگ خاص
- Team State Performance: عملکرد تیم در هر State

**فیلترها و Slicers**:
- State (multiselect)
- Severity
- Team
- Sprint
- Date Range
- Duration Threshold

---

### 8. RESOLUTION ANALYSIS - جدید

**وضعیت**: ✅ Active

**نوع داشبورد**: Quality & Decision Analysis

**متریک‌های کلیدی**: CR01–CR15, V36–V38, V43–V45

**فیلدهای مرجع**: F-BUG-061, 084, 006, 064, 065

**بینش و کاربرد**:
- تحلیل دقیق دلایل بسته شدن باگ‌ها (By Design, Cannot Reproduce, Completed, Duplicate, Invalid, Obsolete, Won't Fix)
- محاسبه نرخ Cannot Reproduce (نشان‌دهنده مشکل در تست یا گزارش‌دهی)
- شناسایی نرخ Duplicate Detection (کیفیت گزارش‌دهی)
- ارزیابی نرخ Invalid/Obsolete (نویز در سیستم)
- محاسبه Successful Completion Rate (نرخ باگ‌های واقعاً رفع‌شده)
- تحلیل By Design Rate (باگ‌هایی که طراحی صحیح بودند)
- محاسبه Actionable Bugs Rate (باگ‌های قابل‌اقدام)
- شناسایی الگوهای Close Reason به تفکیک تیم، ماژول، Severity

**ویژوال‌های کلیدی**:
- Donut/Pie Chart: توزیع Close Reason ها
- Stacked Bar Chart: Close Reason به تفکیک Severity
- Matrix: Close Reason × Team/Module
- KPI Cards: CR09 (Cannot Reproduce Rate), CR10 (Duplicate Rate), CR12 (Completion Rate), CR15 (Actionable Bugs Rate)
- Line Chart: روند Close Reason ها در طول زمان
- Treemap: Close Reason به تفکیک Module
- Table: Top 10 Duplicate Bugs با لینک به باگ اصلی
- Column Chart: Close Reason به تفکیک Reporter (شناسایی Reporter های پرنویز)

**Drill-through**:
- Bug Details: جزئیات باگ‌های با Close Reason خاص
- Duplicate Chain: زنجیره باگ‌های Duplicate
- Cannot Reproduce Analysis: دلایل Cannot Reproduce

**فیلترها و Slicers**:
- Close Reason (multiselect)
- Severity
- Team
- Module
- Reporter
- Date Range

---

### 9. BOTTLENECK ANALYSIS - جدید

**وضعیت**: ✅ Active

**نوع داشبورد**: Process Optimization

**متریک‌های کلیدی**: SF04, SF10, T16–T17, T37–T39, SF24, SF25

**فیلدهای مرجع**: F-BUG-006, 036, 052, 053, 054, 073–082

**بینش و کاربرد**:
- شناسایی دقیق گلوگاه‌های زمانی در فرآیند (کدام State کندترین است)
- تحلیل باگ‌های Stuck (بیش از threshold در یک حالت)
- محاسبه Flow Efficiency برای هر بخش از فرآیند
- شناسایی باگ‌های Stale (بدون update برای مدت طولانی)
- تعیین Bottleneck State به صورت پویا
- ارزیابی Wait Time vs Active Work Time
- بهینه‌سازی ظرفیت در بخش‌های پرازدحام

**ویژوال‌های کلیدی**:
- Bar Chart (Horizontal): Average Duration به تفکیک State (مرتب شده نزولی برای نمایش Bottleneck)
- Scatter Plot: Wait Time vs Active Work Time (باگ‌های بالای خط مساوی مشکل دارند)
- Heatmap: باگ‌های Stuck به تفکیک State × Week
- KPI Card: SF24 (Bottleneck State), SF25 (Flow Efficiency)
- Funnel Chart: تعداد باگ در هر State (نمایش drop-off)
- Table: Top 20 Stale Bugs (بدون update طولانی)
- Line Chart: روند Average Duration در Bottleneck State
- Gauge: Flow Efficiency با target و threshold

**Drill-through**:
- Bottleneck Details: جزئیات باگ‌های در Bottleneck State
- State History: تاریخچه State برای یک باگ خاص

**فیلترها و Slicers**:
- State
- Duration Threshold (slider)
- Severity
- Team
- Date Range

---

### 10. BUSINESS IMPACT

**وضعیت**: 🔶 Conditional

**شرط**: نیاز به تعریف فیلدهای Business سفارشی (RevenueImpact، UsersAffected، CustomerComplaints)

**متریک‌های کلیدی**: B03–B25

**فیلدهای مرجع**: F-BUG-059, 004, 005, 006

**بینش و کاربرد**:
- اولویت‌بندی رفع باگ بر اساس تاثیر بیزنسی
- ارزیابی هزینه کیفیت پایین (Cost of Poor Quality)
- شناسایی باگ‌های Security و Compliance بحرانی
- محاسبه ریسک درآمد و ارزش در معرض خطر
- تصمیم‌گیری مدیریتی مبتنی بر تاثیر مالی

**ویژوال‌های کلیدی**:
- KPI Cards: B03, B13, B15, B20
- Waterfall Chart: Cost of Poor Quality Breakdown
- Scatter Plot: Business Impact vs Severity
- Treemap: Impact به تفکیک Module

---

### 11. RISK & PREDICTIONS

**وضعیت**: 🔶 Conditional

**شرط**: نیاز به RiskScore و مدل‌های ML (F-BUG-066-069)

**متریک‌های کلیدی**: R01–R09, R11–R25

**فیلدهای مرجع**: F-BUG-004, 006, 066-069

**بینش و کاربرد**:
- ارزیابی ریسک کلی و پیش‌بینی مشکلات آینده
- شناسایی ماژول‌ها یا تیم‌های پرریسک
- تصمیم‌گیری درباره آماده بودن برای انتشار (Release Risk)
- پیش‌بینی تعداد باگ در اسپرینت بعدی
- شناسایی الگوهای تکرارشونده و Anomaly

**ویژوال‌های کلیدی**:
- Gauge: R20 (Release Risk Score)
- Scatter Plot: Risk Score vs Bug Count
- Heatmap: Risk به تفکیک Module × Team
- Line Chart: روند Risk Score

---

### 12. CUSTOMER SATISFACTION

**وضعیت**: 🔶 Conditional

**شرط**: نیاز به داده‌های Customer Feedback و Support خارجی

**متریک‌های کلیدی**: C01–C20

**فیلدهای مرجع**: F-BUG-010

**بینش و کاربرد**:
- ارزیابی رضایت مشتری و تاثیر باگ‌ها بر NPS و CSAT
- شناسایی باگ‌های Customer-Reported و اولویت‌بندی آن‌ها
- کاهش ریسک Churn با تمرکز بر باگ‌های تاثیرگذار
- بهبود زمان پاسخ و رفع مشکلات مشتری
- ارتباط مستقیم بین کیفیت محصول و وفاداری مشتری

**ویژوال‌های کلیدی**:
- KPI Cards: C02, C07, C09, C14
- Line Chart: روند Customer Reported Bugs
- Scatter Plot: Response Time vs Customer Impact
- Table: Top Customer Issues

---

### 13. TRENDS & PATTERNS

**وضعیت**: ✅ Active

**متریک‌های کلیدی**: TR01–TR15

**فیلدهای مرجع**: F-BUG-001, 004-006, 027, 050

**بینش و کاربرد**:
- شناسایی روند رشد یا کاهش باگ در طول زمان
- کشف الگوهای تکرارشونده در ماژول‌ها یا تیم‌ها
- ارزیابی بهبود کیفیت با Quality Trend Index
- شناسایی فصلی بودن (Seasonality) در تولید باگ
- تصمیم‌گیری استراتژیک مبتنی بر روندهای بلندمدت

**ویژوال‌های کلیدی**:
- Line Chart: روندهای بلندمدت (Bugs, Quality, Escape Rate)
- Area Chart: Moving Average 7/30 days
- Scatter Plot: روند به تفکیک Module/Team
- Seasonal Index Chart: الگوهای ماهانه

---

## ویژگی‌های عمومی

### Navigation و Drill-through

**Drill-through Pages**:
- Bug Details با حفظ فیلترها
- Team Analysis با فیلتر تیم
- Sprint Details با فیلتر اسپرینت
- Module Analysis با فیلتر ماژول
- State Details با فیلتر State - جدید
- Bug Flow Timeline - جدید

**Navigation**:
- منوی بالا برای جابجایی بین صفحات
- دکمه Home و Back روی صفحات Drill-through

### Bookmarks

- **Default**: نمای پیش‌فرض تمام داده‌ها
- **Critical Focus**: فیلتر روی Severity = Critical
- **This Sprint**: فیلتر روی اسپرینت جاری
- **Production Issues**: فیلتر روی باگ‌های Production
- **High Risk**: فیلتر روی باگ‌های پرریسک
- **Stuck Bugs**: فیلتر روی باگ‌های Stuck در یک State - جدید
- **Cannot Reproduce**: فیلتر روی باگ‌های Cannot Reproduce - جدید

### Slicers همگام

فیلترهای زیر در تمام صفحات همگام‌سازی شده‌اند:
- **تاریخ**: Date Range
- **شدت**: Severity
- **پروژه**: Project/Team
- **اسپرینت**: Sprint
- **State**: State - جدید
- **Close Reason**: Close Reason - جدید

---

## خلاصه داشبوردهای جدید

### STATE FLOW ANALYSIS
**هدف**: تحلیل جریان و شناسایی گلوگاه‌های State
**چارت‌های کلیدی**: Sankey, Funnel, Box Plot, Heatmap, Waterfall
**بینش**: Triage Efficiency, First Time Pass Rate, Bottleneck State, Back-flow Rate

### RESOLUTION ANALYSIS
**هدف**: تحلیل دلایل بسته شدن باگ‌ها
**چارت‌های کلیدی**: Donut, Stacked Bar, Matrix, Treemap
**بینش**: Cannot Reproduce Rate, Duplicate Detection Rate, Actionable Bugs Rate

### BOTTLENECK ANALYSIS
**هدف**: شناسایی و بهینه‌سازی گلوگاه‌های فرآیند
**چارت‌های کلیدی**: Horizontal Bar, Scatter Plot, Heatmap, Funnel
**بینش**: Bottleneck State, Flow Efficiency, Stale Bugs, Wait Time Analysis

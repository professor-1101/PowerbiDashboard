# سند اعتبارسنجی BI — ردیابی باگ Azure DevOps

## دامنه و ساختار

این سند نسخه نهایی و مرجع سیستم ردیابی باگ بر پایه Azure DevOps است.

### اجزای سیستم

- **bug-fields.md**: تعریف فیلدهای خام و شناسه‌ها (F-BUG-*, F-TASK-*)
- **bug-metrics.md**: تعریف متریک‌ها و Measures (گروه‌های V/SF/CR/T/E/Q/P/S/J/B/R/C/TR)
- **bug-dashboards.md**: توصیف داشبوردها و ویژوال‌ها

---

## تصمیمات طراحی

### State های باگ

State های صحیح در Azure DevOps:
- Open
- Triage
- Active
- In Progress
- Ready for Retest
- Resolved
- Done
- Closed

### Close Reason های باگ

Close Reason های استاندارد:
- By Design
- Cannot Reproduce
- Completed
- Duplicate
- Invalid
- Obsolete
- Won't Fix

### فیلدهای حذف‌شده از canonical

فیلدهای زیر از مدل canonical حذف شده‌اند:
- Environment (Custom)
- RevenueImpact
- UsersAffected
- CustomerComplaints
- ReopenReason

### فیلد Canonical برای Escaped

دو فیلد IsEscaped و IsCustomerReported در یک فیلد استاندارد ادغام شدند:
- **فیلد canonical**: `is_escaped` با شناسه `F-BUG-010`
- این فیلد مبنای تمام متریک‌های Escape و Customer-Reported است

---

## لایه Fields

### گروه‌های دسترس‌پذیری

#### قابل دریافت مستقیم
`F-BUG-001..006, 027..036, 070..072` و `F-TASK-001..012`

#### نیازمند History
`F-BUG-037..054, 073..083, 085..086`

#### نیازمند Custom/Business
`F-BUG-059, 060..065, 084`

#### نیازمند Risk/ML
`F-BUG-066..069`

### فیلدهای هسته‌ای

**شناسه و متن**: F-BUG-001 (BugID), 002 (Title), 003 (Description)

**شدت و اولویت**: F-BUG-004 (Severity), 005 (Priority)

**وضعیت**: F-BUG-006 (State)

**Escaped**: F-BUG-010 (is_escaped)

**تاریخ‌ها**: F-BUG-027..036

**State Transition**: F-BUG-073..083 (جدید - شامل Triage, InProgress, ReadyForRetest Duration و State History)

**Effort**: F-BUG-042..048

**زمان محاسباتی**: F-BUG-049..054

**افراد**: F-BUG-019..026

**زمینه**: F-BUG-011..018, 070..072

**کیفیت**: F-BUG-060..065, 084 (CloseReason - جدید), 085..086 (RetestPass/Fail - جدید)

**Task**: F-TASK-001..012

---

## لایه Metrics

### گروه‌های متریک

**Volume (V)**: 45 متریک — شمارش باگ به تفکیک حالت، شدت، اولویت، دسته (اصلاح شده با State های جدید)

**State Flow (SF)**: 30 متریک — جدید — تحلیل جریان State، Triage Efficiency، Retest Pass Rate، Bottleneck Detection

**Close Reason (CR)**: 15 متریک — جدید — تحلیل دلایل بسته شدن، Cannot Reproduce Rate، Duplicate Detection

**Time & Flow (T)**: 34 متریک — Lead Time, Cycle Time, Aging, Flow Efficiency

**Effort (E)**: 26 متریک — Dev, Test, Fix, Analysis Effort و نسبت‌ها

**Quality (Q)**: 32 متریک — Escape Rate, Reopen Rate, DRE, Quality Index

**People (P)**: 30 متریک — بهره‌وری، توزیع بار، کیفیت کار افراد

**Sprint (S)**: 30 متریک — Velocity, Burndown, Carryover, Technical Debt

**Project (J)**: 20 متریک — Bug Density, Schedule/Cost Variance, Health Score

**Risk (R)**: 21 متریک — Risk Score, Predictions, Anomaly Detection

**Customer (C)**: 16 متریک — CSAT, NPS, Customer-Reported Bugs

**Trend (TR)**: 15 متریک — روندها، Moving Average، الگوها

### نگاشت به فیلدها

تمام متریک‌ها به فیلدهای `F-BUG-*` و `F-TASK-*` مرجع دارند.

متریک‌های Escaped بر فیلد canonical `F-BUG-010 / is_escaped` استوارند.

متریک‌های State Flow بر فیلدهای جدید `F-BUG-073..083` استوارند.

متریک‌های Close Reason بر فیلد جدید `F-BUG-084` استوارند.

---

## لایه Dashboards

### وضعیت داشبوردها

| شناسه | عنوان | وضعیت | نوع |
|------|-------|-------|-----|
| 1 | EXECUTIVE | ✅ Active | Overview |
| 2 | VOLUME ANALYSIS | ✅ Active | Volume |
| 3 | TIME & FLOW | ✅ Active | Time |
| 4 | QUALITY & STABILITY | ✅ Active | Quality |
| 5 | TEAM PERFORMANCE | ✅ Active | People |
| 6 | SPRINT ANALYSIS | ✅ Active | Sprint |
| 7 | STATE FLOW ANALYSIS | ✅ Active | Process - جدید |
| 8 | RESOLUTION ANALYSIS | ✅ Active | Quality - جدید |
| 9 | BOTTLENECK ANALYSIS | ✅ Active | Process - جدید |
| 10 | BUSINESS IMPACT | 🔶 Conditional | Business |
| 11 | RISK & PREDICTIONS | 🔶 Conditional | Risk |
| 12 | CUSTOMER SATISFACTION | 🔶 Conditional | Customer |
| 13 | TRENDS & PATTERNS | ✅ Active | Trend |

### داشبوردهای Conditional

**BUSINESS IMPACT**: نیاز به فیلدهای Business سفارشی

**RISK & PREDICTIONS**: نیاز به RiskScore و مدل‌های ML

**CUSTOMER SATISFACTION**: نیاز به داده‌های Customer Feedback خارجی

### داشبوردهای جدید

**STATE FLOW ANALYSIS**: 
- تحلیل جریان باگ بین State ها
- شناسایی گلوگاه‌ها در هر State
- محاسبه Triage Efficiency و Retest Pass Rate
- ویژوال‌های کلیدی: Sankey Diagram, Funnel Chart, Box Plot, Heatmap

**RESOLUTION ANALYSIS**:
- تحلیل دلایل بسته شدن باگ‌ها
- محاسبه Cannot Reproduce Rate و Duplicate Detection Rate
- ارزیابی Actionable Bugs Rate
- ویژوال‌های کلیدی: Donut Chart, Stacked Bar, Matrix, Treemap

**BOTTLENECK ANALYSIS**:
- شناسایی دقیق گلوگاه‌های زمانی
- تحلیل باگ‌های Stuck و Stale
- محاسبه Flow Efficiency برای هر بخش
- ویژوال‌های کلیدی: Horizontal Bar, Scatter Plot, Heatmap, Gauge

---

## انسجام مدل

**لایه Fields**: `bug-fields.md` — مرجع رسمی تعریف و شناسه فیلدها

**لایه Metrics**: `bug-metrics.md` — هر متریک به فیلدهای F-BUG-*/F-TASK-* ارجاع دارد

**لایه Dashboards**: `bug-dashboards.md` — هر داشبورد به متریک‌ها و فیلدهای کلیدی مرجع دارد

---

## تغییرات اصلی

### اصلاح State ها
- State های قدیمی (New/Active/Resolved/Closed) به State های صحیح (Open/Triage/Active/In Progress/Ready for Retest/Resolved/Done/Closed) تغییر یافتند
- 11 فیلد جدید برای State Transition اضافه شدند (F-BUG-073..083)

### اضافه شدن Close Reason
- فیلد جدید F-BUG-084 (CloseReason) به صورت جداگانه از Resolution تعریف شد
- 7 مقدار استاندارد: By Design, Cannot Reproduce, Completed, Duplicate, Invalid, Obsolete, Won't Fix

### متریک‌های جدید
- گروه State Flow (SF01-SF30): 30 متریک برای تحلیل جریان
- گروه Close Reason (CR01-CR15): 15 متریک برای تحلیل دلایل بسته شدن

### داشبوردهای جدید
- STATE FLOW ANALYSIS: تحلیل جامع جریان State ها
- RESOLUTION ANALYSIS: تحلیل دقیق Close Reason ها
- BOTTLENECK ANALYSIS: شناسایی و بهینه‌سازی گلوگاه‌ها

### فیلدهای Retest
- F-BUG-085 (RetestPassCount) و F-BUG-086 (RetestFailCount) برای تحلیل کیفیت Retest اضافه شدند

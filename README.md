# سیستم ردیابی باگ Azure DevOps - Power BI Dashboard

## خلاصه پروژه

این پروژه یک سیستم کامل BI برای ردیابی و تحلیل باگ‌های Azure DevOps ارائه می‌دهد.

**وضعیت**: ✅ آماده برای پیاده‌سازی در Power BI

---

## فایل‌های کلیدی

### داده و Excel
- **`BugTracking_Final.xlsx`** - فایل اصلی با 5 شیت (100 باگ × 74 فیلد)
- **`bugs_complete_data.xlsx`** - داده خام کامل

### مستندات
- **`IMPLEMENTATION-GUIDE.md`** - راهنمای پیاده‌سازی Power BI
- **`ANALYSIS-REPORT.md`** - تحلیل جامع (امتیاز: 9.75/10)
- **`VALIDATION-REPORT.md`** - گزارش اعتبارسنجی
- **`SUMMARY.md`** - خلاصه اجرایی

### چارت‌ها
پوشه **`charts/`** - 8 چارت PNG نمونه

---

## آمار سریع

- **74 فیلد** (100% کامل)
- **314 متریک** در 12 گروه
- **13 داشبورد** (10 Active، 3 Conditional)
- **100 ردیف** داده نمونه
- **8 چارت** نمونه

---

## شروع سریع

```
1. باز کردن: BugTracking_Final.xlsx در Excel
2. مطالعه: IMPLEMENTATION-GUIDE.md
3. Import به Power BI Desktop
4. ایجاد Measures از فایل bug-metrics-final.md
5. ساخت Dashboards از فایل bug-dashboards-final.md
```

---

## مراحل بعدی

**فاز 1**: Import داده + Measures اصلی + 3 داشبورد (1-2 روز)
**فاز 2**: تکمیل Measures + 7 داشبورد باقی (3-5 روز)
**فاز 3**: اتصال به Azure DevOps واقعی (1-2 روز)

---

**Branch**: `claude/azure-devops-bug-tracking-BzOIh`
**تاریخ**: 2025-12-25
**نسخه**: 1.0
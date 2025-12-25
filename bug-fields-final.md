# راهنمای فیلدهای باگ Azure DevOps

## فیلدهای معتبر و قابل استفاده

### گروه Core (هسته‌ای)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-001** | BugID / System.Id | Bug | شناسه یکتای هر باگ؛ کل joinهای مدل، دریل‌ترو و لینک بین جداول/داشبوردها بر اساس این فیلد |
| **F-BUG-002** | Title / System.Title | Bug | عنوان کوتاه خوانای باگ برای نمایش در جداول، کارت‌های Top N و سرچ متنی |
| **F-BUG-003** | Description / System.Description | Bug | توضیح کامل باگ؛ برای تحلیل کیفی، جستجو در متن و یافتن الگوهای موضوعی |
| **F-BUG-004** | Severity / Microsoft.VSTS.Common.Severity | Bug | سطح شدت باگ (Critical/High/Medium/Low)، محور اصلی KPIهای ریسک، SLA و اولویت رسیدگی |
| **F-BUG-005** | Priority / Microsoft.VSTS.Common.Priority | Bug | اولویت کسب‌وکاری/عملیاتی؛ برای مرتب‌سازی Backlog و فیلتر کردن باگ‌های مهم‌تر |
| **F-BUG-006** | State / System.State | Bug | وضعیت جاری باگ (Open/Triage/Active/In Progress/Ready for Retest/Resolved/Done/Closed)، پایه تمام شمارش‌های Open/Closed و تحلیل جریان کار |

### گروه Classification (دسته‌بندی)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-007** | Category (Custom) | Bug | دسته‌بندی سفارشی نوع باگ (UI، Backend، Performance، Security)، برای تحلیل ریشه مشکل و تمرکز به تفکیک نوع نقص |
| **F-BUG-009** | IsRegression (Custom) | Bug | پرچم بولین برای Regression بودن؛ مبنای متریک‌های Regression Rate و کیفیت رگرشن تست |
| **F-BUG-010** | is_escaped (canonical) | Bug | پرچم بولین canonical برای باگ‌های Escaped؛ ورودی اصلی Escape Rate و Customer-Reported Bugs |

### گروه Context (زمینه)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-011** | ProjectID / System.TeamProject | Bug | شناسه فنی پروژه در Azure DevOps؛ برای فیلتر و مقایسه بین چند پروژه |
| **F-BUG-012** | ProjectName | Bug | نام خوانای پروژه برای نمایش در ویژوال‌ها، کارت‌ها و تفکیک متریک‌ها بین محصولات/پروژه‌ها |
| **F-BUG-013** | TeamID | Bug | شناسه یکتای تیم تحویل؛ برای مدل‌سازی رابطه تیم‌ها، فیلتر Team و متریک‌های عملکرد تیمی |
| **F-BUG-014** | TeamName | Bug | نام تیم تحویل یا مالک باگ؛ محور اصلی تحلیل بار کاری و کیفیت به تفکیک تیم |
| **F-BUG-015** | ModuleID | Bug | شناسه داخلی ماژول/کامپوننت؛ برای ارتباط با جداول دیگر در صورت وجود |
| **F-BUG-016** | ModuleName / System.AreaPath | Bug | نام یا مسیر Area/Module؛ برای Drill-down روی کیفیت هر ماژول و ساخت Treemap/Bar |
| **F-BUG-017** | SprintID / Iteration | Bug | شناسه اسپرینت/Iteration به صورت فنی؛ برای Join با تقویم اسپرینت و مقایسه بین اسپرینت‌ها |
| **F-BUG-018** | SprintName / IterationPath | Bug | نام/مسیر اسپرینت برای نمایش در محور X نمودارهای اسپرینتی و اسلایسر Sprint |
| **F-BUG-070** | Tags / System.Tags | Bug | مجموعه تگ‌ها روی باگ؛ برای دسته‌بندی دلخواه، فیلتر پویا و اتصال به دسته‌بندی‌های Effort/ماژول |
| **F-BUG-071** | ExternalTicketID | Bug | شناسه باگ/تیکت متناظر در سیستم‌های خارجی (Jira، CRM)؛ برای ساخت لینک بین سیستم‌ها |
| **F-BUG-072** | Comments | Bug | کامنت‌ها و گفت‌وگوهای ثبت‌شده روی باگ؛ منبع تحلیل کیفی و متن‌کاوی |

### گروه People (افراد)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-019** | ReporterID / System.CreatedBy.id | Bug | شناسه کاربری شخص گزارش‌دهنده؛ برای تحلیل کیفیت گزارش‌گری و الگوهای گزارش باگ |
| **F-BUG-020** | ReporterName / System.CreatedBy.displayName | Bug | نام نمایش‌داده‌شونده گزارشگر؛ مناسب برای جداول جزئیات و متریک‌های Top Reporters |
| **F-BUG-021** | AssigneeID / System.AssignedTo.id | Bug | شناسه کاربری فرد مسئول رفع باگ؛ پایه متریک‌های بهره‌وری و توزیع بار کاری |
| **F-BUG-022** | AssigneeName / System.AssignedTo.displayName | Bug | نام مسئول فعلی باگ برای نمایش در جدول‌ها، کارت‌ها و تحلیل عملکرد هر نفر |
| **F-BUG-023** | VerifierID (Custom) | Bug | شناسه فردی که رفع باگ را تایید می‌کند؛ برای تحلیل کیفیت تست/تایید و تفکیک نقش‌ها |
| **F-BUG-024** | VerifierName (Custom) | Bug | نام تاییدکننده نهایی؛ قابل استفاده در گزارش‌های QA و متریک‌های قبول/رد رفع باگ |
| **F-BUG-025** | ResolverID (Custom) | Bug | شناسه فردی که عملاً باگ را رفع کرده؛ برای سنجش بهره‌وری و نرخ موفقیت رفع |
| **F-BUG-026** | ResolverName (Custom) | Bug | نام حل‌کننده اصلی باگ؛ برای Leaderboard توسعه‌دهندگان و تحلیل کیفی روی افراد |

### گروه Date (تاریخ)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-027** | CreatedDate / System.CreatedDate | Bug | تاریخ ایجاد اولیه باگ؛ مبنای سن باگ، Lead Time و تمام تحلیل‌های زمانی |
| **F-BUG-028** | AssignedDate | Bug | زمانی که باگ به فردی Assign شده؛ پایه محاسبه Response Time |
| **F-BUG-029** | StartedDate | Bug | شروع واقعی کار روی باگ (ورود به In Progress)؛ مبنای Cycle Time از شروع تا رفع |
| **F-BUG-030** | ResolvedDate | Bug | تاریخی که باگ به وضعیت Resolved می‌رسد؛ برای سنجش زمان رفع و تحلیل SLA |
| **F-BUG-031** | VerifiedDate | Bug | تاریخی که تیم QA/Verifier رفع را تایید می‌کند؛ برای جداسازی زمان رفع از زمان تایید |
| **F-BUG-032** | ClosedDate / Microsoft.VSTS.Common.ClosedDate | Bug | زمان بسته‌شدن نهایی باگ؛ انتهای Lead Time و معیار اصلی در متریک‌های زمان حل |
| **F-BUG-033** | DueDate | Bug | موعد تعهد شده برای رفع باگ؛ برای چک کردن On-time بودن و ساخت KPIهای SLA Deadline |
| **F-BUG-034** | FirstReopenDate | Bug | اولین باری که باگ بعد از بسته شدن دوباره باز شده؛ برای تحلیل کیفیت رفع اولیه |
| **F-BUG-035** | LastReopenDate | Bug | آخرین تاریخ بازگشایی؛ مفید برای دیدن آخرین چرخه شکست رفع و تحلیل باگ‌های دردسرساز |
| **F-BUG-036** | LastModifiedDate / System.ChangedDate | Bug | آخرین زمان تغییر هر فیلد در باگ؛ برای متریک DaysSinceLastUpdate و شناسایی باگ‌های راکد |

### گروه State Transition (انتقال وضعیت) - جدید

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-073** | TriageDate | Bug | تاریخ ورود به حالت Triage؛ برای محاسبه زمان صرف‌شده در Triage |
| **F-BUG-074** | InProgressDate | Bug | تاریخ ورود به حالت In Progress؛ برای محاسبه زمان توسعه فعال |
| **F-BUG-075** | ReadyForRetestDate | Bug | تاریخ ورود به حالت Ready for Retest؛ برای محاسبه زمان انتظار تست |
| **F-BUG-076** | DoneDate | Bug | تاریخ ورود به حالت Done؛ برای جداسازی Done از Closed |
| **F-BUG-077** | PreviousState | Bug | آخرین State قبل از State فعلی؛ برای تحلیل جریان و back-flow |
| **F-BUG-078** | StateTransitionCount | Bug | تعداد کل تغییرات State؛ برای شناسایی باگ‌های با جریان پیچیده |
| **F-BUG-079** | TriageDurationHrs | Bug | زمان صرف‌شده در Triage (ساعت)؛ KPI کلیدی برای کارایی Triage |
| **F-BUG-080** | InProgressDurationHrs | Bug | زمان صرف‌شده در In Progress (ساعت)؛ نشان‌دهنده زمان توسعه فعال |
| **F-BUG-081** | ReadyForRetestDurationHrs | Bug | زمان صرف‌شده در Ready for Retest (ساعت)؛ شناسایی تاخیر در تست |
| **F-BUG-082** | ActiveDurationHrs | Bug | زمان صرف‌شده در Active (ساعت)؛ برای تحلیل زمان انتظار قبل از شروع کار |
| **F-BUG-083** | StateHistory (JSON) | Bug | تاریخچه کامل تغییرات State با timestamp؛ منبع داده برای تحلیل جریان و Sankey |

### گروه Reopen (بازگشایی)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-037** | ReopenCount | Bug | تعداد دفعاتی که باگ پس از بسته‌شدن دوباره باز شده؛ شاخص کلیدی کیفیت رفع و پایداری |
| **F-BUG-038** | AssigneeChangeCount | Bug | تعداد تغییرات مجری؛ بالابودن این عدد نشانه handoff زیاد و ناکارایی در تخصیص |
| **F-BUG-039** | StateChangeCount | Bug | تعداد دفعات تغییر State؛ برای درک پیچیدگی جریان کار و رفت‌وبرگشت‌های زیاد در فرایند |
| **F-BUG-041** | FixAttempts | Bug | تعداد تلاش‌های ثبت‌شده برای رفع؛ با ReopenCount ترکیب می‌شود تا First Time Fix Rate محاسبه شود |

### گروه Effort (تلاش)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-042** | AnalysisEffortHrs | Bug | مجموع ساعت‌های تحلیل/Investigate مرتبط با باگ؛ برای برآورد هزینه تحلیل نقص |
| **F-BUG-043** | DevEffortHrs | Bug | Effort توسعه روی این باگ؛ ورودی تحلیل بار توسعه‌ای باگ‌ها |
| **F-BUG-044** | FixEffortHrs | Bug | Effort صرف‌شده فقط برای فعالیت‌های Fix/Hotfix؛ مناسب برای سنجش هزینه رفع نقص |
| **F-BUG-045** | TestEffortHrs | Bug | ساعت‌های تست/QA انجام‌شده برای این باگ؛ برای اندازه‌گیری ظرفیت تست صرف‌شده روی باگ‌ها |
| **F-BUG-046** | ReopenEffortHrs | Bug | Effort اضافی پس از Reopen؛ نشان‌دهنده هزینه پنهان کیفیت پایین رفع اولیه |
| **F-BUG-047** | TotalEffortHrs | Bug | مجموع Effort همه دسته‌ها روی این باگ؛ برای محاسبه میانگین هزینه هر باگ |
| **F-BUG-048** | EstimatedEffortHrs | Bug | مجموع تخمین اولیه ساعت‌ها؛ مبنای مقایسه برنامه‌ریزی‌شده در برابر کار واقعی |

### گروه Time Calc (محاسبات زمانی)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-049** | LeadTimeHrs | Bug | زمان کل از ایجاد تا بسته‌شدن؛ KPI اصلی سرعت پاسخگویی/رفع باگ در سطح فرآیند |
| **F-BUG-050** | CycleTimeHrs | Bug | زمان از شروع کار تا رفع/بستن؛ نشان‌دهنده سرعت اجرای واقعی وقتی کار شروع شده |
| **F-BUG-051** | ResponseTimeHrs | Bug | زمان بین ایجاد تا اولین Assign؛ برای اندازه‌گیری سرعت واکنش تیم به باگ‌های جدید |
| **F-BUG-052** | WaitTimeHrs | Bug | برآورد زمان‌های انتظار در چرخه باگ؛ ورودی محاسبه Flow Efficiency |
| **F-BUG-053** | ActiveWorkTimeHrs | Bug | زمان فعال واقعی کار روی باگ؛ برای تحلیل بهره‌وری جریان و شناسایی گلوگاه‌ها |
| **F-BUG-054** | AgeDays | Bug | سن فعلی باگ به روز؛ برای Aging Buckets و پیدا کردن باگ‌های قدیمی و ریسک‌دار |

### گروه Quality (کیفیت)

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-BUG-060** | RootCause | Bug | ریشه اصلی مشکل (Design، Coding، Config، Data، Testing)؛ ورودی تحلیل علت‌العلل |
| **F-BUG-061** | Resolution | Bug | نحوه رفع باگ (Fixed، Won't Fix، Duplicate، As Designed، Cannot Reproduce)؛ برای کیفیت تصمیم‌گیری |
| **F-BUG-084** | CloseReason | Bug | دلیل دقیق بسته شدن (By Design، Cannot Reproduce، Completed، Duplicate، Invalid، Obsolete، Won't Fix)؛ تحلیل دقیق‌تر از Resolution |
| **F-BUG-062** | TestCaseID | Bug | شناسه تست‌کیس مرتبط؛ کمک به ردیابی پوشش تست و تحلیل ضعف تست‌ها |
| **F-BUG-064** | IsDuplicate | Bug | پرچم تکراری بودن؛ برای اندازه‌گیری نویز در گزارش باگ و کار اضافه روی موارد تکراری |
| **F-BUG-065** | DuplicateOfBugID | Bug | شناسه باگ اصلی که این باگ به آن لینک شده؛ برای ادغام آمار Duplicateها |
| **F-BUG-085** | RetestPassCount | Bug | تعداد دفعاتی که باگ در Retest قبول شده؛ برای محاسبه Retest Pass Rate |
| **F-BUG-086** | RetestFailCount | Bug | تعداد دفعاتی که باگ در Retest رد شده؛ برای شناسایی باگ‌های مشکل‌دار در تست |

### فیلدهای Task

| ID | فیلد | منبع | توضیح |
|----|------|------|-------|
| **F-TASK-001** | System.Id | Task | شناسه یکتای هر Task؛ برای تجمیع Effort و دیباگ جزئیات سطح Task |
| **F-TASK-002** | System.Parent | Task | شناسه Bug والد؛ کل اتصال Effort Taskها به باگ‌ها از این فیلد ساخته می‌شود |
| **F-TASK-003** | System.Title | Task | عنوان Task؛ برای نمایش در Drill-through و بررسی ریزفعالیت‌های انجام‌شده |
| **F-TASK-004** | System.State | Task | وضعیت Task (New/In Progress/Done)؛ برای دیدن وضعیت اجرای کارهای مرتبط با باگ |
| **F-TASK-005** | System.AssignedTo.displayName | Task | نام شخصی که Task به او Assign شده؛ ورودی اصلی تحلیل Effort و بار کاری در سطح فرد |
| **F-TASK-006** | System.Tags | Task | تگ‌های Task؛ منبع اصلی استخراج دسته Effort بر اساس Tag Mapping |
| **F-TASK-007** | Microsoft.VSTS.Scheduling.CompletedWork | Task | ساعات انجام‌شده روی Task؛ مبنای محاسبه Total/Dev/Test Effort هر باگ |
| **F-TASK-008** | Microsoft.VSTS.Scheduling.RemainingWork | Task | ساعت‌های باقی‌مانده تخمینی؛ برای تحلیل Work In Progress و پیش‌بینی اتمام کار |
| **F-TASK-009** | Microsoft.VSTS.Scheduling.OriginalEstimate | Task | تخمین اولیه Effort؛ برای مقایسه Estimate در برابر CompletedWork |
| **F-TASK-010** | System.CreatedDate | Task | تاریخ ایجاد Task؛ برای تحلیل زمان‌بندی کارهای فرزند نسبت به خود Bug |
| **F-TASK-011** | System.ChangedDate | Task | آخرین زمان تغییر Task؛ برای شناسایی Taskهای راکد یا قدیمی |
| **F-TASK-012** | EffortCategory (محاسبه‌شده) | Task | دسته‌بندی محاسبه‌شده Effort (Dev/Test/Analysis/Fix) بر اساس Tag/Title |

---

## موارد غیرفعال / مشروط

### فیلدهای Business

| ID | فیلد | دلیل | شرط فعال‌سازی |
|----|------|------|---------------|
| **F-BUG-059** | BusinessImpact | وابسته به Custom Field | تعریف فیلد سفارشی در Azure DevOps |
| **F-BUG-063** | CodeComplexity | نیاز به ابزار تحلیل استاتیک | ادغام با ابزار Code Analysis یا تعریف Custom Field |
| **F-BUG-066** | RiskScore | نیاز به مدل ML | پیاده‌سازی مدل ریسک یا تعریف Custom Field |
| **F-BUG-067** | RecurrenceProbability | نیاز به مدل پیش‌بینی | پیاده‌سازی مدل ML پیش‌بینی تکرار |
| **F-BUG-068** | EscapeProbability | نیاز به مدل پیش‌بینی | پیاده‌سازی مدل ML پیش‌بینی Escape |
| **F-BUG-069** | PredictedResolutionHrs | نیاز به مدل پیش‌بینی | پیاده‌سازی مدل ML برآورد زمان رفع |

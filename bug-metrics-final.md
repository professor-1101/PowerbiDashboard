# راهنمای متریک‌های باگ Azure DevOps

## متریک‌های معتبر و قابل استفاده

### گروه VOLUME (V01–V45)

```dax
V01_Total_Bugs = COUNTROWS('Bugs')
V02_Open_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Open", "Triage", "Active", "In Progress", "Ready for Retest"})
V03_Triage_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Triage")
V04_Active_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Active")
V05_InProgress_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "In Progress")
V06_ReadyForRetest_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Ready for Retest")
V07_Resolved_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Resolved")
V08_Done_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Done")
V09_Closed_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Closed")
V10_Reopened_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[ReopenCount] > 0)
V11_Multi_Reopened_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[ReopenCount] > 1)
V12_Escaped_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[is_escaped] = TRUE)
V13_Regression_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[IsRegression] = TRUE)
V14_Critical_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Severity] = "Critical")
V15_High_Severity_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Severity] = "High")
V16_Medium_Severity_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Severity] = "Medium")
V17_Low_Severity_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Severity] = "Low")
V18_P0_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Priority] = "P0")
V19_P1_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Priority] = "P1")
V20_P2_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Priority] = "P2")
V21_Blocking_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[IsBlocking] = TRUE)
V22_Customer_Reported_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[is_escaped] = TRUE)
V23_Security_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "Security")
V24_Performance_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "Performance")
V25_UI_UX_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "UI-UX")
V26_Functional_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "Functional")
V27_Data_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "Data")
V28_Bugs_by_Module = COUNTROWS('Bugs')
V29_Bugs_by_Sprint = COUNTROWS('Bugs')
V30_Bugs_by_Project = COUNTROWS('Bugs')
V31_Bugs_by_Team = COUNTROWS('Bugs')
V32_Bugs_by_Developer = COUNTROWS('Bugs')
V33_Bugs_by_Tester = COUNTROWS('Bugs')
V34_Bugs_by_Reporter = COUNTROWS('Bugs')
V35_Duplicate_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[IsDuplicate] = TRUE)
V36_Wont_Fix_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Won't Fix")
V37_Cannot_Reproduce_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Cannot Reproduce")
V38_Fixed_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Resolution] = "Fixed")
V39_Bugs_in_Production = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Tags] CONTAINS "Production")
V40_Bugs_in_QA = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Tags] CONTAINS "QA")
V41_Backlog_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] = "Open")
V42_Bug_Backlog_Size = [V41_Backlog_Bugs]
V43_Invalid_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Invalid")
V44_Obsolete_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Obsolete")
V45_Completed_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Completed")
```

**فیلدهای مرجع**: F-BUG-001, 004, 005, 006, 007, 009, 010, 011-018, 037, 061, 064, 070, 084

---

### گروه STATE FLOW (SF01–SF30) - جدید

```dax
SF01_Avg_Triage_Duration = AVERAGE('Bugs'[TriageDurationHrs])
SF02_Median_Triage_Duration = MEDIAN('Bugs'[TriageDurationHrs])
SF03_Max_Triage_Duration = MAX('Bugs'[TriageDurationHrs])
SF04_Bugs_Stuck_in_Triage = 
    CALCULATE(
        COUNTROWS('Bugs'), 
        'Bugs'[State] = "Triage",
        'Bugs'[TriageDurationHrs] > 24
    )
SF05_Avg_Active_Duration = AVERAGE('Bugs'[ActiveDurationHrs])
SF06_Avg_InProgress_Duration = AVERAGE('Bugs'[InProgressDurationHrs])
SF07_Median_InProgress_Duration = MEDIAN('Bugs'[InProgressDurationHrs])
SF08_Avg_ReadyForRetest_Duration = AVERAGE('Bugs'[ReadyForRetestDurationHrs])
SF09_Median_ReadyForRetest_Duration = MEDIAN('Bugs'[ReadyForRetestDurationHrs])
SF10_Bugs_Stuck_in_Retest = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[State] = "Ready for Retest",
        'Bugs'[ReadyForRetestDurationHrs] > 48
    )
SF11_State_Transition_Count_Avg = AVERAGE('Bugs'[StateTransitionCount])
SF12_Complex_Flow_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[StateTransitionCount] > 8)
SF13_Simple_Flow_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[StateTransitionCount] <= 4)
SF14_Triage_Efficiency = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[TriageDurationHrs] <= 4),
        CALCULATE(COUNTROWS('Bugs'), NOT(ISBLANK('Bugs'[TriageDurationHrs]))),
        0
    )
SF15_First_Time_Pass_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[RetestFailCount] = 0),
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Resolved", "Done", "Closed"}),
        0
    )
SF16_Retest_Pass_Rate = 
    DIVIDE(
        [V45_Completed_Bugs],
        [V45_Completed_Bugs] + CALCULATE(COUNTROWS('Bugs'), 'Bugs'[RetestFailCount] > 0),
        0
    )
SF17_Back_Flow_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[PreviousState] > 'Bugs'[State]),
        COUNTROWS('Bugs'),
        0
    )
SF18_Open_to_Triage_Time_Avg = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[TriageDate]))),
        DATEDIFF('Bugs'[CreatedDate], 'Bugs'[TriageDate], HOUR)
    )
SF19_Triage_to_Active_Time_Avg = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[TriageDate])) && 'Bugs'[State] != "Triage"),
        DATEDIFF('Bugs'[TriageDate], 'Bugs'[AssignedDate], HOUR)
    )
SF20_Active_to_InProgress_Time_Avg = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[InProgressDate]))),
        DATEDIFF('Bugs'[AssignedDate], 'Bugs'[InProgressDate], HOUR)
    )
SF21_InProgress_to_ReadyForRetest_Time_Avg = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[ReadyForRetestDate]))),
        DATEDIFF('Bugs'[InProgressDate], 'Bugs'[ReadyForRetestDate], HOUR)
    )
SF22_ReadyForRetest_to_Done_Time_Avg = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[DoneDate]))),
        DATEDIFF('Bugs'[ReadyForRetestDate], 'Bugs'[DoneDate], HOUR)
    )
SF23_Done_to_Closed_Time_Avg = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[ClosedDate])) && NOT(ISBLANK('Bugs'[DoneDate]))),
        DATEDIFF('Bugs'[DoneDate], 'Bugs'[ClosedDate], HOUR)
    )
SF24_Bottleneck_State = 
    VAR MaxDuration = MAX(
        {[SF01_Avg_Triage_Duration], [SF05_Avg_Active_Duration], 
         [SF06_Avg_InProgress_Duration], [SF08_Avg_ReadyForRetest_Duration]}
    )
    RETURN
    SWITCH(TRUE(),
        [SF01_Avg_Triage_Duration] = MaxDuration, "Triage",
        [SF05_Avg_Active_Duration] = MaxDuration, "Active",
        [SF06_Avg_InProgress_Duration] = MaxDuration, "In Progress",
        [SF08_Avg_ReadyForRetest_Duration] = MaxDuration, "Ready for Retest",
        "Unknown"
    )
SF25_Flow_Efficiency_State = 
    DIVIDE(
        [SF06_Avg_InProgress_Duration],
        [SF05_Avg_Active_Duration] + [SF06_Avg_InProgress_Duration] + [SF08_Avg_ReadyForRetest_Duration],
        0
    )
SF26_State_Change_Velocity = 
    DIVIDE(
        SUM('Bugs'[StateTransitionCount]),
        DISTINCTCOUNT('Bugs'[BugID]),
        0
    )
SF27_Bugs_by_Current_State = 
    CALCULATE(
        COUNTROWS('Bugs'),
        ALLEXCEPT('Bugs', 'Bugs'[State])
    )
SF28_State_Distribution_Pct = 
    DIVIDE(
        [SF27_Bugs_by_Current_State],
        [V01_Total_Bugs],
        0
    )
SF29_Critical_Bugs_in_Triage = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[State] = "Triage",
        'Bugs'[Severity] = "Critical"
    )
SF30_Avg_Time_to_Start_Work = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[InProgressDate]))),
        DATEDIFF('Bugs'[CreatedDate], 'Bugs'[InProgressDate], HOUR)
    )
```

**فیلدهای مرجع**: F-BUG-006, 027, 028, 029, 030, 032, 073-083, 085, 086

---

### گروه CLOSE REASON (CR01–CR15) - جدید

```dax
CR01_By_Design_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "By Design")
CR02_Cannot_Reproduce_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Cannot Reproduce")
CR03_Completed_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Completed")
CR04_Duplicate_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Duplicate")
CR05_Invalid_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Invalid")
CR06_Obsolete_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Obsolete")
CR07_Wont_Fix_Count = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[CloseReason] = "Won't Fix")
CR08_Close_Reason_Distribution = 
    DIVIDE(
        COUNTROWS('Bugs'),
        CALCULATE(COUNTROWS('Bugs'), ALL('Bugs'[CloseReason])),
        0
    )
CR09_Cannot_Reproduce_Rate = 
    DIVIDE(
        [CR02_Cannot_Reproduce_Count],
        [V09_Closed_Bugs],
        0
    )
CR10_Duplicate_Detection_Rate = 
    DIVIDE(
        [CR04_Duplicate_Count],
        [V09_Closed_Bugs],
        0
    )
CR11_Invalid_Report_Rate = 
    DIVIDE(
        [CR05_Invalid_Count],
        [V09_Closed_Bugs],
        0
    )
CR12_Successful_Completion_Rate = 
    DIVIDE(
        [CR03_Completed_Count],
        [V09_Closed_Bugs],
        0
    )
CR13_By_Design_Rate = 
    DIVIDE(
        [CR01_By_Design_Count],
        [V09_Closed_Bugs],
        0
    )
CR14_Wont_Fix_Rate = 
    DIVIDE(
        [CR07_Wont_Fix_Count],
        [V09_Closed_Bugs],
        0
    )
CR15_Actionable_Bugs_Rate = 
    DIVIDE(
        [CR03_Completed_Count],
        [V09_Closed_Bugs] - [CR04_Duplicate_Count] - [CR05_Invalid_Count],
        0
    )
```

**فیلدهای مرجع**: F-BUG-084, 006, 009

---

### گروه TIME & FLOW (T01–T40)

```dax
T01_Avg_Lead_Time = AVERAGE('Bugs'[LeadTimeHrs])
T02_Median_Lead_Time = MEDIAN('Bugs'[LeadTimeHrs])
T03_Avg_Cycle_Time = AVERAGE('Bugs'[CycleTimeHrs])
T04_Median_Cycle_Time = MEDIAN('Bugs'[CycleTimeHrs])
T05_P75_Cycle_Time = PERCENTILEX.INC('Bugs', 'Bugs'[CycleTimeHrs], 0.75)
T06_P90_Cycle_Time = PERCENTILEX.INC('Bugs', 'Bugs'[CycleTimeHrs], 0.90)
T07_P95_Lead_Time = PERCENTILEX.INC('Bugs', 'Bugs'[LeadTimeHrs], 0.95)
T08_Max_Lead_Time = MAX('Bugs'[LeadTimeHrs])
T09_Max_Cycle_Time = MAX('Bugs'[CycleTimeHrs])
T10_Min_Lead_Time = MIN('Bugs'[LeadTimeHrs])
T11_Avg_Resolution_Time = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[ResolvedDate]))),
        DATEDIFF('Bugs'[CreatedDate], 'Bugs'[ResolvedDate], HOUR)
    )
T12_Avg_Close_Time = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[ClosedDate]))),
        DATEDIFF('Bugs'[CreatedDate], 'Bugs'[ClosedDate], HOUR)
    )
T13_Avg_Response_Time = AVERAGE('Bugs'[ResponseTimeHrs])
T14_Avg_Fix_Time = AVERAGE('Bugs'[FixEffortHrs])
T15_Avg_Verification_Time = 
    AVERAGEX(
        FILTER('Bugs', NOT(ISBLANK('Bugs'[VerifiedDate])) && NOT(ISBLANK('Bugs'[ResolvedDate]))),
        DATEDIFF('Bugs'[ResolvedDate], 'Bugs'[VerifiedDate], HOUR)
    )
T16_Avg_Wait_Time = AVERAGE('Bugs'[WaitTimeHrs])
T17_Avg_Active_Work_Time = AVERAGE('Bugs'[ActiveWorkTimeHrs])
T18_Avg_Age_Days = AVERAGE('Bugs'[AgeDays])
T19_Bugs_Aging_7Days = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[AgeDays] > 7)
T20_Bugs_Aging_14Days = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[AgeDays] > 14)
T21_Bugs_Aging_30Days = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[AgeDays] > 30)
T22_Bugs_Aging_60Days = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[AgeDays] > 60)
T23_Bugs_Aging_90Days = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[AgeDays] > 90)
T27_Avg_Reopen_Time = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[ReopenCount] > 0),
        DATEDIFF('Bugs'[ClosedDate], 'Bugs'[FirstReopenDate], HOUR)
    )
T28_Time_in_Backlog_Avg = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[State] = "Open"),
        DATEDIFF('Bugs'[CreatedDate], TODAY(), DAY)
    )
T29_Flow_Efficiency = 
    DIVIDE(
        [T17_Avg_Active_Work_Time],
        [T01_Avg_Lead_Time],
        0
    )
T37_Avg_Days_Since_Last_Update = 
    AVERAGEX(
        'Bugs',
        DATEDIFF('Bugs'[LastModifiedDate], TODAY(), DAY)
    )
T38_Stale_Bugs = CALCULATE(COUNTROWS('Bugs'), DATEDIFF('Bugs'[LastModifiedDate], TODAY(), DAY) > 30)
T39_Recently_Updated_Bugs = CALCULATE(COUNTROWS('Bugs'), DATEDIFF('Bugs'[LastModifiedDate], TODAY(), DAY) <= 7)
```

**فیلدهای مرجع**: F-BUG-027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 049-054

---

### گروه EFFORT (E01–E26)

```dax
E01_Total_Effort = SUM('Bugs'[TotalEffortHrs])
E02_Avg_Effort_per_Bug = AVERAGE('Bugs'[TotalEffortHrs])
E03_Median_Effort_per_Bug = MEDIAN('Bugs'[TotalEffortHrs])
E04_Total_Dev_Effort = SUM('Bugs'[DevEffortHrs])
E05_Total_Test_Effort = SUM('Bugs'[TestEffortHrs])
E06_Total_Analysis_Effort = SUM('Bugs'[AnalysisEffortHrs])
E07_Total_Fix_Effort = SUM('Bugs'[FixEffortHrs])
E08_Total_Reopen_Effort = SUM('Bugs'[ReopenEffortHrs])
E09_Avg_Dev_Effort = AVERAGE('Bugs'[DevEffortHrs])
E10_Avg_Test_Effort = AVERAGE('Bugs'[TestEffortHrs])
E11_Avg_Analysis_Effort = AVERAGE('Bugs'[AnalysisEffortHrs])
E12_Avg_Fix_Effort = AVERAGE('Bugs'[FixEffortHrs])
E13_Dev_Effort_Pct = DIVIDE([E04_Total_Dev_Effort], [E01_Total_Effort], 0)
E14_Test_Effort_Pct = DIVIDE([E05_Total_Test_Effort], [E01_Total_Effort], 0)
E15_Analysis_Effort_Pct = DIVIDE([E06_Total_Analysis_Effort], [E01_Total_Effort], 0)
E16_Fix_Effort_Pct = DIVIDE([E07_Total_Fix_Effort], [E01_Total_Effort], 0)
E17_Reopen_Effort_Pct = DIVIDE([E08_Total_Reopen_Effort], [E01_Total_Effort], 0)
E18_Critical_Bugs_Effort = 
    CALCULATE(
        SUM('Bugs'[TotalEffortHrs]),
        'Bugs'[Severity] = "Critical"
    )
E19_High_Bugs_Effort = 
    CALCULATE(
        SUM('Bugs'[TotalEffortHrs]),
        'Bugs'[Severity] = "High"
    )
E20_Escaped_Bugs_Effort = 
    CALCULATE(
        SUM('Bugs'[TotalEffortHrs]),
        'Bugs'[is_escaped] = TRUE
    )
E21_Effort_Variance = 
    AVERAGEX(
        'Bugs',
        'Bugs'[TotalEffortHrs] - 'Bugs'[EstimatedEffortHrs]
    )
E22_Effort_Variance_Pct = 
    DIVIDE(
        [E21_Effort_Variance],
        AVERAGE('Bugs'[EstimatedEffortHrs]),
        0
    )
E23_Estimate_Accuracy = 1 - ABS([E22_Effort_Variance_Pct])
E24_Effort_per_Severity_Critical = 
    DIVIDE(
        [E18_Critical_Bugs_Effort],
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Severity] = "Critical"),
        0
    )
E25_Effort_per_Severity_High = 
    DIVIDE(
        [E19_High_Bugs_Effort],
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Severity] = "High"),
        0
    )
E26_Wasted_Effort_Reopen = [E08_Total_Reopen_Effort]
```

**فیلدهای مرجع**: F-BUG-004, 010, 042-048, F-TASK-007

---

### گروه QUALITY (Q01–Q35)

```dax
Q01_Escape_Rate = DIVIDE([V12_Escaped_Bugs], [V01_Total_Bugs], 0)
Q02_Regression_Rate = DIVIDE([V13_Regression_Bugs], [V01_Total_Bugs], 0)
Q03_Reopen_Rate = DIVIDE([V10_Reopened_Bugs], [V09_Closed_Bugs], 0)
Q04_Multi_Reopen_Rate = DIVIDE([V11_Multi_Reopened_Bugs], [V09_Closed_Bugs], 0)
Q05_Fix_Success_Rate = 1 - [Q03_Reopen_Rate]
Q06_First_Time_Fix_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[FixAttempts] = 1),
        CALCULATE(COUNTROWS('Bugs'), NOT(ISBLANK('Bugs'[FixAttempts]))),
        0
    )
Q07_Duplicate_Rate = DIVIDE([V35_Duplicate_Bugs], [V01_Total_Bugs], 0)
Q08_Critical_Severity_Pct = DIVIDE([V14_Critical_Bugs], [V01_Total_Bugs], 0)
Q09_High_Severity_Pct = DIVIDE([V15_High_Severity_Bugs], [V01_Total_Bugs], 0)
Q10_Defect_Detection_Effectiveness_DDE = 
    DIVIDE(
        [V01_Total_Bugs] - [V12_Escaped_Bugs],
        [V01_Total_Bugs],
        0
    )
Q11_Defect_Removal_Efficiency_DRE = [Q10_Defect_Detection_Effectiveness_DDE]
Q12_Testing_Effectiveness = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Resolved", "Done", "Closed"}),
        [V01_Total_Bugs],
        0
    )
Q13_Quality_Index = 
    ([Q05_Fix_Success_Rate] * 0.4) + 
    ([Q10_Defect_Detection_Effectiveness_DDE] * 0.3) +
    ((1 - [Q01_Escape_Rate]) * 0.3)
Q14_Bug_Density = 
    DIVIDE(
        [V01_Total_Bugs],
        1000,
        0
    )
Q15_Critical_Bug_Density = 
    DIVIDE(
        [V14_Critical_Bugs],
        1000,
        0
    )
Q16_Security_Bug_Pct = DIVIDE([V23_Security_Bugs], [V01_Total_Bugs], 0)
Q17_Performance_Bug_Pct = DIVIDE([V24_Performance_Bugs], [V01_Total_Bugs], 0)
Q18_Regression_Leak_Rate = 
    DIVIDE(
        [V13_Regression_Bugs],
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Resolved", "Done", "Closed"}),
        0
    )
Q19_Root_Cause_Analysis_Completion = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), NOT(ISBLANK('Bugs'[RootCause]))),
        [V01_Total_Bugs],
        0
    )
Q20_Bug_Leakage_Ratio = 
    DIVIDE(
        [V12_Escaped_Bugs],
        [V01_Total_Bugs] - [V12_Escaped_Bugs],
        0
    )
Q28_Test_Case_Coverage = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), NOT(ISBLANK('Bugs'[TestCaseID]))),
        [V01_Total_Bugs],
        0
    )
Q29_Avg_Reopen_Count = AVERAGE('Bugs'[ReopenCount])
```

**فیلدهای مرجع**: F-BUG-004, 006, 010, 037, 041, 060, 061, 062, 064

---

### گروه PEOPLE (P01–P30)

```dax
P01_Bugs_per_Developer = 
    DIVIDE(
        COUNTROWS('Bugs'),
        DISTINCTCOUNT('Bugs'[AssigneeName]),
        0
    )
P02_Avg_Resolution_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Resolved", "Done", "Closed"}),
        DISTINCTCOUNT('Bugs'[AssigneeName]),
        0
    )
P03_Reopen_Rate_by_Developer = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[ReopenCount] > 0),
        COUNTROWS('Bugs'),
        0
    )
P04_Avg_Fix_Time_by_Developer = AVERAGE('Bugs'[FixEffortHrs])
P05_Developer_Workload_Hours = SUM('Bugs'[TotalEffortHrs])
P06_Developer_Efficiency = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Resolved", "Done", "Closed"}),
        [P05_Developer_Workload_Hours],
        0
    )
P07_Top_Performer_Score = 
    ([P06_Developer_Efficiency] * 0.4) +
    ((1 - [P03_Reopen_Rate_by_Developer]) * 0.3) +
    ([P02_Avg_Resolution_Rate] * 0.3)
P15_Reporter_Accuracy = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[IsDuplicate] = FALSE && 'Bugs'[CloseReason] != "Invalid"),
        COUNTROWS('Bugs'),
        0
    )
P16_Verifier_Rejection_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[RetestFailCount] > 0),
        CALCULATE(COUNTROWS('Bugs'), NOT(ISBLANK('Bugs'[VerifierName]))),
        0
    )
P18_Bugs_per_Team = 
    DIVIDE(
        COUNTROWS('Bugs'),
        DISTINCTCOUNT('Bugs'[TeamName]),
        0
    )
P19_Team_Avg_Lead_Time = [T01_Avg_Lead_Time]
P25_Team_Quality_Score = 
    ([Q05_Fix_Success_Rate] * 0.35) +
    ((1 - [Q01_Escape_Rate]) * 0.35) +
    ([Q12_Testing_Effectiveness] * 0.30)
```

**فیلدهای مرجع**: F-BUG-014, 019, 020, 021, 022, 023, 024, 025, 026, 037, 044, 047, 064, 086

---

### گروه SPRINT (S01–S30)

```dax
S01_Sprint_Velocity = COUNTROWS('Bugs')
S02_Sprint_Completed_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[State] IN {"Resolved", "Done", "Closed"}
    )
S03_Sprint_Carryover = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[State] NOT IN {"Resolved", "Done", "Closed"}
    )
S04_Sprint_Carryover_Rate = DIVIDE([S03_Sprint_Carryover], [S01_Sprint_Velocity], 0)
S05_Sprint_Completion_Rate = DIVIDE([S02_Sprint_Completed_Bugs], [S01_Sprint_Velocity], 0)
S06_Sprint_Avg_Cycle_Time = [T03_Avg_Cycle_Time]
S09_Sprint_Inflow = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[CreatedDate] >= EARLIER('Sprint'[StartDate]) &&
        'Bugs'[CreatedDate] <= EARLIER('Sprint'[EndDate])
    )
S10_Sprint_Outflow = [S02_Sprint_Completed_Bugs]
S11_Sprint_WIP = [S03_Sprint_Carryover]
S12_Sprint_Scope_Change = 
    ABS([S09_Sprint_Inflow] - [S01_Sprint_Velocity])
S13_Sprint_Scope_Stability = 
    DIVIDE(
        [S01_Sprint_Velocity] - [S12_Sprint_Scope_Change],
        [S01_Sprint_Velocity],
        0
    )
S14_Sprint_Throughput = [S02_Sprint_Completed_Bugs]
S15_Sprint_Avg_Lead_Time = [T01_Avg_Lead_Time]
S16_Sprint_Commitment_Reliability = [S05_Sprint_Completion_Rate]
S17_Sprint_Quality_Index = [Q13_Quality_Index]
S26_Sprint_Bug_Density = [Q14_Bug_Density]
```

**فیلدهای مرجع**: F-BUG-006, 010, 017, 018, 027, 032, 049, 050, 070

---

### گروه PROJECT (J01–J20)

```dax
J01_Project_Total_Bugs = [V01_Total_Bugs]
J02_Project_Bug_Density = [Q14_Bug_Density]
J03_Project_Defect_Density = [J02_Project_Bug_Density]
J04_Project_Critical_Bug_Density = [Q15_Critical_Bug_Density]
J05_Project_Escape_Rate = [Q01_Escape_Rate]
J06_Project_Reopen_Rate = [Q03_Reopen_Rate]
J07_Project_Quality_Index = [Q13_Quality_Index]
J08_Project_Avg_Lead_Time = [T01_Avg_Lead_Time]
J09_Project_Avg_Cycle_Time = [T03_Avg_Cycle_Time]
J10_Project_Total_Effort = [E01_Total_Effort]
J11_Project_Schedule_Variance = 
    AVERAGEX(
        'Bugs',
        DATEDIFF('Bugs'[DueDate], 'Bugs'[ClosedDate], DAY)
    )
J12_Project_Cost_Variance = [E21_Effort_Variance]
J13_Project_On_Time_Delivery_Rate = 
    DIVIDE(
        CALCULATE(
            COUNTROWS('Bugs'),
            'Bugs'[ClosedDate] <= 'Bugs'[DueDate]
        ),
        CALCULATE(COUNTROWS('Bugs'), NOT(ISBLANK('Bugs'[DueDate]))),
        0
    )
J14_Project_Escaped_Bugs = [V12_Escaped_Bugs]
J15_Project_Regression_Bugs = [V13_Regression_Bugs]
J16_Project_Health_Score = 
    ([J07_Project_Quality_Index] * 0.4) +
    ([J13_Project_On_Time_Delivery_Rate] * 0.3) +
    ((1 - [J05_Project_Escape_Rate]) * 0.3)
J17_Project_Productivity = 
    DIVIDE(
        [S02_Sprint_Completed_Bugs],
        [J10_Project_Total_Effort],
        0
    )
J18_Project_Cost_of_Quality = [E08_Total_Reopen_Effort] + [E20_Escaped_Bugs_Effort]
J19_Project_Rework_Rate = DIVIDE([E08_Total_Reopen_Effort], [E01_Total_Effort], 0)
J20_Project_First_Time_Quality = 1 - [J19_Project_Rework_Rate]
```

**فیلدهای مرجع**: F-BUG-001, 004, 006, 010, 011, 012, 027, 032, 033, 047, 049, 050

---

### گروه BUSINESS IMPACT (B03–B25) - Conditional

```dax
B03_Revenue_at_Risk = SUM('Bugs'[BusinessImpact])
B04_Avg_Revenue_Impact_per_Bug = AVERAGE('Bugs'[BusinessImpact])
B05_High_Impact_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[BusinessImpact] > 10000)
B09_Security_Risk_Level = 
    SWITCH(TRUE(),
        [V23_Security_Bugs] > 10, "High",
        [V23_Security_Bugs] > 5, "Medium",
        "Low"
    )
B10_Compliance_Risk_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "Compliance")
B11_Data_Loss_Risk_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Category] = "Data Loss")
B12_Critical_Business_Impact_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[Severity] = "Critical",
        'Bugs'[BusinessImpact] > 0
    )
B13_Cost_of_Poor_Quality = [J18_Project_Cost_of_Quality]
B14_Avg_Impact_by_Severity = 
    AVERAGEX(
        VALUES('Bugs'[Severity]),
        CALCULATE(AVERAGE('Bugs'[BusinessImpact]))
    )
B15_Total_Business_Impact = SUM('Bugs'[BusinessImpact])
B16_Impact_per_Module = 
    AVERAGEX(
        VALUES('Bugs'[ModuleName]),
        CALCULATE(SUM('Bugs'[BusinessImpact]))
    )
B17_High_Severity_Impact = 
    CALCULATE(
        SUM('Bugs'[BusinessImpact]),
        'Bugs'[Severity] IN {"Critical", "High"}
    )
B18_Production_Bug_Impact = 
    CALCULATE(
        SUM('Bugs'[BusinessImpact]),
        'Bugs'[Tags] CONTAINS "Production"
    )
B19_Escaped_Bug_Impact = 
    CALCULATE(
        SUM('Bugs'[BusinessImpact]),
        'Bugs'[is_escaped] = TRUE
    )
B20_Impact_Risk_Score = 
    ([B15_Total_Business_Impact] * 0.4) +
    ([B19_Escaped_Bug_Impact] * 0.35) +
    ([B17_High_Severity_Impact] * 0.25)
B21_Avg_Resolution_Cost = AVERAGE('Bugs'[TotalEffortHrs]) * 100
B22_Security_Bug_Impact = 
    CALCULATE(
        SUM('Bugs'[BusinessImpact]),
        'Bugs'[Category] = "Security"
    )
B23_Performance_Bug_Impact = 
    CALCULATE(
        SUM('Bugs'[BusinessImpact]),
        'Bugs'[Category] = "Performance"
    )
B24_Compliance_Cost = 
    CALCULATE(
        SUM('Bugs'[TotalEffortHrs]),
        'Bugs'[Category] = "Compliance"
    ) * 100
B25_Revenue_Impact_by_Priority = 
    CALCULATE(
        SUM('Bugs'[BusinessImpact]),
        ALLEXCEPT('Bugs', 'Bugs'[Priority])
    )
```

**فیلدهای مرجع**: F-BUG-004, 005, 006, 007, 010, 016, 047, 059, 070

---

### گروه RISK & PREDICTIONS (R01–R25) - Conditional

```dax
R01_Overall_Risk_Score = AVERAGE('Bugs'[RiskScore])
R02_High_Risk_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[RiskScore] > 7)
R03_Medium_Risk_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[RiskScore] >= 4 && 'Bugs'[RiskScore] <= 7)
R04_Low_Risk_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[RiskScore] < 4)
R05_Risk_Distribution = 
    DIVIDE(
        COUNTROWS('Bugs'),
        CALCULATE(COUNTROWS('Bugs'), ALL('Bugs'[RiskScore])),
        0
    )
R06_Critical_Risk_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[RiskScore] > 8,
        'Bugs'[Severity] = "Critical"
    )
R07_Predicted_Escapes = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[EscapeProbability] > 0.7
    )
R08_Predicted_Reopens = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[RecurrenceProbability] > 0.5
    )
R09_Risk_Adjusted_Backlog = 
    SUMX(
        FILTER('Bugs', 'Bugs'[State] = "Open"),
        'Bugs'[RiskScore]
    )
R11_Escape_Prediction_Accuracy = 
    VAR ActualEscapes = [V12_Escaped_Bugs]
    VAR PredictedEscapes = [R07_Predicted_Escapes]
    RETURN DIVIDE(ABS(ActualEscapes - PredictedEscapes), ActualEscapes, 0)
R12_Module_Risk_Score = 
    AVERAGEX(
        VALUES('Bugs'[ModuleName]),
        CALCULATE(AVERAGE('Bugs'[RiskScore]))
    )
R13_Team_Risk_Score = 
    AVERAGEX(
        VALUES('Bugs'[TeamName]),
        CALCULATE(AVERAGE('Bugs'[RiskScore]))
    )
R15_Risk_Trend = 
    VAR CurrentRisk = [R01_Overall_Risk_Score]
    VAR PreviousRisk = CALCULATE([R01_Overall_Risk_Score], DATEADD('Date'[Date], -1, MONTH))
    RETURN CurrentRisk - PreviousRisk
R16_High_Risk_Critical_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[RiskScore] > 7,
        'Bugs'[Severity] = "Critical"
    )
R17_Risk_Velocity = 
    DIVIDE(
        [R16_High_Risk_Critical_Bugs],
        [V01_Total_Bugs],
        0
    )
R18_Predicted_Resolution_Accuracy = 
    VAR ActualResolutionTime = [T11_Avg_Resolution_Time]
    VAR PredictedResolutionTime = AVERAGE('Bugs'[PredictedResolutionHrs])
    RETURN DIVIDE(ABS(ActualResolutionTime - PredictedResolutionTime), ActualResolutionTime, 0)
R19_Anomaly_Bugs = CALCULATE(COUNTROWS('Bugs'), 'Bugs'[IsAnomaly] = TRUE)
R20_Release_Risk_Score = 
    ([R01_Overall_Risk_Score] * 0.3) +
    ([V14_Critical_Bugs] * 0.25) +
    ([V12_Escaped_Bugs] * 0.25) +
    ([T18_Avg_Age_Days] * 0.20)
R21_Time_to_Risk_Threshold = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[RiskScore] > 7),
        'Bugs'[AgeDays]
    )
R22_Sprint_Risk_Forecast = 
    VAR CurrentVelocity = [S01_Sprint_Velocity]
    VAR RiskFactor = [R01_Overall_Risk_Score] / 10
    RETURN CurrentVelocity * (1 - RiskFactor)
R23_Predicted_Bugs_Next_Sprint = 
    VAR AvgBugsPerSprint = AVERAGEX(VALUES('Sprint'[SprintID]), [S09_Sprint_Inflow])
    VAR Trend = [TR04_Bug_Trend_7Days]
    RETURN AvgBugsPerSprint * (1 + Trend)
R24_Risk_Burndown_Rate = 
    DIVIDE(
        [R02_High_Risk_Bugs],
        CALCULATE([R02_High_Risk_Bugs], DATEADD('Date'[Date], -7, DAY)),
        0
    ) - 1
R25_Critical_Path_Risk = 
    CALCULATE(
        SUM('Bugs'[RiskScore]),
        'Bugs'[IsBlocking] = TRUE
    )
```

**فیلدهای مرجع**: F-BUG-004, 006, 054, 066, 067, 068, 069

---

### گروه CUSTOMER SATISFACTION (C01–C20) - Conditional

```dax
C01_Customer_Reported_Bugs = [V22_Customer_Reported_Bugs]
C02_Customer_Bug_Rate = DIVIDE([C01_Customer_Reported_Bugs], [V01_Total_Bugs], 0)
C03_Avg_Customer_Response_Time = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[is_escaped] = TRUE),
        'Bugs'[ResponseTimeHrs]
    )
C04_Avg_Customer_Resolution_Time = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[is_escaped] = TRUE),
        'Bugs'[LeadTimeHrs]
    )
C05_Customer_Critical_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[is_escaped] = TRUE,
        'Bugs'[Severity] = "Critical"
    )
C06_Customer_High_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[is_escaped] = TRUE,
        'Bugs'[Severity] = "High"
    )
C07_Customer_Satisfaction_Index = 
    1 - ([C02_Customer_Bug_Rate] * 0.4 + [Q01_Escape_Rate] * 0.6)
C08_Customer_Impact_Score = 
    ([C05_Customer_Critical_Bugs] * 10) +
    ([C06_Customer_High_Bugs] * 5) +
    ([C01_Customer_Reported_Bugs] * 1)
C09_SLA_Compliance_Rate = 
    DIVIDE(
        CALCULATE(
            COUNTROWS('Bugs'),
            'Bugs'[ClosedDate] <= 'Bugs'[DueDate],
            'Bugs'[is_escaped] = TRUE
        ),
        [C01_Customer_Reported_Bugs],
        0
    )
C10_Customer_Reopen_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[ReopenCount] > 0, 'Bugs'[is_escaped] = TRUE),
        [C01_Customer_Reported_Bugs],
        0
    )
C11_Avg_Customer_Effort = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[is_escaped] = TRUE),
        'Bugs'[TotalEffortHrs]
    )
C12_Customer_Escalation_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[Priority] = "P0", 'Bugs'[is_escaped] = TRUE),
        [C01_Customer_Reported_Bugs],
        0
    )
C14_Customer_Experience_Score = 
    ([C07_Customer_Satisfaction_Index] * 0.4) +
    ((1 - [C10_Customer_Reopen_Rate]) * 0.3) +
    ([C09_SLA_Compliance_Rate] * 0.3)
C16_Escaped_Bug_Fix_Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS('Bugs'), 'Bugs'[State] IN {"Resolved", "Done", "Closed"}, 'Bugs'[is_escaped] = TRUE),
        [C01_Customer_Reported_Bugs],
        0
    )
C17_Customer_Waiting_Bugs = 
    CALCULATE(
        COUNTROWS('Bugs'),
        'Bugs'[State] NOT IN {"Resolved", "Done", "Closed"},
        'Bugs'[is_escaped] = TRUE
    )
C18_Avg_Customer_Wait_Time = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[is_escaped] = TRUE),
        'Bugs'[WaitTimeHrs]
    )
C19_Customer_Bug_Trend = 
    VAR CurrentMonth = [C01_Customer_Reported_Bugs]
    VAR PreviousMonth = CALCULATE([C01_Customer_Reported_Bugs], DATEADD('Date'[Date], -1, MONTH))
    RETURN DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth, 0)
C20_Customer_Priority_Response = 
    AVERAGEX(
        FILTER('Bugs', 'Bugs'[is_escaped] = TRUE && 'Bugs'[Priority] = "P0"),
        'Bugs'[ResponseTimeHrs]
    )
```

**فیلدهای مرجع**: F-BUG-005, 006, 010, 027, 032, 033, 037, 047, 049, 051, 052

---

### گروه TRENDS (TR01–TR15)

```dax
TR01_Bug_Trend_30Days = 
    VAR Current = [V01_Total_Bugs]
    VAR Previous = CALCULATE([V01_Total_Bugs], DATEADD('Date'[Date], -30, DAY))
    RETURN DIVIDE(Current - Previous, Previous, 0)
TR02_Quality_Trend_Index = 
    VAR CurrentQuality = [Q13_Quality_Index]
    VAR PreviousQuality = CALCULATE([Q13_Quality_Index], DATEADD('Date'[Date], -1, MONTH))
    RETURN CurrentQuality - PreviousQuality
TR03_Escape_Rate_Trend = 
    VAR Current = [Q01_Escape_Rate]
    VAR Previous = CALCULATE([Q01_Escape_Rate], DATEADD('Date'[Date], -1, MONTH))
    RETURN Current - Previous
TR04_Bug_Trend_7Days = 
    VAR Current = [V01_Total_Bugs]
    VAR Previous = CALCULATE([V01_Total_Bugs], DATEADD('Date'[Date], -7, DAY))
    RETURN DIVIDE(Current - Previous, Previous, 0)
TR05_Moving_Avg_Bugs_7Days = 
    CALCULATE(
        AVERAGEX(
            DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -7, DAY),
            [V01_Total_Bugs]
        )
    )
TR06_Moving_Avg_Bugs_30Days = 
    CALCULATE(
        AVERAGEX(
            DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -30, DAY),
            [V01_Total_Bugs]
        )
    )
TR07_Critical_Bug_Trend = 
    VAR Current = [V14_Critical_Bugs]
    VAR Previous = CALCULATE([V14_Critical_Bugs], DATEADD('Date'[Date], -1, MONTH))
    RETURN DIVIDE(Current - Previous, Previous, 0)
TR08_Reopen_Rate_Trend = 
    VAR Current = [Q03_Reopen_Rate]
    VAR Previous = CALCULATE([Q03_Reopen_Rate], DATEADD('Date'[Date], -1, MONTH))
    RETURN Current - Previous
TR09_Lead_Time_Trend = 
    VAR Current = [T01_Avg_Lead_Time]
    VAR Previous = CALCULATE([T01_Avg_Lead_Time], DATEADD('Date'[Date], -1, MONTH))
    RETURN DIVIDE(Current - Previous, Previous, 0)
TR10_Velocity_Trend = 
    VAR Current = [S01_Sprint_Velocity]
    VAR Previous = CALCULATE([S01_Sprint_Velocity], DATEADD('Date'[Date], -1, MONTH))
    RETURN DIVIDE(Current - Previous, Previous, 0)
TR11_Effort_Trend = 
    VAR Current = [E01_Total_Effort]
    VAR Previous = CALCULATE([E01_Total_Effort], DATEADD('Date'[Date], -1, MONTH))
    RETURN DIVIDE(Current - Previous, Previous, 0)
TR12_Module_Bug_Pattern = 
    AVERAGEX(
        VALUES('Bugs'[ModuleName]),
        CALCULATE([V01_Total_Bugs])
    )
TR13_Team_Bug_Pattern = 
    AVERAGEX(
        VALUES('Bugs'[TeamName]),
        CALCULATE([V01_Total_Bugs])
    )
TR14_Seasonal_Bug_Index = 
    VAR CurrentMonth = MONTH(TODAY())
    VAR AvgForMonth = 
        CALCULATE(
            AVERAGE('Bugs'[BugID]),
            MONTH('Bugs'[CreatedDate]) = CurrentMonth
        )
    VAR OverallAvg = AVERAGE('Bugs'[BugID])
    RETURN DIVIDE(AvgForMonth, OverallAvg, 1)
TR15_Bug_Growth_Rate = 
    VAR CurrentQuarter = [V01_Total_Bugs]
    VAR PreviousQuarter = CALCULATE([V01_Total_Bugs], DATEADD('Date'[Date], -1, QUARTER))
    RETURN DIVIDE(CurrentQuarter - PreviousQuarter, PreviousQuarter, 0)
```

**فیلدهای مرجع**: F-BUG-001, 004, 006, 010, 014, 016, 027, 049

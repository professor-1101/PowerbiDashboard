# 🔍 Complete Field Analysis - 58 Fields Used in Formulas

## Summary

**Fields used in formulas**: 58 fields
**CSV columns available**: 28 columns
**Excel current columns**: 74 columns

---

## 📊 Field Classification - Complete Analysis

### 🟢 Category 1: Direct from CSV (18 fields)

Available directly in the current CSV export:

| Field Name | CSV Column | Status |
|------------|------------|--------|
| BugID | ID | ✅ Available |
| Title | Title | ✅ Available (not in formulas but used in reports) |
| Description | Description | ✅ Available (not in formulas but used in reports) |
| Severity | Severity | ✅ Available |
| Priority | Priority | ✅ Available |
| State | State | ✅ Available |
| Category | Bug Type | ✅ Available (needs extraction: "ANZ (تحلیل)" → "ANZ") |
| Tags | Tags | ✅ Available |
| TeamName | Team Project | ✅ Available |
| SprintName | Iteration Path | ✅ Available (needs extraction) |
| AssigneeName | Assigned To | ✅ Available (needs name extraction) |
| CloseReason | Closed Reason | ✅ Available |
| ClosedDate | Closed Date | ✅ Available |
| ResolvedDate | Resolved Date | ✅ Available |
| LastModifiedDate | State Change Date | ✅ Available |
| DueDate | Target Date / Due Date | ✅ Available |
| IsRegression | Tags / Bug Type | ✅ Available (needs calculation from tags) |
| is_escaped | ❌ NOT in CSV | ⚠️ **MISSING - need to remove or set to 0** |

### 🟡 Category 2: Calculate from Azure DevOps Revisions (16 fields)

These fields **CAN** be calculated if we query `WorkItemRevisions` table:

| Field Name | Calculation Method | Requires Revisions? |
|------------|-------------------|---------------------|
| CreatedDate | First revision date | ✅ YES |
| AssignedDate | First time State → "Active" or Assigned To changed | ✅ YES |
| TriageDate | First time State → "Triage" | ✅ YES |
| InProgressDate | First time State → "In Progress" | ✅ YES |
| ReadyForRetestDate | First time State → "Ready for Retest" | ✅ YES |
| VerifiedDate | First time State → "Verified" | ✅ YES |
| DoneDate | First time State → "Done" | ✅ YES |
| FirstReopenDate | First time reopened (Closed → Active) | ✅ YES |
| LastReopenDate | Last time reopened | ✅ YES |
| StateTransitionCount | Count of State changes | ✅ YES |
| StateChangeCount | Same as StateTransitionCount | ✅ YES |
| AssigneeChangeCount | Count of Assigned To changes | ✅ YES |
| StateHistory | JSON/text of all state changes | ✅ YES |
| PreviousState | Previous state before current | ✅ YES |
| LeadTimeHrs | (ClosedDate - CreatedDate) in hours | ✅ YES (needs CreatedDate) |
| CycleTimeHrs | (ClosedDate - First Active Date) in hours | ✅ YES (needs state history) |

**Azure DevOps Query Needed:**
```sql
SELECT
    [System.Id],
    [System.Rev],
    [System.RevisedDate],
    [System.ChangedDate],
    [System.State],
    [System.AssignedTo],
    [System.ChangedBy],
    [System.Reason]
FROM WorkItemRevisions
WHERE [System.WorkItemType] = 'Bug'
ORDER BY [System.Id], [System.Rev]
```

### 🟠 Category 3: Calculate from Current Data (6 fields)

Can be calculated from fields we already have:

| Field Name | Calculation | Source Fields |
|------------|-------------|---------------|
| IsDuplicate | CloseReason == "Duplicate" ? 1 : 0 | CloseReason |
| AgeDays | (TODAY() - CreatedDate).days for open bugs | CreatedDate, State |
| TriageDurationHrs | (AssignedDate - TriageDate) in hours | TriageDate, AssignedDate |
| ReadyForRetestDurationHrs | Duration in Ready for Retest state | State history |
| WaitTimeHrs | Sum of waiting periods | State history |
| ResponseTimeHrs | Time to first response | CreatedDate, AssignedDate |

### 🔵 Category 4: Dashboard/Manual Entry (12 fields)

These fields are for manual data entry or external tracking:

| Field Name | Type | Availability | Notes |
|------------|------|--------------|-------|
| FixEffortHrs | Decimal | ❌ Manual entry | Developer's estimate |
| AnalysisEffortHrs | Decimal | ❌ Manual entry | Analysis time |
| TestEffortHrs | Decimal | ❌ Manual entry | Testing time |
| ReopenEffortHrs | Decimal | ❌ Manual entry | Rework effort |
| TotalEffortHrs | Decimal | ❌ Calculated | Sum of all effort fields |
| EstimatedEffortHrs | Decimal | ❌ Manual entry | Initial estimate |
| ModuleName | Text | ❌ Manual entry | Code module name |
| RootCause | Text | ❌ Manual entry | Descriptive text |
| TestCaseID | Text | ❌ Manual entry | Related test case |
| VerifierName | Text | ❌ Manual entry | QA tester name |
| DuplicateOfBugID | Integer | ❌ Manual entry | If duplicate, original bug ID |
| FixAttempts | Integer | ❌ Manual entry | Number of fix attempts |

### 🔴 Category 5: Calculated/Derived Metrics (6 fields)

These are custom business metrics not in Azure DevOps:

| Field Name | Calculation | Status |
|------------|-------------|--------|
| BusinessImpact | ❌ Custom field | Not in CSV, needs definition |
| RiskScore | ❌ Custom formula | Calculated from Severity + Impact |
| EscapeProbability | ❌ Statistical model | Machine learning metric |
| RecurrenceProbability | ❌ Statistical model | ML metric |
| IsBlocking | ❌ Custom flag | Need to define criteria |
| IsAnomaly | ❌ Statistical detection | ML metric |

---

## 🎯 Updated Recommendation

Based on complete analysis of all 58 fields used in formulas:

### Keep These Fields (44 total):

**From CSV (18):**
- BugID, Title, Description, Severity, Priority, State, Category, Tags
- TeamName, SprintName, AssigneeName, CloseReason
- ClosedDate, ResolvedDate, LastModifiedDate, DueDate
- IsRegression
- is_escaped (keep but set to 0 - used in formulas!)

**From Revisions Query (16):**
- CreatedDate, AssignedDate, TriageDate, InProgressDate
- ReadyForRetestDate, VerifiedDate, DoneDate
- FirstReopenDate, LastReopenDate
- StateTransitionCount, StateChangeCount, AssigneeChangeCount
- StateHistory, PreviousState
- LeadTimeHrs, CycleTimeHrs

**Calculated (6):**
- IsDuplicate, AgeDays, TriageDurationHrs
- ReadyForRetestDurationHrs, WaitTimeHrs, ResponseTimeHrs

**Manual Entry (4 - most important):**
- FixEffortHrs, RootCause, ModuleName, TestCaseID

### Total: 44 essential fields (down from 74)

---

## 🚨 Critical Missing Data - Action Required

### Option 1: Get WorkItemRevisions Data (RECOMMENDED)

Export a second CSV with revision history:

```sql
SELECT
    [System.Id] AS BugID,
    [System.Rev],
    [System.ChangedDate],
    [System.CreatedDate],
    [System.State],
    [System.AssignedTo],
    [System.Reason]
FROM WorkItemRevisions
WHERE [System.Id] IN (
    SELECT [System.Id]
    FROM WorkItems
    WHERE [System.WorkItemType] = 'Bug'
)
ORDER BY [System.Id], [System.Rev]
```

Then process this data to calculate the 16 history-dependent fields.

### Option 2: Use Approximations (TEMPORARY)

Until we get revision data:

```python
# Approximations
df['CreatedDate'] = df['State Change Date']  # Approximation
df['AssignedDate'] = df['State Change Date']
df['LeadTimeHrs'] = (df['ClosedDate'] - df['CreatedDate']).dt.total_seconds() / 3600
df['CycleTimeHrs'] = df['LeadTimeHrs'] * 0.7  # Rough estimate

# Conservative estimates
df['StateTransitionCount'] = 2  # Minimum: Created → Closed
df['AssigneeChangeCount'] = 0
df['FirstReopenDate'] = pd.NaT
df['LastReopenDate'] = pd.NaT

# Durations
df['TriageDurationHrs'] = 0
df['ReadyForRetestDurationHrs'] = 0
df['WaitTimeHrs'] = 0
df['ResponseTimeHrs'] = 24  # Default: 1 day
```

### Option 3: Remove Unused Metrics (LAST RESORT)

If we can't get revision data and don't want approximations:
- Delete formulas/charts that depend on these 16 fields
- Update KPIs_Detail sheet to remove related metrics
- This will reduce dashboard functionality significantly

---

## 📋 Implementation Priority

### Phase 1: CSV Import (Immediate)
- Import 18 fields from current CSV
- Calculate IsDuplicate, IsRegression
- Set is_escaped = 0 for all (keep column for formula compatibility)
- Extract AssigneeName, Category, SprintName

### Phase 2: Request Revisions Data (This Week)
- Get WorkItemRevisions export from Azure DevOps
- Calculate all 16 history-dependent fields
- This unlocks full dashboard functionality

### Phase 3: Manual Fields (As Needed)
- Add FixEffortHrs, ModuleName, RootCause, TestCaseID
- These can be filled gradually by teams

### Phase 4: Advanced Metrics (Future)
- BusinessImpact, RiskScore, ML metrics
- Requires business rules definition

---

## ✅ Revised Field Count

| Category | Count | Status |
|----------|-------|--------|
| From CSV | 18 | ✅ Ready to import |
| From Revisions | 16 | ⚠️ Need WorkItemRevisions query |
| Calculated | 6 | ✅ Can calculate |
| Manual Entry | 4 | 🔵 Optional/gradual |
| **TOTAL ESSENTIAL** | **44** | **vs 74 original** |

**Reduction**: 74 → 44 (30 fields removed!)

---

## 🎯 Next Steps

1. **Import CSV** with 18 core fields (can do now)
2. **Request Azure DevOps WorkItemRevisions export** (critical for time metrics)
3. **Calculate 6 derived fields** from existing data
4. **Create Manual Entry fields** with N/A defaults
5. **Test all 43 charts** to ensure they still work

**Key Insight**: The user was RIGHT - we need history data from WorkItemRevisions to calculate time metrics properly. The current CSV export is insufficient for fields like CreatedDate, LeadTime, CycleTime, ReopenCount, etc.

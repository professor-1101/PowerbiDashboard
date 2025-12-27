# 🎯 Final Fields List - Clean & Minimal

## Summary

**Current Excel**: 74 columns
**Actually used in charts**: 8 columns
**Final clean version**: 24 columns

**Reduction**: 74 → 24 (50 fields deleted! 🗑️)

---

## ✅ FINAL 24 FIELDS (Clean List)

### 🟢 Core Fields (8 fields - Directly from CSV)

| # | Field Name | CSV Source | Type | Usage |
|---|------------|------------|------|-------|
| 1 | BugID | ID | Integer | ✅ Used in charts |
| 2 | Title | Title | Text | ✅ Used in charts |
| 3 | Description | Description | Text | ✅ Used in charts |
| 4 | Severity | Severity | Text | ✅ Used in charts |
| 5 | Priority | Priority | Integer | ✅ Used in charts |
| 6 | State | State | Text | ✅ Used in charts |
| 7 | Category | Bug Type | Text | ✅ Used in charts |
| 8 | Tags | Tags | Text | Metadata |

### 🟡 Extracted/Calculated Fields (10 fields)

| # | Field Name | Calculation | Type | Usage |
|---|------------|-------------|------|-------|
| 9 | ProjectName | Extract from "Team Project" | Text | Grouping |
| 10 | TeamName | Team Project | Text | Analysis |
| 11 | SprintName | Extract from "Iteration Path" | Text | Trend analysis |
| 12 | AssigneeName | Extract name from "Assigned To" | Text | Workload |
| 13 | AssigneeID | Extract ID from "Assigned To" | Text | Linking |
| 14 | ResolverName | Extract name from "Closed By" | Text | Resolution |
| 15 | ResolverID | Extract ID from "Closed By" | Text | Linking |
| 16 | is_duplicate | CloseReason == "Duplicate" ? 1 : 0 | Integer | Quality |
| 17 | IsRegression | Tags contains "regression" ? 1 : 0 | Integer | Quality |
| 18 | Comments | Comment Count | Integer | Activity |

### 📅 Date Fields (5 fields - From CSV)

| # | Field Name | CSV Source | Type | Usage |
|---|------------|------------|------|-------|
| 19 | ClosedDate | Closed Date | DateTime | Time analysis |
| 20 | ResolvedDate | Resolved Date | DateTime | Time analysis |
| 21 | LastModifiedDate | State Change Date | DateTime | Tracking |
| 22 | DueDate | Target Date OR Due Date | DateTime | Planning |
| 23 | CloseReason | Closed Reason | Text | Resolution analysis |

### 🔵 Dashboard-Only Field (1 field - Manual Entry)

| # | Field Name | Source | Type | Usage |
|---|------------|--------|------|-------|
| 24 | Resolution | N/A - Manual entry | Text | ✅ Used in Resolution_Analysis chart |

---

## 🗑️ DELETED FIELDS (51 fields removed)

These fields were **NOT used in any chart** and **NOT available in CSV**:

### Time/Date Fields (13 deleted)
- CreatedDate
- TriageDate
- AssignedDate
- StartedDate
- InProgressDate
- ReadyForRetestDate
- VerifiedDate
- DoneDate
- FirstReopenDate
- LastReopenDate
- AgeDays
- CycleTimeHrs
- LeadTimeHrs

### Effort Fields (7 deleted)
- AnalysisEffortHrs
- DevEffortHrs
- FixEffortHrs
- TestEffortHrs
- ReopenEffortHrs
- TotalEffortHrs
- EstimatedEffortHrs

### Duration Fields (6 deleted)
- TriageDurationHrs
- ActiveDurationHrs
- InProgressDurationHrs
- ReadyForRetestDurationHrs
- ResponseTimeHrs
- WaitTimeHrs
- ActiveWorkTimeHrs

### Workflow Fields (10 deleted)
- ReopenCount
- StateChangeCount
- StateTransitionCount
- StateHistory
- PreviousState
- AssigneeChangeCount
- FixAttempts

### Module/Project IDs (5 deleted)
- ProjectID
- TeamID
- ModuleID
- ModuleName
- SprintID

### Other Fields (10 deleted)
- is_escaped
- ExternalTicketID
- ReporterID
- ReporterName
- VerifierID
- VerifierName
- TestCaseID
- RootCause (not in CSV, descriptive text)
- IsDuplicate (replaced by is_duplicate)
- DuplicateOfBugID
- RetestPassCount
- RetestFailCount

---

## 🎨 Color Coding in Excel

Apply header colors based on data source:

```python
🟢 GREEN - Direct from CSV (13 fields):
   BugID, Title, Description, Severity, Priority, State, Category, Tags,
   TeamName, ClosedDate, ResolvedDate, LastModifiedDate, DueDate, CloseReason

🟡 YELLOW - Calculated (10 fields):
   ProjectName, SprintName, AssigneeName, AssigneeID, ResolverName, ResolverID,
   is_duplicate, IsRegression, Comments

🔵 BLUE - Dashboard-Only (1 field):
   Resolution
```

---

## 📊 Data Transformation Rules

### 1. Severity Cleanup
```python
# Current: "3 - Medium", "1 - Critical"
# Target: "Critical", "High", "Medium", "Low"

def clean_severity(value):
    if pd.isna(value):
        return "Medium"
    severity_map = {
        "1 - Critical": "Critical",
        "2 - High": "High",
        "3 - Medium": "Medium",
        "4 - Low": "Low"
    }
    return severity_map.get(value, value)
```

### 2. State Normalization
```python
# Normalize state values
def normalize_state(value):
    if pd.isna(value):
        return "Open"
    state_map = {
        "triage": "New",
        "In Progress": "Active",
        "Committed": "Active",
        "Waiting": "Active",
        "Done": "Closed"
    }
    return state_map.get(value, value)
```

### 3. Category Extraction
```python
# Current: "ANZ (تحلیل)", "FN (عملیاتی)"
# Target: "ANZ", "FN"

def extract_category(value):
    if pd.isna(value):
        return "Other"
    # Extract code before parenthesis
    match = re.match(r'^([A-Z]+)', value)
    return match.group(1) if match else value
```

### 4. Name/ID Extraction
```python
# Current: "Seyfollahi Artin <RPK\ASeyfollahi>"
# Extract: Name = "Seyfollahi Artin", ID = "ASeyfollahi"

def extract_assignee_info(value):
    if pd.isna(value) or value == "":
        return "", ""
    match = re.match(r"(.+?)\s*<RPK\\(.+?)>", value)
    if match:
        name = match.group(1).strip()
        user_id = match.group(2).strip()
        return name, user_id
    return value, ""
```

### 5. Project/Sprint Extraction
```python
# Current: "SAJAK\Estate_Sprint 44"
# Extract: Project = "SAJAK", Sprint = "Estate_Sprint 44"

def extract_sprint_info(value):
    if pd.isna(value):
        return "", ""
    parts = value.split("\\")
    project = parts[0] if len(parts) > 0 else ""
    sprint = parts[1] if len(parts) > 1 else ""
    return project, sprint
```

### 6. Calculate Flags
```python
# is_duplicate
df['is_duplicate'] = (df['CloseReason'] == 'Duplicate').astype(int)

# IsRegression
df['IsRegression'] = df['Tags'].str.contains('regression|تکراری', case=False, na=False).astype(int)
```

---

## 📁 Final Excel Structure

### Sheet 1: raw_data
- 820 rows × 24 columns
- Color-coded headers
- Clean, validated data

### Sheet 2: Field_Definitions
- Field name
- Description
- Data type
- Source (CSV/Calculated/Manual)
- Usage in charts

### Sheet 3-12: Dashboard Sheets (unchanged)
- PowerBI_Dashboard
- Volume_Analysis
- Team_Performance
- Sprint_Analysis
- Time_Flow
- Quality_Analysis
- State_Flow
- Resolution_Analysis
- (etc.)

---

## ✅ Implementation Checklist

- [ ] Parse CSV with UTF-8 encoding
- [ ] Clean Severity values ("1 - Critical" → "Critical")
- [ ] Normalize State values ("triage" → "New")
- [ ] Extract Category codes ("ANZ (تحلیل)" → "ANZ")
- [ ] Extract AssigneeName and AssigneeID
- [ ] Extract ResolverName and ResolverID
- [ ] Extract ProjectName from TeamName
- [ ] Extract SprintName from Iteration Path
- [ ] Calculate is_duplicate flag
- [ ] Calculate IsRegression flag
- [ ] Set Resolution = N/A for all rows
- [ ] Apply color coding to headers
- [ ] Create Field_Definitions sheet
- [ ] Validate all 820 rows processed
- [ ] Test charts still work

---

**Result**: Clean, focused dataset with only useful fields! 🎯

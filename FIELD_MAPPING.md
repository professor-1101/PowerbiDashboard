# 🗺️ Field Mapping: Azure DevOps CSV → Excel Dashboard

## 📊 CSV Analysis Summary

- **Source File**: `Untitled query (1).csv`
- **Total Records**: 820 bugs
- **Total Columns**: 28 columns
- **Date Range**: Nov 2025 - Dec 2025

---

## 📋 Complete Field Mapping

### 🟢 Direct Fields (Available in CSV - No Changes Needed)

| Excel Field Name | CSV Column Name | Data Type | Notes |
|------------------|----------------|-----------|-------|
| BugID | ID | Integer | ✅ Direct mapping |
| Title | Title | Text | ✅ Direct mapping |
| State | State | Text | Values: Open, Active, Done, Resolved, triage, Waiting, In Progress, Committed |
| Severity | Severity | Text | Values: "3 - Medium", "1 - Critical", "2 - High", "4 - Low" (needs cleanup) |
| Priority | Priority | Integer/Text | Values: 1, 2, 3, 4 or empty |
| AssignedTo | Assigned To | Text | Format: "Name Surname <RPK\Username>" (needs cleanup) |
| TeamName | Team Project | Text | Values: SAJAK, Dem, Infrastructure Bizagi Extension |
| SprintName | Iteration Path | Text | Format: "ProjectName\Sprint XX" |
| CloseReason | Closed Reason | Text | Values: Completed, Invalid, By Design, Cannot Reproduce, Duplicate, Won't Fix, Obsolete |
| ClosedDate | Closed Date | DateTime | Format: "MM/DD/YYYY HH:MM:SS AM/PM" |
| ClosedBy | Closed By | Text | Format: "Name Surname <RPK\Username>" (needs cleanup) |
| ResolvedDate | Resolved Date | DateTime | Format: "MM/DD/YYYY HH:MM:SS AM/PM" |
| Tags | Tags | Text | ✅ EXISTS! Values: "Bizagi_Team", "#تکراری", etc. |

### 🟡 Calculable Fields (Need to be Created from CSV Data)

| Excel Field Name | Calculation Method | Source Columns | Notes |
|------------------|-------------------|----------------|-------|
| is_reopen | `IF(ReopenCount > 0, 1, 0)` | State Change Date | **Needs WorkItemRevisions query** |
| is_duplicate | `IF(Closed Reason == "Duplicate", 1, 0)` | Closed Reason | Can calculate from existing data |
| ReopenCount | Count of "Active" state changes after "Closed" | State Change Date | **Needs WorkItemRevisions query** |
| StateChangeCount | Count of all state transitions | State Change Date | **Needs WorkItemRevisions query** |
| Category | Derived from Bug Type | Bug Type | Values: ANZ, FN, PER (from "Bug Type" column) |
| ProjectName | Extract from Iteration Path | Iteration Path | Split "SAJAK\Estate_Sprint 44" → "SAJAK" |
| SprintNumber | Extract from Iteration Path | Iteration Path | Split "SAJAK\Estate_Sprint 44" → "44" |
| CreatedDate | First state change date | State Change Date | **Needs WorkItemRevisions query** |
| LeadTimeHrs | (ClosedDate - CreatedDate) in hours | CreatedDate, ClosedDate | Depends on CreatedDate |
| CycleTimeHrs | (ClosedDate - FirstActiveDate) in hours | State transitions | **Needs WorkItemRevisions query** |
| AgeDays | (Today - CreatedDate) for open bugs | CreatedDate | Depends on CreatedDate |
| Description | Direct but needs cleanup | Description | Remove HTML tags |
| AssigneeName | Extract name from "Assigned To" | Assigned To | Split "Name Surname <RPK\Username>" |
| AssigneeID | Extract username from "Assigned To" | Assigned To | Extract "Username" from <RPK\Username> |
| ResolverName | Extract name from "Closed By" | Closed By | Split "Name Surname <RPK\Username>" |
| ResolverID | Extract username from "Closed By" | Closed By | Extract "Username" from <RPK\Username> |
| CommentCount | Direct mapping | Comment Count | ✅ Available in CSV |

### 🔵 Dashboard-Only Fields (Cannot be derived from CSV - Manual Entry)

| Excel Field Name | Type | Availability | Notes |
|------------------|------|--------------|-------|
| FixEffortHrs | Decimal | ❌ NOT in CSV | Must be entered manually in dashboard |
| RootCause | Text | ❌ NOT in CSV | Descriptive text field, not in query |
| Resolution | Text | ❌ NOT in CSV | Technical solution description |
| ModuleName | Text | ❌ NOT in CSV | Code module affected - manual entry |

### 🔴 Missing Fields (Don't Exist Anywhere - Remove or Mark N/A)

| Excel Field Name | Status | Action |
|------------------|--------|--------|
| is_escaped | ❌ Does NOT exist | Set to 0 or remove column |
| TestEffortHrs | ❌ Does NOT exist | Set to N/A or remove column |
| VerifierName | ❌ Does NOT exist | Set to N/A or remove column |
| VerifierID | ❌ Does NOT exist | Set to N/A or remove column |
| RetestEffortHrs | ❌ Does NOT exist | Set to N/A or remove column |
| ExternalTicketID | ❌ Does NOT exist | Set to N/A or remove column |

---

## 🔄 Data Transformation Rules

### Severity Cleanup
```python
# Current: "3 - Medium", "1 - Critical", "2 - High", "4 - Low"
# Target: "Critical", "High", "Medium", "Low"

severity_map = {
    "1 - Critical": "Critical",
    "2 - High": "High",
    "3 - Medium": "Medium",
    "4 - Low": "Low"
}
```

### State Normalization
```python
# Current: Open, Active, Done, Resolved, triage, Waiting, In Progress, Committed
# Target: Map to standard states

state_map = {
    "Open": "Open",
    "triage": "New",
    "Active": "Active",
    "In Progress": "Active",
    "Committed": "Active",
    "Waiting": "Active",
    "Resolved": "Resolved",
    "Done": "Closed"
}
```

### Name Extraction
```python
# Current: "Seyfollahi Artin <RPK\ASeyfollahi>"
# Extract: Name = "Seyfollahi Artin", ID = "ASeyfollahi"

import re

def extract_name(field):
    if pd.isna(field) or field == "":
        return "", ""
    match = re.match(r"(.+?)\s*<RPK\\(.+?)>", field)
    if match:
        name = match.group(1).strip()
        user_id = match.group(2).strip()
        return name, user_id
    return field, ""
```

### DateTime Parsing
```python
# Current: "12/24/2025 11:53:24 AM"
# Target: datetime object

pd.to_datetime(df['Closed Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
```

### Sprint/Project Extraction
```python
# Current: "SAJAK\Estate_Sprint 44"
# Extract: Project = "SAJAK", Sprint = "Estate_Sprint 44", Number = 44

def parse_iteration(iteration_path):
    if pd.isna(iteration_path):
        return "", "", None
    parts = iteration_path.split("\\")
    project = parts[0] if len(parts) > 0 else ""
    sprint = parts[1] if len(parts) > 1 else ""

    # Extract sprint number
    sprint_num = None
    match = re.search(r'(\d+)$', sprint)
    if match:
        sprint_num = int(match.group(1))

    return project, sprint, sprint_num
```

---

## ⚠️ Critical Missing Data (Requires Azure DevOps Revisions Query)

The following fields **CANNOT** be calculated from the current CSV and require a **WorkItemRevisions** query:

### Required Query 1: WorkItemRevisions for Time Metrics
```sql
SELECT
    [System.Id],
    [System.CreatedDate],
    [System.ChangedDate],
    [System.State],
    [System.Reason],
    [System.ChangedBy]
FROM WorkItemLinks
WHERE
    [System.WorkItemType] = 'Bug'
    AND [System.TeamProject] = @Project
ORDER BY [System.Id], [System.ChangedDate]
```

**This query provides:**
- CreatedDate (first revision)
- ReopenCount (count of "Closed" → "Active" transitions)
- StateChangeCount (total state changes)
- CycleTimeHrs (first Active to Closed)
- LeadTimeHrs (Created to Closed)

### Workaround (Temporary Solution)
Until we get WorkItemRevisions data:
```python
# Use State Change Date as approximation for CreatedDate
df['CreatedDate'] = pd.to_datetime(df['State Change Date'])

# Mark all bugs as not reopened (conservative estimate)
df['is_reopen'] = 0
df['ReopenCount'] = 0
df['StateChangeCount'] = 1  # At least one state

# Calculate approximate LeadTime
df['LeadTimeHrs'] = (df['ClosedDate'] - df['CreatedDate']).dt.total_seconds() / 3600
df['CycleTimeHrs'] = df['LeadTimeHrs']  # Approximation
```

---

## 📝 Implementation Steps

1. ✅ **Parse CSV** with correct encoding (UTF-8 with BOM)
2. ⏳ **Clean Data**:
   - Extract names from "Name <RPK\ID>" format
   - Parse severity from "X - Name" format
   - Normalize state values
   - Parse datetime fields
3. ⏳ **Add Calculated Fields**:
   - is_duplicate (from CloseReason)
   - Category (from Bug Type)
   - ProjectName/SprintName (from Iteration Path)
4. ⏳ **Add Placeholder Fields** (for missing data):
   - is_reopen = 0
   - ReopenCount = 0
   - StateChangeCount = 1
   - is_escaped = 0
   - TestEffortHrs = N/A
5. ⏳ **Color Code Excel Cells** based on field categories
6. ⏳ **Create Field_Definitions sheet** with documentation

---

## 🎨 Excel Color Coding

Apply PatternFill colors in Excel:

```python
from openpyxl.styles import PatternFill

# Color definitions
GREEN = PatternFill(start_color='D4EDDA', end_color='D4EDDA', fill_type='solid')   # Direct
YELLOW = PatternFill(start_color='FFF3CD', end_color='FFF3CD', fill_type='solid')  # Calculable
BLUE = PatternFill(start_color='CCE5FF', end_color='CCE5FF', fill_type='solid')    # Dashboard
RED = PatternFill(start_color='F8D7DA', end_color='F8D7DA', fill_type='solid')     # Missing

# Apply to header row
green_fields = ['BugID', 'Title', 'State', 'Severity', 'Priority', ...]
yellow_fields = ['is_reopen', 'is_duplicate', 'Category', ...]
blue_fields = ['FixEffortHrs', 'RootCause', 'Resolution', 'ModuleName']
red_fields = ['is_escaped', 'TestEffortHrs', 'VerifierName', ...]
```

---

## ✅ Validation Checklist

- [ ] CSV parsed successfully (820 records)
- [ ] All 28 CSV columns mapped
- [ ] Severity values cleaned ("Critical", "High", "Medium", "Low")
- [ ] State values normalized
- [ ] Names extracted from RPK format
- [ ] DateTime fields parsed correctly
- [ ] is_duplicate calculated
- [ ] Tags field preserved
- [ ] Missing fields marked as N/A or 0
- [ ] Color coding applied to all columns
- [ ] Field_Definitions sheet created

---

**Next Step**: Create Python script to implement this mapping and generate the final Excel file.

# python-report-automation
# Internal Reporting Automation Tool

## Project Background
In my previous roles, I identified that team members were spending significant time manually processing system logs into performance reports. This script was developed to automate that workflow.

## Technical Details
- **Data Parsing**: Uses `pandas` to read and clean raw CSV system logs.
- **KPI Metrics**: Automatically calculates Daily Task Count, Average Duration, and Success Rates
- **Output**: Generates a formatted Excel `.xlsx` report for management review

## Impact
- **Efficiency**: Reduced manual reporting time from 2 hours to under 1 minute
- **Accuracy**: Eliminated human error in manual calculations, improving data reliability
#  Executive Summary: Business Impact & Usage

### The Problem This Solves
In many departments (Procurement, Logistics, HR), teams spend hours every week manually opening CSV files, filtering data in Excel, and calculating KPIs. This process is:
1. **Slow**: Takes hours of manual labor.
2. **Error-Prone**: Human fatigue leads to calculation mistakes.
3. **Static**: Reports are often outdated by the time they are finished.

###  How a Company Benefits
By using this Python automation, a "Regular Company" achieves:
* **Reclaimed Productivity**: Saves ~2 hours per employee/week (approx. 100 hours/year per person).
* **Data Integrity**: 100% calculation accuracy for Success Rates and Durations.
* **Instant Insights**: One-click reporting allows for faster response to supply chain or process bottlenecks.

### Real-Time Demo for HR/Recruiters
If you want to see this work right now without installing Python:
1. Open the `system_logs.csv` file in this repo to see the "Raw Data."
2. Open the `main.py` file to see the "Logic."
3. This script transforms that messy raw data into a structured Excel report (Sample: `performance_summary_report.xlsx`) automatically.

**"I don't just automate tasks; I optimize business workflows to save time and reduce costs."**

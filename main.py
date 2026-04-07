import pandas as pd
from datetime import datetime

def run_report_automation(input_file):
    print(f"--- Starting Report Automation: {datetime.now()} ---")
    
    # 1. Load the data
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: system_logs.csv not found.")
        return

    # 2. Data Cleaning
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    # 3. Calculate KPIs (Key Performance Indicators)
    # This logic reflects your CV experience in reporting and KPI tracking
    daily_summary = df.groupby('date').agg({
        'task_id': 'count',
        'duration_minutes': 'mean',
        'status': lambda x: (x == 'Success').sum()
    }).rename(columns={
        'task_id': 'Total_Tasks',
        'duration_minutes': 'Avg_Duration_Min',
        'status': 'Successful_Tasks'
    })

    # Calculate Success Rate %
    daily_summary['Success_Rate'] = (daily_summary['Successful_Tasks'] / daily_summary['Total_Tasks']) * 100

    # 4. Export to Excel
    output_file = 'performance_summary_report.xlsx'
    daily_summary.to_excel(output_file)
    
    print(f"--- Automation Complete ---")
    print(f"Report saved as: {output_file}")
    print(f"Summary Table:\n{daily_summary}")

if __name__ == "__main__":
    run_report_automation('system_logs.csv')

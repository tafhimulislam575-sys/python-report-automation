import pandas as pd
import os
from datetime import datetime

def generate_business_report(input_csv):
    """
    Simulates a real-world business automation task: 
    Transforming raw system logs into a management-ready KPI summary.
    """
    if not os.path.exists(input_csv):
        print(f"❌ Error: {input_csv} not found. Please ensure the data file exists.")
        return

    # Load data
    df = pd.read_csv(input_csv)
    
    # Process Timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['Date'] = df['timestamp'].dt.date

    # logic: Grouping by date to see performance trends
    # This mirrors Category Management / Procurement tracking
    summary = df.groupby('Date').agg({
        'task_id': 'count',
        'duration_minutes': 'mean',
        'status': lambda x: (x == 'Success').sum()
    }).rename(columns={
        'task_id': 'Total_Volume',
        'duration_minutes': 'Avg_Process_Time',
        'status': 'Completed_Successfully'
    })

    # Add Success Rate Percentage
    summary['Success_Rate_%'] = (summary['Completed_Successfully'] / summary['Total_Volume'] * 100).round(2)

    # Save to Excel
    output_file = 'Management_KPI_Report.xlsx'
    summary.to_excel(output_file)

    # Console Output for immediate 'Wow' factor
    print("="*50)
    print("✅ AUTOMATION COMPLETE")
    print("="*50)
    print(f"FILE GENERATED: {output_file}")
    print("-"*50)
    print(summary)
    print("="*50)
    print("BENEFIT: This report was generated in < 1 second.")

if __name__ == "__main__":
    generate_business_report('system_logs.csv')

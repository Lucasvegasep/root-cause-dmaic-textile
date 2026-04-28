import pandas as pd
import matplotlib.pyplot as plt

def generate_pareto(df, group_col, value_col, level_name):
    """
    Generates a Pareto Analysis for Root Cause Identification.
    Reference: QA-DMAIC-001
    """
    # 1. Data Aggregation
    data = df.groupby(group_col)[value_col].sum().sort_values(ascending=False).reset_index()
    data['cum_perc'] = 100 * data[value_col].cumsum() / data[value_col].sum()
    
    print(f"--- Pareto Level: {level_name} ---")
    print(data)
    
    # Logic to isolate the 80% (Root Causes)
    vital_few = data[data['cum_perc'] <= 81]
    return vital_few

# --- Execution Example based on Textile Case ---
# Level 1: Sections (SOMET vs VAMATEX)
sections_data = pd.DataFrame({
    'section': ['SOMET', 'VAMATEX'],
    'downtime': [39.8, 33.4]
})

# Level 2: Specific Machinery (Root Cause found in Loom 1 & 4)
looms_data = pd.DataFrame({
    'loom_id': ['Loom 1', 'Loom 4', 'Loom 2', 'Loom 3', 'Loom 5'],
    'failures': [150, 135, 15, 10, 5] # 95.8% concentrated in Loom 1 & 4
})

generate_pareto(looms_data, 'loom_id', 'failures', "Level 2: Specific Looms")

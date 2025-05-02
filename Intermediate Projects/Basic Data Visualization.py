import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load data from CSV or Excel file"""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

def visualize_data(df):
    """Create visualizations for the given DataFrame"""
    # Set style
    sns.set_style("whitegrid")
    
    # Display basic info
    print("\nData Overview:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Numeric columns visualization
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    if len(numeric_cols) > 0:
        # Histograms for numeric columns
        print("\nHistograms of Numeric Columns:")
        df[numeric_cols].hist(figsize=(12, 8))
        plt.tight_layout()
        plt.show()
        
        # Box plots for numeric columns
        print("\nBox Plots of Numeric Columns:")
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df[numeric_cols])
        plt.xticks(rotation=45)
        plt.show()
        
        # Correlation heatmap if there are multiple numeric columns
        if len(numeric_cols) > 1:
            print("\nCorrelation Heatmap:")
            plt.figure(figsize=(10, 8))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
            plt.show()
    
    # Categorical columns visualization
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    if len(categorical_cols) > 0:
        for col in categorical_cols:
            # Bar plots for categorical columns
            print(f"\nValue Counts for {col}:")
            plt.figure(figsize=(10, 5))
            sns.countplot(data=df, x=col)
            plt.xticks(rotation=45)
            plt.show()
            
            # Cross-tabulation with first numeric column if available
            if len(numeric_cols) > 0:
                num_col = numeric_cols[0]
                print(f"\n{col} vs {num_col}:")
                plt.figure(figsize=(12, 6))
                sns.barplot(data=df, x=col, y=num_col)
                plt.xticks(rotation=45)
                plt.show()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the path to your data file (CSV or Excel): ")
    
    try:
        df = load_data(file_path)
        print("Data loaded successfully!")
        visualize_data(df)
    except Exception as e:
        print(f"Error: {e}")

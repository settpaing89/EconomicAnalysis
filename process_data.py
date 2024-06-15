import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('sp500_daily.csv', index_col='date', parse_dates=True)

# Define the Federal Reserve's interest rate announcement dates (example dates)
announcement_dates = [
    '2023-06-14', '2023-07-26', '2023-09-20',
    '2023-11-01', '2023-12-13'
]

# Convert announcement dates to datetime format
announcement_dates = pd.to_datetime(announcement_dates)

# Define the window for analysis (30 days before and after the announcement)
window_days = 30

# Create a list to store DataFrames for each window
window_data_list = []

# Extract data within the window around each announcement date
for date in announcement_dates:
    start_date = date - pd.Timedelta(days=window_days)
    end_date = date + pd.Timedelta(days=window_days)
    window_data = data[start_date:end_date].copy()
    window_data['announcement_date'] = date
    window_data_list.append(window_data)

# Concatenate all DataFrames into one
combined_window_data = pd.concat(window_data_list)

# Remove duplicates (if any)
combined_window_data = combined_window_data.drop_duplicates()

# Save the combined window data to a new CSV file
combined_window_data.to_csv('sp500_window_data.csv')

# Display the first few rows of the combined window data
print(combined_window_data.head())


# Load the combined window data
combined_window_data = pd.read_csv('sp500_window_data.csv', index_col='date', parse_dates=True)

# Plot the closing prices
plt.figure(figsize=(12, 6))
sns.lineplot(data=combined_window_data, x=combined_window_data.index, y='close', hue='announcement_date', legend=None)
for announcement_date in announcement_dates:
    plt.axvline(x=announcement_date, color='r', linestyle='--', label='Interest Rate Announcement' if announcement_date == announcement_dates[0] else "")
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('S&P 500 Closing Prices Around Interest Rate Announcements')
plt.legend()
plt.show()


#Box plot
# Convert announcement_date to string for better visualization
combined_window_data['announcement_date'] = combined_window_data['announcement_date'].astype(str)

# Create a box plot of closing prices around announcement dates
plt.figure(figsize=(12, 6))
sns.boxplot(data=combined_window_data, x='announcement_date', y='close')
plt.xlabel('Announcement Date')
plt.ylabel('Close Price')
plt.title('Distribution of S&P 500 Closing Prices Around Interest Rate Announcements')
plt.show()




#prediction analysis    
# Load historical S&P 500 closing price data
sp500_data = pd.read_csv('sp500_window_data.csv', index_col='date', parse_dates=True)

# Sample significant events (example data)
significant_events = {
    'Date': ['2023-05-15', '2023-08-30', '2024-01-20'],
    'Event': ['Earnings Announcement', 'Product Launch', 'Regulatory Change']
}

# Convert significant events data to DataFrame
significant_events_df = pd.DataFrame(significant_events)
significant_events_df['Date'] = pd.to_datetime(significant_events_df['Date'])

# Plot historical S&P 500 closing prices
plt.figure(figsize=(12, 6))
plt.plot(sp500_data.index, sp500_data['close'], color='blue', label='S&P 500 Closing Prices')

# Plot significant events
for i, event in significant_events_df.iterrows():
    plt.axvline(x=event['Date'], color='red', linestyle='--', label=event['Event'])

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Significance of S&P 500 Closing Prices')
plt.legend()
plt.grid(True)
plt.show()



# Load historical S&P 500 closing price data
sp500_data = pd.read_csv('sp500_window_data.csv', index_col='date', parse_dates=True)

# Create a pivot table for heatmap visualization
pivot_data = sp500_data.pivot_table(index=sp500_data.index.year, columns=sp500_data.index.month, values='close')

# Create the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_data, cmap='YlGnBu', annot=True, fmt=".2f", linewidths=.5)
plt.title('Heatmap of S&P 500 Closing Prices Over Time')
plt.xlabel('Month')
plt.ylabel('Year')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

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

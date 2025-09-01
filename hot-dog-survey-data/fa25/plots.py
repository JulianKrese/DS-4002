import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(filepath):
	"""
	Loads the Excel file and performs basic cleaning:
	- Drops empty columns/rows
	- Strips whitespace from column names
	- Renames columns for easier access
	- Fills missing values if appropriate
	"""
	df = pd.read_excel(filepath)
	df.columns = df.columns.str.strip()
	df = df.dropna(how='all')
	df = df.dropna(axis=1, how='all')
	# Clean string values using map instead of deprecated applymap
	for col in df.select_dtypes(include=['object']).columns:
		df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
	
	print("Original columns:", df.columns.tolist())  # Debug print
	
	# Rename columns for convenience
	df = df.rename(columns={
		'Timestamp': 'timestamp',
		'What year are you in?': 'year',
		'Is hotdog a sandwich?': 'response'  # Added missing question mark
	})
	
	print("Renamed columns:", df.columns.tolist())  # Debug print
	return df

def plot_response_counts(df):
	"""
	Plots the count of each unique response (e.g., Yes/No/Other).
	"""
	plt.figure(figsize=(8, 5))
	response_col = 'response' if 'response' in df.columns else 'Is hotdog a sandwich?'
	sns.countplot(x=response_col, data=df, order=df[response_col].value_counts().index)
	plt.title('Is Hotdog a Sandwich? Response Counts')
	plt.xlabel('Response')
	plt.ylabel('Count')
	plt.tight_layout()
	plt.savefig('response_counts.png', dpi=300, bbox_inches='tight')
	plt.close()

def plot_year_distribution(df):
	"""
	Plots the distribution of student years.
	"""
	plt.figure(figsize=(8, 5))
	sns.countplot(x='year', data=df, order=df['year'].value_counts().index)
	plt.title('Year Distribution')
	plt.xlabel('Year')
	plt.ylabel('Count')
	plt.tight_layout()
	plt.savefig('year_distribution.png', dpi=300, bbox_inches='tight')
	plt.close()

def plot_response_by_year(df):
	"""
	Plots the response breakdown by student year.
	"""
	plt.figure(figsize=(10, 6))
	sns.countplot(x='year', hue='response', data=df)
	plt.title('Is Hotdog a Sandwich? Response by Year')
	plt.xlabel('Year')
	plt.ylabel('Count')
	plt.legend(title='Response')
	plt.tight_layout()
	plt.savefig('response_by_year.png', dpi=300, bbox_inches='tight')
	plt.close()

if __name__ == "__main__":
	filepath = "Is hotdog a sandwich_ (Responses).xlsx"
	df = load_and_clean_data(filepath)
	plot_response_counts(df)
	plot_year_distribution(df)
	plot_response_by_year(df)

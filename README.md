# Hot Dog Sandwich Survey Analysis

## Repository Structure
```
HotDog/
├── Is hotdog a sandwich_ (Responses).xlsx  # Raw survey data
├── plots.py                               # Data analysis and visualization script
├── response_counts.png                    # Generated visualization
├── year_distribution.png                  # Generated visualization
├── response_by_year.png                   # Generated visualization
└── README.md                             # Project documentation
```

## MI1 - Data

### Provenance
- **Data Source**: Survey responses collected via online survey sent to UVA undergraduate students
- **Collection Date**: August 2025
- **Collection Method**: Online survey distributed to UVA undergraduate students
- **Sample Size**: 207 responses

### Management Plan
- Data is stored in Excel format (.xlsx)
- Raw data is preserved in its original form
- Analysis is performed using Python scripts
- Visualizations are automatically generated and saved as PNG files
- [Add any data backup/version control strategies]

### Data Dictionary

| Variable | Type | Description | Units/Format |
|----------|------|-------------|--------------|
| Timestamp | DateTime | Time when survey was submitted | YYYY-MM-DD HH:MM:SS |
| What year are you in? | Integer | Student's academic year | 1-4 |
| Is hotdog a sandwich? | String | Student's response to main survey question | Yes/No/[Other possible responses] |

## MI2 - Uncertainties

### Known Data Issues
1. [List any known biases in data collection]
2. [Note any missing or incomplete data]
3. [Discuss any data quality issues]

### Assumptions
1. Survey responses are truthful
2. Academic year is accurately reported
3. [Add other assumptions made in analysis]

## MI3 - Ethics/Bias

### Potential Biases
1. **Sample Bias**: 
   - Survey may not represent entire UVA student population
   - [Add specific demographic representation issues]

2. **Response Bias**:
   - [Discuss any potential response biases]
   - [Note any leading questions or survey design issues]

3. **Analysis Bias**:
   - [Note any assumptions or decisions in analysis that could introduce bias]

### Privacy Considerations
- All responses are anonymous
- No personally identifiable information is collected
- [Add any additional privacy measures]

### Ethical Implications
- [Discuss any ethical considerations of the research question]
- [Note any potential impacts of results]
- [Address any cultural or social sensitivities]

## Usage

To generate the visualizations:
1. Ensure Python 3.x is installed
2. Install required packages: pandas, matplotlib, seaborn
3. Run the analysis script:
```bash
python plots.py
```

## Results

Three visualizations are generated:
1. `response_counts.png`: Distribution of responses to whether a hot dog is a sandwich
2. `year_distribution.png`: Distribution of respondents by academic year
3. `response_by_year.png`: Response patterns broken down by academic year

[Add key findings and interpretations]

---
*Note: Items in brackets [ ] indicate sections that need to be filled in with specific information about your study.*

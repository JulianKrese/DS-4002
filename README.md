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

### Data Dictionary

| Variable | Type | Description | Units/Format |
|----------|------|-------------|--------------|
| Timestamp | DateTime | Time when survey was submitted | YYYY-MM-DD HH:MM:SS |
| What year are you in? | Integer | Student's academic year | 1-4 |
| Is hotdog a sandwich? | String | Student's response to main survey question | Yes/No/[Other possible responses] |

## MI2 - Uncertainties

### Assumptions
1. Survey responses are truthful and accurate
2. Academic year is accurately reported

## MI3 - Ethics/Bias

### Potential Biases
1. **Sample Bias**: 
   - Survey may not represent entire UVA student population
   - Student demographics are not recorded and may not be a representative sample
   - Disporportionate amount of 4th and 3rd years

## Results

Three visualizations are generated:
1. `response_counts.png`: Distribution of responses to whether a hot dog is a sandwich
2. `year_distribution.png`: Distribution of respondents by academic year
3. `response_by_year.png`: Response patterns broken down by academic year

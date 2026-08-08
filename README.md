# Labour Market Intelligence Germany

A data analytics dashboard analyzing the German IT job market using real job offers from two official sources.

## Project Overview
This project collects, cleans, analyzes and visualizes IT job offers from Germany to answer key questions:
- Which cities hire the most?
- Which IT jobs are most in demand?
- What salaries are offered?
- Which skills are most requested?
- How has hiring evolved over time?

## Data Sources
- Bundesagentur fur Arbeit (Federal Employment Agency Germany)
- Adzuna Jobs API

## Tech Stack
- Python 3.13
- Pandas — data manipulation
- Matplotlib — data visualization
- Streamlit — interactive web dashboard
- REST APIs — data collection

## Project Structure
- collection.py — collect data from Bundesagentur API
- collection_adzuna.py — collect data from Adzuna API
- merge.py — combine both data sources
- cleaning.py — clean and prepare data
- analysis.py — exploratory data analysis
- app.py — Streamlit web dashboard

## Key Insights
- 1,120 real job offers collected
- Berlin, Hamburg and Frankfurt are the top hiring cities
- Data Engineer is the most demanded IT job
- Munich offers the highest average salary at 93,685 EUR
- Machine Learning and Python are the most requested skills
- 
## Power BI Dashboard
Complementing the Streamlit app, this project also includes a Power BI dashboard built on
a proper star-schema data model — showcasing data modeling and DAX skills beyond Python/pandas analysis.

### Data Model
- **fact_job_offers** — 1,127 job postings with measures (salary, contract type, category)
- **dim_city, dim_company, dim_date, dim_skill** — dimension tables
- **bridge_offer_skill** — many-to-many bridge table linking offers to detected skills

### Screenshots

**Overview**
![Overview](powerbi/screenshots/overview.png)

**Skills Demand**
![Skills Demand](powerbi/screenshots/skills.png)

**Market Trends**
![Market Trends](powerbi/screenshots/Trends.png)

**Employers & Contracts**
![Employers & Contracts](powerbi/screenshots/employers.png)

### Files
- [`powerbi/TalentRadar_DE_PowerBI.pbix`](powerbi/TalentRadar_DE_PowerBI.pbix) — open in Power BI Desktop to explore interactively
- [`powerbi/report_export.pdf`](powerbi/report_export.pdf) — static PDF export of the full report

### Note on Data Quality
Only job postings from the Adzuna source (42 out of 1,127 offers) include salary data. Salary-related measures display alongside a sample-size indicator to avoid misleading interpretation.

## Live Demo
Coming soon on Streamlit Cloud

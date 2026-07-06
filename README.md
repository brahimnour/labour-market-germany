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

## Live Demo
Coming soon on Streamlit Cloud
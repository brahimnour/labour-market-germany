import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="German Employment Analytics Platform",
    page_icon="DE",
    layout="wide"
)

# COULEURS
BORDEAUX  = "#6B1E2E"
ROSE      = "#E8C4C4"
ROSE_DARK = "#C48A8A"
CREME     = "#F5EDE8"
TEXTE     = "#2C1810"

# CSS GLOBAL
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {CREME};
        }}
        section[data-testid="stSidebar"] {{
            background-color: {BORDEAUX} !important;
        }}
        section[data-testid="stSidebar"] * {{
            color: white !important;
        }}
        h1, h2, h3 {{
            color: {BORDEAUX};
            font-family: Georgia, serif;
        }}
    </style>
""", unsafe_allow_html=True)

# LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("job_offers_germany_combined_clean.csv",
                      sep=";", encoding="utf-8-sig")
    df["city"] = df["city"].replace({
        "Frankfurt am Main": "Frankfurt",
        "Eschborn, Taunus" : "Frankfurt",
        "Langen (Hessen)"  : "Frankfurt",
        "Bad Vilbel"       : "Frankfurt"
    })
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

df = load_data()
# Normaliser les titres de postes
df["title"] = df["title"].str.replace(r'\s*\(m/w/d\)|\s*\(w/m/d\)|\s*\(f/m/d\)', '', regex=True)
df["title"] = df["title"].str.strip()
df_salary = df[df["salary_avg"].notna()]

# SIDEBAR
st.sidebar.markdown(f"""
    <div style="text-align:center; padding:20px 0;">
        <h2 style="color:white; font-family:Georgia,serif; letter-spacing:2px;">
            LABOUR MARKET<br>GERMANY
        </h2>
        <p style="color:{ROSE}; font-size:12px;">IT Job Market Analysis</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Home",
     "Top Cities",
     "Top Jobs",
     "Top Companies",
     "Salary Analysis",
     "Contract Types",
     "Top Skills",
     "Evolution",
     "Data Explorer"]
)

# PAGE HOME
if page == "Home":

    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {BORDEAUX}, #9B3A4A);
                    padding: 70px 50px; border-radius: 0px; text-align: center;
                    margin-bottom: 40px;">
            <h1 style="color:white; font-size:52px; font-family:Georgia,serif;
                       margin-bottom:15px; letter-spacing:2px;">
                German Employment Analytics<br>Platform
            </h1>
            <p style="color:{ROSE}; font-size:16px;">
                Explore Germany's labour market through interactive analytics<br>on jobs, skills, companies and regional demand
            </p>
        </div>
    """, unsafe_allow_html=True)

    # KPI CARDS
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Offers",  len(df))
    with col2:
        st.metric("Cities",        df["city"].nunique())
    with col3:
        st.metric("Companies",     df["company"].nunique())
    with col4:
        st.metric("With Salary",   len(df_salary))
    with col5:
        avg = int(df_salary["salary_avg"].mean())
        st.metric("Avg Salary",    f"{avg:,} EUR")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # IMAGES DES VILLES
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif; text-align:center;'>Top Hiring Cities</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    cities_data = [
        ("Berlin",    "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=400&q=80"),
        ("Hamburg",   "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80"),
        ("Frankfurt", "https://images.unsplash.com/photo-1569880153113-76e33fc52d5f?w=400&q=80"),
        ("Munich",    "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=400&q=80"),
        ("Cologne",   "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=400&q=80"),
    ]

    cols = st.columns(5)
    for i, (city, img_url) in enumerate(cities_data):
        count   = len(df[df["city"] == city])
        avg_sal = df_salary[df_salary["city"] == city]["salary_avg"].mean()
        sal_text = f"{int(avg_sal):,} EUR avg" if not pd.isna(avg_sal) else "Salary N/A"
        with cols[i]:
            st.markdown(f"""
                <div style="border-radius:10px; overflow:hidden;
                            box-shadow:0 4px 15px rgba(107,30,46,0.2);">
                    <img src="{img_url}" style="width:100%; height:130px; object-fit:cover;">
                    <div style="background:{BORDEAUX}; padding:10px; text-align:center;">
                        <p style="color:white; font-weight:bold;
                                  font-family:Georgia,serif; margin:0;">{city}</p>
                        <p style="color:{ROSE}; font-size:11px; margin:0;">{count} offers</p>
                        <p style="color:{ROSE}; font-size:11px; margin:0;">{sal_text}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")

    # FEATURE CARDS
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif; text-align:center;'>Explore the Analysis</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    cards = [
        (col1, "Top Cities",    "Which German cities hire the most IT professionals?"),
        (col2, "Top Jobs",      "Which IT job titles are most in demand?"),
        (col3, "Top Companies", "Which companies are recruiting the most?"),
    ]
    for col, title, desc in cards:
        with col:
            st.markdown(f"""
                <div style="background:white; border-top:5px solid {BORDEAUX};
                            padding:25px; border-radius:10px; height:140px;
                            box-shadow:0 4px 15px rgba(107,30,46,0.1);">
                    <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;">{title}</h3>
                    <p style="color:#475569;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    cards2 = [
        (col4, "Salary Analysis", "Average salaries by city and job type."),
        (col5, "Top Skills",      "Most requested technical skills."),
        (col6, "Data Explorer",   "Browse and filter all 1120 job offers."),
    ]
    for col, title, desc in cards2:
        with col:
            st.markdown(f"""
                <div style="background:white; border-top:5px solid {BORDEAUX};
                            padding:25px; border-radius:10px; height:140px;
                            box-shadow:0 4px 15px rgba(107,30,46,0.1);">
                    <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;">{title}</h3>
                    <p style="color:#475569;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:{ROSE_DARK}; font-size:12px;'>Data sources: Bundesagentur fur Arbeit + Adzuna — {len(df)} offers collected</p>", unsafe_allow_html=True)

# PAGE TOP CITIES
elif page == "Top Cities":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Top Cities Hiring in Germany</h1>", unsafe_allow_html=True)
    st.markdown("Which German cities recruit the most IT professionals?")
    st.markdown("---")

    top_cities = df["city"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    top_cities.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Top 10 Cities by Number of Job Offers", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.subheader("Raw Numbers")
    st.dataframe(top_cities.reset_index().rename(
        columns={"city": "City", "count": "Number of Offers"}))

# PAGE TOP JOBS
elif page == "Top Jobs":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Most Demanded IT Jobs</h1>", unsafe_allow_html=True)
    st.markdown("Which job titles appear most in German IT job offers?")
    st.markdown("---")

    top_jobs = df["title"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    top_jobs.plot(kind="barh", ax=ax, color="#9B3A4A")
    ax.set_title("Top 10 Most Demanded IT Jobs", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.dataframe(top_jobs.reset_index().rename(
        columns={"title": "Job Title", "count": "Number of Offers"}))

# PAGE TOP COMPANIES
elif page == "Top Companies":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Top Companies Hiring</h1>", unsafe_allow_html=True)
    st.markdown("Which companies are recruiting the most right now?")
    st.markdown("---")

    top_companies = df["company"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    top_companies.plot(kind="barh", ax=ax, color=ROSE_DARK)
    ax.set_title("Top 10 Companies by Number of Job Offers", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.dataframe(top_companies.reset_index().rename(
        columns={"company": "Company", "count": "Number of Offers"}))

# PAGE SALARY ANALYSIS
elif page == "Salary Analysis":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Salary Analysis</h1>", unsafe_allow_html=True)
    st.markdown("Average IT salaries in Germany based on real job offers.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Offers with salary", len(df_salary))
    with col2:
        st.metric("Average salary", f"{int(df_salary['salary_avg'].mean()):,} EUR")
    with col3:
        st.metric("Max salary", f"{int(df_salary['salary_max'].max()):,} EUR")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Average Salary by City")
    salary_by_city = df_salary.groupby("city")["salary_avg"].mean().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    salary_by_city.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Average IT Salary by City (EUR)", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Average salary (EUR)", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Salary Distribution")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    df_salary["salary_avg"].hist(bins=20, ax=ax, color=BORDEAUX, edgecolor="white")
    ax.set_title("Salary Distribution in Germany IT Market", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Salary (EUR)", color=TEXTE)
    ax.set_ylabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px;">
            <p style="color:{BORDEAUX}; font-weight:bold; font-family:Georgia,serif;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                Munich offers the highest average IT salary at 93,685 EUR,
                followed by Berlin at 92,410 EUR.
                Hamburg has the most offers but lower average salaries at 65,607 EUR.
            </p>
        </div>
    """, unsafe_allow_html=True)

# PAGE CONTRACT TYPES
elif page == "Contract Types":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Contract Types</h1>", unsafe_allow_html=True)
    st.markdown("Distribution of full-time vs part-time positions.")
    st.markdown("---")

    contract_types = df[df["contract_time"] != "Not provided"]["contract_time"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    contract_types.plot(kind="bar", ax=ax, color=[BORDEAUX, ROSE_DARK])
    ax.set_title("Contract Types Distribution", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Contract type", color=TEXTE)
    ax.set_ylabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE, rotation=0)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px;">
            <p style="color:{BORDEAUX}; font-weight:bold; font-family:Georgia,serif;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                92% of IT positions in Germany are full-time.
                Part-time IT roles are rare — only 8% of offers.
            </p>
        </div>
    """, unsafe_allow_html=True)

# PAGE TOP SKILLS
elif page == "Top Skills":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Most Demanded IT Skills</h1>", unsafe_allow_html=True)
    st.markdown("Which technical skills do employers mention most in Germany?")
    st.markdown("---")

    skills = [
        "Python", "SQL", "Excel", "Power BI", "Machine Learning",
        "Git", "AWS", "Azure", "Docker", "JavaScript",
        "Spark", "TensorFlow", "Java", "Linux", "Scala",
        "Kubernetes", "Tableau", "R", "Airflow", "dbt"
    ]

    skill_counts = {}
    for skill in skills:
        count = df["title"].str.contains(skill, case=False, na=False).sum()
        if "description" in df.columns:
            count += df["description"].str.contains(skill, case=False, na=False).sum()
        skill_counts[skill] = count

    skill_series = pd.Series(skill_counts).sort_values(ascending=False)
    skill_series = skill_series[skill_series > 0]

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    skill_series.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Most Demanded IT Skills in Germany", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of mentions", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.dataframe(skill_series.reset_index().rename(
        columns={"index": "Skill", 0: "Mentions"}))

# PAGE EVOLUTION
elif page == "Evolution":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Job Offers Evolution Over Time</h1>", unsafe_allow_html=True)
    st.markdown("How has hiring evolved week by week?")
    st.markdown("---")

    df_time = df[df["date"].notna()].copy()
    offers_by_week = df_time.groupby(df_time["date"].dt.isocalendar().week).size()

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    offers_by_week.plot(kind="line", ax=ax, color=BORDEAUX, marker="o", linewidth=2.5)
    ax.fill_between(offers_by_week.index, offers_by_week.values, alpha=0.15, color=BORDEAUX)
    ax.set_title("Job Offers Evolution by Week", color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Week number", color=TEXTE)
    ax.set_ylabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px;">
            <p style="color:{BORDEAUX}; font-weight:bold; font-family:Georgia,serif;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                The best time to apply for an IT job in Germany is between
                April and June — hiring peaks around week 22.
            </p>
        </div>
    """, unsafe_allow_html=True)

# PAGE DATA EXPLORER
elif page == "Data Explorer":
    st.markdown(f"<h1 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Data Explorer</h1>", unsafe_allow_html=True)
    st.markdown("Browse and filter all job offers.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        cities_filter = st.multiselect(
            "Filter by City",
            options=sorted(df["city"].dropna().unique()),
            default=[]
        )
    with col2:
        source_filter = st.multiselect(
            "Filter by Source",
            options=df["source"].unique(),
            default=[]
        )
    with col3:
        salary_only = st.checkbox("Show only offers with salary")

    df_filtered = df.copy()

    if cities_filter:
        df_filtered = df_filtered[df_filtered["city"].isin(cities_filter)]
    if source_filter:
        df_filtered = df_filtered[df_filtered["source"].isin(source_filter)]
    if salary_only:
        df_filtered = df_filtered[df_filtered["salary_avg"].notna()]

    st.markdown(f"**{len(df_filtered)} offers found**")
    st.dataframe(df_filtered[[
        "title", "company", "city", "source",
        "contract_time", "salary_min", "salary_max", "date"
    ]].reset_index(drop=True))

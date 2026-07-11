import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# PAGE CONFIG
st.set_page_config(
    page_title="Germany Labour Market Intelligence",
    page_icon="DE",
    layout="wide"
)

# COULEURS
BORDEAUX  = "#6B1E2E"
ROSE      = "#E8C4C4"
ROSE_DARK = "#C48A8A"
CREME     = "#F5EDE8"
TEXTE     = "#2C1810"
BLANC     = "#FFFFFF"

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
        div[data-testid="stMetric"] {{
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            border-left: 4px solid {BORDEAUX};
            box-shadow: 0 2px 8px rgba(107,30,46,0.1);
        }}
        .stButton > button {{
            background-color: {BORDEAUX};
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-family: Georgia, serif;
            font-size: 14px;
            width: 100%;
            transition: all 0.3s;
        }}
        .stButton > button:hover {{
            background-color: #9B3A4A;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(107,30,46,0.3);
        }}
        .stDownloadButton > button {{
            background-color: {BORDEAUX};
            color: white;
            border: none;
            border-radius: 8px;
        }}
        .stTextInput > div > div > input {{
            border: 2px solid {ROSE};
            border-radius: 8px;
        }}
        .stMultiSelect > div {{
            border: 2px solid {ROSE};
            border-radius: 8px;
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
    df["title"] = df["title"].str.replace(
        r'\s*\(m/w/d\)|\s*\(w/m/d\)|\s*\(f/m/d\)', '', regex=True)
    df["title"] = df["title"].str.strip()
    df["date"]  = pd.to_datetime(df["date"], errors="coerce")
    return df

df       = load_data()
df_salary = df[df["salary_avg"].notna()]

# FOOTER
def show_footer():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background:{BORDEAUX}; padding:30px; margin-top:40px;
                    border-radius:10px; text-align:center;">
            <p style="color:{ROSE}; font-family:Georgia,serif; font-size:16px;
                      font-weight:bold; margin-bottom:10px;">
                Labour Market Intelligence Germany
            </p>
            <p style="color:{ROSE}; font-size:12px; margin-bottom:15px;">
                Data sources: Bundesagentur fur Arbeit + Adzuna API
                — {len(df)} offers collected
            </p>
            <p style="margin:0;">
                <a href="https://github.com/brahimnour/labour-market-germany"
                   style="color:white; text-decoration:none; margin:0 15px;
                          font-size:13px;">
                    GitHub
                </a>
                <a href="https://www.linkedin.com/in/nour-brahim"
                   style="color:white; text-decoration:none; margin:0 15px;
                          font-size:13px;">
                    LinkedIn
                </a>
            </p>
            <p style="color:{ROSE_DARK}; font-size:11px; margin-top:15px;">
                Built with Python, Pandas, Matplotlib and Streamlit
            </p>
        </div>
    """, unsafe_allow_html=True)

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
     "Top Jobs",
     "Top Skills",
     "Top Companies",
     "Top Regions",
     "Labour Market Trends",
     "Insights",
     "About & Methodology"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
    <div style="padding:10px;">
        <p style="color:{ROSE}; font-size:11px; margin:4px 0;">
            Total offers : <b style="color:white;">{len(df)}</b>
        </p>
        <p style="color:{ROSE}; font-size:11px; margin:4px 0;">
            Cities : <b style="color:white;">{df['city'].nunique()}</b>
        </p>
        <p style="color:{ROSE}; font-size:11px; margin:4px 0;">
            Companies : <b style="color:white;">{df['company'].nunique()}</b>
        </p>
        <p style="color:{ROSE}; font-size:11px; margin:4px 0;">
            Avg Salary : <b style="color:white;">{int(df_salary['salary_avg'].mean()):,} EUR</b>
        </p>
    </div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# PAGE HOME
# ══════════════════════════════════════════════════════════
if page == "Home":

    # HERO
    st.markdown(f"""
        <div style="background:linear-gradient(135deg, {BORDEAUX}, #9B3A4A);
                    padding:80px 50px; text-align:center; margin-bottom:40px;
                    border-radius:12px;">
            <p style="color:{ROSE}; font-size:12px; letter-spacing:5px;
                      margin-bottom:8px;">
                DATA INTELLIGENCE PLATFORM
            </p>
            <h1 style="color:white; font-size:54px; font-family:Georgia,serif;
                       margin-bottom:12px; letter-spacing:2px;">
                LABOUR MARKET<br>GERMANY
            </h1>
            <p style="color:{ROSE}; font-size:16px; max-width:600px;
                      margin:0 auto 20px auto;">
                A comprehensive analysis of the German IT job market
                based on 1,120 real job offers collected from official sources.
            </p>
            <p style="color:{ROSE_DARK}; font-size:12px;">
                Bundesagentur fur Arbeit + Adzuna API
            </p>
        </div>
    """, unsafe_allow_html=True)

    # KPI CARDS
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Offers",   f"{len(df):,}")
    with col2:
        st.metric("Cities Covered", df["city"].nunique())
    with col3:
        st.metric("Companies",      df["company"].nunique())
    with col4:
        st.metric("With Salary",    len(df_salary))
    with col5:
        st.metric("Avg Salary",     f"{int(df_salary['salary_avg'].mean()):,} EUR")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # IMAGES VILLES
    st.markdown(f"""
        <h2 style="color:{BORDEAUX}; font-family:Georgia,serif;
                   text-align:center; margin-bottom:20px;">
            Top Hiring Cities
        </h2>
    """, unsafe_allow_html=True)

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
        sal_txt = f"{int(avg_sal):,} EUR" if not pd.isna(avg_sal) else "N/A"
        with cols[i]:
            st.markdown(f"""
                <div style="border-radius:10px; overflow:hidden;
                            box-shadow:0 4px 15px rgba(107,30,46,0.2);
                            margin-bottom:10px;">
                    <img src="{img_url}"
                         style="width:100%; height:120px; object-fit:cover;">
                    <div style="background:{BORDEAUX}; padding:10px;
                                text-align:center;">
                        <p style="color:white; font-weight:bold;
                                  font-family:Georgia,serif; margin:0;
                                  font-size:13px;">{city}</p>
                        <p style="color:{ROSE}; font-size:11px;
                                  margin:2px 0;">{count} offers</p>
                        <p style="color:{ROSE}; font-size:11px;
                                  margin:0;">{sal_txt} avg</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # NAVIGATION CARDS
    st.markdown(f"""
        <h2 style="color:{BORDEAUX}; font-family:Georgia,serif;
                   text-align:center; margin-bottom:20px;">
            Explore the Analysis
        </h2>
        <p style="text-align:center; color:{TEXTE}; margin-bottom:30px;">
            Select a section below or use the sidebar to navigate
        </p>
    """, unsafe_allow_html=True)

    nav_items = [
        ("Top Jobs",             "Which IT jobs are most in demand in Germany?",      "💼"),
        ("Top Skills",           "Which technical skills do employers request most?",  "🛠"),
        ("Top Companies",        "Which companies are hiring the most right now?",     "🏢"),
        ("Top Regions",          "Which cities and regions recruit the most?",         "📍"),
        ("Labour Market Trends", "How has hiring and salaries evolved over time?",     "📈"),
    ]

    col1, col2, col3 = st.columns(3)
    cols_nav = [col1, col2, col3, col1, col2]

    for i, (title, desc, icon) in enumerate(nav_items):
        with cols_nav[i]:
            st.markdown(f"""
                <div style="background:white; border-top:5px solid {BORDEAUX};
                            padding:20px; border-radius:10px; margin-bottom:15px;
                            box-shadow:0 4px 15px rgba(107,30,46,0.1);
                            min-height:130px;">
                    <p style="font-size:24px; margin:0 0 8px 0;">{icon}</p>
                    <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;
                               font-size:15px; margin:0 0 8px 0;">{title}</h3>
                    <p style="color:#475569; font-size:12px;
                               margin:0;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    show_footer()
    # ══════════════════════════════════════════════════════════
# PAGE TOP JOBS
# ══════════════════════════════════════════════════════════
elif page == "Top Jobs":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            Most Demanded IT Jobs in Germany
        </h1>
        <p style="color:{TEXTE}; font-size:15px; margin-bottom:10px;">
            The German IT market is highly competitive. Understanding which job titles
            appear most frequently helps candidates target their applications and
            helps companies benchmark their hiring needs.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # FILTRES
    col1, col2 = st.columns(2)
    with col1:
        city_filter = st.multiselect(
            "Filter by City",
            options=sorted(df["city"].dropna().unique()),
            default=[]
        )
    with col2:
        search = st.text_input("Search a job title", placeholder="e.g. Data Engineer")

    df_jobs = df.copy()
    if city_filter:
        df_jobs = df_jobs[df_jobs["city"].isin(city_filter)]
    if search:
        df_jobs = df_jobs[df_jobs["title"].str.contains(search, case=False, na=False)]

    st.markdown(f"**{len(df_jobs)} offers matching your filters**")
    st.markdown("<br>", unsafe_allow_html=True)

    # GRAPH
    top_jobs = df_jobs["title"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    bars = top_jobs.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Top 10 Most Demanded IT Jobs",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(top_jobs.values):
        ax.text(v + 0.1, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    # KEY INSIGHT
    top_job = top_jobs.index[0]
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif; font-size:16px;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                <b>{top_job}</b> is the most demanded IT job in Germany
                with <b>{top_jobs.values[0]}</b> open positions.
                Data Engineering roles dominate the market,
                reflecting the growing need for data infrastructure.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # TABLE + EXPORT
    st.markdown("---")
    st.subheader("Full Data")
    st.dataframe(df_jobs[["title", "company", "city", "date", "source"]].reset_index(drop=True))
    st.download_button(
        label="Download as CSV",
        data=df_jobs.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_jobs_germany.csv",
        mime="text/csv"
    )
    show_footer()

# ══════════════════════════════════════════════════════════
# PAGE TOP SKILLS
# ══════════════════════════════════════════════════════════
elif page == "Top Skills":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            Most Demanded IT Skills in Germany
        </h1>
        <p style="color:{TEXTE}; font-size:15px; margin-bottom:10px;">
            Skills analysis is extracted from job titles and descriptions.
            Knowing which skills employers mention most helps candidates
            prioritize their learning roadmap.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # FILTRES
    city_filter = st.multiselect(
        "Filter by City",
        options=sorted(df["city"].dropna().unique()),
        default=[]
    )

    df_skills = df.copy()
    if city_filter:
        df_skills = df_skills[df_skills["city"].isin(city_filter)]

    skills = [
        "Python", "SQL", "Excel", "Power BI", "Machine Learning",
        "Git", "AWS", "Azure", "Docker", "JavaScript",
        "Spark", "TensorFlow", "Java", "Linux", "Scala",
        "Kubernetes", "Tableau", "R", "Airflow", "dbt",
        "Kafka", "Databricks", "Snowflake", "FastAPI", "Django"
    ]

    skill_counts = {}
    for skill in skills:
        count = df_skills["title"].str.contains(skill, case=False, na=False).sum()
        if "description" in df_skills.columns:
            count += df_skills["description"].str.contains(
                skill, case=False, na=False).sum()
        skill_counts[skill] = count

    skill_series = pd.Series(skill_counts).sort_values(ascending=False)
    skill_series = skill_series[skill_series > 0]

    # GRAPH
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)

    colors = [BORDEAUX if i < 3 else ROSE_DARK for i in range(len(skill_series))]
    skill_series.plot(kind="barh", ax=ax, color=colors)
    ax.set_title("Most Demanded IT Skills in Germany",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of mentions", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(skill_series.values):
        ax.text(v + 0.1, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)

    top3_patch  = mpatches.Patch(color=BORDEAUX,  label="Top 3 skills")
    rest_patch  = mpatches.Patch(color=ROSE_DARK, label="Other skills")
    ax.legend(handles=[top3_patch, rest_patch])
    plt.tight_layout()
    st.pyplot(fig)

    # KEY INSIGHT
    top_skill = skill_series.index[0]
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif; font-size:16px;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                <b>{top_skill}</b> is the most requested skill in the German IT market
                with <b>{skill_series.values[0]}</b> mentions.
                The top 3 skills are <b>{skill_series.index[0]}</b>,
                <b>{skill_series.index[1]}</b> and <b>{skill_series.index[2]}</b>.
                Mastering these three will significantly increase your chances
                of landing a job in Germany.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Skills Ranking Table")
    st.dataframe(skill_series.reset_index().rename(
        columns={"index": "Skill", 0: "Mentions"}))
    st.download_button(
        label="Download as CSV",
        data=skill_series.reset_index().to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_skills_germany.csv",
        mime="text/csv"
    )
    show_footer()

# ══════════════════════════════════════════════════════════
# PAGE TOP COMPANIES
# ══════════════════════════════════════════════════════════
elif page == "Top Companies":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            Top Companies Hiring in Germany
        </h1>
        <p style="color:{TEXTE}; font-size:15px; margin-bottom:10px;">
            Identifying which companies post the most job offers gives candidates
            a direct target list for applications and reveals which organizations
            are expanding their IT teams the fastest.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # FILTRES
    col1, col2 = st.columns(2)
    with col1:
        city_filter = st.multiselect(
            "Filter by City",
            options=sorted(df["city"].dropna().unique()),
            default=[]
        )
    with col2:
        search_company = st.text_input(
            "Search a company", placeholder="e.g. Google")

    df_comp = df.copy()
    if city_filter:
        df_comp = df_comp[df_comp["city"].isin(city_filter)]
    if search_company:
        df_comp = df_comp[df_comp["company"].str.contains(
            search_company, case=False, na=False)]

    top_companies = df_comp["company"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    top_companies.plot(kind="barh", ax=ax, color=ROSE_DARK)
    ax.set_title("Top 10 Companies by Number of Job Offers",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(top_companies.values):
        ax.text(v + 0.1, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    # KEY INSIGHT
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif; font-size:16px;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                <b>{top_companies.index[0]}</b> leads German IT recruitment
                with <b>{top_companies.values[0]}</b> open positions,
                followed by <b>{top_companies.index[1]}</b> and
                <b>{top_companies.index[2]}</b>.
                Consulting firms and training centers dominate the top rankings,
                reflecting strong demand for IT talent across all sectors.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Full Company Data")
    st.dataframe(df_comp[["title", "company", "city",
                            "contract_time", "date"]].reset_index(drop=True))
    st.download_button(
        label="Download as CSV",
        data=df_comp.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_companies_germany.csv",
        mime="text/csv"
    )
    show_footer()

# ══════════════════════════════════════════════════════════
# PAGE TOP REGIONS
# ══════════════════════════════════════════════════════════
elif page == "Top Regions":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            Top Hiring Regions in Germany
        </h1>
        <p style="color:{TEXTE}; font-size:15px; margin-bottom:10px;">
            Germany's IT market is concentrated in a few major cities.
            Understanding regional distribution helps candidates decide
            where to relocate and helps companies understand competition.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # FILTRES
    contract_filter = st.multiselect(
        "Filter by Contract Type",
        options=["full_time", "part_time"],
        default=[]
    )

    df_reg = df.copy()
    if contract_filter:
        df_reg = df_reg[df_reg["contract_time"].isin(contract_filter)]

    # GRAPH VILLES
    st.subheader("Offers by City")
    top_cities = df_reg["city"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    top_cities.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Top 10 Cities by Number of IT Job Offers",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(top_cities.values):
        ax.text(v + 0.5, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    # GRAPH SALAIRES PAR VILLE
    st.subheader("Average Salary by City")
    salary_by_city = df_salary.groupby("city")["salary_avg"].mean().sort_values(
        ascending=False).head(8)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    salary_by_city.plot(kind="barh", ax=ax, color=ROSE_DARK)
    ax.set_title("Average IT Salary by City (EUR)",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Average salary (EUR)", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(salary_by_city.values):
        ax.text(v + 100, i, f"{int(v):,}", va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    # KEY INSIGHT
    top_city     = top_cities.index[0]
    top_sal_city = salary_by_city.index[0]
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif; font-size:16px;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                <b>{top_city}</b> has the highest number of IT job offers
                with <b>{top_cities.values[0]}</b> positions available.
                However, <b>{top_sal_city}</b> offers the best average salary
                at <b>{int(salary_by_city.values[0]):,} EUR</b>.
                For maximum earning potential, Munich is the top destination.
                For maximum job opportunities, Berlin leads the market.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.download_button(
        label="Download as CSV",
        data=df_reg.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_regions_germany.csv",
        mime="text/csv"
    )
    show_footer() # ══════════════════════════════════════════════════════════
# PAGE LABOUR MARKET TRENDS
# ══════════════════════════════════════════════════════════
elif page == "Labour Market Trends":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            Labour Market Trends
        </h1>
        <p style="color:{TEXTE}; font-size:15px; margin-bottom:10px;">
            Tracking how the job market evolves over time reveals seasonal
            patterns, hiring peaks and market growth trends.
            This analysis covers hiring evolution, salary distribution
            and contract type breakdown.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # KPI SALAIRES
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Offers with Salary", len(df_salary))
    with col2:
        st.metric("Average Salary", f"{int(df_salary['salary_avg'].mean()):,} EUR")
    with col3:
        st.metric("Min Salary", f"{int(df_salary['salary_min'].min()):,} EUR")
    with col4:
        st.metric("Max Salary", f"{int(df_salary['salary_max'].max()):,} EUR")

    st.markdown("<br>", unsafe_allow_html=True)

    # GRAPH EVOLUTION TEMPORELLE
    st.subheader("Job Offers Evolution Over Time")
    df_time = df[df["date"].notna()].copy()
    offers_by_week = df_time.groupby(
        df_time["date"].dt.isocalendar().week).size()

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    offers_by_week.plot(kind="line", ax=ax, color=BORDEAUX,
                        marker="o", linewidth=2.5, markersize=5)
    ax.fill_between(offers_by_week.index, offers_by_week.values,
                    alpha=0.15, color=BORDEAUX)
    ax.set_title("Weekly Job Offers Evolution",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Week number", color=TEXTE)
    ax.set_ylabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    # GRAPH DISTRIBUTION SALAIRES
    st.subheader("Salary Distribution")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    df_salary["salary_avg"].hist(bins=20, ax=ax,
                                  color=BORDEAUX, edgecolor="white")
    ax.set_title("Salary Distribution in Germany IT Market",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Salary (EUR)", color=TEXTE)
    ax.set_ylabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    # GRAPH TYPES DE CONTRATS
    st.subheader("Contract Types Distribution")
    contract_types = df[df["contract_time"] != "Not provided"][
        "contract_time"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor(CREME)
    ax.set_facecolor(CREME)
    contract_types.plot(kind="bar", ax=ax, color=[BORDEAUX, ROSE_DARK])
    ax.set_title("Full-time vs Part-time Positions",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Contract type", color=TEXTE)
    ax.set_ylabel("Number of offers", color=TEXTE)
    ax.tick_params(colors=TEXTE, rotation=0)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    # KEY INSIGHT
    peak_week = offers_by_week.idxmax()
    st.markdown(f"""
        <div style="background:white; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif; font-size:16px;">
                Key Insight
            </p>
            <p style="color:{TEXTE};">
                Hiring peaks at <b>week {peak_week}</b> — the best time
                to apply for an IT job in Germany is between April and June.
                The average IT salary is <b>{int(df_salary['salary_avg'].mean()):,} EUR</b>
                and <b>92% of positions are full-time</b>.
                Munich offers the highest salaries while Berlin has the most opportunities.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.download_button(
        label="Download Salary Data as CSV",
        data=df_salary.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="salary_data_germany.csv",
        mime="text/csv"
    )
    show_footer()

# ══════════════════════════════════════════════════════════
# PAGE INSIGHTS
# ══════════════════════════════════════════════════════════
elif page == "Insights":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            Key Insights
        </h1>
        <p style="color:{TEXTE}; font-size:15px; margin-bottom:10px;">
            The most important conclusions from our analysis of
            the German IT job market.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    insights = [
        ("Berlin leads in volume",
         f"Berlin has the highest number of IT job offers with "
         f"{len(df[df['city']=='Berlin'])} positions available — "
         f"making it Germany's IT capital."),
        ("Munich pays the most",
         f"Munich offers the highest average IT salary at "
         f"{int(df_salary[df_salary['city']=='Munich']['salary_avg'].mean()):,} EUR, "
         f"significantly above the national average of "
         f"{int(df_salary['salary_avg'].mean()):,} EUR."),
        ("Data Engineering is the top job",
         "Data Engineer is the most demanded IT role in Germany, "
         "reflecting the growing need for data infrastructure and pipelines."),
        ("Machine Learning dominates skills",
         "Machine Learning is the most mentioned skill across all job offers, "
         "followed by Git and Python — mastering these three is essential."),
        ("Full-time dominates",
         "92% of IT positions in Germany are full-time. "
         "Part-time IT roles are rare and mostly in consulting."),
        ("Best time to apply is spring",
         "Hiring peaks between April and June — "
         "submitting applications in Q2 maximizes your chances."),
        ("Two sources, richer data",
         f"Combining Bundesagentur fur Arbeit ({len(df[df['source']=='Bundesagentur'])} offers) "
         f"and Adzuna ({len(df[df['source']=='Adzuna'])} offers) "
         f"gives a more complete picture of the market."),
        ("Consulting firms recruit the most",
         "Consulting and training companies like Reply Deutschland and "
         "alfatraining lead recruitment — IT talent is in demand across all sectors."),
    ]

    for i, (title, text) in enumerate(insights):
        color = BORDEAUX if i % 2 == 0 else ROSE_DARK
        st.markdown(f"""
            <div style="background:white; border-left:6px solid {color};
                        padding:20px 25px; border-radius:8px; margin-bottom:15px;
                        box-shadow:0 2px 8px rgba(107,30,46,0.08);">
                <p style="color:{color}; font-weight:bold;
                          font-family:Georgia,serif; font-size:15px;
                          margin:0 0 8px 0;">
                    {i+1}. {title}
                </p>
                <p style="color:{TEXTE}; margin:0; font-size:13px;">
                    {text}
                </p>
            </div>
        """, unsafe_allow_html=True)

    show_footer()

# ══════════════════════════════════════════════════════════
# PAGE ABOUT & METHODOLOGY
# ══════════════════════════════════════════════════════════
elif page == "About & Methodology":

    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            About & Methodology
        </h1>
        <p style="color:{TEXTE}; font-size:15px;">
            Everything you need to know about how this platform was built,
            where the data comes from and how it was processed.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # DATA SOURCES
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Data Sources</h2>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div style="background:white; border-top:5px solid {BORDEAUX};
                        padding:20px; border-radius:10px; height:200px;
                        box-shadow:0 2px 8px rgba(107,30,46,0.1);">
                <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;">
                    Bundesagentur fur Arbeit
                </h3>
                <p style="color:{TEXTE}; font-size:13px;">
                    Official German Federal Employment Agency API.
                    Provides verified job listings from official German employers.
                    Free and public access with key "jobboerse-jobsuche".
                </p>
                <p style="color:{ROSE_DARK}; font-size:12px;">
                    {len(df[df['source']=='Bundesagentur'])} offers collected
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style="background:white; border-top:5px solid {ROSE_DARK};
                        padding:20px; border-radius:10px; height:200px;
                        box-shadow:0 2px 8px rgba(107,30,46,0.1);">
                <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;">
                    Adzuna Jobs API
                </h3>
                <p style="color:{TEXTE}; font-size:13px;">
                    International job search engine with structured API access.
                    Provides salary data, job descriptions and contract types
                    not available in official sources.
                </p>
                <p style="color:{ROSE_DARK}; font-size:12px;">
                    {len(df[df['source']=='Adzuna'])} offers collected
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ETL PIPELINE
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>ETL Pipeline</h2>",
                unsafe_allow_html=True)

    steps = [
        ("Extract",   "collection.py + collection_adzuna.py",
         "API calls to both sources using Python requests library. "
         "5 job titles x 5 cities = 25 searches per source."),
        ("Transform", "merge.py + cleaning.py",
         "Merge both DataFrames, normalize city names, "
         "remove duplicates, filter salary outliers, parse dates."),
        ("Load",      "job_offers_germany_combined_clean.csv",
         "Final clean dataset with 1,120 offers and 15 columns "
         "ready for analysis and visualization."),
        ("Analyze",   "analysis.py",
         "Exploratory Data Analysis with pandas and matplotlib. "
         "Top jobs, skills, companies, regions and salary analysis."),
        ("Visualize", "app.py",
         "Interactive Streamlit dashboard deployed on Streamlit Cloud "
         "with filters, charts and export features."),
    ]

    for step, file, desc in steps:
        st.markdown(f"""
            <div style="display:flex; align-items:flex-start;
                        margin-bottom:12px;">
                <div style="background:{BORDEAUX}; color:white;
                            padding:8px 14px; border-radius:6px;
                            font-family:Georgia,serif; font-weight:bold;
                            min-width:100px; text-align:center;
                            margin-right:15px; font-size:13px;">
                    {step}
                </div>
                <div style="background:white; padding:12px 16px;
                            border-radius:6px; flex:1;
                            box-shadow:0 2px 6px rgba(107,30,46,0.08);">
                    <p style="color:{BORDEAUX}; font-weight:bold;
                              margin:0 0 4px 0; font-size:12px;">
                        {file}
                    </p>
                    <p style="color:{TEXTE}; margin:0; font-size:12px;">
                        {desc}
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # TECH STACK
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Tech Stack</h2>",
                unsafe_allow_html=True)

    techs = [
        ("Python 3.13",  "Core programming language"),
        ("Pandas",       "Data manipulation and analysis"),
        ("Matplotlib",   "Data visualization and charts"),
        ("Streamlit",    "Interactive web dashboard"),
        ("Requests",     "HTTP API calls and data collection"),
        ("Git + GitHub", "Version control and code hosting"),
    ]

    cols = st.columns(3)
    for i, (tech, desc) in enumerate(techs):
        with cols[i % 3]:
            st.markdown(f"""
                <div style="background:white; border-left:4px solid {BORDEAUX};
                            padding:12px 15px; border-radius:6px;
                            margin-bottom:10px;
                            box-shadow:0 2px 6px rgba(107,30,46,0.08);">
                    <p style="color:{BORDEAUX}; font-weight:bold;
                              margin:0 0 3px 0; font-size:13px;">{tech}</p>
                    <p style="color:{TEXTE}; margin:0;
                              font-size:11px;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # CONTACT
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Contact</h2>",
                unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background:white; padding:20px; border-radius:10px;
                    box-shadow:0 2px 8px rgba(107,30,46,0.1);">
            <p style="color:{TEXTE}; margin:0 0 8px 0;">
                <b style="color:{BORDEAUX};">Author :</b> Nour Brahim
            </p>
            <p style="color:{TEXTE}; margin:0 0 8px 0;">
                <b style="color:{BORDEAUX};">GitHub :</b>
                <a href="https://github.com/brahimnour/labour-market-germany"
                   style="color:{BORDEAUX};">
                    github.com/brahimnour/labour-market-germany
                </a>
            </p>
            <p style="color:{TEXTE}; margin:0;">
                <b style="color:{BORDEAUX};">LinkedIn :</b>
                <a href="https://www.linkedin.com/in/nour-brahim"
                   style="color:{BORDEAUX};">
                    linkedin.com/in/nour-brahim
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)

    show_footer()

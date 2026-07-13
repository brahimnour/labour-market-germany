import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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

# DARK MODE COLORS
DARK_BG   = "#1A1A2E"
DARK_CARD = "#16213E"
DARK_TEXT = "#E0E0E0"

# TRADUCTIONS
translations = {
    "EN": {
        "title"        : "German Employment Analytics Platform",
        "subtitle"     : "A comprehensive analysis of the German IT job market based on 1,120 real job offers collected from two official sources.",
        "explore_btn"  : "Explore the Analysis",
        "choose"       : "What would you like to explore?",
        "total_offers" : "Total Offers",
        "cities"       : "Cities",
        "companies"    : "Companies",
        "avg_salary"   : "Avg Salary",
        "sources"      : "Data Sources",
        "top_jobs"     : "Top Jobs",
        "top_skills"   : "Top Skills",
        "top_companies": "Top Companies",
        "top_regions"  : "Top Regions",
        "trends"       : "Labour Market Trends",
        "insights"     : "Insights",
        "about"        : "About & Methodology",
        "desc_jobs"    : "Most demanded IT jobs",
        "desc_skills"  : "Most requested technical skills",
        "desc_comp"    : "Companies hiring the most",
        "desc_regions" : "Cities and regions recruiting the most",
        "desc_trends"  : "Hiring evolution and salary trends",
        "desc_insights": "Key conclusions from the analysis",
        "desc_about"   : "Data sources and methodology",
        "footer_about" : "About",
        "footer_contact": "Contact",
        "key_insight"  : "Key Insight",
        "filter_city"  : "Filter by City",
        "filter_contract": "Filter by Contract Type",
        "search_job"   : "Search a job title",
        "search_comp"  : "Search a company",
        "download"     : "Download as CSV",
        "full_data"    : "Full Data",
        "dark_mode"    : "Dark Mode",
    },
    "FR": {
        "title"        : "Plateforme d'Analyse du Marché de l'Emploi Allemand",
        "subtitle"     : "Une analyse complète du marché IT allemand basée sur 1 120 offres d'emploi réelles collectées depuis deux sources officielles.",
        "explore_btn"  : "Explorer l'Analyse",
        "choose"       : "Que voulez-vous explorer ?",
        "total_offers" : "Total Offres",
        "cities"       : "Villes",
        "companies"    : "Entreprises",
        "avg_salary"   : "Salaire Moy.",
        "sources"      : "Sources",
        "top_jobs"     : "Top Métiers",
        "top_skills"   : "Top Compétences",
        "top_companies": "Top Entreprises",
        "top_regions"  : "Top Régions",
        "trends"       : "Tendances du Marché",
        "insights"     : "Insights",
        "about"        : "À Propos",
        "desc_jobs"    : "Métiers IT les plus demandés",
        "desc_skills"  : "Compétences techniques les plus recherchées",
        "desc_comp"    : "Entreprises qui recrutent le plus",
        "desc_regions" : "Villes et régions qui recrutent le plus",
        "desc_trends"  : "Évolution du recrutement et des salaires",
        "desc_insights": "Conclusions clés de l'analyse",
        "desc_about"   : "Sources de données et méthodologie",
        "footer_about" : "À Propos",
        "footer_contact": "Contact",
        "key_insight"  : "Insight Clé",
        "filter_city"  : "Filtrer par Ville",
        "filter_contract": "Filtrer par Type de Contrat",
        "search_job"   : "Rechercher un métier",
        "search_comp"  : "Rechercher une entreprise",
        "download"     : "Télécharger en CSV",
        "full_data"    : "Données Complètes",
        "dark_mode"    : "Mode Sombre",
    },
    "DE": {
        "title"        : "Deutsche Arbeitsmarkt-Analyseplattform",
        "subtitle"     : "Eine umfassende Analyse des deutschen IT-Arbeitsmarkts basierend auf 1.120 echten Stellenangeboten aus zwei offiziellen Quellen.",
        "explore_btn"  : "Analyse erkunden",
        "choose"       : "Was möchten Sie erkunden?",
        "total_offers" : "Angebote",
        "cities"       : "Städte",
        "companies"    : "Unternehmen",
        "avg_salary"   : "Durchsch. Gehalt",
        "sources"      : "Quellen",
        "top_jobs"     : "Top Jobs",
        "top_skills"   : "Top Fähigkeiten",
        "top_companies": "Top Unternehmen",
        "top_regions"  : "Top Regionen",
        "trends"       : "Markttrends",
        "insights"     : "Erkenntnisse",
        "about"        : "Über uns",
        "desc_jobs"    : "Meistgefragte IT-Jobs",
        "desc_skills"  : "Meistgefragte technische Fähigkeiten",
        "desc_comp"    : "Unternehmen mit den meisten Stellenangeboten",
        "desc_regions" : "Städte mit den meisten Stellenangeboten",
        "desc_trends"  : "Entwicklung der Einstellungen und Gehälter",
        "desc_insights": "Wichtigste Erkenntnisse der Analyse",
        "desc_about"   : "Datenquellen und Methodik",
        "footer_about" : "Über uns",
        "footer_contact": "Kontakt",
        "key_insight"  : "Wichtige Erkenntnis",
        "filter_city"  : "Nach Stadt filtern",
        "filter_contract": "Nach Vertragstyp filtern",
        "search_job"   : "Berufsbezeichnung suchen",
        "search_comp"  : "Unternehmen suchen",
        "download"     : "Als CSV herunterladen",
        "full_data"    : "Alle Daten",
        "dark_mode"    : "Dunkelmodus",
    }
}

# SESSION STATE
if "lang" not in st.session_state:
    st.session_state.lang = "EN"
if "dark" not in st.session_state:
    st.session_state.dark = False
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "show_explore" not in st.session_state:
    st.session_state.show_explore = False

t   = translations[st.session_state.lang]
BG  = DARK_BG   if st.session_state.dark else CREME
TXT = DARK_TEXT if st.session_state.dark else TEXTE
CARD = DARK_CARD if st.session_state.dark else "#FFFFFF"

# CSS GLOBAL
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {BG};
        }}
        section[data-testid="stSidebar"] {{
            display: none;
        }}
        h1, h2, h3 {{
            color: {BORDEAUX};
            font-family: Georgia, serif;
        }}
        p, li {{
            color: {TXT};
        }}
        .stDownloadButton > button {{
            background-color: {BORDEAUX};
            color: white;
            border: none;
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

df        = load_data()
df_salary = df[df["salary_avg"].notna()]

# FOOTER
def show_footer():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background:{BORDEAUX}; padding:30px; margin-top:40px;
                    border-radius:10px; text-align:center;">
            <p style="color:{ROSE}; font-family:Georgia,serif; font-size:16px;
                      font-weight:bold; margin-bottom:10px;">
                German Employment Analytics Platform
            </p>
            <p style="color:{ROSE}; font-size:12px; margin-bottom:15px;">
                Bundesagentur fur Arbeit + Adzuna API — {len(df)} offers
            </p>
            <p style="margin:8px 0;">
                <a href="https://github.com/brahimnour/labour-market-germany"
                   style="color:white; text-decoration:none; margin:0 12px; font-size:13px;">
                    GitHub
                </a>
                <a href="https://www.linkedin.com/in/nour-brahim"
                   style="color:white; text-decoration:none; margin:0 12px; font-size:13px;">
                    LinkedIn
                </a>
                <a href="mailto:brahimnour220@gmail.com"
                   style="color:white; text-decoration:none; margin:0 12px; font-size:13px;">
                    {t['footer_contact']}
                </a>
            </p>
            <p style="color:{ROSE_DARK}; font-size:11px; margin-top:15px;">
                Built with Python · Pandas · Matplotlib · Streamlit
            </p>
        </div>
    """, unsafe_allow_html=True)

# BACK BUTTON
def back_button():
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.session_state.show_explore = False
        st.rerun()

# TOP BAR
col_lang1, col_lang2, col_lang3, col_dark, col_space = st.columns([1, 1, 1, 1, 6])
with col_lang1:
    if st.button("EN"):
        st.session_state.lang = "EN"
        st.rerun()
with col_lang2:
    if st.button("FR"):
        st.session_state.lang = "FR"
        st.rerun()
with col_lang3:
    if st.button("DE"):
        st.session_state.lang = "DE"
        st.rerun()
with col_dark:
    if st.button("🌙" if not st.session_state.dark else "☀️"):
        st.session_state.dark = not st.session_state.dark
        st.rerun()

# PAGE HOME
if st.session_state.page == "Home":

    # HERO
    st.markdown(f"""
        <div style="background:linear-gradient(135deg, {BORDEAUX}, #9B3A4A);
                    padding:80px 50px; text-align:center; margin-bottom:40px;
                    border-radius:12px;">
            <p style="color:{ROSE}; font-size:12px; letter-spacing:5px;
                      margin-bottom:8px;">DATA INTELLIGENCE PLATFORM</p>
            <h1 style="color:white; font-size:48px; font-family:Georgia,serif;
                       margin-bottom:16px; letter-spacing:2px;">
                {t['title']}
            </h1>
            <p style="color:{ROSE}; font-size:16px; max-width:650px;
                      margin:0 auto 30px auto; line-height:1.6;">
                {t['subtitle']}
            </p>
        </div>
    """, unsafe_allow_html=True)

    # KPI CARDS
    col1, col2, col3, col4, col5 = st.columns(5)
    kpis = [
        (t['total_offers'], f"{len(df):,}"),
        (t['cities'],       df['city'].nunique()),
        (t['companies'],    df['company'].nunique()),
        (t['sources'],      "2"),
        (t['avg_salary'],   f"{int(df_salary['salary_avg'].mean()):,} EUR"),
    ]
    for col, (label, value) in zip([col1, col2, col3, col4, col5], kpis):
        with col:
            st.markdown(f"""
                <div style="background:{CARD}; padding:15px; border-radius:10px;
                            border-left:4px solid {BORDEAUX}; text-align:center;
                            box-shadow:0 2px 8px rgba(107,30,46,0.1);
                            margin-bottom:10px;">
                    <p style="color:{ROSE_DARK}; font-size:11px; margin:0;">{label}</p>
                    <p style="color:{BORDEAUX}; font-size:20px; font-weight:bold;
                              font-family:Georgia,serif; margin:4px 0 0 0;">{value}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # EXPLORE BUTTON
    col_center = st.columns([2, 2, 2])[1]
    with col_center:
        if st.button(f"🔍 {t['explore_btn']}", use_container_width=True):
            st.session_state.show_explore = not st.session_state.show_explore
            st.rerun()

    # EXPLORE CARDS
    if st.session_state.show_explore:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
            <h2 style="color:{BORDEAUX}; font-family:Georgia,serif;
                       text-align:center; margin-bottom:20px;">
                {t['choose']}
            </h2>
        """, unsafe_allow_html=True)

        explore_items = [
            ("top_jobs",       t['top_jobs'],       t['desc_jobs']),
            ("top_skills",     t['top_skills'],     t['desc_skills']),
            ("top_companies",  t['top_companies'],  t['desc_comp']),
            ("top_regions",    t['top_regions'],    t['desc_regions']),
            ("trends",         t['trends'],         t['desc_trends']),
            ("insights",       t['insights'],       t['desc_insights']),
            ("about",          t['about'],          t['desc_about']),
        ]

        col1, col2, col3, col4 = st.columns(4)
        cols_grid = [col1, col2, col3, col4, col1, col2, col3]

        for i, (page_key, title, desc) in enumerate(explore_items):
            with cols_grid[i]:
                st.markdown(f"""
                    <div style="background:{CARD}; border-top:4px solid {BORDEAUX};
                                padding:18px; border-radius:10px; margin-bottom:12px;
                                box-shadow:0 3px 10px rgba(107,30,46,0.1);
                                min-height:110px;">
                        <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;
                                   font-size:14px; margin:0 0 6px 0;">{title}</h3>
                        <p style="color:{TXT}; font-size:12px; margin:0;">{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"→ {title}", key=f"btn_{page_key}",
                             use_container_width=True):
                    st.session_state.page = page_key
                    st.session_state.show_explore = False
                    st.rerun()

    show_footer()

# PAGE TOP JOBS
elif st.session_state.page == "top_jobs":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['top_jobs']}
        </h1>
        <p style="color:{TXT}; font-size:15px; margin-bottom:10px;">
            The German IT market is highly competitive. Understanding which job titles
            appear most frequently helps candidates target their applications.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        city_filter = st.multiselect(
            t['filter_city'],
            options=sorted(df["city"].dropna().unique()),
            default=[]
        )
    with col2:
        search = st.text_input(t['search_job'], placeholder="e.g. Data Engineer")

    df_jobs = df.copy()
    if city_filter:
        df_jobs = df_jobs[df_jobs["city"].isin(city_filter)]
    if search:
        df_jobs = df_jobs[df_jobs["title"].str.contains(
            search, case=False, na=False)]

    st.markdown(f"**{len(df_jobs)} offers**")
    top_jobs = df_jobs["title"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    top_jobs.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Top 10 Most Demanded IT Jobs",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(top_jobs.values):
        ax.text(v + 0.1, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(f"""
        <div style="background:{CARD}; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif;">{t['key_insight']}</p>
            <p style="color:{TXT};">
                <b>{top_jobs.index[0]}</b> is the most demanded IT job
                with <b>{top_jobs.values[0]}</b> open positions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader(t['full_data'])
    st.dataframe(df_jobs[["title", "company", "city",
                            "date", "source"]].reset_index(drop=True))
    st.download_button(
        label=t['download'],
        data=df_jobs.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_jobs_germany.csv",
        mime="text/csv"
    )
    show_footer()

# PAGE TOP SKILLS
elif st.session_state.page == "top_skills":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['top_skills']}
        </h1>
        <p style="color:{TXT}; font-size:15px; margin-bottom:10px;">
            Skills extracted from job titles and descriptions.
            Knowing which skills are most requested helps prioritize learning.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    city_filter = st.multiselect(
        t['filter_city'],
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

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    colors = [BORDEAUX if i < 3 else ROSE_DARK for i in range(len(skill_series))]
    skill_series.plot(kind="barh", ax=ax, color=colors)
    ax.set_title("Most Demanded IT Skills",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of mentions", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(skill_series.values):
        ax.text(v + 0.1, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    top3 = mpatches.Patch(color=BORDEAUX,  label="Top 3")
    rest = mpatches.Patch(color=ROSE_DARK, label="Others")
    ax.legend(handles=[top3, rest])
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(f"""
        <div style="background:{CARD}; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif;">{t['key_insight']}</p>
            <p style="color:{TXT};">
                Top 3 : <b>{skill_series.index[0]}</b>,
                <b>{skill_series.index[1]}</b> and
                <b>{skill_series.index[2]}</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.dataframe(skill_series.reset_index().rename(
        columns={"index": "Skill", 0: "Mentions"}))
    st.download_button(
        label=t['download'],
        data=skill_series.reset_index().to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_skills_germany.csv",
        mime="text/csv"
    )
    show_footer()

# PAGE TOP COMPANIES
elif st.session_state.page == "top_companies":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['top_companies']}
        </h1>
        <p style="color:{TXT}; font-size:15px; margin-bottom:10px;">
            Identifying which companies post the most offers gives candidates
            a direct target list for applications.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        city_filter = st.multiselect(
            t['filter_city'],
            options=sorted(df["city"].dropna().unique()),
            default=[]
        )
    with col2:
        search_comp = st.text_input(t['search_comp'], placeholder="e.g. Google")

    df_comp = df.copy()
    if city_filter:
        df_comp = df_comp[df_comp["city"].isin(city_filter)]
    if search_comp:
        df_comp = df_comp[df_comp["company"].str.contains(
            search_comp, case=False, na=False)]

    top_companies = df_comp["company"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    top_companies.plot(kind="barh", ax=ax, color=ROSE_DARK)
    ax.set_title("Top 10 Companies",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(top_companies.values):
        ax.text(v + 0.1, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(f"""
        <div style="background:{CARD}; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif;">{t['key_insight']}</p>
            <p style="color:{TXT};">
                <b>{top_companies.index[0]}</b> leads with
                <b>{top_companies.values[0]}</b> positions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.dataframe(df_comp[["title", "company", "city",
                            "contract_time", "date"]].reset_index(drop=True))
    st.download_button(
        label=t['download'],
        data=df_comp.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_companies_germany.csv",
        mime="text/csv"
    )
    show_footer()

# PAGE TOP REGIONS
elif st.session_state.page == "top_regions":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['top_regions']}
        </h1>
        <p style="color:{TXT}; font-size:15px; margin-bottom:10px;">
            Germany's IT market is concentrated in a few major cities.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    contract_filter = st.multiselect(
        t['filter_contract'],
        options=["full_time", "part_time"],
        default=[]
    )
    df_reg = df.copy()
    if contract_filter:
        df_reg = df_reg[df_reg["contract_time"].isin(contract_filter)]

    st.subheader("Offers by City")
    top_cities = df_reg["city"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    top_cities.plot(kind="barh", ax=ax, color=BORDEAUX)
    ax.set_title("Top 10 Cities",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Number of offers", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(top_cities.values):
        ax.text(v + 0.5, i, str(v), va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Average Salary by City")
    salary_by_city = df_salary.groupby("city")["salary_avg"].mean().sort_values(
        ascending=False).head(8)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    salary_by_city.plot(kind="barh", ax=ax, color=ROSE_DARK)
    ax.set_title("Average Salary by City (EUR)",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Average salary (EUR)", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    for i, v in enumerate(salary_by_city.values):
        ax.text(v + 100, i, f"{int(v):,}", va="center",
                color=BORDEAUX, fontweight="bold", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(f"""
        <div style="background:{CARD}; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif;">{t['key_insight']}</p>
            <p style="color:{TXT};">
                <b>{top_cities.index[0]}</b> has the most offers
                ({top_cities.values[0]}).
                <b>{salary_by_city.index[0]}</b> offers the best salary
                ({int(salary_by_city.values[0]):,} EUR).
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.download_button(
        label=t['download'],
        data=df_reg.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="top_regions_germany.csv",
        mime="text/csv"
    )
    show_footer()

# PAGE TRENDS
elif st.session_state.page == "trends":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['trends']}
        </h1>
        <p style="color:{TXT}; font-size:15px; margin-bottom:10px;">
            Tracking market evolution reveals seasonal patterns and hiring peaks.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Offers with Salary", len(df_salary))
    with col2:
        st.metric("Average Salary",
                  f"{int(df_salary['salary_avg'].mean()):,} EUR")
    with col3:
        st.metric("Min Salary",
                  f"{int(df_salary['salary_min'].min()):,} EUR")
    with col4:
        st.metric("Max Salary",
                  f"{int(df_salary['salary_max'].max()):,} EUR")

    st.markdown("<br>", unsafe_allow_html=True)

    df_time = df[df["date"].notna()].copy()
    offers_by_week = df_time.groupby(
        df_time["date"].dt.isocalendar().week).size()

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    offers_by_week.plot(kind="line", ax=ax, color=BORDEAUX,
                        marker="o", linewidth=2.5, markersize=5)
    ax.fill_between(offers_by_week.index, offers_by_week.values,
                    alpha=0.15, color=BORDEAUX)
    ax.set_title("Weekly Job Offers Evolution",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Week number", color=TXT)
    ax.set_ylabel("Number of offers", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    df_salary["salary_avg"].hist(bins=20, ax=ax,
                                  color=BORDEAUX, edgecolor="white")
    ax.set_title("Salary Distribution",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Salary (EUR)", color=TXT)
    ax.set_ylabel("Number of offers", color=TXT)
    ax.tick_params(colors=TXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    contract_types = df[df["contract_time"] != "Not provided"][
        "contract_time"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    contract_types.plot(kind="bar", ax=ax, color=[BORDEAUX, ROSE_DARK])
    ax.set_title("Contract Types",
                 color=BORDEAUX, fontfamily="serif", fontsize=14)
    ax.set_xlabel("Contract type", color=TXT)
    ax.set_ylabel("Number of offers", color=TXT)
    ax.tick_params(colors=TXT, rotation=0)
    for spine in ax.spines.values():
        spine.set_edgecolor(ROSE_DARK)
    plt.tight_layout()
    st.pyplot(fig)

    peak_week = offers_by_week.idxmax()
    st.markdown(f"""
        <div style="background:{CARD}; border-left:5px solid {BORDEAUX};
                    padding:20px; border-radius:8px; margin:20px 0;">
            <p style="color:{BORDEAUX}; font-weight:bold;
                      font-family:Georgia,serif;">{t['key_insight']}</p>
            <p style="color:{TXT};">
                Hiring peaks at <b>week {peak_week}</b>.
                Average salary : <b>{int(df_salary['salary_avg'].mean()):,} EUR</b>.
                92% full-time positions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.download_button(
        label=t['download'],
        data=df_salary.to_csv(index=False, sep=";").encode("utf-8"),
        file_name="salary_data_germany.csv",
        mime="text/csv"
    )
    show_footer()

# PAGE INSIGHTS
elif st.session_state.page == "insights":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['insights']}
        </h1>
        <p style="color:{TXT}; font-size:15px; margin-bottom:10px;">
            Key conclusions from our analysis of the German IT job market.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    insights_list = [
        ("Berlin leads in volume",
         f"Berlin has {len(df[df['city']=='Berlin'])} IT positions — Germany's IT capital."),
        ("Munich pays the most",
         f"Munich average salary : {int(df_salary[df_salary['city']=='Munich']['salary_avg'].mean()):,} EUR."),
        ("Data Engineering is top job",
         "Data Engineer is the most demanded IT role in Germany."),
        ("Machine Learning dominates",
         "Machine Learning is the most mentioned skill across all offers."),
        ("Full-time dominates",
         "92% of IT positions are full-time."),
        ("Best time to apply is spring",
         "Hiring peaks between April and June."),
        ("Two sources, richer data",
         f"Bundesagentur ({len(df[df['source']=='Bundesagentur'])}) + Adzuna ({len(df[df['source']=='Adzuna'])}) offers."),
        ("Consulting firms recruit most",
         "Reply Deutschland and alfatraining lead IT recruitment."),
    ]

    for i, (title, text) in enumerate(insights_list):
        color = BORDEAUX if i % 2 == 0 else ROSE_DARK
        st.markdown(f"""
            <div style="background:{CARD}; border-left:6px solid {color};
                        padding:20px 25px; border-radius:8px; margin-bottom:15px;
                        box-shadow:0 2px 8px rgba(107,30,46,0.08);">
                <p style="color:{color}; font-weight:bold;
                          font-family:Georgia,serif; font-size:15px;
                          margin:0 0 8px 0;">{i+1}. {title}</p>
                <p style="color:{TXT}; margin:0; font-size:13px;">{text}</p>
            </div>
        """, unsafe_allow_html=True)

    show_footer()

# PAGE ABOUT
elif st.session_state.page == "about":
    back_button()
    st.markdown(f"""
        <h1 style="color:{BORDEAUX}; font-family:Georgia,serif;">
            {t['about']}
        </h1>
        <p style="color:{TXT}; font-size:15px;">
            Everything about how this platform was built.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Data Sources</h2>",
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div style="background:{CARD}; border-top:5px solid {BORDEAUX};
                        padding:20px; border-radius:10px;">
                <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;">
                    Bundesagentur fur Arbeit
                </h3>
                <p style="color:{TXT}; font-size:13px;">
                    Official German Federal Employment Agency API.
                    Free and public access.
                </p>
                <p style="color:{ROSE_DARK}; font-size:12px;">
                    {len(df[df['source']=='Bundesagentur'])} offers collected
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style="background:{CARD}; border-top:5px solid {ROSE_DARK};
                        padding:20px; border-radius:10px;">
                <h3 style="color:{BORDEAUX}; font-family:Georgia,serif;">
                    Adzuna Jobs API
                </h3>
                <p style="color:{TXT}; font-size:13px;">
                    Provides salary data, descriptions and contract types.
                </p>
                <p style="color:{ROSE_DARK}; font-size:12px;">
                    {len(df[df['source']=='Adzuna'])} offers collected
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>ETL Pipeline</h2>",
                unsafe_allow_html=True)

    steps = [
        ("Extract",   "collection.py + collection_adzuna.py",
         "API calls. 5 jobs x 5 cities = 25 searches per source."),
        ("Transform", "merge.py + cleaning.py",
         "Merge, normalize, remove duplicates, parse dates."),
        ("Load",      "job_offers_germany_combined_clean.csv",
         "1,120 offers, 15 columns."),
        ("Analyze",   "analysis.py", "EDA with pandas and matplotlib."),
        ("Visualize", "app.py", "Streamlit dashboard on Streamlit Cloud."),
    ]

    for step, file, desc in steps:
        st.markdown(f"""
            <div style="display:flex; align-items:flex-start; margin-bottom:12px;">
                <div style="background:{BORDEAUX}; color:white;
                            padding:8px 14px; border-radius:6px;
                            font-weight:bold; min-width:100px;
                            text-align:center; margin-right:15px; font-size:13px;">
                    {step}
                </div>
                <div style="background:{CARD}; padding:12px 16px;
                            border-radius:6px; flex:1;">
                    <p style="color:{BORDEAUX}; font-weight:bold;
                              margin:0 0 4px 0; font-size:12px;">{file}</p>
                    <p style="color:{TXT}; margin:0; font-size:12px;">{desc}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Tech Stack</h2>",
                unsafe_allow_html=True)

    techs = [
        ("Python 3.13", "Core programming language"),
        ("Pandas",      "Data manipulation"),
        ("Matplotlib",  "Charts and graphs"),
        ("Streamlit",   "Web dashboard"),
        ("Requests",    "API data collection"),
        ("Git + GitHub","Version control"),
    ]
    cols = st.columns(3)
    for i, (tech, desc) in enumerate(techs):
        with cols[i % 3]:
            st.markdown(f"""
                <div style="background:{CARD}; border-left:4px solid {BORDEAUX};
                            padding:12px 15px; border-radius:6px; margin-bottom:10px;">
                    <p style="color:{BORDEAUX}; font-weight:bold;
                              margin:0 0 3px 0; font-size:13px;">{tech}</p>
                    <p style="color:{TXT}; margin:0; font-size:11px;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{BORDEAUX}; font-family:Georgia,serif;'>Contact</h2>",
                unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background:{CARD}; padding:20px; border-radius:10px;">
            <p style="color:{TXT}; margin:0 0 8px 0;">
                <b style="color:{BORDEAUX};">Author :</b> Nour Brahim
            </p>
            <p style="color:{TXT}; margin:0 0 8px 0;">
                <b style="color:{BORDEAUX};">GitHub :</b>
                <a href="https://github.com/brahimnour/labour-market-germany"
                   style="color:{BORDEAUX};">
                    github.com/brahimnour/labour-market-germany
                </a>
            </p>
            <p style="color:{TXT}; margin:0 0 8px 0;">
                <b style="color:{BORDEAUX};">LinkedIn :</b>
                <a href="https://www.linkedin.com/in/nour-brahim"
                   style="color:{BORDEAUX};">
                    linkedin.com/in/nour-brahim
                </a>
            </p>
            <p style="color:{TXT}; margin:0;">
                <b style="color:{BORDEAUX};">Email :</b>
                <a href="mailto:brahimnour220@gmail.com"
                   style="color:{BORDEAUX};">
                    brahimnour220@gmail.com
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)

    show_footer()

import os
import re
import streamlit as st
import pandas as pd
import mysql.connector
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration with fallbacks
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "ola_ride_db")
DB_PORT = os.getenv("DB_PORT", "3306")

# Page configuration
st.set_page_config(
    page_title="Ola Ride Insights Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Database Connection ----------
def get_connection():
    """Simple database connection with cloud/local detection"""
    try:
        if "mysql" in st.secrets:  # when running on Streamlit Cloud
            return mysql.connector.connect(
                host=st.secrets["mysql"]["host"],
                port=int(st.secrets["mysql"].get("port", "3306")),
                user=st.secrets["mysql"]["user"],
                password=st.secrets["mysql"]["password"],
                database=st.secrets["mysql"]["database"]
            )
        else:  # local development with .env
            return mysql.connector.connect(
                host=DB_HOST,
                port=int(DB_PORT),
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None

# ---------- Load Queries from GitHub ----------
@st.cache_data
def load_queries():
    """Load SQL queries from GitHub repository"""
    url = "https://raw.githubusercontent.com/Neeraj08823/OLA-Ride/main/queries.sql"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to fetch queries from GitHub")
        return {}
    
    def parse_queries_with_comments(script):
        blocks = []
        current_comment = None
        current_query = []
        
        for line in script.splitlines():
            if line.strip().startswith('--'):
                if current_comment and current_query:
                    blocks.append((current_comment, '\n'.join(current_query).strip()))
                    current_query = []
                current_comment = line.strip()
            else:
                if line.strip() or current_query:
                    current_query.append(line)
                    
        if current_comment and current_query:
            blocks.append((current_comment, '\n'.join(current_query).strip()))
            
        return [block for block in blocks if block[1] and len(block[1].strip()) > 2]

    # Parse queries and create dictionary
    queries = {}
    parsed_queries = parse_queries_with_comments(response.text)
    
    for comment, query in parsed_queries:
        # Clean the comment to use as key
        clean_comment = comment[2:].strip()  # Remove -- and whitespace
        queries[clean_comment] = query

    if queries:
        return queries
    else:
        raise Exception("No queries found")
    
    
# ---------- Execute Query ----------
@st.cache_data
def run_query(query):
    """Execute SQL query and return DataFrame"""
    conn = get_connection()
    if conn is None:
        return pd.DataFrame()
    
    try:
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Query execution failed: {e}")
        if conn:
            conn.close()
        return pd.DataFrame()

# Main title
st.markdown(
    "<h1 style='text-align: center;'>🚗 Ola Ride Insights Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Power BI Dashboard","SQL Analysis"]
)


# ================= SQL Analysis Page =================
if page == "SQL Analysis":
    st.markdown(
    "<h2 style='text-align: center;'>📑 Ola Ride Analysis</h2>",
    unsafe_allow_html=True
)

    # Load queries
    queries_dict = load_queries()
    comment_list = list(queries_dict.keys())

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🧩 Select Query")
        selected_label = st.selectbox("", comment_list, label_visibility='collapsed')
        run_btn = st.button("Ask❔", width='stretch')
        if run_btn:
            st.success("✅ Query Executed Successfully!")

    with col2:
        if run_btn:
            st.subheader("📊 Details")
            try:
                query = queries_dict[selected_label]
                df_result = run_query(query)    
                st.dataframe(df_result, width='stretch')
            except Exception as e:
                st.error(f"❌ Error: {e}")


# ================= Power BI Dashboard Page =================
elif page == "Power BI Dashboard":
    st.markdown(
    "<h2 style='text-align: center;'>📈 Interactive Power BI Dashboard</h2>",
    unsafe_allow_html=True
)
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiN2U4MTlhMDEtNWEwNi00MWZlLWI1OTYtY2MxOTI2NzVjMTVjIiwidCI6ImU0MmJhN2Y2LTY1OWEtNDdkMS1iNzg2LTYyODhjODllYzM0MiJ9&pageName=7aa61ed7c83d1369c8d0",
        width=1500,
        height=600,
        scrolling=True,
    )
# --- FOOTER ---
st.markdown(
    """
    <div style="text-align: center; padding: 12px; font-size: 14px; color: #aaa;">
        Build using Streamlit, Power BI & MySQL<br>
        © 2025 Neeraj Kumar | 
        <a href="https://github.com/Neeraj08823/OLA-Ride" target="_blank" style="color:#111d4a; text-decoration: none;">GitHub Repo</a>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
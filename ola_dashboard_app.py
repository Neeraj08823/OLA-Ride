import os
import re
import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Page configuration
st.set_page_config(
    page_title="Ola Ride Insights Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Page configuration
st.set_page_config(
    page_title="Ola Ride Insights Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Utility to load queries from queries.sql ---
def load_queries(sql_file="queries.sql"):
    with open(sql_file, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"--\s*(Q\d+)\s*[:-]\s*(.+?)\n(.*?)(?=(?:\n--\s*Q\d+\s*[:-])|\Z)"
    matches = re.findall(pattern, content, flags=re.S)

    queries = {}
    for qnum, title, sql_body in matches:
        key = f"{qnum} - {title.strip()}"
        # remove inline comment lines inside body
        body_lines = [ln for ln in sql_body.splitlines() if not ln.strip().startswith("--")]
        q_clean = "\n".join(body_lines).strip().rstrip(";")
        queries[key] = q_clean
    return queries


# Main title
st.markdown(
    "<h1 style='text-align: center;'>🚗 Ola Ride Insights Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Power BI Dashboard","SQL Analysis"]
)


@st.cache_data
def run_query(query=None):
    """Run a SQL query and return the result as a DataFrame.
    If no query is provided, fetch default overview data."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        if query is None:
            query = "SELECT * FROM ola_rides LIMIT 1000"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return pd.DataFrame()  # return empty df if error

# Load default data for Overview page
df = run_query()


# ================= SQL Analysis Page =================
if page == "SQL Analysis":
    st.markdown(
    "<h2 style='text-align: center;'>📑 Ola Ride Analysis</h2>",
    unsafe_allow_html=True
)

    # Load queries
    queries_dict = load_queries("queries.sql")
    comment_list = list(queries_dict.keys())

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🧩 Select Query")
        selected_label = st.selectbox("", comment_list, label_visibility='collapsed')
        run_btn = st.button("Ask❔", use_container_width=True)
        if run_btn:
            st.success("✅ Query Executed Successfully!")

    with col2:
        if run_btn:
            st.subheader("📊 Details")
            try:
                query = queries_dict[selected_label]
                df_result = run_query(query)    
                st.dataframe(df_result, use_container_width=True)
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

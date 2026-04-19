import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Customer Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("Customer Shopping Behavior Dashboard",text_alignment="center")
st.subheader("Interactive analysis of customer shopping patterns",text_alignment="center")


# Load csv file
@st.cache_data()
def load_data():
    df = pd.read_csv("customer_shopping_behavior.csv")
    return df

df = load_data()

# Sidebar
st.sidebar.title("🔍 Filter")
category = st.sidebar.multiselect(
    "Category",
    df['Category'].unique()
)
gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique()
)
age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (30,50)
)

# Filter
filtered_df = df[
    (df["Category"].isin(category)) &
    (df["Age"].between(age_range[0],age_range[1])) &
    (df["Gender"].isin(gender))
]

# KPI Selection
col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered_df['Purchase Amount (USD)'].sum():,.0f}")
col2.metric("Avg Purchase",f"${filtered_df['Purchase Amount (USD)'].mean():.2f}")
col3.metric("Customers",filtered_df.shape[0])
col4.metric("Categories", filtered_df["Category"].nunique())

st.divider()

# Charts

col5,col6=st.columns(2)

with col5:
    st.subheader("📈 Purchase by Age")
    fig1 =px.scatter(
        filtered_df,
        x='Age',
        y="Purchase Amount (USD)",
        color="Gender"
    )
    st.plotly_chart(fig1,use_container_width=True)

with col6:
    st.subheader("🛒 Category Sales")
    cat_data = filtered_df.groupby("Category")["Purchase Amount (USD)"].sum().reset_index()
    fig2 = px.bar(cat_data, x="Category",y="Purchase Amount (USD)",color="Category")
    st.plotly_chart(fig2,use_container_width=True)

# Full Width
st.subheader("📊 Purchase Distribution")

fig3 = px.histogram(
    filtered_df,
    x="Purchase Amount (USD)",
    nbins=30,
    color="Gender"
)
st.plotly_chart(fig3,use_container_width=True)

st.divider()

# Tabs

tab1,tab2 = st.tabs(["📄 Data", "📊 Summary"])

with tab1:
    st.dataframe(filtered_df,use_container_width=True)

with tab2:
    st.write(filtered_df.describe())


# Download
st.download_button(
    "⬇ Download Data",
    filtered_df.to_csv(index=False),
    "Filtered_Data.csv",
    "text/csv"
)




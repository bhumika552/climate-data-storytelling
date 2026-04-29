import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Climate Data Storytelling",
    layout="wide"
)

st.title(" Climate Data Storytelling Dashboard")
st.write("Interactive visualizations of temperature, CO₂ growth, sea level rise and future forecasting.")

# ---------------------------
# Data
# ---------------------------
df = pd.DataFrame({
    "Year":[1880,1900,1950,2000,2020],
    "Temp_Anomaly":[-0.12,-0.08,0.02,0.45,1.02],
    "CO2":[290,295,310,370,415],
    "Sea_Level":[0,2,5,12,20]
})

st.subheader("Climate Dataset")
st.dataframe(df)

# ---------------------------
# 1 Temperature vs CO2 Dashboard
# ---------------------------
st.subheader("1. Temperature vs CO₂ Growth")

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=df["Year"],
        y=df["Temp_Anomaly"],
        mode="lines+markers",
        name="Temperature"
    )
)

fig1.add_trace(
    go.Scatter(
        x=df["Year"],
        y=df["CO2"],
        mode="lines+markers",
        name="CO2",
        yaxis="y2"
    )
)

fig1.update_layout(
    title="Temperature vs CO₂ Growth",
    template="plotly_dark",
    yaxis=dict(title="Temperature Anomaly"),
    yaxis2=dict(
        title="CO₂ ppm",
        overlaying="y",
        side="right"
    )
)

st.plotly_chart(fig1, use_container_width=True)


# ---------------------------
# 2 Bubble Chart
# ---------------------------
st.subheader("2. CO₂ vs Temperature vs Sea Level")

fig2 = px.scatter(
    df,
    x="CO2",
    y="Temp_Anomaly",
    size="Sea_Level",
    color="Year",
    hover_name="Year",
    title="Climate Relationship Bubble Chart",
    template="plotly_dark",
    size_max=60
)

st.plotly_chart(fig2, use_container_width=True)


# ---------------------------
# 3 Area Chart
# ---------------------------
st.subheader("3. Sea Level Rise Over Time")

fig3 = px.area(
    df,
    x="Year",
    y="Sea_Level",
    title="Sea Level Rise",
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)


# ---------------------------
# 4 Climate Spiral
# ---------------------------
st.subheader("4. Climate Spiral Visualization")

fig4 = px.line_polar(
    df,
    r="Temp_Anomaly",
    theta="Year",
    line_close=True,
    title="Climate Spiral",
    template="plotly_dark"
)

st.plotly_chart(fig4, use_container_width=True)


# ---------------------------
# 5 Future Forecast
# ---------------------------
st.subheader("5. Future Global Warming Forecast")

X = df[["Year"]]
y = df["Temp_Anomaly"]

model = LinearRegression()
model.fit(X, y)

future = pd.DataFrame({
    "Year":[2030,2040,2050]
})

future["Predicted"] = model.predict(future)

combined = pd.concat([
    df[["Year","Temp_Anomaly"]].rename(
        columns={"Temp_Anomaly":"Temp"}
    ),
    future.rename(
        columns={"Predicted":"Temp"}
    )
])

fig5 = px.line(
    combined,
    x="Year",
    y="Temp",
    markers=True,
    title="Future Warming Forecast",
    template="plotly_dark"
)

st.plotly_chart(fig5, use_container_width=True)


st.success("Dashboard Loaded Successfully ")
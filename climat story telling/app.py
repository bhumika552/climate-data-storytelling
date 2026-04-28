import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# -----------------------
# Data
# -----------------------
df = pd.DataFrame({
"Year":[1880,1900,1950,2000,2020],
"Temp_Anomaly":[-0.12,-0.08,0.02,0.45,1.02],
"CO2":[290,295,310,370,415],
"Sea_Level":[0,2,5,12,20]
})

# -----------------------
# 1 Interactive Climate Dashboard Line
# -----------------------
fig = go.Figure()

fig.add_trace(
go.Scatter(
x=df["Year"],
y=df["Temp_Anomaly"],
mode='lines+markers',
name='Temperature'
)
)

fig.add_trace(
go.Scatter(
x=df["Year"],
y=df["CO2"],
mode='lines+markers',
name='CO2',
yaxis='y2'
)
)

fig.update_layout(
title="Temperature vs CO2 Growth",
template="plotly_dark",
yaxis=dict(title="Temperature"),
yaxis2=dict(
title="CO2 ppm",
overlaying='y',
side='right'
)
)

fig.show()


# -----------------------
# 2 Bubble Chart
# -----------------------
fig = px.scatter(
df,
x="CO2",
y="Temp_Anomaly",
size="Sea_Level",
color="Year",
hover_name="Year",
title="CO2 vs Temperature vs Sea Level",
template="plotly_dark",
size_max=60
)
fig.show()


# -----------------------
# 3 Area Chart Storytelling
# -----------------------
fig = px.area(
df,
x="Year",
y="Sea_Level",
title="Sea Level Rise Over Time",
template="plotly_dark"
)

fig.show()


# -----------------------
# 4 Climate Spiral Style Scatter
# -----------------------
fig = px.line_polar(
df,
r="Temp_Anomaly",
theta="Year",
line_close=True,
title="Climate Spiral Visualization",
template="plotly_dark"
)

fig.show()


# -----------------------
# 5 Forecast Graph
# -----------------------
X=df[['Year']]
y=df['Temp_Anomaly']

model=LinearRegression()
model.fit(X,y)

future=pd.DataFrame({
"Year":[2030,2040,2050]
})

future["Predicted"]=model.predict(future)

combined=pd.concat([
df[["Year","Temp_Anomaly"]].rename(
columns={"Temp_Anomaly":"Temp"}
),
future.rename(
columns={"Predicted":"Temp"}
)
])

fig=px.line(
combined,
x="Year",
y="Temp",
markers=True,
title="Future Global Warming Forecast",
template="plotly_dark"
)

fig.show()
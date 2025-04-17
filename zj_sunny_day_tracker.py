from preswald import connect, get_df, text, table, slider, plotly
import pandas as pd
import plotly.express as px

connect()
df = get_df("weather_data")

df["TEMP"] = df["TEMP"].astype(str).str.replace(",", ".").str.strip()
df["TEMP"] = pd.to_numeric(df["TEMP"], errors="coerce")
df = df.dropna(subset=["TEMP"])
df["TEMP_F"] = df["TEMP"] * 9/5 + 32

threshold = slider("Set Your Sunny Temp Threshold (°F)", min_val=0, max_val=100, default=60)
sunny_count = len(df[df["TEMP_F"] > threshold])

text("# Zaara's Sunny Day Tracker")
table(df[["YEAR", "MO", "DY", "HR", "TEMP_F"]].head(100), title="Hourly Temp Readings")
text(f"There are **{sunny_count}** hourly readings above {threshold}°F.")

fig = px.scatter(
    df,
    x="TEMP_F",
    y="WND_SPD",
    title="Wind Speed vs Temperature",
    labels={"TEMP_F": "Temperature (°F)", "WND_SPD": "Wind Speed"}
)
plotly(fig)

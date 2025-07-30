from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "NASA CTT API is live. Visit /ctt to view today's cloud top temperature."

@app.route("/ctt")
def ctt():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    url = (
        f"https://wvs.earthdata.nasa.gov/api/v1/snapshot?"
        f"REQUEST=GetSnapshot&TIME={today}"
        f"&extent=-125,30,-65,50"
        f"&layers=MODIS_Terra_Cloud_Top_Temperature_Day"
        f"&CRS=EPSG:4326&format=image/png&width=1200&height=600"
    )
    return redirect(url)

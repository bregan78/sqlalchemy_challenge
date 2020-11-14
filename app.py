# 1. import Flask
from flask import Flask, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect =True)
Base.classes.keys()
Station=Base.classes.station
Measurement=Base.classes.measurement
# Create our session (link) from Python to the DB
session = Session(engine)


# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    results1 = session.query( Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()
# Save the query results as a Pandas DataFrame and set the index to the date column
    df = pd.DataFrame(results1[:], columns=['date', 'prcp'])
    #df.set_index('date', inplace=True, )
    df = df.dropna()

    prcp_dict = dict(zip(df['date'], df['prcp']))
    print("Server received request for 'precep' page...")
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations=session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    most_obser = session.query(Station.station, func.count(Station.station)).group_by(Station.station).\
    filter(Measurement.station == Station.station).order_by(func.count(Station.station).desc()).all()

    last_date_station = session.query(Measurement.date).filter(Measurement.station == most_obser[0][0]).order_by(Measurement.date.desc()).first()
    date = dt.datetime.strptime(last_date_station[0], "%Y-%m-%d")
    
    Month_12_ago_station = dt.date(date.year, date.month, date.day) - dt.timedelta(days=365)

    results = session.query( Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= Month_12_ago_station).\
    filter(Measurement.station ==most_obser[0][0]).\
    order_by(Measurement.date).all()

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)

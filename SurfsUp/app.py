# Import the dependencies.
import json
import sqlalchemy
import statistics
import requests
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    return (
        "Welcome to the home page!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start><br/>"
        "/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    one_year_precip_query = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '2016-08-23', Measurement.date <= '2017-08-23')
    precip_dict = dict(one_year_precip_query)

    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations_list = session.query(Measurement.station).group_by(Measurement.station).all()
    stations_string = []
    for station in stations_list:
        stations_string.append(station[0])
    stations_dict = {'Stations List': stations_string}

    return jsonify(stations_dict)

@app.route("/api/v1.0/tobs")
def temps():
    active_observations = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2016-08-23', Measurement.date <= '2017-08-23').all()
    observations_string = []
    for obs in active_observations:
        observations_string.append(obs[0])
    observations_dict = {'Temperature Observations': observations_string}

    return jsonify(observations_dict)

@app.route("/api/v1.0/<start>")
def start_date(start):
    start_temp_query = session.query(Measurement.tobs).filter\
        (Measurement.date >= start).all()
    start_temp_list = []
    for temp in start_temp_query:
        start_temp_list.append(temp[0])
    max_temp = max(start_temp_list)
    min_temp = min(start_temp_list)
    avg_temp = statistics.mean(start_temp_list)
    start_temp_dict = {'TMAX': max_temp,
                 'TMIN': min_temp,
                 'TAVG': avg_temp}
    
    return jsonify(start_temp_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_and_end(start, end): 
    range_temp_query = session.query(Measurement.tobs).filter\
            (Measurement.date >= start, Measurement.date <= end).all()
    #range_temp_query = session.query(Measurement.tobs).filter(Measurement.date >= '2016-08-23', Measurement.date <= '2017-08-23').all()
    temp_list = []
    for temp in range_temp_query:
        temp_list.append(temp[0])
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    avg_temp = statistics.mean(temp_list)
    temp_dict = {'TMAX': max_temp,
                 'TMIN': min_temp,
                 'TAVG': avg_temp}
    
    return jsonify(temp_dict)

if __name__ == "__main__":
    app.run(debug=True)
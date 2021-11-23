from flask import Flask, render_template, request
from flask_mqtt import Mqtt
from rbf import getTempData
import os
from dotenv import load_dotenv

app = Flask(__name__)

# # use the free broker from HIVEMQ
# app.config['MQTT_BROKER_URL'] = os.getenv('MQTT_BROKER_URL')
# app.config['MQTT_BROKER_PORT'] = os.getenv('MQTT_BROKER_PORT')
# # set the username here if you need authentication for the broker
# app.config['MQTT_USERNAME'] = os.getenv('MQTT_USERNAME')
# # set the password here if the broker demands authentication
# app.config['MQTT_PASSWORD'] = os.getenv('MQTT_PASSWORD')
# # set the time interval for sending a ping to the broker to 5 seconds
# app.config['MQTT_KEEPALIVE'] = os.getenv('MQTT_KEEPALIVE')
# # set TLS to disabled for testing purposes
# app.config['MQTT_TLS_ENABLED'] = os.getenv('MQTT_TLS_ENABLED')

# mqtt = Mqtt(app)


# @mqtt.on_connect()
# def handle_connect(client, userdata, flags, rc):
#     mqtt.subscribe('home/temp')


# @mqtt.on_message()
# def handle_mqtt_message(client, userdata, message):
#     data = dict(
#         topic=message.topic,
#         payload=message.payload.decode()
#     )

#     # add write to file functionality


@app.route("/")
def home():
    dataList = getTempData()

    return render_template('index.html', data=dataList)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    coordList = request.form['coordList']
    print(coordList)
    return render_template('subscribe.html', coordList=coordList)
    # your code
    # return a response

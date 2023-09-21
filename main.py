import time
import board
import adafruit_hcsr04
import paho.mqtt.client as mqtt
import socket
import json

def read_distance(sonar):
    return round(sonar.distance, 2)

def open_or_closed(sonar):
    if sonar.distance <= 60:
        return "closed"
    elif sonar.distance > 60:
        return "open"
    else:
        return "error"

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

mqtt_host = "192.168.0.149"
mqtt_port = "1883"
mqtt_topic_prefix = "garage_sensor"
mqtt_user = "home_assistant"
mqtt_password = ""

hostname = socket.gethostname()

sens_topic = f"{mqtt_topic_prefix}/sensor"
status_topic = f"{mqtt_topic_prefix}/status"
state_topic = f"{mqtt_topic_prefix}/state"

client = mqtt.Client()
client.username_pw_set(mqtt_user, mqtt_password)
client.connect(mqtt_host, int(mqtt_port))
client.loop_start()

while True:
    if sonar.distance != 0:
        sensor_online = "online"
    else:
        sensor_online = "offline"
    sensor_payload = json.dumps({
        "state": open_or_closed(sonar),
        "distance": read_distance(sonar),
    })
    print(f"Publishing sensor is {sensor_online} to {status_topic}")
    client.publish(status_topic, sensor_online, qos=1, retain=True)
    print("published availability.")
    print(f'Sensor payload: {sensor_payload}')
    print(f'pub_topic: {sens_topic}')
    client.publish(sens_topic, sensor_payload, qos=1, retain=True)

    time.sleep(10)

#client.disconnect()
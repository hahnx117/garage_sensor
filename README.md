# garage_sensor

## Home Assistant `configuration.yaml`

```
mqtt:
  - sensor:
      name: "Garage Door State"
      state_topic: "garage_sensor/sensor"
      json_attributes_topic: "garage_sensor/sensor"
      value_template: "{{ value_json.state }}"
      availability:
        - topic: "garage_sensor/status"
          payload_available: "online"
          payload_not_available: "offline"

  - sensor:
      name: "Garage Door Sensor Availability"
      state_topic: "garage_sensor/sensor"
      json_attributes_topic: "garage_sensor/sensor"
      value_template: "{{ value_json.status }}"

  - sensor:
      name: "Garage Door Distance"
      state_topic: "garage_sensor/sensor"
      json_attributes_topic: "garage_sensor/sensor"
      value_template: "{{ value_json.distance }}"
      unit_of_measurement: "cm"

  - sensor:
      name: "Garage Door Last Read Time"
      state_topic: "garage_sensor/sensor"
      json_attributes_topic: "garage_sensor/sensor"
      value_template: "{{ value_json.last_read }}"
```
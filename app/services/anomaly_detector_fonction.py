def anomaly_detector(temperature):
    if (temperature < 10) and (temperature > 40):
        return "anomaly"

    if temperature[-1] == "%":
        return "anomaly"
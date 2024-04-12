def anomaly_detector(temperature, anomaly_know=None):
    if temperature[-1] == "F":
        new_temp = (int(temperature[0:-2]) - 32) / 1.8
        return str(new_temp) + "°C"

    if temperature[-1] == "K":
        new_temp = int(temperature[0:-2]) - 273.15
        return str(new_temp) + "°C"

    if (new_temp < 10) and (new_temp > 40):
        return "anomaly"

    if anomaly_know == "yes":
        if temperature[-1] == "F":
            new_temp = (int(temperature[0:-2]) - 32) / 1.8
            return str(new_temp) + "°C"

        if temperature[-1] == "K":
            new_temp = int(temperature[0:-2]) - 273.15
            return str(new_temp) + "°C"

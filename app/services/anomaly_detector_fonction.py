def anomaly_detector(temperature, anomaly_know=None):
    if anomaly_know == "yes":
        if temperature[-1] == "F":
            new_temp = (float(temperature[0:-2]) - 32) / 1.8
            return str(new_temp) + "°C"

        if temperature[-1] == "K":
            new_temp = float(temperature[0:-2]) - 273.15
            return str(new_temp) + "°C"

        if temperature[-1] == "%":
            return str(new_temp)


    if (temperature < 10) and (temperature > 40):
        return "anomaly"

    if temperature[-1] == "%":
        return "anomaly"
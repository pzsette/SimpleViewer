def convert_to_degree(value):
    degrees = float(value[0])
    minutes = float(value[1]) / 60.0
    seconds = float(value[2]) / 3600.0

    return degrees + minutes + seconds
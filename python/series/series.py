def slices(series, length):
    series_len = len(series)

    if length > series_len or length <= 0:
        raise ValueError("Error Length: *{length}*".format(length=length))

    series_sliced = []

    for i in range(series_len):
        if i + length > series_len:
            break
        series_sliced.append(series[i:i+length])
    return series_sliced

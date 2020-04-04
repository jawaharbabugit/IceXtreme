for i in range(len(data.columns)):
    cat = data.columns[i]
    encoder = LabelBinarizer()
    catout = encoder.fit_transform(data[cat])

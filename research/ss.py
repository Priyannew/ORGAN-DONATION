def algo(datas,r):
    data = pd.read_csv('sarath.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = DecisionTreeClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]


def get_input(request, id):
    # if 'user' in request.session:
    get = analyse_team_form.objects.get(id=id)
    get.approve = True
    get.save()
    messages.info(request, "Sucessfully Analysed")
    r=get.id
    inputvar = []
    get.save()
    season= get.season
    landscape= get.landscape
    road_condition= get.road_condition
    weather= get.weather
    distance=get.distance
    cost_of_living=get.cost_of_living
    annual_income= get.annual_income
    inputvar.append(season)
    inputvar.append(landscape)
    inputvar.append(road_condition)
    inputvar.append(weather)
    inputvar.append(distance)
    inputvar.append(cost_of_living)
    inputvar.append(annual_income)
    print('input:', inputvar)
    f = algo(inputvar, r)
    print('OUTPUT:', f)
    st = analyse_team_form.objects.filter(id=r).update(solutions=f)
    return redirect('/analyse_team_index/')
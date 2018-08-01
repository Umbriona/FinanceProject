from sklearn import mixture as mix


def regime_construct_1(stock_data):

    unsup = mix.GaussianMixture(n_components=3, covariance_type='spherical', n_init=100, random_state=42)
    unsup.fit(stock_data)
    regime = unsup.predict(stock_data)
    return regime

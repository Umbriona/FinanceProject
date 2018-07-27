from sklearn import mixture as mix


unsup = mix.GaussianMixture(n_components=2, covariance_type='spherical', n_init=100, random_state=42)

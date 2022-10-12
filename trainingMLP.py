import tensorflow as tf


def training_MLP(X, y, Xt, nsteps, noutputs):
    # Defining the model
    model = tf.keras.Sequential()
    model.add(tf.keraslayers.Dense(20, activation='relu', input_dim=nsteps))
    model.add(tf.keraslayers.Dense(20, activation='relu'))
    model.add(tf.keraslayers.Dense(noutputs))
    model.compile(optimizer='adam', loss='mse')

    # Fitting the model
    model.fit(X, y, epochs=100, verbose=0)
    out = model.predict(Xt, verbose=0)
    return out, model
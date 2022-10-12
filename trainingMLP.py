import tensorflow as tf


def training_MLP(X, y, Xt, nsteps, noutputs):
    try:
        X.shape
        y.shape
        Xt.shape
        # Defining the model
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(
            20, activation='relu', input_dim=nsteps))
        model.add(tf.keras.layers.Dense(20, activation='relu'))
        model.add(tf.keras.layers.Dense(noutputs))
        model.compile(optimizer='adam', loss='mse')

        # Fitting the model
        model.fit(X, y, epochs=100, verbose=0)
        out = model.predict(Xt, verbose=0)
        return out, model
    except:
        print('Data passed do not required criteria')

import tensorflow as tf


def training_MLP(X, y, Xt, nsteps, L1, L2, noutputs):
    try:
        X.shape
        y.shape
        Xt.shape
        if L1 == 0 or L2 == 0:
            # Defining the model
            model = tf.keras.Sequential()
            model.add(tf.keras.layers.Dense(
                L1+L2, activation='relu', input_dim=nsteps))
            model.add(tf.keras.layers.Dense(noutputs))
            model.compile(optimizer='adam', loss='mse')

            # Fitting the model
            model.fit(X, y, epochs=100, verbose=0)
            out = model.predict(Xt, verbose=0)
            return out, model
        else:
            # Defining the model
            model = tf.keras.Sequential()
            model.add(tf.keras.layers.Dense(
                L1, activation='relu', input_dim=nsteps))
            model.add(tf.keras.layers.Dense(L2, activation='relu'))
            model.add(tf.keras.layers.Dense(noutputs))
            model.compile(optimizer='adam', loss='mse')

            # Fitting the model
            model.fit(X, y, epochs=100, verbose=0)
            out = model.predict(Xt, verbose=0)
            return out, model
    except:
        print('Data passed do not required criteria')

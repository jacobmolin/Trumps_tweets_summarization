from random import randint
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils


def modelling(X_modified, Y_modified, run_model_fit):
    model = Sequential()

    layers = 2
    units = 400
    drop = 0.2
    batch_size = 50
    epochs = 100

    model.add(LSTM(units, input_shape=(
        X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
    model.add(Dropout(drop))
    model.add(LSTM(units))
    model.add(Dropout(drop))
    model.add(Dense(Y_modified.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')

    filename = ''

    if run_model_fit:
        # Create filename
        filename = 'models/text_generator'
        for i in range(layers):  # Write layer info
            filename += f'_{units}_{drop}'
        filename += f'_e{epochs}_bs{batch_size}{randint(0,100)}.h5'

        model.fit(X_modified, Y_modified, epochs=epochs,
                  batch_size=batch_size, verbose=2)
        print('filename:', filename)
        model.save_weights(filename)

    return [model, filename]

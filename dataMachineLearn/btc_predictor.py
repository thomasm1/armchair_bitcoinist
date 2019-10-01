from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurren import LSTM
from keras.models import Sequential
import lstm, time 

# 1.) data
x_train, y_train, x_test, y_test = lstm.load_data('Coinbase_BTCUSD_d.csv', 50, True)

# 2.) build model
model = Sequential()

model.add(LSTM(
    input_dim=1,
    output_dim=50,
    return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(
    100,
    return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(
    ouput_dim=1))
model.add(Activation('linear'))

start= time.time()
model.compile(loss='mse', optimizer='rmsprop')
print ('compilation time : ', time.time() - start)

# 3.) train model
model.fit(
    x_train, 
    y_train,
    batch_size=512, # cases -days
    nb_epoch=1, # 1 variation
    validation_split=0.05) # 
)

# 4.) Plot prediction
predictions = lstm.predict_sequences_multiple(model, x_test, 50,50)
lstm.plot_results_multiple(predictions, y_test, 50)

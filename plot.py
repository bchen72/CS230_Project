from utilities import plotLossOverEpochs
import pickle
history = pickle.load(open("/home/ubuntu/augmenter-cs230/trained_models_LSTM/0_history", "rb"))
plotLossOverEpochs(history)

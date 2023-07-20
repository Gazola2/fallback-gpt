import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Carregar o modelo treinado
with open('./saved_models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Carregar o tokenizer salvo
with open('./saved_tokenizer/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Carregar o LabelEncoder salvo
with open('./saved_models/label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

# Carregar as classes do LabelEncoder
label_classes = np.load('saved_models/label_encoder_classes.npy')

# Frase de teste
frase = 'poder'

# Tokenizar a frase
tokens = tokenizer.texts_to_sequences([frase])

# Fazer padding nos tokens
tokens_padded = pad_sequences(tokens, maxlen=250)

# Fazer a classificação usando o modelo
predicao = model.predict(tokens_padded)

# Obter a classe predita
classe_predita = label_classes[np.argmax(predicao)]

# Imprimir o resultado
print('Frase:', frase)
print('Classe predita:', classe_predita)
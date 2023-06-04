from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        with open('../saved_models/model_lstm.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('../saved_tokenizer/tokenizer.json', 'rb') as f:
            tokenizer = pickle.load(f)
                
        # Carregar as classes do LabelEncoder
        label_classes = np.load('../saved_models/label_encoder_classes.npy')

        # Frase de teste
        frase = tracker.latest_message['text']

        # Tokenizar a frase
        tokens = tokenizer.texts_to_sequences([frase])

        # Fazer padding nos tokens
        tokens_padded = pad_sequences(tokens, maxlen=250)

        # Fazer a classificação usando o modelo
        predicao = model.predict(tokens_padded)

        # Obter a classe predita
        classe_predita = label_classes[np.argmax(predicao)]

        print('Frase:', frase)
        print('Classe predita:', classe_predita)
        
        dispatcher.utter_message(text="Teste")

        return [UserUtteranceReverted()]
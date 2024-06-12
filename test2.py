import streamlit as st
import torch
from io import StringIO
import os
from keyphrasetransformer import KeyPhraseTransformer

# Function to extract key phrases
def keywordnew(content):
    kp = KeyPhraseTransformer(model_type="t5", model_name="Suva/uptag-keyphrase-model")
    result = kp.get_key_phrases(content)
    return result

# Streamlit app title and subtitle
st.title("Keyword Extraction App")
st.subheader("Extract key phrases from your text using a custom-trained model")

# Input text area for user query
question = st.text_area("Enter your text here:")

# Submit button
if st.button('Submit'):
    if question:
        result = keywordnew(question)
        st.subheader("Extracted Key Phrases:")
        st.write(result)
    else:
        st.error("Please enter some text to extract key phrases!")
else:
    st.info("Enter text and click 'Submit' to extract key phrases.")



# import streamlit as st
# import torch
# from io import StringIO
# import os
# from keyphrasetransformer import KeyPhraseTransformer

# def keywordnew(content):
#     kp = KeyPhraseTransformer(model_type="t5", model_name="Suva/uptag-keyphrase-model")
#     result = kp.get_key_phrases(content)
#     return result

# question = st.text_input("Enter your query:")

# if st.button('Submit'):
#     result = keywordnew(question)
#     st.write(result)
# else:
#     st.error("Please enter a query!")

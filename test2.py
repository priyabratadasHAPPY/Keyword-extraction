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
st.title("Blog Keyword Extraction Tool")
st.subheader("Find the best keywords for your blog posts")

# Input text area for user query
st.write("Enter your blog content below to extract key phrases that can help you optimize your posts for search engines.")
question = st.text_area("Enter your blog content here:")

# Submit button
if st.button('Submit'):
    if question:
        result = keywordnew(question)
        st.subheader("Extracted Key Phrases:")
        st.write(result)
        st.info("Use these key phrases to optimize your blog posts and improve your search engine rankings.")
    else:
        st.error("Please enter some text to extract key phrases!")
else:
    st.info("Enter your blog content and click 'Submit' to extract key phrases.")


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

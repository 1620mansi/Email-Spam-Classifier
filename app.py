import pickle
import streamlit as st

model = pickle.load(open('model/model.pkl', 'rb'))
vector = pickle.load(open('model/vectors.pkl', 'rb'))

st.title("Email Spam Classifier")

email = st.text_area(label='Enter email here')

if st.button('Predict'):
    result = model.predict(vector.transform([email]).toarray())[0]
    if result == 1:
        st.header("This email is spam")
    else:
        st.header("This email is not spam")

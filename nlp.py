import streamlit as st
import os


import spacy


def text_analyzer(text):
  
    nlp=spacy.load('en')
    doc=nlp(text)
    alldata=[('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in doc]
    return alldata
  
  
def main():
  
    st.title("NLP WEBAPP")
    st.subheader("NLP on fire")
    
    
    if st.checkbox("show Tokens and lemma"):
        st.subheader("Tokenize your text")
        
        message=st.text_area("Enter Text", "Type here...")
        if st.button("analyze"):
            nlp_result=text_analyzer(message)
            st.json(nlp_result)
   
  


if __name__ == '__main__':
	main()

  


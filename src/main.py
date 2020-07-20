import logging
from typing import List

import numpy as np
from numpy import ndarray
import streamlit as st

logging.basicConfig(level=logging.WARNING)
device = "cpu"
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""

default_value_goes_here = """
New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York. 
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband. 
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other. 
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage. 
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the 
2010 marriage license application, according to court documents. 
Prosecutors said the marriages were part of an immigration scam. 
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further. 
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective 
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002. 
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say. 
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages. 
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted. 
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s 
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali. 
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force. 
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""


###
### Main UI
###

#@st.cache()
#def load_bert(name = 'distilbert-base-cased'):
#    model = DistilBertModel.from_pretrained(name)
#    tokenizer = DistilBertTokenizer.from_pretrained(name)
#    return model, tokenizer


#@st.cache()
#def load_all():
#    model, tokenizer = load_bert()
#    return model, tokenizer

#model, tokenizer = load_all()


st.title("Aditya Jitta Capstone Test App")
#st.write('torch version  is', torch.__version__)


user_input = st.text_area("Text to Summarize", default_value_goes_here, height = 400)


#sentence_extractor = SentenceExtractor()
#sentences = sentence_extractor(user_input, 40, 400)
#st.write('Sentences: ', sentences)
summ_size = st.slider('Summary size', 1, 10, 1)
#if st.button('Summarize'):
#    text_embeddings = feature_matrix(sentences)
#    summary = generate_summary(sentences, text_embeddings, ratio_value = summ_size*0.1)
#    '''
#    ### Summary
#    '''
#    summary = ' '.join(summary)
#    st.write(HTML_WRAPPER.format(summary), unsafe_allow_html=True)
#else:
#    st.write('Click to summarize')


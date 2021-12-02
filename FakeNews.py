#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:12:33 2021

@author: Devanshu(21200390)
"""

import streamlit as st
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
stop_words = stopwords.words()

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
	st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
	st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

@st.cache(suppress_st_warning=True)
def cleaning(text):        
	# converting to lowercase, removing URL links, special characters, punctuations...
	text = text.lower()    
	# removing the stop-words          
	text_tokens = word_tokenize(text)
	tokens_without_sw = [word for word in text_tokens if not word in stop_words]
	filtered_sentence = (" ").join(tokens_without_sw)
	text = filtered_sentence
	
	return text

@st.cache(suppress_st_warning=True)
def load_data():
	news_data = pd.read_csv("Input\\NewsDatashortv.csv")        # read csv file 
	return news_data

@st.cache(suppress_st_warning=True)
def create_chart(X_axis, fake_lst, real_lst, sub_uni):
	plt.bar(X_axis - 0.2, fake_lst, 0.4, label = 'Fake')
	plt.bar(X_axis + 0.2, real_lst, 0.4, label = 'Real')
	  
	plt.xticks(X_axis, sub_uni)
	plt.xlabel("News Subjects")
	plt.ylabel("Number of Fake/Real News")
	plt.title("Real/Fake News Statistics")
	plt.legend()
	ax = plt.gca()
	plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
	st.pyplot(plt)

@st.cache(suppress_st_warning=True)
def create_fake_table(news_data):
	dt_fake = news_data[news_data.label == "fake"]["text"].apply(cleaning)
	p_fake = Counter(" ".join(dt_fake).split()).most_common(10)
	rslt_fake = pd.DataFrame(p_fake, columns=['Word', 'Frequency'])
	st.table(rslt_fake)

@st.cache(suppress_st_warning=True)
def create_real_table(news_data):
	dt_real = news_data[news_data.label == "real"]["text"].apply(cleaning)
	p_real = Counter(" ".join(dt_real).split()).most_common(10)
	rslt_real = pd.DataFrame(p_real, columns=['Word', 'Frequency'])
	st.table(rslt_real)


local_css("Input\\style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
icon("search")

# Code for choosing analytics type and search by name or ticker code functionality

try:
	st.title("Fake News Analyser Dashboard")
	data_load_state = st.text('Loading data...')                                  # Create a text element and let the user know the data is loading
	
	news_data = load_data()
	
	# Notify the reader that the data was successfully loaded.
	data_load_state.text('Loading data...complete!')
	data_load_state.text('')   

	sub_uni = news_data.subject.unique()
	X_axis = np.arange(len(sub_uni))
	fake_lst = []
	real_lst = []

	st.sidebar.title("News Subjects:")
	for i in sub_uni:
		st.sidebar.markdown(i)
		fake_news = news_data[(news_data.label == "fake") & (news_data.subject == i)]     
		real_news = news_data[(news_data.label == "real") & (news_data.subject == i)] 
		if fake_news.empty:
			fake_lst.append(0)
		else:
			fake_lst.append(len(fake_news))
		if real_news.empty:
			real_lst.append(0)
		else:
			real_lst.append(len(real_news))

	option = st.selectbox('Analytics type',('Please choose','Subject wise news','Most frequent words under fake news corpus', 'Most frequent words under real news corpus'))  # show user stock search type to select one

	if option == "Subject wise news":
		create_chart(X_axis, fake_lst, real_lst, sub_uni)
		
	elif option == "Most frequent words under fake news corpus":
		create_fake_table(news_data)		

	elif option == "Most frequent words under real news corpus":
		create_real_table(news_data)
		
	else:
		st.error("Please select a valid option")

except Exception as e:
	print(e)
	st.error(e)
	traceback.print_exc()



Introduction - 
----------------------------

The digital world that we live has created various means of producing and consuming information of any kind. For instance, social media becomes one of the most 
popular for news production and consumption due to its easy access, fast dissemination, and low cost. However, it also enables wide spread of “Fake News”.
Fake news is news or stories created to deliberately misinform or deceive readers. Historically, misinformation has been seen as the normal situation, and news
sources were routinely considered untrustworthy. It was stated that ‘if you want to know any fact about politics, you must read at least three different papers,
compare at least three different versions of the same fact, and come in the end to your own conclusion. Nowadays, however, what makes fake news most alarming
is the speed with which it spreads. And the role of technologies in the spread of false, inaccurate or misleading information has quickly followed the invention of
such technologies.

The root causes, the spread and the consequences of fake news are all complex issues. In recent years many researchers and organisations have started studying
fake news and proposed several approaches to address the issue. The following projects are dealing with Fake News.

Hadoop/MapReduce implementation for Fake News Detection - 
----------------------------

In this project, I gained hands-on experience with the MapReduce programming model building by running an application using Hadoop. As explained above, fake news datasets are in abundance. However, there are very few platforms that can analyse such datasets. In this project, I am implementing some learning algorithms to analyse fake news datasets using Hadoop/MapReduce model:

* Identify a source or sources of fake news.

* Define the type of analysis on the fake news dataset.

* Choose a learning algorithm for fake news analysis.

* Implement the selected learning algorithm in Hadoop/MapReduce. (Recommendation: Cloudera HDP data platform or AWS platform)

* Build a Dashboard to run this analysis and display the results.

Steps to execute the python code:
----------------------------

First install the following pip dependencies
1. pip install pandas
2. pip install numpy
3. pip install matplotlib
4. pip install streamlit
5. pip install nltk

Then,
1. Open CMD from the ProjectSourceCode folder.
2. Run command -> streamlit run FakeNews.py
3. This will run the python code on local host

----------------------------------------------------------------------------------------------------

To run the cloud hosted application:
----------------------------

1. Open any browser
2. Open cloud hosted application link
3. This will run the cloud hosted datawarehouse application of fakenews


OR


To run from Bash Terminal:
----------------------------

1. Access the Pem file that was created to access the application
2. RUN THE COMMAND -> ssh -i fakenews.pem centos@34.243.126.238
3. Run the command -> sudo su
4. run the command -> cd FakeNews/
5. run the command -> cd FakeNewsCloud/
6. Run the command -> tmux a -t 0 
7. This will open the tmux session
8. Run command -> streamlit run FakeNews.py --server.port=80
9. Now copy the external server URL into a browser and it will launch the hosted application

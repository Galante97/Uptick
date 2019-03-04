'''
http://www.nltk.org/howto/sentiment.html
'''

import imp
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

## create a text file named "test.txt"
with open('test.txt', 'r') as myfile:
    data=myfile.read()
    

print(data)
sid = SentimentIntensityAnalyzer()

ss = sid.polarity_scores(data)

for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]), end='')

print()

# **dictionaries in python**: accesses variables like a dictionary 
##print(ss['neg'], ss['pos'])

if ss['neg'] > ss['pos']:
    print ('This is a NEGATIVE article :(')
elif ss['neg'] < ss['pos']:
    print ('This is a POSITIVE article :)')
else:
    print ('neutral')





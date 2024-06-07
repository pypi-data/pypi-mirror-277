from .ficto import predict, help, counts

__all__ = ['predict', 'help', 'counts']

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import joblib
import pkg_resources


import warnings
warnings.filterwarnings('ignore')
    
# This function counts the number of adjectives
def _n_adj(text):
    adj=0
    for i in text:
        if i[0] == 'J' or i == 'ADJ':
            adj=adj+1
    return adj

# This function counts the number of pronouns
def _n_pronoun(text):
    pronoun=0
    for i in text:
        if (i[0] == 'P') or (i[:3] in ['WP$','WPO','WPS']) or i == 'PRON':
            pronoun=pronoun+1
    return pronoun

# This function counts the number of adverbs
def _n_adv(text):
    adv=0
    for i in text:
        if (i[0] == 'R') or (i[:3] in ['WRB']) or i == 'ADV':
            adv=adv+1
    return adv


def counts(text):
    tagged_words= pos_tag(word_tokenize(text), tagset='universal')
    taglist=[]
    for k in tagged_words:
        taglist.append(k[1])
    
    adj=_n_adj(taglist)
    adv=_n_adv(taglist)
    pronoun=_n_pronoun(taglist)
    
    return [adj, adv, pronoun]


def predict(text):
    pc = counts(text)
    if pc[0] == 0:
        pc[0] += 1
    if pc[2] == 0:
        pc[2] += 1
    RADJPRON = pc[0]/pc[2]
    RADVADJ = pc[1]/pc[0]

    model_path = pkg_resources.resource_filename(__name__, 'fictometer.sav')

    logreg=joblib.load(model_path)

    output = logreg.predict([[RADJPRON, RADVADJ]])
    output = int(output[0])
    prob = logreg.predict_proba([[RADJPRON, RADVADJ]])[0]

    if output == 1:
        return "Fiction", prob[1]
    else:
        return "Non-Fiction", prob[0]

    
def help():
    
    print("""counts(text):
It takes a text as input and returns a list having the count of 'adjectives', 'adverbs' and 'pronouns' in that text respectively.

predict(text):
It takes text as input, then uses counts(), then calculates RADJPRON and RADVADJ, and returns a tuple having 'result' and 'confidence'.""")

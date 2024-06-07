from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from ._tags import _n_adj, _n_adv, _n_pronoun, _n_verb, _n_noun
import pickle
import pkg_resources

import warnings
warnings.filterwarnings('ignore')
    
def counts(text):
    tagged_words= pos_tag(word_tokenize(text), tagset='universal')
    taglist=[]
    for k in tagged_words:
        taglist.append(k[1])
    
    adj=_n_adj(taglist)
    adv=_n_adv(taglist)
    # noun=_n_noun(taglist)
    # verb=_n_verb(taglist)
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
    sav_file = pkg_resources.resource_filename(__name__, 'fictometer.sav')
    logreg = pickle.load(open(sav_file, 'rb'))
    output = logreg.predict([[RADJPRON, RADVADJ]])
    prob = logreg.predict_proba([[RADJPRON, RADVADJ]])

    if output == 1:
        return "Fiction", f"confidence = {prob[0][0] if prob[0][0]>prob[0][1] else prob[0][1]}"
    else:
        return "Non-Fiction", f"confidence = {prob[0][0] if prob[0][0]>prob[0][1] else prob[0][1]}"
    
def help():
    
    print("""counts(text):
It takes a text as input and returns a list having the count of 'adjectives', 'adverbs' and 'pronouns' in that text respectively.

predict(text):
It takes text as input, then uses counts(), then calculates RADJPRON and RADVADJ, and returns a tuple having 'result' and 'confidence'.""")

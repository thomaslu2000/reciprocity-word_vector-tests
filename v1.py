"""
This script only takes the example sentences and matches among them.
The final outputs orders the text in order of similarity.
The vectors are labeled with a letter and index like 'h1'
The letter is the category of the text (h is hiking, c is cooking, d is disney, t is tech)
The number is just the index of each text (it doesn't have a meaning)
"""

import gensim.downloader as api
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import numpy as np
from scipy.spatial.distance import cosine, euclidean
import time

print("initializing")

# These lists are just pre-cleaned text for demonstration purposes

hiking = [
    "beauty joshua tree national park part close proximity la . matter google map seem say , people la tell destination half hour away… depend traffic . well , joshua tree ’ half hour drive num mile ; num easy mile due east outside palm spring . park make 794,000 acre straddle mojave colorado desert . first time drive western gate felt like step one dr. sue ’ book spiny joshua tree ’ shake pom-poms across valley floor . legend mormon pioneer saw outstretched arm tree remind biblical character joshua , lead promise land . name stuck .",
"year look dreamy photo online people hike narrows zion national park . silky , turquoise water flow deep , dark canyon . num foot vertical cliff . faint beam sunlight bounce colorful canyon wall . look like something exists fairy tale . well last weekend , finally get chance backpack narrow , know photograph narrows justice . yet , ’ help . ’ favorite photo weekend . hike narrows amazing experience , hopefully photos inspire visit narrow soon . information narrow ,",
"april , go zion national park first time . man impress . tower monolith , crazy sandstone formation , epic view , easily could spend week explore . thing , east mesa trail hike top observation point stand one favorite hike . way less crowd hike angel ’ landing , ’ nothing like hike side sheer cliff face , zilch valley floor . morning start little grey , eventually sun broke , make fine photo opportunity . ’ map collection favorite shot hike .",
"pick shorter hike , something take hour afternoon , rather day epic . like choose hike network trail head longer loop ’ feeling , choose short route weather turn truly terrible . course trail cafe nearby post-hike latte get bonus point . make sure read trail beforehand . creek ford , steep slippery section trail prone flooding , save dry day ."
]

cooking = [
    "baked persimmon crisp simple stunning dessert also serve breakfast cold morning . get crisps butter breadcrumb mixture softness persimmon . ’ mouthful delicious treat barely take effort . year one excite one far ! couple photography project , make new friend , attend culinary event , try different ingredient cook nearly non-stop , idea month zoom make u reach november . regret , contentment desire continue learn . one spend day appreciate , make time worth living . make one look forward next day . amongst , much need escape get plan , imagine excitement ( smile cheek cheek ) . yes , go petite trip ! get ready explore absorb . plan , pack organize , go ahead try extremely easy dessert .",
"well , ’ , weird soul planet could never enjoy ice cream extent . yes , take tiny bite spoonful get really hot rare ice cream mood . week ’ back , get crazy idea make ice cream home . start pure experiment turn success . honestly speak , never felt proud make something successfully first time . make even happy everybody taste , enjoy .",
"decent chocolate treat soul satisfying , mood uplifting switch miserable day chirpy one . live west coast , ’ ever nag weather ’ blue late yell sugar rush boost spirit . plus , valentine ’ day chocolate delicacy float virtual food world food channel , ’ tough flow temptation . ’ nothing bad , food good food , may say . well , chocolate good health several way , obviously long ’ . mention several time past chocoholic time , crave hit hard . ’ airy , fluffy , velvety mousse , melt mouth , could dig gobble non-stop .",
"surprised smile cheek cheek saw cream puff rise tall . keep finger cross hop ’ fall flat . ’ still stand firm take oven . keep star impatiently cool , hold one hand.. perfect least world . cream puff fill strawberry"
]

tech = [
"mobile technology form technology mostly use cellular communication relate aspect . us form platform many transmitter ability send data time single channel . platform call code-division multiple access ( cdma ) . platform allow many user make use single frequency restrict likelihood interference frequency two source",
"mobile technology improve simple device use phone call message multi-tasking device use gps navigation , internet browsing , gaming , instant message tool etc .",
"mobile technology start remarkable achievement world technology , transform user comfort technology due present diverse functionality . mobile first introduce , use basically sms , call game . presently transform digital world make life business much easy ; marketer ability sell product ease mobile technology",
"mobile make possible user transfer file file bluetooth wifi . mobile also equip internet connectivity , make easy user gain information also download file internet"
]

disney = [
    "cinderella another one story technically exist outside version — even disney short three decade earlier — really . people think think girl glass slipper . heck , kind people think think concept disney princess , idea anyone find true love magic believe .",
"regular inhabitant top spot best pixar movie ever , andrew stanton num gem wonderful , hysterical , move piece family entertainment . story clownfish name marlin ( albert brook ) try find abducted son nemo ( alexander gould ) perfect balance visual whimsy , emotional relatability , adventure storytelling . ’ one best pixar film , ’ one best animate film company .",
"check one progressive animate film era , movie tell chinese legend mulan , girl force impersonate man fight people . lot disney title late ’ 90 kind goofy comedy rich , empower drama stand test time .",
"second disney film ever , one iconic film company history . puppet want real boy one foundational film history animation , disney . show could do team creator respect source material audience . ’ see since kid , owe revisit geppetto , jiminy cricket , unforgettable puppet ."
]

punctuation = ",.?-—()"

#This downloads the somewhat small text8 data for use in the word2vec system
print("downloading")
corpus = api.load('text8')


print("loading")

t0 = time.time()
model = Word2Vec(corpus)
word_vectors = model.wv

# Google's pretrained vector system is also available, but it would have to be downloaded externally
# word_vectors = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

print("word2vec modelling time: " + str(time.time() - t0))

def aveFunc(sent):
    """
    Averages the word vectors of all words in the given sentence 
    (some of the extra variables are simply to account for different possible dimensions)
    """
    count = 0
    found = False
    total = 0
    for w in sent:
        if w not in punctuation and w in word_vectors.vocab:
            count += 1
            try:
                # t =  word_vectors.word_vec(w)
                t = word_vectors[w]
                if not found:
                    total = np.zeros(len(t))
                    total += t
                    found = True
                else:
                    total += t
            except TypeError as e:
                print(w)
    return total / count

print("creating averages")
t0 = time.time()
hvecs = [aveFunc(s.split()) for s in hiking]
cvecs = [aveFunc(s.split()) for s in cooking]
tvecs = [aveFunc(s.split()) for s in tech]
dvecs = [aveFunc(s.split()) for s in disney]
total_time = time.time() - t0
print("average vectorizing time: "+ str(total_time/16))


print("calculating")
lists = []
cats = "hctd"
vecs = [hvecs, cvecs, tvecs, dvecs]
t0 = time.time()

# This snippet compares each text vector with one of the predetermined vectors below.
# the chosen vector can be changed below
for catInd in range(4):
    vec = vecs[catInd]
    for i in range(len(vec)):
        lists.append([cats[catInd]+str(i), cosine(vec[i], hvecs[1])])
total_time = time.time() - t0

print("ave comparison time: " + str(total_time / 16))

print("printing")

# This Line outputs the other texts in order of similarity. Each text has a name like h1
# The letter at the front is the category of topic, so "h1" would hopefully have the other h vectors at the front of the list
print(sorted(lists, key= lambda x: x[1]))

print("done")
import nltk
from nltk.corpus import wordnet
from nltk.metrics import edit_distance
import csv

need_syn=[]
change_syn=[]
cancel_syn=[]
review_syn=[]
available_syn=[]
find_deal_syn=[]
reorder_syn=[]
total_syn=[]
expect_syn=[]
update_syn=[]
check_syn=[]
help_syn=[]
needs=[]
checks=[]
helps=[]
availables=[]
changes=[]
cancels=[]
reviews=[]
expects=[]
find_deals=[]
reorders=[]
totals=[]
updates=[]
allowed_words=[]

for syn in wordnet.synsets("need"):
    for l in syn.lemmas():
        need_syn.append(l.name())
for syn in wordnet.synsets("order"):
    for l in syn.lemmas():
        need_syn.append(l.name())        
for k in need_syn:
    l=len(k)
    needs.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        needs.append(word)
        needs.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        needs.append(word)
        needs.append(wordd)

for syn in wordnet.synsets("change"):
    for l in syn.lemmas():
        change_syn.append(l.name())
for k in change_syn:
    l=len(k)
    changes.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        changes.append(word)
        changes.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        changes.append(word)
        changes.append(wordd)
changes.append('alter')
changes.append('altering')
changes.append('altered')        


for syn in wordnet.synsets("cancel"):
    for l in syn.lemmas():
        cancel_syn.append(l.name())
for k in cancel_syn:
    l=len(k)
    cancels.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        cancels.append(word)
        cancels.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        cancels.append(word)
        cancels.append(wordd)
cancels.append('cancelling')
cancels.append('cancelled')        

for syn in wordnet.synsets("review"):
    for l in syn.lemmas():
        review_syn.append(l.name())
for k in review_syn:
    l=len(k)
    reviews.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        reviews.append(word)
        reviews.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        reviews.append(word)
        reviews.append(wordd)

for syn in wordnet.synsets("find"):
    for l in syn.lemmas():
        find_deal_syn.append(l.name())
for syn in wordnet.synsets("buy"):
    for l in syn.lemmas():
        find_deal_syn.append(l.name())
for syn in wordnet.synsets("best"):
    for l in syn.lemmas():
        find_deal_syn.append(l.name())               
for k in find_deal_syn:
    l=len(k)
    find_deals.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        find_deals.append(word)
        find_deals.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        find_deals.append(word)
        find_deals.append(wordd)
find_deals.append('found')
find_deals.append('bought')        

for syn in wordnet.synsets("reorder"):
    for l in syn.lemmas():
        reorder_syn.append(l.name())
for k in reorder_syn:
    l=len(k)
    reorders.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        reorders.append(word)
        reorders.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        reorders.append(word)
        reorders.append(wordd)

for syn in wordnet.synsets("total"):
    for l in syn.lemmas():
        total_syn.append(l.name())
for k in total_syn:
    l=len(k)
    totals.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        totals.append(word)
        totals.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        totals.append(word)
        totals.append(wordd)
totals.append('totalling')
totals.append('totalled')        

for syn in wordnet.synsets("expect"):
    for l in syn.lemmas():
        expect_syn.append(l.name())
for k in expect_syn:
    l=len(k)
    expects.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        expects.append(word)
        expects.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        expects.append(word)
        expects.append(wordd)        

for syn in wordnet.synsets("decrease"):
    for l in syn.lemmas():
        update_syn.append(l.name())
for syn in wordnet.synsets("increase"):
    for l in syn.lemmas():
        update_syn.append(l.name())            
for k in update_syn:
    l=len(k)
    updates.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        updates.append(word)
        updates.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        updates.append(word)
        updates.append(wordd)

for syn in wordnet.synsets("available"):
    for l in syn.lemmas():
        available_syn.append(l.name())
for k in available_syn:
    l=len(k)
    availables.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        availables.append(word)
        availables.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        availables.append(word)
        availables.append(wordd)

for syn in wordnet.synsets("checks"):
    for l in syn.lemmas():
        check_syn.append(l.name())
for k in check_syn:
    l=len(k)
    checks.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        checks.append(word)
        checks.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        checks.append(word)
        checks.append(wordd)

for syn in wordnet.synsets("help"):
    for l in syn.lemmas():
        help_syn.append(l.name())
for k in help_syn:
    l=len(k)
    helps.append(k)
    if(k[l-1]=='e'):
        word=wordd=""
        word=k+'d'
        for i in range(l-1):
            wordd=wordd+k[i]
        wordd=wordd+'ing'
        helps.append(word)
        helps.append(wordd)
    else:
        word=wordd=""
        for i in range(l):
            word=word+k[i]
            wordd=wordd+k[i]
        word=word+'ed'    
        wordd=wordd+'ing'
        helps.append(word)
        helps.append(wordd)
helps.append('how')

allowed_words=needs+changes+cancels+reviews+find_deals+updates+totals+reorders+expects+checks+helps+availables

total_dict_length=len(allowed_words)

with open('dict.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(allowed_words)

print 'Printing contents of the csv--'

with open('dict.csv','rb') as csvvfile:
	csvreader=csv.reader(csvvfile,delimiter=',')
	for row in csvreader:
		print row    	
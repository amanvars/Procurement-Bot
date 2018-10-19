# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from pattern.en import singularize
import sys
#sys.path.insert(0,"I:\Projects\finderBuddyzhcetwarriors\finderBuddy")
#sys.path.insert(0,"C:\Users\aman_AV\Desktop\Finder_Buddy\finder_Buddy")
#from msgbox import threshold
from .logic_adapter import LogicAdapter
import nltk
from nltk.corpus import wordnet
from reportlab.pdfgen import canvas 
global names, prices, item
names=[]
prices =[]
item=''
threshold=25
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
    reviews.append('view')
    reviews.append('viewing')
    reviews.append('viewed')

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
find_deals.append('search')

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
expects.append('delivery')

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
ps=[]
ps=needs+helps+totals+updates+changes+reviews+cancels+find_deals+reorders+expects+checks+availables

class LanguageAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(LanguageAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'order' and 'buy' and 'temperature'.
        """
        words = ['last','first','previous','old']
        #allowed_words=allowed_words+words
        if any(x in statement.text.split() for x in allowed_words):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement

        import sqlite3
        con1 = sqlite3.connect('item_list.db')
        con2 = sqlite3.connect('order_list.db')

        from nltk import word_tokenize,pos_tag
        import nltk

        noise_list=['!','?','value','wanna','can','deal','you','please','me','some','wish','wishes','wished','wishing'
            ,'availability','product','stock','place','us','date','value','bill','amount',"is","are","the","a","an","I"
            ,"we","will","please","my","our",'sheets',
            'of','from','We','to','order','what','for','was','quantity','number','request','on']
        def remove_noise(input_string):
            words=input_string.split()
            noise_free_words = [word for word in words if word not in noise_list] 
            noise_free_text = " ".join(noise_free_words) 
            return noise_free_text

        def pre_process(res):
            from nltk.stem.wordnet import WordNetLemmatizer
            from nltk.stem.porter import PorterStemmer 
            from pattern.en import pluralize,singularize
            lem=WordNetLemmatizer()
            stemmer=PorterStemmer()
            i=0
            for k in res:
                k.lower()
                k=str(k)
                print type(k)
                ml=[]
                ml.append(k)
                tagg=pos_tag(ml)
                if(tagg[0][1]=='VBG' or tagg[0][1]=='VBD' or tagg[0][1]=='VBN' or tagg[0][1]=='VBP'):
                    k=lem.lemmatize(k,pos='v')
                if(tagg[0][1]=='NNS'):
                    res[i]=singularize(k)    
                print k
                i=i+1
                return res    

        res1=remove_noise(str(statement.text)).split()
        res=pre_process(res1)
        print res

        cll=[]
        cll=helps+checks
        sll=[]
        sll=helps+availables+totals+expects
        allo=[]
        allo=changes+cancels+reviews+find_deals+updates+totals+reorders+expects+checks+helps+availables
        allo.append('how')
        allo.append('place')
        allo.append('something')
        if any(x in res for x in needs) and not any(x in res for x in allo):
            print "Need query"
            if(len(res)>2):
                ml=[]
                ml.append(res[2])
                tagg=pos_tag(ml)
            else:
                ml=[]
                ml.append(res[1])
                tagg=pos_tag(ml)    
            if not (len(res)>1 and (res[1].isdigit() or res[1] is not "") and (tagg[0][1]=='NNS' or tagg[0][1]=='NN' )):
                response=Statement("FinderBuddy understands that you're trying to order something\nBut FinderBuddy can't process this\nTry entering statements like-\n=>I want/need/require <quantity> <product>\n=>#place_order /product_name/quantity/color(if any)")
            print "Token 1 is "+res[1]
            if(res[1].isdigit()):
                qty=int(res[1])
                print "Quantity is "+str(qty)
                del(res[0])
                del(res[0])
                prod=clr=""
                print pos_tag(res)
                for k in res:
                    ml=[]
                    ml.append(k)
                    tagg=pos_tag(ml)
                    """if(tagg[0][1]=='NNS' or tagg[0][1]=='NN'):
                        if(tagg[0][1]=='NNS'):
                            prod+=singularize(k)
                        else:
                            prod+=k    
                    elif(tagg[0][1]=='JJ' or tagg[0][1]=='NN'):
                        clr+=k"""
                    if(len(res)>=2):
                        print "Here I stand with "+str(ml)
                        if(tagg[0][1]=='JJ' or tagg[0][1]=='NN' and clr==""):
                            clr+=k
                        if(tagg[0][1]=='NNS'):
                            prod+=singularize(k)
                        elif(tagg[0][1]=='NN' and clr==""):
                            prod+=k
                    else:
                        if(tagg[0][1]=='NNS'):
                            prod+=singularize(k)
                        else:
                            prod+=k    
                                                
                print "Product is "+prod
                print "Color is "+clr
            else:
                qty=1
                print "Quantity is "+str(qty)
                del(res[0])
                prod=clr=""
                print pos_tag(res)  
                for k in res:
                    ml=[]
                    ml.append(k)
                    tagg=pos_tag(ml)
                    if(tagg[0][1]=='NNS' or tagg[0][1]=='NN'):
                        print "Processsing"+tagg[0][0]
                        if(tagg[0][1]=='NNS'):
                            prod+=singularize(k)
                        else:
                            prod+=k 
                    elif(tagg[0][1]=='JJ' or k=='blue'):
                        clr+=k        
                prod=res[len(res)-1]   
                print "Product is "+prod
                print "Color is "+clr
                cur1=''
                cur0=con1.execute("SELECT * FROM ITEMS WHERE NAME=?",(prod,))
                rows=cur0.fetchall()
                if(len(rows)==0):
                    print "Here nulling"
                    response=Statement("Sorry this item is not available in the inventory.You may command FinderBuddy to search it online.")
                    response.remove_response("Sorry this item is not available in the inventory.You may command FinderBuddy to search it online.")
                    response.confidence=1
                    return response
            if(clr==""):
                print "In colorless state"
                cur1=''
                cur0 = con1.execute("SELECT COLOR FROM ITEMS WHERE NAME=?",(prod,))
                rows=cur0.fetchall()
                if(len(rows)==1):
                    cur1 = con1.execute("SELECT * FROM ITEMS where NAME=?", (prod,));
                else:
                    print "Colorless else"
                    t="Available colors are "
                    s=len(rows)
                    i=0
                    for row in rows:
                        t=t+row[0]
                        if(i<s-1):
                            t=t+','
                        i=i+1    
                    t=t+". Please specify your choice"    
                    response=Statement(t)
                    response.remove_response(t)
                    response.confidence=1
                    return response    
            else:
                print "There"
                cur1 = con1.execute("SELECT * FROM ITEMS where NAME=? and COLOR=?", (prod,clr));
            pid=nm=qt_av=rt=cl=0
            for row in cur1:
                pid = row[0]
                nm = row[1]
                qt_av = row[2]
                rt = row[3]
                cl = row[4]
            pr = rt * qty;
            qty_lft = qt_av-qty;
            if qt_av>=qty and qty_lft>=0:
                q2 = """INSERT INTO USER_ORDER (PROD,PROD_ID,QTY,RATE,COLOR,PRICE,PLACED_AT,DELIVER_AT)
                         VALUES ( ?, ?,?, ? ,? ,?,date('now','localtime'),date('now','localtime','+4 day'));"""
                q1= """UPDATE ITEMS SET QTY_AVAIL=? where NAME = ?;"""
                con2.execute(q2,(nm,pid,qty,rt,cl,pr))
                con1.execute(q1,(qty_lft,nm))
                con1.commit()
                con2.commit()

                q3 = "select seq from sqlite_sequence where name='USER_ORDER' "
                c = con2.execute(q3);
                odno = c.fetchone()[0]
                response=Statement("Order Successfully Placed with Order ID: "+str(odno)+". Use me Again :)")
                response.remove_response("Order Successfully Placed with Order ID: "+str(odno)+". Use me Again :)")
                pdfname=str(odno)+'.pdf'
                c=canvas.Canvas(pdfname)
                c.setFont('Helvetica-Bold',20)
                c.drawString(200,700,"Order Receipt")
                c.setFont('Times-Roman',14)
                c.drawString(50,600,'Order No.')
                c.line(150,590,190,590)
                k=str(odno)
                c.setFont('Courier',14)
                c.drawString(150,600,k)
                q = "select * FROM  USER_ORDER WHERE ORDER_ID = ? "
                cur = con2.execute(q,(odno,))
                for row in cur:
                    k=str(row[5])+' '+str(row[1])
                    c.setFont('Times-Roman',14)
                    c.drawString(50,550,"Product Name")
                    c.line(150,540,190,540)
                    c.setFont('Courier',14)
                    c.drawString(155,550,k)
                    c.setFont('Times-Roman',14)
                    c.drawString(50,500,"Quantity")
                    c.line(150,490,190,490)
                    c.setFont('Courier',14)
                    c.drawString(155,500,str(row[3]))
                    c.setFont('Times-Roman',14)
                    c.drawString(50,450,"Price")
                    c.line(150,440,190,440)
                    c.setFont('Courier',14)
                    c.drawString(155,450,str(row[6]))
                    c.setFont('Times-Roman',14)
                    c.drawString(50,400,"Order Date")
                    c.line(150,390,190,390)
                    c.setFont('Courier',14)
                    c.drawString(155,400,str(row[7]))
                    c.setFont('Times-Roman',14)
                    c.drawString(50,350,"Delivery Date")
                    c.line(150,340,190,340)
                    c.setFont('Courier',14)
                    c.drawString(155,350,str(row[8]))
                c.setFont('Times-Italic',16)    
                c.drawString(250,250,"Your order has been successfully placed")
                c.drawString(250,200,"Hope to see you again soon")
                c.line(50,115,150,115)
                c.setFont('Times-Roman',14)
                c.drawString(50,100,"Signature of the customer")    
                c.save()
            else:
                response=Statement("Not Enough Quantity available.You can command FinderBuddy to find the best deals of "+clr+" "+prod+" for you")
                response.remove_response("Not Enough Quantity available.You can command FinderBuddy to find the best deals of "+clr+" "+prod+" for you")
            response.confidence=1
            return response           

    #CHANGE ORDER TAGS
        elif any(x in res for x in changes) and not any(x in res for x in helps):
            print "Change query"
            response=Statement("")
            if(res[0]=='want' or res[0]=='need'):
                del(res[0])    
            if not(len(res)==3 and (res[1].isdigit() or res[1]=='previous' or res[1]=='last' or res[1]=='first') and res[2].isdigit()):
                  response=Statement("FinderBuddy understands that you may be trying to change your order\nBut FinderBuddy can't really process this\nTry entering statements like-\n=>Change order <order id> to <new quantity>\n=>I want to change my previous/last/first order to <new quantity>")
                  response.confidence=1
                  return response
            if(res[1].isdigit()):
                ord_id=int(res[1])
            elif(res[1]=='previous' or res[1]=='last'):
                q="select ORDER_ID FROM  USER_ORDER LIMIT 1 OFFSET (select COUNT(*) FROM  USER_ORDER)-1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]
            elif(res[1]=='first'):
                q="select ORDER_ID FROM  USER_ORDER ORDER BY ORDER_ID ASC LIMIT 1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]  
            print "Order id is "+str(ord_id)
            q = "select * FROM  USER_ORDER WHERE ORDER_ID = ? "
            cur = con2.execute(q,(ord_id,))
            ck=1
            qty_chn=int(res[2])
            for row in cur:
                oid = row[0]
                print "Row is "+str(row[0])+" "+str(row[2])
                if oid==ord_id:
                    ck=0
                    pid = row[2]
                    qty = int(row[3])
                    rt = row[4]
                    abs = qty_chn-qty
                    print "Quantity to be changed is "+str(qty_chn)+" "+str(qty)
                    print "abs is "+str(abs)
                    pr = abs*rt
                    print "pr is "+str(pr)
                    q = "select * FROM  ITEMS WHERE PROD_ID = ? "
                    curr = con1.execute(q,(pid,))
                    print curr
                    for x in curr:
                        qt_av = x[2]
                        if qt_av>=abs:
                            q= "UPDATE ITEMS SET QTY_AVAIL = QTY_AVAIL - ? WHERE PROD_ID = ?"
                            con1.execute(q,(abs,pid))
                            con1.commit()
                            #con2.execute(qx,(oid,prd,pid,qty,rt,cl,pr,pld,dld))
                            con2.execute("update USER_ORDER  SET QTY = QTY + ?, PRICE = PRICE + ? WHERE ORDER_ID = ?",(abs,pr,oid,))
                            con2.commit()
                            response=Statement("Order with Order Id: "+str(oid)+" succesfully changed with quantity: "+str(qty_chn))
                            response.remove_response("Order with Order Id: "+str(oid)+" succesfully changed with quantity: "+str(qty_chn))
                        else:
                            response = Statement("Sorry!! Not enough Quantity available to fulfil your need.")
                            response.remove_response("Sorry!! Not enough Quantity available to fulfil your need.")
            if ck==1:
                response=Statement("No order present with this order id.")
                response.remove_response("No order present with this order id.")
            response.confidence=1
            return response 


        #CANCEL ORDER TAGS---
        elif any(x in res for x in cancels) and not any(x in res for x in helps):
            print "Cancel query"
            if(res[0]=='want' or res[0]=='need'):
                del(res[0])
            if not(len(res)==2 and (res[1].isdigit() or res[1]=='previous' or res[1]=='last' or res[1]=='first')):
                  response=Statement("FinderBuddy understands that you may be trying to cancel your order\nBut FinderBuddy can't really process this\nTry entering statements like-\n=>Cancel order <order id>\n=>I want to cancel my previous/last/first order")
                  response.confidence=1
                  return response
            if(res[1].isdigit()):
                ord_id=int(res[1])
            elif(res[1]=='previous' or res[1]=='last'):
                q="select ORDER_ID FROM  USER_ORDER LIMIT 1 OFFSET (select COUNT(*) FROM  USER_ORDER)-1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]
            elif(res[1]=='first'):
                q="select ORDER_ID FROM  USER_ORDER ORDER BY ORDER_ID ASC LIMIT 1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]    
            print "Order id is "+str(ord_id)
            q = "select * FROM  USER_ORDER WHERE ORDER_ID = ? "
            cur = con2.execute(q,(ord_id,))
            ck=1
            for row in cur:
                oid = row[0]
                if oid==ord_id:
                    ck=0
                    pid = row[2]
                    qty = row[3]
                    q = "DELETE FROM USER_ORDER WHERE ORDER_ID = ?"
                    con2.execute(q,(ord_id,))
                    con2.commit()
                    q= "UPDATE ITEMS SET QTY_AVAIL = QTY_AVAIL + ? WHERE PROD_ID = ?"
                    con1.execute(q,(qty,pid))
                    con1.commit()

            if ck==0:
                response=Statement("Order with Order Id:"+str(oid)+" succesfully cancelled")
                response.remove_response("Order with Order Id:"+str(oid)+" succesfully cancelled")
            else:
                response=Statement("No order present with this order id.")
                response.remove_response("No order present with this order id.")
            response.confidence=1
            return response


        #REVIEW ORDER TAGS--
        elif any(x in res for x in reviews) and not any(x in res for x in helps):
            print "Review query" 
            if(res[0]=='want' or res[0]=='need'):
                del(res[0])
            if not(len(res)==2 and (res[1].isdigit() or res[1]=='previous' or res[1]=='last' or res[1]=='first')):
                response=Statement("FinderBuddy understands that you may be trying to review your order\nBut FinderBuddy can't really process this\nTry entering statements like-\n=>Review order <order id>\n=>I want to review my previous/last/first order")
                response.confidence=1
                return response
            if(res[1].isdigit()):
                ord_id=int(res[1])
            elif(res[1]=='previous' or res[1]=='last'):
                q="select ORDER_ID FROM  USER_ORDER LIMIT 1 OFFSET (select COUNT(*) FROM  USER_ORDER)-1" 
                cur= con2.execute(q)
                for row in cur:
                    ord_id=row[0]
            elif(res[1]=='first'):
                q="select ORDER_ID FROM  USER_ORDER ORDER BY ORDER_ID ASC LIMIT 1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]    
            print "Order id is "+str(ord_id)
            q = "select * FROM  USER_ORDER WHERE ORDER_ID = ? "
            cur = con2.execute(q,(ord_id,))
            ck=1
            for row in cur:
                oid = row[0]
                if oid:
                    ck=0
                    prd = row[1]
                    qt = row[3]
                    cl = row[5]
                    pr = row[6]
                    pld = row[7]
                    dld = row[8]
            if ck==0:
                response=Statement("Order Details:\n"+"Order Id:"+str(oid)+"\nProduct:"+str(prd)+"\nQuantity:"+str(qt)+"\nColor:"+str(cl)+"\nPrice:Rs."+str(pr)+"\nOrder Date:"+str(pld)+"\nExpected Delivery:"+str(dld)  \
                                        +"\nHope to see you again :)")
                response.remove_response("Order Details:\n"+"Order Id:"+str(oid)+"\nProduct:"+str(prd)+"\nQuantity:"+str(qt)+"\nColor:"+str(cl)+"\nPrice:Rs."+str(pr)+"\nOrder Date:"+str(pld)+"\nExpected Delivery:"+str(dld)  \
                                        +"\nHope to see you again :)")
            else:
                response=Statement("No order present with this order id.")
                response.remove_response("No order present with this order id.")
            response.confidence=1
            return response    


        #FIND_DEAL_QUERY---
        elif any(x in res for x in find_deals) and not any(x in res for x in sll):
            print "Find Deal query"  
            if(res[0]=='want' or res[0]=='need'):
                del(res[0])    
            ml=[]
            ml.append(res[1])
            tagg=pos_tag(ml)    
            if not(len(res)>1 and (res[1].isdigit() or tagg[0][1]=='NN' or tagg[0][1]=='NNS' or tagg[0][1]=='JJ')):
                response=Statement("FinderBuddy understands that you're trying to order something from suppliers\nBut FinderBuddy can't really process this\nTry statements like-\n=>buy/best/find <quantity> <product>\n=>#find_deal /<product>")
                response.confidence=1
                return response
            if(res[1].isdigit()):
                qty=int(res[1])
                del(res[1])
            else:
                qty=1
            from bs4 import BeautifulSoup
            import urllib2
            global item
            item=''
            for i in range(1,len(res)-1):
                item=item+res[i]+" "            
            item +=res[len(res)-1]
            print item
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            search1 = item.replace(" ","-")
            search2 = item.replace(" ","+")
            url1='http://www.kelkoo.co.uk/kss-'+search1+'.html'
            url2='https://www.mintprice.com/c/search?show=16&sortby=price_low_to_high&page=1&search='+search2
            query1=urllib2.urlopen(url1)
            query2=urllib2.urlopen(url2)
            soup1=BeautifulSoup(query1)
            soup2=BeautifulSoup(query2)
            print(".................start............")
            global names, prices
            names=[]
            prices=[]
            for row in soup1.find_all('h3', attrs={'class': 'result-title'}):
                names.append(row.span.text)
            for row in soup1.find_all('p',attrs={'class':'price'}):
                prices.append(row.strong.text)
            print("....................................................")
            print names
            print prices
            print(".................end............")
            for row in soup2.find_all('div',attrs={'class':'caption'}):
                names.append(row.h3.text)
            for row in soup2.find_all('p',attrs={'class':'price'}):
                prices.append(row.strong.text)
            print names
            print prices        
            d1 =  names[0].decode().encode('utf-8')
            p1 =  prices[0].strip().decode().encode('utf-8')
            d2 =  names[1].decode().encode('utf-8')
            p2 =  prices[1].strip().decode().encode('utf-8')
            d3 =  names[2].decode().encode('utf-8')
            p3 =  prices[2].strip().decode().encode('utf-8')
            od1 =  names[3].decode().encode('utf-8')
            op1 =  prices[3].strip().decode().encode('utf-8')
            od2 =  names[4].decode().encode('utf-8')
            op2 =  prices[4].strip().decode().encode('utf-8')
            od3 =  names[5].decode().encode('utf-8')
            op3 =  prices[5].strip().decode().encode('utf-8')
            response = Statement(u"Below are some suggestions\n\t"+d1+" || "+p1+"\n\t"+d2+" || "+p2+"\n\t"+d3+" || "+p3+"\n\t"+od1+" || "+op1+"\n\t"+od2+" || "+op2+"\n\t"+od3+" || "+op3)
            response.confidence = 1
            return response

        #REORDER QUERIES--
        elif any(x in res for x in ['reorder']) and not any(x in res for x in helps):
            print "Need reorder based query" 
            if not (len(res)>1 and (res[1]=='previous' or res[1]=='last' or res[1]=='first' or res[1].isdigit())):
                response=Statement("FinderBuddy understands that you're trying to repeat an order\nBut FinderBuddy can't really process this\nTry statements like-\nreorder my previous/first/last order\n=>reorder order <order id>")
                response.confidence=1
                return response
            if(res[1].isdigit()):
                ord_id=int(res[1])
            elif(res[1]=='previous' or res[1]=='last'):
                q="select ORDER_ID FROM  USER_ORDER LIMIT 1 OFFSET (select COUNT(*) FROM  USER_ORDER)-1" 
                cur= con2.execute(q)
                for row in cur:
                    ord_id=row[0]
            elif(res[1]=='first'):
                q="select ORDER_ID FROM  USER_ORDER ORDER BY ORDER_ID ASC LIMIT 1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]    
            print "Order id is "+str(ord_id)
            q="select * FROM USER_ORDER WHERE ORDER_ID=?"
            cur = con2.execute(q,(ord_id,))
            ck=1
            for row in cur:
                oid = row[0]
                if oid:
                    ck=0
                    prod = row[1]
                    prod_id=row[3]
                    qty = row[3]
                    rate=row[4]
                    clr = row[5]
                    pr = row[6]
            if ck==0:
                if(clr==""):
                    print "Here"
                    cur1 = con1.execute("SELECT * FROM ITEMS where NAME=?", (prod,));
                else:
                    print "There"
                    cur1 = con1.execute("SELECT * FROM ITEMS where NAME=? and COLOR=?", (prod,clr));
                pid=nm=qt_av=rt=cl=0
                for row in cur1:
                    pid = row[0]
                    nm = row[1]
                    qt_av = row[2]
                    rt = row[3]
                    cl = row[4]
                pr = rt * qty;
                qty_lft = qt_av-qty;
                if qt_av>=qty and qty_lft>=0:
                    q2 = """INSERT INTO USER_ORDER (PROD,PROD_ID,QTY,RATE,COLOR,PRICE,PLACED_AT,DELIVER_AT)
                         VALUES ( ?, ?,?, ? ,? ,?,date('now','localtime'),date('now','localtime','+4 day'));"""
                    q1= """UPDATE ITEMS SET QTY_AVAIL=? where NAME = ?;"""
                    con2.execute(q2,(nm,pid,qty,rt,cl,pr))
                    con1.execute(q1,(qty_lft,nm))
                    con1.commit()
                    con2.commit()
                    q3 = "select seq from sqlite_sequence where name='USER_ORDER' "
                    c = con2.execute(q3);
                    odno = c.fetchone()[0]
                    response=Statement("Order Successfully Placed with Order ID: "+str(odno)+". Use me Again :)")
                    response.remove_response("Order Successfully Placed with Order ID: "+str(odno)+". Use me Again :)")
                    pdfname=str(odno)+'.pdf'
                    c=canvas.Canvas(pdfname)
                    c.setFont('Helvetica-Bold',20)
                    c.drawString(200,700,"Order Receipt")
                    c.setFont('Times-Roman',14)
                    c.drawString(50,600,'Order No.')
                    c.line(150,590,190,590)
                    k=str(odno)
                    c.setFont('Courier',14)
                    c.drawString(150,600,k)
                    q = "select * FROM  USER_ORDER WHERE ORDER_ID = ? "
                    cur = con2.execute(q,(odno,))
                    for row in cur:
                        k=str(row[5])+' '+str(row[1])
                        c.setFont('Times-Roman',14)
                        c.drawString(50,550,"Product Name")
                        c.line(150,540,190,540)
                        c.setFont('Courier',14)
                        c.drawString(155,550,k)
                        c.setFont('Times-Roman',14)
                        c.drawString(50,500,"Quantity")
                        c.line(150,490,190,490)
                        c.setFont('Courier',14)
                        c.drawString(155,500,str(row[3]))
                        c.setFont('Times-Roman',14)
                        c.drawString(50,450,"Price")
                        c.line(150,440,190,440)
                        c.setFont('Courier',14)
                        c.drawString(155,450,str(row[6]))
                        c.setFont('Times-Roman',14)
                        c.drawString(50,400,"Order Date")
                        c.line(150,390,190,390)
                        c.setFont('Courier',14)
                        c.drawString(155,400,str(row[7]))
                        c.setFont('Times-Roman',14)
                        c.drawString(50,350,"Delivery Date")
                        c.line(150,340,190,340)
                        c.setFont('Courier',14)
                        c.drawString(155,350,str(row[8]))
                    c.setFont('Times-Italic',16)
                    c.drawString(250,250,"Your order has been successfully placed")
                    c.drawString(250,200,"Hope to see you again soon")
                    c.line(50,115,150,115)
                    c.setFont('Times-Roman',14)
                    c.drawString(50,100,"Signature of the customer")
                    c.save()

                else:
                    response=Statement("Not Enough Quantity available.You can command FinderBuddy to find the best deals of "+clr+" "+prod+" for you")
                    response.remove_response("Not Enough Quantity available.You can command FinderBuddy to find the best deals of "+clr+" "+prod+" for you")
                response.confidence=1
                return response            
            else:
                response=Statement("No order present with this order id.")
                response.remove_response("No order present with this order id.")
            response.confidence=1
            return response    

        #TOTAL BASED QUERY--    
        elif any(x in res for x in totals):
            print "Total based query"
            if not (len(res)==2 and (res[1]=='previous' or res[1]=='last' or res[1]=='first' or res[1].isdigit())):
                response=Statement("FinderBuddy understands that you're trying to find the total value of an order\nBut FinderBuddy can't really process this\nTry statements like-\nfind total of my previous/first/last order\n=>total order <order id>")
                response.confidence=1
                return response
            if(res[1].isdigit()):
                ord_id=int(res[1])
            elif(res[1]=='previous' or res[1]=='last'):
                q="select ORDER_ID FROM  USER_ORDER LIMIT 1 OFFSET (select COUNT(*) FROM  USER_ORDER)-1" 
                cur= con2.execute(q)
                for row in cur:
                    ord_id=row[0]
            elif(res[1]=='first'):
                q="select ORDER_ID FROM  USER_ORDER ORDER BY ORDER_ID ASC LIMIT 1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]    
            print "Order id is "+str(ord_id)
            q="select * FROM USER_ORDER WHERE ORDER_ID=?"
            cur = con2.execute(q,(ord_id,))
            ck=1
            for row in cur:
                oid = row[0]
                if oid:
                    ck=0
                    qty = row[3]
                    rate=row[4]

            if ck==0:
                total=qty*rate
                response=Statement("Total value of order with order id "+str(ord_id)+" is "+unichr(163)+str(total))
                response.remove_response("Total value of order with order id "+str(ord_id)+" is "+unichr(163)+str(total))
                response.confidence=1
                return response            
            else:
                response=Statement("No order present with this order id.")
                response.remove_response("No order present with this order id.")
            response.confidence=1
            return response    

        #DELIVERY DATE BASED QUERY--
        elif any(x in res for x in expects) and not any(x in res for x in helps):
            print "Delivery date based query"
            if(res[0]=='find'):
                del(res[0])
            print res
            if not (len(res)>1 and (res[1]=='previous' or res[1]=='last' or res[1]=='first' or res[1].isdigit())):
                response=Statement("FinderBuddy understands that you're trying to find the delivery date of an order\nBut FinderBuddy can't really process this\nTry statements like-\nfind expected delivery date of my previous/first/last order/<order id>\n")
                response.confidence=1
                return response
            if(res[1].isdigit()):
                ord_id=int(res[1])
            elif(res[1]=='previous' or res[1]=='last'):
                q="select ORDER_ID FROM  USER_ORDER LIMIT 1 OFFSET (select COUNT(*) FROM  USER_ORDER)-1" 
                cur= con2.execute(q)
                for row in cur:
                    ord_id=row[0]
            elif(res[1]=='first'):
                q="select ORDER_ID FROM  USER_ORDER ORDER BY ORDER_ID ASC LIMIT 1" 
                cur = con2.execute(q)
                for row in cur:
                    ord_id=row[0]    
            print "Order id is "+str(ord_id)
            q="select * FROM USER_ORDER WHERE ORDER_ID=?"
            cur = con2.execute(q,(ord_id,))
            ck=1
            for row in cur:
                oid = row[0]
                if oid:
                    ck=0
                    dld=row[8]

            if ck==0:
                response=Statement("Delivery date of order with order id "+str(ord_id)+" is "+str(dld))
                response.remove_response("Delivery date of order with order id "+str(ord_id)+" is "+str(dld))
                response.confidence=1
                return response            
            else:
                response=Statement("No order present with this order id.")
                response.remove_response("No order present with this order id.")
            response.confidence=1
            return response   

        #UPDATE BASED QUERY--
        elif any(x in res for x in updates) and not any(x in res for x in helps):
            print "Update based query"
            print res 
            ml=[]
            ml.append(res[1])
            tagg=pos_tag(ml)
            nl=[]
            nl.append(res[2])
            tagg1=pos_tag(nl)
            if not(len(res)>1 and (tagg[0][1]=='NN' or tagg[0][1]=='NNS' or tagg[0][1]=='JJ') and (tagg1[0][1]=='NN' or tagg1[0][1]=='NNS' or res[2].isdigit())):
                response=Statement("FinderBuddy understands that you're trying to update the quantity of a product\nBut FinderBuddy can't really process this\nTry using statements like-\n=>reduce/increase/decrease/decrement/increment quantity of <color(if any)> <product> <new quantity>")
                response.confidence=1
                return response
            prod=""
            clr=""
            if ((tagg[0][1]=='NN' or tagg[0][1]=='NNS' or tagg[0][1]=='JJ') and (tagg1[0][1]=='NN' or tagg1[0][1]=='NNP')):
                clr=res[1]
                prod=res[2]
                qty_chn=int(res[3])
            else:
                prod=res[1]
                qty_chn=int(res[2])
            print "Color is "+clr
            print "Product is "+prod
            print "Quantity is "+str(qty_chn)
            q= "update ITEMS SET QTY_AVAIL=? where NAME = ? and COLOR=?;"
            con1.execute(q,(qty_chn,prod,clr))
            con1.commit()
            response=Statement("Updated item "+str(clr)+" "+str(prod)+" succesfully to "+str(qty_chn))
            response.confidence=1
            return response

        #RETRIEVAL BASED QUERY    
        elif any(x in res for x in availables) and not any(x in res for x in cll):
            print "Retrieval based query" 
            if(res[0]=='find'):
                del(res[0])
            ml=[]
            ml.append(res[1])
            tagg=pos_tag(res[1]) 
            if not(len(res)>1 and (tagg[0][1]=='NN' or tagg[0][1]=='NNS' or tagg[0][1]=='JJ')):
                response=Statement("FinderBuddy understands that you're trying to find the available quantity of an item\nBut FinderBuddy can't really process this\nTry using statements like-\n=>find available quantity of <color(if any)> <product>")
                response.confidence=1
                return response
            clr=prod=""    
            if(len(res)>2):
                nl=[]
                nl.append(res[2])
                tagg1=pos_tag(nl)
                clr=res[1]
                prod=res[2]
            else:
                prod=res[1]
            print "Color is "+clr 
            print "Product is "+prod 
            qty=""
            if(clr==""):
                q= "select * FROM ITEMS WHERE NAME=?" 
                cur1=con1.execute(q,(prod,))
                for row in cur1:
                    qty=row[2]
                if(qty==""):
                    response=Statement("No such product exists")
                else:        
                    response=Statement("Available quantity of "+str(clr)+" "+str(prod)+" is "+str(qty))
                response.confidence=1
                return response
            else:
                q="select * FROM ITEMS WHERE NAME=? and COLOR=?"
                cur1=con1.execute(q,(prod,clr,))
                for row in cur1:
                    qty=row[2]
                if(qty==""):
                    response=Statement("No such product exists")
                else:      
                    response=Statement("Available quantity of "+str(clr)+" "+str(prod)+" is "+str(qty))
                response.confidence=1
                return response

        #THRESHOLD BASED QUERY
        elif any(x in res for x in checks) and not any(x in res for x in helps):
            print "Threshold based query"
            print "Threshold is "+str(threshold)
            q="select NAME,COLOR FROM ITEMS WHERE QTY_AVAIL<=? "
            cur1=con1.execute(q,(threshold,))
            a="Items which are short are\n"
            i=0
            for row in cur1:
                a=a+row[1]+" "
                a+=row[0]+"\n"
                i=i+1
            if(i==0):
                response=Statement("Relax-no items are short!! :)")
            else:        
                response=Statement(a)
            response.confidence=1
            return response             

        #HELP BASED QUERY
        elif any(x in res for x in helps):
            print "Help needed" 
            a = "To place an Order, please type:  #place_order /product_name/quantity/color(if any)"
            b = "To change an Order, please type:  #change_order /order_id/quantity(to change)"
            c = "To review an Order, please type:  #review_order /order_id"
            d = "To cancel an Order, please type:  #cancel_order /order_id"
            g = "To know your previous Order, please type:  #previous_order"
            k = "To check what all items are about to finish, please type: #check"
            e = "For help, please type:  #help"
            g = "Other than this,you can also just type in the keywords of your query "
            h = "like want/need/find/reorder along with the order id and product name"
            f = "pattern is sensitive and use of small case letters is recommended\n"
            i = "Hope this helped\nIn case of further queries,please feel free to contact the developers "
            j = "\n\tAnushka Chawla->anushkachawla@zhcet.ac.in\n\tAman Varshney->amanvars@zhcet.ac.in"
            response = Statement(a+"\n"+b+"\n"+c+"\n"+d+"\n"+g+"\n"+k+"\n"+e+"\n"+"\n"+g+h+f+"\n\n"+i+j)
            response.confidence=1
            response.remove_response(a+"\n"+b+"\n"+c+"\n"+d+"\n"+g+"\n"+k+"\n"+e+"\n"+"\n"+g+h+f+"\n\n"+i+j)
            return response


        response=Statement("Processing your request")
        response.confidence = 1
        return response
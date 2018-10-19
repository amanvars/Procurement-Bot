from __future__ import unicode_literals
import sys
#sys.path.insert(0,"I:\Projects\finderBuddyzhcetwarriors\finderBuddy")
from .logic_adapter import LogicAdapter
import nltk
from nltk.metrics import edit_distance
import csv


class SpellAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(SpellAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):

        ed=9999

        from chatterbot.conversation import Statement

        res=str(statement.text).split()
        options=[]
        strr=""

        with open('dict.csv','rb') as csvvfile:
            csvreader=csv.reader(csvvfile,delimiter=str(','))
            print "Word to be corrected is "+res[0]
            for row in csvreader:
                for col in row:
                    k=edit_distance(res[0],col)
                    #print "Word compared is "+str(col)
                    #print "Edit distance is "+str(k)
                    if(k<3):
                        options.append(col)
                        aux=strr.split()
                        if col not in aux:
                            strr=strr+" "+col
                            print col

        response=Statement("The query you entered seems wrong.Try possible options like "+strr)
        response.remove_response("The query you entered seems wrong.Try possible options like "+strr)
        response.confidence=1
        return response            

                 
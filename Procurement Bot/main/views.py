# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.http import JsonResponse


class ChatterBotIndexView(TemplateView):
    template_name = "index.html"

def simple_template(request):
    return render(request, "app.html", {})

def help_temp(request):
    return render(request, "help.html", {})

def dev_temp(request):
    return render(request, "dev.html", {})

noise_list=['availability','wanna','product','stock','place','us','date','value','bill','amount',"is","are","the","a","an","I","we","will","please","my","our",'sheets',
                    'of','from','We','to','order','what','for','was','quantity','number','request','on']
def remove_noise(input_string):
    words=input_string.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text


def checkinput(request):

    if 'ipt' in request.GET:
        i = request.GET['ipt']
        i=i[1:-1]
        print(i)
    else:
        i=None
        print("NO")

    bot = ChatBot("finder_Buddy",
         storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
         logic_adapters=[
            "chatterbot.logic.InventoryAdapter",
            "chatterbot.logic.FindDealAdapter",
            "chatterbot.logic.LanguageAdapter",
            "chatterbot.logic.ChoiceAdapter",
             "chatterbot.logic.SpellAdapter",
            "chatterbot.logic.BestMatch",
             "chatterbot.logic.GreetingAdapter"
         ],
         filters=[
             'chatterbot.filters.RepetitiveResponseFilter'
         ],
        output_adapter="chatterbot.output.TerminalAdapter",
        database="database"
    )

    bot.set_trainer(ChatterBotCorpusTrainer)

    bot.train(
        "chatterbot.corpus.english"
    )


    bot_input = bot.get_response(remove_noise(i))
    da ={}
    da['ans']= bot_input
    return JsonResponse(da)
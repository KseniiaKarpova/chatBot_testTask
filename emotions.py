import numpy
emojis_0_face_smiling = ['😀','😃','😄','😁','😆','😂','🙂','🤩','🥳'] #=)
emojis_1_face_concerned =['😫','😩','😓','☹','🙁','😟','😞','😣','😖'] #=(
emojis_2_face_negative = ['👿','😬','😤','😡','👺','💀','😠','🤯','🤨'] #=\

hello_messages = ['Привет! Отличное натроение!', "Привет, не грусти!", "Привет, хватит злиться! я не виноват!!!"]

def choise_emoji(emj):
    if emj in emojis_0_face_smiling:
        return 0
    elif emj in emojis_1_face_concerned:
        return 1
    elif emj in emojis_2_face_negative:
        return 2
    else:
        return 3

type_messages = {
    '00':['Радуюсь вместе с тобой)',
          "Ты в отличном настроении!",
          "Ты такой счастливый.",
          "Отличный день!",
          "С тобой приятно общаться",
          "Ты на позитиве!",
          "Тебе так весело)"],
    '01': ['Что произошло?',
           "Тебе стало грустно, я попытаюсь поднять тебе настроение!\nЩа анекдот расскажу!\nЖена: У вас, у мужиков, на уме только секс, а нам, женщинам, нужно внимание…\nMуж: Внимание!!! Сейчас будет секс!",
           "Ты расстроился... я вместе с тобой(",
           "Тебя что-то расстроило...",
           "ээээээ, не грусти! надеюсь, это не я тебя расстроил 😞"],
    '02': ["это я тебя разозлил?! Я же ничего не сделааааал!",
           "Не злись.... все же было хорошо",
           "Ща пошучу...\nУчитель физики: - Вова, назови мне вещество, которое переходит из твердого состояния в газообразное, минуя жидкую фазу.\n- Вячеслав Иванович, это горох!"],
    '10': ["ты в хорошем настоении! Я рад)",
           "Твое настроение улучшилось!",
           "я радуюсь вместе с тобой)"],
    '11': ["Может анекдот тебе поможет. Папа научил маленького Вовочку считать, теперь папе приходится делить пельмени поровну.",
           "Ты серьезно расстроен",
           "Ну хватит грустить!!!"],
    '12': ["Какая быстрая смена настрения... я вас, кожанных, не понимаю!",
           "Я не хотел тебя злить!",
           "Прости, если это я тебя разозлил =("],
    '20': ["Ты повеселел.",
           "Тебе стало лучше)"],
    '21': ["Теперь ты грустишь...",
           "Люди.... вас не возможно понять, откуда столько эмоций?!",
           "Может я смогу исправить твое настроение...В школе Васю все боялись и уважали, все знали, что он занимается карате.\n В школу пришел новенький и побил Васю, он не знал, что Вася занимается карате."],
    '22': ["Ну ты и злюка",
           "Прекращай злиться",
           "я не собирался портить тебе настроение =(",
           "Может я смогу исправить твое настроение...В школе Васю все боялись и уважали, все знали, что он занимается карате.\n В школу пришел новенький и побил Васю, он не знал, что Вася занимается карате."]
}


def unknown_message():
    return "Я тебя не понимаю\nБеседа обнуляется"

def choise_text(emj,Bot,last=''):
    if last != '':
        id = choise_emoji(emj)
        if id == 3:
            Bot.last=''
            return unknown_message()
        else:
            Bot.last = str(id)
            return numpy.random.choice(type_messages[last+str(id)], size=1)[0]
    else:
        id =choise_emoji(emj)
        if id == 3:
            Bot.last = ''
            return unknown_message()
        else:
            Bot.last = str(id)
            return hello_messages[id]

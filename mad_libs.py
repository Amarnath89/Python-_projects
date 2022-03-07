from random import randint
import copy


word_dict = {
    'Name':['அமர்நாத் ',' கோகுல் ','பரணி ','எழில் ','கெளதம் '],
    'College_Name':['மகேந்திர இன்ஸ்டிடியூட் ஒப் டெக்னாலஜி நாமக்கல் '],
    'Game':['கிரிக்கெட்', 'ஹாக்கி',' புட்பால்',' டென்னிஸ்', 'ரன்னிங் '],
    'music':['ஆர் ரகுமான் ','அனிருத்','ஜிவ் பிரகாஷ்', 'யுவன்', 'ஆதி '],
    'Native':['செந்தாரப்பட்டி', 'மதுரை', 'வேலூர்', 'சின்ன சேலம்',' திருவண்ணாமலை'],
    'Bike':['யமாஹா',' பல்சர்', 'ஹீரோ', 'அப்பாச்சி' ]

}


Self_intro = (
    "வணக்கம் என் பெயர் {}"+
    "நான் {} கல்லூரில் படிக்கின்றேன் "+
    "எனக்கு பிடித்த விளையாட்டு{} "+
    "எனக்கு {} பிடிக்கும் "+
    "எனது சொந்த ஊர் {}" +
    "எனக்கு பிடித்த பைக் {} பைக் ."
)


def get_word(type, local_dict):
    ''' get a random word from the word_dict based on word type '''
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)


def create_story():
    ''' create a random story from word dict '''
   
    local_dict = copy.deepcopy(word_dict)
    return Self_intro.format(
       get_word('Name',local_dict),
       get_word('College_Name',local_dict),
       get_word('Game',local_dict),
       get_word('music',local_dict),
       get_word('Native',local_dict),
       get_word('Bike',local_dict)
)


story1 = create_story()
print(story1)
story2 = create_story()
print(story2)
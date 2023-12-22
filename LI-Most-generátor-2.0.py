import random

slova = ['negr', 'baseballka', 'frajer', 'džopa', 'špalek', 'kamos', 'fňukat', 'flákat', 'vobcan', 'plechovka',
         'mazec', 'mama', 'táta', 'havrani', 'jebač', 'trubka', 'kecat', 'vopravce', 'kokot', 'bobek', 'kolegyna',
         'mrdka', 'mladej', 'dvojka', 'trefa', 'šutry', 'šalina', 'pikoš', 'pivko', 'dřát', 'haluz', 'kudla',
         'bordel', 'kulový', 'fousatý', 'palička', 'frčet', 'feťák', 'bombička', 'široký', 'kulička', 'vykolejit',
         'vlez', 'vopice', 'flákotat', 'kudlit', 'koudla', 'kobyla', 'kost', 'vášnivej', 'prdel', 'žaludek', 'špek',
         'fajnšmekr', 'šelma', 'rachot', 'špunt', 'makak', 'mrzutý', 'drandit', 'štvát', 'vyřezat', 'míň', 'houska',
         'kalamita', 'hodit', 'špára', 'kompot', 'běhoun', 'šumák', 'pětek', 'chlapík', 'šílenec', 'břicho', 'pošuk',
         'duch', 'předělat', 'bóbr', 'vajgl', 'mihule', 'tvrdý', 'kosa', 'šutrovat', 'kápo', 'kečup', 'máca',
         'pytel', 'šmejdi', 'mamka', 'tácko', 'držet', 'pablbít', 'černoch', 'pivník', 'srajda', 'kulomet', 'bouřka',
         'frajerek', 'feťák', 'flákotat', 'kudlit', 'koudla', 'krást', 'šváb', 'šmekr', 'šlajsna', 'háček', 'bambulit',
         'klika', 'kocour', 'potlach', 'čmoud', 'houmlesák', 'zkaženec', 'fízl', 'parchant', 'hladej', 'moudra', 'chrchel',
         'duchodce', 'štikla', 'šůrovat', 'břít', 'bomba', 'klokan', 'škudla', 'kobelka', 'bóček', 'flákota', 'šmudla']

slabyky = ['ka', 'če', 'ře', 'se', 'ti', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', 'ů', 'ý', 'č',
           'ď', 'ě', 'ň', 'ř', 'š', 'ť', 'ž']

slovesa = ['říkat', 'běžet', 'skákat', 'zpívat', 'dělat', 'jet', 'vidět', 'dát', 'vzít', 'stát', 'mít', 'jít', 'číst',
           'jíst', 'psát', 'myslet', 'znát', 'přijít', 'dělat', 'přejít', 'projet', 'předělat', 'říkat', 'moci', 'chtít',
           'jet', 'umět', 'nechat', 'čekat', 'vědět', 'hrát', 'vidět', 'získat', 'setkat', 'stát', 'stavět', 'smět',
           'zapomenout', 'uspořádat', 'číst', 'poprosit', 'požádat', 'napsat', 'řešit', 'pracovat', 'učit', 'spatřit',
           'porozumět', 'vycházet', 'přemýšlet', 'čekat', 'dokázat', 'zasáhnout', 'zahrát', 'otevřít', 'nasadit',
           'překonat', 'přinést', 'ukázat', 'smát', 'soudit', 'sdělit', 'hlásit', 'stihnout', 'nastavit', 'přeložit',
           'odhalit', 'zapsat', 'doplnit', 'zavřít', 'objevit', 'dělat', 'zpívat', 'získat', 'učinit', 'prosít', 'přemýšlet',
           'rozvíjet', 'dokončit', 'nabídnout', 'přidat', 'převést', 'vyniknout', 'pomoci', 'měřit', 'zkontrolovat', 'změnit',
           'vytvořit', 'dát', 'prozkoumat', 'dovolit', 'nastavit', 'věřit', 'dostat', 'vylepšit', 'nosit', 'vyplnit']

def mužský_rod(slovesa):
    nová_slovesa = []
    for slovo in slovesa:
        if slovo.endswith('t'):
            nové_slovo = slovo[:-1] + 'l'
        elif slovo.endswith('at'):
            nové_slovo = slovo[:-2] + 'al'
        elif slovo.endswith('ět'):
            nové_slovo = slovo[:-2] + 'el'
        elif slovo.endswith('it'):
            nové_slovo = slovo[:-2] + 'il'
        elif slovo.endswith('et'):
            nové_slovo = slovo[:-2] + 'el'
        elif slovo.endswith('ít'):
            nové_slovo = slovo[:-2] + 'il'
        else:
            nové_slovo = slovo
        if nové_slovo.endswith('t'):
            nové_slovo += 'e'
        nová_slovesa.append(nové_slovo)
    return nová_slovesa

def ženský_rod(slovesa):
    nová_slovesa = []
    for slovo in slovesa:
        if slovo.endswith('t'):
            nové_slovo = slovo[:-1] + 'la'
        elif slovo.endswith('at'):
            nové_slovo = slovo[:-2] + 'ala'
        elif slovo.endswith('ět'):
            nové_slovo = slovo[:-2] + 'ela'
        elif slovo.endswith('it'):
            nové_slovo = slovo[:-2] + 'ila'
        elif slovo.endswith('et'):
            nové_slovo = slovo[:-2] + 'ela'
        elif slovo.endswith('ít'):
            nové_slovo = slovo[:-2] + 'ila'
        else:
            nové_slovo = slovo
        if nové_slovo.endswith('t'):
            nové_slovo += 'a'
        nová_slovesa.append(nové_slovo)
    return nová_slovesa

def střední_rod(slovesa):
    nová_slovesa = []
    for slovo in slovesa:
        if slovo.endswith('t'):
            nové_slovo = slovo[:-1] + 'lo'
        elif slovo.endswith('at'):
            nové_slovo = slovo[:-2] + 'alo'
        elif slovo.endswith('ět'):
            nové_slovo = slovo[:-2] + 'elo'
        elif slovo.endswith('it'):
            nové_slovo = slovo[:-2] + 'ilo'
        elif slovo.endswith('et'):
            nové_slovo = slovo[:-2] + 'elo'
        elif slovo.endswith('ít'):
            nové_slovo = slovo[:-2] + 'ilo'
        else:
            nové_slovo = slovo
        if nové_slovo.endswith('t'):
            nové_slovo += 'o'
        nová_slovesa.append(nové_slovo)
    return nová_slovesa

def generuj_text(paragrafy, rod):
    text = ""
    slovesa_v_rode = slovesa
    if rod == 'mužský':
        slovesa_v_rode = mužský_rod(slovesa)
    elif rod == 'ženský':
        slovesa_v_rode = ženský_rod(slovesa)
    elif rod == 'střední':
        slovesa_v_rode = střední_rod(slovesa)

    for i in range(paragrafy):
        for i in range(20):
            if random.random() < 0.5:
                slovo = random.choice(slova)
                while any(char in slovo for char in ['č', 'ď', 'ě', 'ň', 'ř', 'š', 'ť', 'ž']):
                    slovo = random.choice(slova)
                text += slovo + " "
            else:
                if random.random() < 0.7:
                    syllable = "".join(random.sample(slabyky, random.randint(1, 3)))
                    while any(char in syllable for char in ['č', 'ď', 'ě', 'ň', 'ř', 'š', 'ť', 'ž']):
                        syllable = "".join(random.sample(slabyky, random.randint(1, 3)))
                    text += syllable + " "
                else:
                    sloveso = random.choice(slovesa_v_rode)
                    text += sloveso + " "
        text += "\n\n"
    return text.strip().capitalize() + random.choice([".", "?"])

def zapis_do_souboru(text):
    with open('LoremIpsum.txt', 'w', encoding='utf-8') as file:
        file.write(text)

print("Vítej v Mosteckém lorem ipsum generátoru!")
rod = input("Jaký rod textu chceš generovat (mužský/ženský/střední)? ")
pocet_paragrafu = int(input("Kolik odstavců chceš vygenerovat? "))

generovany_text = generuj_text(pocet_paragrafu, rod)
print(generovany_text)

zapis_do_souboru(generovany_text)

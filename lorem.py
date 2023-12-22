
import random
import nltk
from nltk.util import ngrams
from collections import defaultdict
def rozdel(slovo):
    return [slovo[i:i+2] for i in range(0, len(slovo), 2)]

text = "vzrušený dav. Stoje blízko u vchodu do vozu, sevřen kruhem lidských těl a dýchaje dusný vzduch vycházející z jejich úst, tupě se díval, jak po černých klenutých chodbách klouzají zářivé zřítelnice vlaku. V jeho duchu byly zrovna takové temnoty, zrovna takové pronikavé a prudce se míhající záblesky světla. Dusil se ve zdviženém límci svrchníku, s pažemi přitisknutými k tělu, se rty pevně sevřenými a s čelem zpoceným a chvílemi, když se otevřely dveře do vozu, zmrazeným závany chladného vzduchu, a snažil se nevidět, snažil se nedýchat, snažil se nemyslit, snažil se nežít. Srdce tohoto osmnáctiletého jinocha, ještě téměř dítěte, bylo plné chmurné beznaděje. Nad ním, nad temnotami těch kleneb, té krysí chodby, kterou uháněla kovová obluda hemžící se lidskými červy, tam nahoře byla Paříž, sníh, studená lednová noc, příšera života a smrti válka. Válka. Před čtyřmi lety se tam uhnízdila. Tísnivě ležela na jeho jinošských letech. Přistihla ho zrovna v té mravní krizi, kdy jinoch, znepokojený probuzením smyslů, s úžasem odhaluje bestiální, slepé, drtivé síly života, jimž je vydán napospas, třebaže o život nežádal. A má-li povahu jemnou, srdce něžné a tělo útlé tak jako Petr, pociťuje hnus a hrůzu a neodvažuje se s nimi nikomu svěřit, hrůzu před těmi surovostmi, špinavostmi a nesmyslnostmi plodné a žravé přírody té prasnice požírající svůj vrh. V každém jinochovi od šestnácti do osmnácti let je kus hamletovské duše. Nechtějte na něm, aby chápal válku! (To je dobré pro vás, lidé rozvážní!) Má dost co dělat, aby pochopil život a odpustil mu. Obyčejně se jako do bezpečného útočiště zahrabává do snu a do umění tak dlouho, až zvykne tomu, že se stal člověkem, a až kukla skončí svůj úzkostný vývoj od housenky k motýlu. Jak velice potřebuje klid a tiché soustředění v těch vzrušených jarních dnech dozrávajícího života! Ale to 6 již za ním přicházejí do jeho útulku, vytahují ho, ještě docela útlého v jeho nové kůži, z toho stinného ústraní a vrhají ho na drsný vzduch, mezi otrlé lidstvo, jehož pošetilosti a nenávisti má ihned přijmout za své a odpykávat, třebaže je nechápe. Petr byl volán na vojnu se svými vrstevníky, osmnáctiletými chlapci. Za půl roku bude vlast potřebovat jeho tělo. Válka se ho dožaduje. Už jen šest měsíců mu popřává. Šest měsíců! Kdyby aspoň bylo možné prožít toho půl roku bezmyšlenkovitě! Zůstat v těchto podzemních chodbách! Nespatřit již nikdy kruté denní světlo…! Pohroužil se s uhánějícím vlakem do tmy a zavřel oči… Když je otevřel, na několik kroků před ním, oddělena od něho dvěma cizími těly, stála dívka, jež zrovna přistoupila do vozu. Napřed z ní uviděl jenom jemný profil pod stínem klobouku, světlou kadeř na pohublé tváři, světélko na líbezném líčku, krásnou linii nosu a vyklenutého rtu a pootevřená ústa, ještě teď rozechvělá spěšnou chůzí. Vešla mu do srdce dveřmi jeho očí; vešla tam celičká a dveře se za ní zavřely. Všechny venkovní zvuky zmlkly. Ticho. Klid a mír. Byla tam. Nedívala se na něho. Ba ještě ani nevěděla, že Petr je na světě. Ale byla v něm! Držel její němý obraz schoulený v náručí a neodvažoval se ani dýchat, aby ji neovanul jeho dech… V příští stanici tlačenice. Lidé se s křikem hrnuli do vozu již plného. Vlna lidských těl Petra strhla a nesla s sebou. Nad klenbou podzemní dráhy, tam nahoře v městě, temné výbuchy. Vlak se znovu rozjel. V té chvíli nějaký vyděšený muž, který si zakrýval rukama tvář a sestupoval ke stanici podzemní dráhy, se najednou skutálel ze schodů. Lidé ve vlaku ještě zahlédli, jak se mu mezi prsty řine krev… A znova černá chodba a temnoty… Ve voze zděšené výkřiky: „Němci jsou tady…!“ V tom všeobecném vzrušení všechna natlačená těla splývala v jeden celek a Petrova dlaň přitom uchopila ruku zlehka se ho dotýkající. A když zdvihl oči, spatřil, že je to Ona. Nevytrhla mu svou ruku. Na stisk jeho prstů odpověděly prsty vzrušeně, trochu křečovitě sevřené, a potom její měkká, horká ruka zůstala nehybně ležet v jeho dlani. Tak stáli v ochranném šeru a jejich ruce byly jako dvě ptáčata schoulená v témž hnízdě; a krev jejich srdcí protékala nepřetržitým proudem teplem jejich dlaní. Neřekli si ani slovo. Nedali si ani jediné znamení. Jeho ústa se téměř dotýkala kadeře na její tváři a okraje jejího ucha. Nehleděla na něho. O dvě stanice dále se ho pustila a on ji nezdržoval; proklouzla mezi těly a odešla, aniž ho spatřila. Když zmizela, napadlo ho, aby šel za ní… Pozdě. Vlak již zase jel. Na další zastávce vystoupil z podzemí do města. Zase tam našel noční vzduch, neviditelný lehký dotyk několika sněhových vloček a poděšené, svým strachem se bavící město; a nad městem se kdesi vysoko vznášeli váleční draví ptáci. Ale Petr neviděl nic jiného než tu, která byla v něm. A cestou domů držel v ruce dlaň té neznámé."
slova = text.split()

slabiky = []
for slovo in slova:
    slabiky.extend(rozdel(slovo))

bigramy = list(ngrams(slabiky, 2))

nasledujici_slabika = defaultdict(list)
for slabika1, slabika2 in bigramy:
    nasledujici_slabika[slabika1].append(slabika2)

# Funkce pro generovani
def generuj_text(pocet_slov):
    # nahodna poc. slabika
    aktualni_slabika = random.choice(slabiky)
    text = aktualni_slabika
    pocet_slabik_ve_slove = 0

    for _ in range(pocet_slov - 1):
        mozny_naslednik = nasledujici_slabika[aktualni_slabika]
        
        # Pokud neexistuji nasledujici slabiky zacne nove slovo
        if not mozny_naslednik:
            text += " "
            aktualni_slabika = random.choice(slabiky)
            text += aktualni_slabika
            pocet_slabik_ve_slove = 1
        else:
            # vybrani random slabiky
            naslednik = random.choice(mozny_naslednik)
            text += naslednik
            aktualni_slabika = naslednik
            pocet_slabik_ve_slove += 1

        # mezera
        if pocet_slabik_ve_slove >= 4:
            text += " "
            pocet_slabik_ve_slove = 0
    
    return text

# Vytvori odstavec s x slovy
odstavec = generuj_text(100)
print(odstavec)


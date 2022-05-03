
clue1="In a city nearly boston a green gift from china. The name of the father is first."
clue2="The head of the king was stolen from a beetle in the hand of a troll. Under what is second."
clue3="The most popular spell. Third of course."
clue4="The maker of iebs favorite droid is fourth."
clue5="Bertoldos keyword for the asylum is fifth."
clue6="The best line gandalf says to saruman is sixth."
clue7="The speed of an Awl Pike is seventh."
clue8="The answer to life, the universe, and everything is eighth."
clue9="For each word take only the first.  Erase spaces.  This is ninth."
clue10="Find the clue in the warrens this is last."

clue1ans=["Lu We'nan", "Kuai Xiang", "Ben Ngan", "Sun Yat-Zen", "Bill Naito", "William Naito", "Zhang Xin Sheng", "Terry Shrunk", "Charles Leon", "Asa Lovejoy"]
clue2ans=["Aurora Bridge", "Aurora", "Bridge"]
clue3ans=["Charm", "Charm Person"]
clue4ans=["Holowan Labs", "Coachelle Automata"]
clue5ans=["Malindi", "Sweet Hanna"]
clue6ans=["Saruman, your staff is broken", "One for the dark lord on his dark throne"]
clue7ans=[13, 9]
clue8ans=[42] 

allClues=f"{clue1} {clue2} {clue3} {clue4} {clue5} {clue6} {clue7} {clue8} {clue9} {clue10}"
allAns=clue1ans+clue2ans+clue3ans+clue4ans+clue5ans+clue6ans+clue7ans+clue8ans

def bookCipher(book, number):
    splitBook = book.split()
    print(f"{splitBook[number]} ", end='')

def interateAnswers():
    for part1 in clue1ans:
        for part2 in clue2ans:
            for part3 in clue3ans:
                for part4 in clue4ans:
                    for part5 in clue5ans:
                        for part6 in clue6ans:
                            for part7 in clue7ans:
                                for part8 in clue8ans:
                                    print(f"{part1[0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}{part7}{part8}")

def interateSplitAnswers():
    for part1 in clue1ans:
        for part2 in clue2ans:
            for part3 in clue3ans:
                for part4 in clue4ans:
                    for part5 in clue5ans:
                        for part6 in clue6ans:
                            for part7 in clue7ans:
                                for part8 in clue8ans:
                                    for splitPart1 in part1.split():
                                        print(f"{splitPart1[0]}", end='')
                                    for splitPart2 in part2.split():
                                        print(f"{splitPart2[0]}", end='')
                                    for splitPart3 in part3.split():
                                        print(f"{splitPart3[0]}", end='')
                                    for splitPart4 in part4.split():
                                        print(f"{splitPart4[0]}", end='')
                                    for splitPart5 in part5.split():
                                        print(f"{splitPart5[0]}", end='')
                                    for splitPart6 in part6.split():
                                        print(f"{splitPart6[0]}", end='')
                                    print(f"{part7}", end='')
                                    print(f"{part8}", end='')
                                    print("")

def iterateBookCipher():
    for part1 in clue1ans:
        for part2 in clue2ans:
            for part3 in clue3ans:
                for part4 in clue4ans:
                    for part5 in clue5ans:
                        for part6 in clue6ans:
                            for part7 in clue7ans:
                                for part8 in clue8ans:
                                    allAns=f"{part1} {part2} {part3} {part4} {part5} {part6} {part7} {part8}"
                                    try:
                                        bookCipher(allAns, 13)
                                    except:
                                        pass
                                    try:
                                        bookCipher(allAns, 42)
                                    except:
                                        pass
                                    print("\n")
                                    try:
                                        bookCipher(allAns, 13)
                                    except:
                                        pass
                                    try:
                                        bookCipher(allAns, 6)
                                    except:
                                        pass
                                    try:
                                        bookCipher(allAns, 9)
                                    except:
                                        pass
                                    print("\n")

#interateAnswers()
#interateSplitAnswers()
#iterateBookCipher()
#bookCipher(allClues, 13)
#bookCipher(allClues, 42)
#bookCipher(allClues, 13)
#bookCipher(allClues, 6)
#bookCipher(allClues, 9)

Babel1="""girding lactates miliaria pacify spaewives roneoed misworded nonfuel containeri
zations asystolic technology chias infomercial reimmerses mislived phosphoenolpy
ruvates mopped witchlike invasive nenuphars potshares urbanizations latescence p
ipkin wambengers carbineer radicalisms simulator outworth venturousnesses uranis
ms rejuvenized grantsmen propagated colleterial tittered probed eejits carnival 
allis reasonings blesser hypersexuality slipshoddiness bombination blamable nite
r bhajia misrelated defenseman mirligoes moisers rattly defiliation expiratory l
athing prequel clonidine futtocks metallographic surfboats photomapping vesicati
ng clying reverers animatingly crusting mitrailleuses dicacity snowmobilists hea
thfowls ghylls citadel epileptoid converging albinisms amphiboles crepiest trans
manche revealability reprocesses whelkier constellations asanas humstrums besott
edness nonbanks rictuses craps gemination hushpuppies vanquishable burpees fluge
lhorns porringer overgeneralizing pressgangs hardcovers cockled hoick paraformal
dehydes trillions erigeron turnout violist diallagoid mothproofer sportsmanships
 patrilineal reafforesting electroplating carpal contributors bedamned polyactin
al cartilaginous transect decretals gesellschaften greatcoated couponings tribut
ers feoffors bosboks nitrometric unhasped peptalk chromatosphere misust gemmates
 transistorizing flaxes sublates misrelying gonadectomies factionist welcome arc
hivist. baaab aabaa aabaa abaab abbab baabb baaba babaa aaaaa ababa ababa baaba 
aabbb baaaa aabaa aabaa baaab aabbb aabaa ababa aabab baaba babaa abbab baabb ab
bab ababa baabb ababb aabaa abbaa abaaa abbaa aabaa baaba aabaa aabaa abbaa abbb
a aaaaa aabba aabaa aabab abbab baabb baaaa aabbb baabb abbaa aaabb baaaa aabaa 
aaabb aabab abbab baabb baaaa oophoritis yomim adventitia liposculptures academi
a fairs rhodanising babbliest overwings plenipotent monosemy pyrophyllite quods 
faultlessness senoras laiking misfeign daemones mattify procurers deplete metaph
osphates appel hoarsest gillravage denaturalizations analgesias magpies overtart
 mobcap untamably godfathered dosshouses untacking somersetted sigillary adoptio
ns unpatriotically cosmographic dioxids diametrically subrents microreader param
orphine bazooms overevaluation extralimital algology polemics ponytailed ventril
oquise balmacaan mooniness yellochs malacology calibered ructations solved whist
led haemoflagellate decadence pioneer sibilancy mezzotint phwoah winterkilling i
mmixes poplar binate nonguest jackrolling frankincenses jangly uninquisitive inc
arnated transubstantial epicede aggregating heptapodies ananke fuddy ensured met
hylase refrigerated bobbejaans illiberalises drubber knesset shophar thrummiest 
tenses boerbuls slaughters lovastatin huffers klutzy depressives endangerment sp
eeler westered flavoproteins nonissue cityfied chigres preheated nonnatural disl
ikened coheiress baguio broose island carageenan consenter yarmulkas internals t
ressing almucantar prediabeteses klystron drucken numnah venetian resentingly un
cursing lactoscope photomultipliers pretend distributaries quicksilvered middlem
an invigorates runniness prescribers habiting switchman phenomenalist reinterro"""

Babel2="""le fogles hypoderms determinableness contrecoups despairs jiggier bespouses impr
ints galere covariants myosotes wetness duels ridgy mangulate irrationalistic tr
ainer spivviest compellations wersher dilutable boblets supremeness fugaciousnes
s cornerman waffie hermeticity tackle marons resods pillory excarnating saturnii
ds prolapse wheeziness talkers exsertions photogrammetrists ignominiously decenc
ies exothermicities lithoing turnouts farmeresses mersalyls overindustrialize zo
ris inodorously ruly screwed typhoidin hedgehops membership ovuliferous prase pr
osodical androsphinx ailantos phobias shochet mistrials cannikin middlebrows mal
axages petunias enantiomorphisms retracts sprees coastwise workdays jollificatio
ns angry realters fiating defray unwithholding styled verbally nonelectrical rad
ulate immunosuppresses sango faddles caiman isotopically benignest coscripts spa
nielling felching reblooms lockage antifederalists glout hitherto entreated labr
adors excursionises beneath epicanthus electronic flied melodists burdash fascia
s thanatophobias tensive bluer ulitis bedeafens peroneuses gentlest bughouses ev
erblooming fomenting seizor highballed eagle whodunnit wonders synovias unprepar
ed unbitting recoyle purlicue frypan inobedience liner good work archivist ... .
...  ... ...  . .....  .. .  .. ....  ... ...  . .  ... .  .... ....  . .  .... 
...  . ...  .... ..  . .....  ... ..  . .  .. ....  ... ...  .... ...  .... ... 
 . .....  . .  .... ..  . ...  .. ...  ..... ..  . .  ... .  ... .  .... ....  .
. ...  .... ..  . .....  . .....  .... ...  .. ...  . .....  ... .  .. .  .... .
...  ..... ..  ... ....  ..... .  ... ....  ... .  .... .....  ... ..  . .....  
.... ....  ..... ..  . .....  ... ...  .... ....  ..... ....  .... ....  ..... .
.  ... ....  ... .....  . .  .. ..  . .....  .... ....  ..... ..  ... ....  . ..
...  .. ....  .. ..  .. ...  .... ....  ..... .... outthrobbed resynthesising di
squietens pardee recapitulating cryptanalysts officering autocycle semilog astri
ngency bergmehl obsessively apperills comonomers tubulose senescence glomerate c
aressingly noels hydrophyton suspiciousness cronets motto cochairwomen paprica o
verreacts zibeths cyclodiene mesomeres photodissociates consubsists raja excommu
nication epistyles stub pleas rearmaments purtenances goethite regreeting harem 
coggling dewitting millstone mixup lawfulness irrigation unapparel recognizably 
whiptails reimbursable hardheadedly superbitches jerrycans discoursed slubbs emb
rute driftages antithetical antifederalists herring usufructuary formicaria elev
en kimchee heathbird insulsities annelidans wheezer unpastured subcostals pterod
actyl lough nervuration imbordered gracelessly khakis stannators snacks lustful 
postsynaptic erythrinas sorbarias ahigh abiogenist bereavements corticosterones 
pashed methacrylates packfongs dissociates ransomed frankly recusation bawdiness
 unfairest allegation enchasing pentaprism coursebook newsdesks wained malapropo
s horsecars pledgers garmentures yielders soubises buprestids dicasteries hovers
 trisections undefended trashy noctilio sententially outman spongins rustproofin
gs perfumeless cornicula coxcomb addresser ate pasquinaded disguiser pantyhose"""

Babel3="""butts verslibrist lucifers filmmaker propinquities diprotodontid seclusions prog
noses glamours fleshworms rupestrian bespice boohais minestone pectizable humorl
essness honeys epilimnions amphiarthrosis subimagines hyperbarically misadminist
ration wastelot prenumbered rewarders gastnesse resuscitation nominalising handh
elds illiteracy gauche undesirableness leafing crossbearer goodfella heath abase
 ebionitisms glamourizing courlan xerophthalmic strawless pollinisers discrimina
ble ultrasmall windrowing combinings fudging masculinely herbous hantavirus econ
omism forwander hypostomes mimer sacristy pontie tumbles relatednesses oversoak 
tollbars recharted xylyl ejectively barrefull preconises rustical buffers oophor
ectomy overbounds streptocarpus binger squirage shard scruffinesses glycosylatio
ns vorticities photodissociation barasinghas stingingnesses teleselling regenera
ble bisters dissentions engorgements galactagogues trappiest roking endocast unt
ypical petroglyphic latten magnetists bole franglais concrewed quarreling stoite
ring razzles dipchick bilayers untameableness dispurveys gambited depilator unle
al encierros appetitive rubious brominisms rueings gnatlike notodontid duits ins
ulse walkshorts shmoozes swipples evoke creaturely furloughing nidderlings amino
butenes juglets cornlofts blackmails tofts unmunitioned nosology outbitches king
les boychick pinching swingbeats anthranilates chlamydomonas toffishnesses chupp
a incorporable coincidental photograms zanze charros heelposts monecious kyles r
estrike hatcheck noncorroding our penultimate meeting, archivist.  it is bitters
weet. cebgbaznvy.pbz  installing aerobically zygosphenes miscibility chondrules 
junket semimonthlies redescriptions mestee kins elastomer ecstasise pronated cus
pid beaujolais unperches iguanodons hypersthenia ninepences oragious directionle
ss inchased pondweed cailleachs supplying summabilities unimaginably vacation no
nwriter linelike breastplates aucuba cyclonic disanchored renationalization runf
lats ragstone sinded prelatical pleiomerous misdealers dawdlers priest contracta
ble overhate dolichocephals retrocognition serjeancy counterirritant yacks washr
oom dovens generousnesses caconymies witchier implementations raggamuffin exuber
ances hebraising nonconservative wincer sewerless olpe capitalizing bobwheel int
erinstitutional tautaug conchate overspend finicky cataclases skittered aetiolog
ically saintless catworks outlandishly prommers coherent demurrer odism frugging
 hoteldom extoller dedifferentiates oversewn dagobas impaludism zoopsychologies 
bitstreams germanders ribonucleotides haematitic whupped suability profanity zoo
gonies quaker indescribables pere isogamete overrashly pugaree crafting clannish
ness souring musit exuberancy kinesis appointor egurgitated exultingly iridized 
incidentally devonport nonconducting obsolesces lazybones mournful jaggies mantr
as bushwas lophobranch applaud sororities metaphysicizes trickishly quasiperiodi
cities stared limnologist twentyish lipopolysaccharides honeybun pillarists inte
rferogram laciest enthrones rortier assailments bethralled transvestitism hyloph
ytes mocassins blamefulnesses satisfies megabyte roupit leud neglecters disincar"""

loreEntry9="""We were dead but now we are free.

Bernal Tesseract woke to the smell of fear.

He scrambled from his bedding and sprinted the low access tunnel that led to the main Warrens. In the sleeping hall all was not well. The clans bunks and nests lay empty. Some rabbits sat on their haunches, oddly, hunkered on the stone floor, their hands clutching their heads, as though trying to ward off some terrible and invisible pain.

But most of the clan stood rapt, erect, in neat lines they stood, and each line was eight rabbits long.

At their head stood a labour of Moles. Eight Moles in blue black robes had arranged themselves in a semicircle, they swayed gently in and out, rocking on their heels and murmuring in atonal unison.

Their darkscreens pulsed with sluggish ivory light that bathed the Warrens in a fractured, rhythmic flash. Bernal yawned. The smell of fear hung heavy all around him but this no longer struck him as important. In the molesong he caught a glimpse of an underground tower, earthworks plunging boldly down into the dark, the masterwork of a great race, a place of nobility, and a place full of secrets. It was a place he should like to visit, Bernal thought. Endless interweaving tunnels, glowing with grublight, and caverns ringing with dirgesong, melancholy yes, but also beautiful, and far from the sharp intruding sun. An orderly place, where an honest rabbit could work hard for a sure meal and a dry place to sleep.

Bernal paused in his reverie, for this last thought took him aback. It seemed overwrought. Food came easy to his clan. The Dead Warrens were an excellent place to sleep. And of the rabbits he knew, most were wily, all were skilled, and none were overfond of work. He opened his eyes.

A column of 24 rabbits, walking three abreast, were being led out of the sleeping hall by three Moles. The other five wandered among the stragglers, rabbits like himself who had not moved in response to the summons. One approached him, its darkscreen flashed white and Bernal felt a sizzling pain behind his eyes.

Fall in, worker. The Moles voice was in his head. Bernal took a staggering step forward and stopped. He opened his mouth to cry out, to rally his clan, but a bright flash from the darkscreen and a sudden surge of pain silenced him.

Try that again and Ill fry you, the Mole said. Now fall in.

Bernal gritted his teeth and refused to move. The Mole reached to adjust a dial on his darkscreen, but at that moment a dull yellow light spilled from the archway that led down into the Deep Warrens.

The Mole hissed, and his clan mates in the hall scurried to his side. The three Moles leading the column rushed back in to join their fellows. They formed a semicircle, their robes swayed about their feet as they rocked in and out. Each turned a dial on his darkscreen, a piercing electric hum filled the hall, and once again they intoned the molesong, waiting. They did not wait long.

A huge green rabbit framed the archway, clad in scavenger armor, a pulse rifle slung across his back. He stared at the Moles from behind the glowing yellow optics of his rebreather helmet and stood his ground. The song of the Moles took on the pitch of an ululating shriek, their darkscreens flashed with white heat, and the psiwave they sent out before them was a visible violet net that crackled in the air.

The net never reached him. It erupted in a hail of sparks, its wasted energy outlining a perfect sphere of empty space that extended for a meter in all directions around the rabbit.

Danger! shrieked the Moles. Hes psi-shielded! Retreat!

But it was too late for that. The rabbit touched a switch on his helmet and with an electric snap all eight darkscreens flashed searing white for an instant, and burned out. The Moles fell to the ground, writhing, and then went still.

Cast their bodies down into the grub tunnel, the green rabbit said. I think the Moles will not bother us for some time.

With that he turned back to the Deep Warrens, his pulse rifle still slung over his shoulder, untouched. The clan gathered together.

Who was that? the young ones wanted to know.

Bernal Tesseract smiled.

That, he said, was Salnar Tesseract. """

#strippedBabel3 = Babel3.strip("\n")
#for word in strippedBabel3.split():
    #print(word[0], end='')

for word in loreEntry9.split():
    print(word[0], end='')
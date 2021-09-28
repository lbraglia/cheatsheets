# Espressioni Regolari

Le espressioni regolari possono esser pensate come una combinazione di
literals (sequenze di caratteri) e metacaratteri, detto pattern, che
servono per identificare una varia famiglia di stringhe che rispettano
il pattern in qualche modo.  
Per **testare espressioni regolari** può essere utile

  - usare un servizio come <http://regexpal.com/>

  - usare tool dalla linea di comando

Nel secondo caso, creare un file di testo con alcune linee ed utilizzare
`grep` (preferibilmente con l’opzione `–color`

    l@np350v5c:~$ echo "Are you ready?" > foo
    l@np350v5c:~$ echo "yes I am" >> foo
    l@np350v5c:~$ grep --color "[^?.]$" foo
    yes I am

Oppure specificare

    grep --color "[^?.]$"

ed iniziare a digitare linee di testo. Appena si manderà a capo grep
analizzerà la frase ed evidenzierà i match avvenuti.  
grep ha numerose opzioni quindi si rimanda al manuale.  
Per un matching compatibile con le espressioni regolari di perl si può
usare il tool `pcregrep`, che costituisce anche un esempio di
programmazione con la libreria `PCRE` (oltre a `pcredemo`).

## Literals

Il pattern più semplice consiste solamente in literal: ad esempio la
literal `nuclear` matcherebbe le linee seguenti

    Chaos in a coutry that has nuclear weapons -- not good.
    lol if you ever say "nuclear" people immediately think death by radiation

Tutte le linee hanno `nuclear` al proprio interno e tutte sono spelled
allo stesso modo, tutte sono scritte con le minuscole e pertanto non vi
è alcuna deviazione dalla literal specificata.  
I pattern più semplici di espressioni regolari si compongono solamente
di literals: avviene un matchse la sequenza di literals avviene da
qualunque parte nel testo analizzato.  
Se però vogliamo ricercare una famiglia più ampia di parole (o esser più
precisi nel matching, ad esempio volendo escludere nuclear-power dalla
selezione) dobbiamo ricorrere ad un linguaggio per esprimere famiglie di
parole.

## Metacaratteri

Nello specifico abbiamo bisogno di un modo per esprimere

  - spazi bianchi delimitatori di parola

  - insieme di literals

  - l’inizio o la fine di una linea

  - alternative (es “guerra” O “pace”)

Ed ecco dove i metacaratteri entrano in azione.

##### Inizio di linea

Il metacarattere che rappresenta l’**inizio di una linea** è il caret.
Ad esempio

    ^i think

matcherà le seguenti linee

    ^i think this will be quite fun
    ^i think i need to go to work
    ^i think i first saw him in 1999

Ad esempio se abbiamo un `i think` nel mezzo di una linea, questa non
verrà matchata.  
Quindi questo è un modo per dire che voglio matchare un testo presente
solamente all’inizio di una linea.

##### Termine di una linea

Il segno del dollaro serve per matchare la **fine di una linea**,
pertanto

    morning$

matcherà con le seguenti frasi

    I walked in the rain this morning
    good morning

##### Gruppi di caratteri

Possiamo elencare un set di caratteri attravero le parentesi quadre. Ad
esempio

    [Bb][Uu][Sh][Hh]

matcherà

    vote Bush?
    the only bush i trust is mine

Entro quadre possiamo specificare un range di caratteri, specificando
inizio, fine e frapponendogli un `-`. Ad esempio

    ^[0-9][a-zA-Z]

matcherà qualsiasi linea che inizierà da una cifra seguita da una
qualsiasi lettera minuscola o maiuscola

    7th inning stretch
    3am - cant sleep

Utilizzato all’inizio di un gruppo di caratteri, il caret indica di NON
matchare la classe di caratteri indicata, ma matchare i rimanenti. Ad
esempio con

    [^?.]$

voglio matchare tutte le frasi che finiscono NON con un punto di domanda
o un punto. Quindi ad esempio si matcherà

    i like basketballs
    dont worry ... we all die anyway! # qui vi è un punto esclamativo
    helicopter under water?? hmmm     # qui interrogativo, ma non alla fine

##### Qualsiasi carattere

Il punto è indicato per matchare qualsiasi carattere, anche la mancanza
di carattere. Ad esempio

    9.11

matcherà

    its stupid the post 9-11 rules
    if any 1 of us did 9/11 we would have been caught in days
    Netbios: scanning ip 203.169.114.66
    call 911!    # esempio che mathca una mancanza

##### Or

Il pipe `|` può esser utilizzato per combinare due espressioni che
possono esser matchate alternativamente

    flood|fire

matcherà

    the global food make sense within the context of the bible
    is firewire like usb?

Si possono impiegare più OR come nel seguente caso

    flood|eartquake|hurricane|coldfire

e combinare espressioni regolari più complesse. Ad esempio

    ^[Gg]ood|[Bb]ad

matcherà le linee

    good to hear
    Good Afternon
    my middle name is trouble, Miss Bad News

Si noti in particolare quest’ultimo che ci insegna che `|` spezza
davvero le espressioni analizzate).

##### Raggruppamento

Nel precedente caso se volessimo matchare un iniziale bad dovremmo
riporre davanti il caret oppure comportarci come segue

    ^([Gg]ood|[Bb]ad)

il che macherà

    bad habbit
    Badcop, its because foo
    Good Monday

##### Espressione opzionale

E’ realizzato mediante il punto di domanda. Ad esempio

    [Gg]eorge( [Ww]\. )? [Bb]ush

matcherà

    george bush
    george bushes
    George W. Bush

##### Escaping

Nel caso precedente nella definizione della espressione regolare,
abbiamo utilizzato la backslash per indicare che intendiamo il punto
vero e proprio e non qualsiasi carattere. Questo si applica quando
invece di intendere un generico metacarattere, vogliamo intendere
effettivamente la lettera/simbolo corrispondente

##### Ripetizione

L’asterisco e il segno + sono metacaratteri usati per indicare la
ripetizione:

  - `*` indica “qualsiasi numero di volte, incluso 0, dell’elemento” cui
    ci si riferisce

  - `+` indica “almeno un numero di volte pari a 1”

Ad esempio

    (.*)

matcherà

    hello?? (24, m, germany)
    asdomar
    you're welcome (buddy)

Un esempio più complesso

    [0-9]+ (.*)[0-9]+

matcherà

    working as MP here 720 MP battalion, 42nd brigade
                       ^^^^^^^^^^^^^^^^^^^^

##### Quantificatori ad intervallo

Le graffe servono per quantificare un intervallo (ovvero il numero
minimo e massimo di match di una espressione che seguono). Ad esempio

    [Bb]ush( +[^ ]+ +){1,5} debate

Matcherà le righe che tra bush e debate, grossolanamente, pongono da 1 a
cinque parole.  
Le graffe non necessariamente debbono avere due numeri specificati. Le
possibilità sono:

  - `m,n`: almeno `m`, ma non più di `n`

  - `m`: esattamente `m` volte

  - `m,`: almeno `m` volte

  - `,n`: non più di n volte (?? è vero??)

##### Memorizzazione del match

Nella maggior parte delle implementazioni, le parentesi tonde possono
esser utilizzate anche per memorizzare il testo matchato dalla
sottoespressione (*subexpression*) inclusa in esso.  
Ci riferiremo in seguito alle variabili `\1`, `\2` ecc per riferirci al
primo, secondo ecc match.  
Ad esempio l’espressione

``` 
 +([a-zA-Z]+) +\1 +
```

matcha le linee dove una qualsiasi parola, in seguito ad uno o più
spazi, è ripetuta due volte vicino e separate da uno o più spazi

    time for bed, night night twitter
    my tattoo is so so itchy today

questo matcha indipendentemente dal valore del primo match tra parentesi

##### Greediness di \*

L’asterisco è greedy quindi cerca di matchare sempre la linea piu lunga
possibile che soddisfa l’espressione regolare cui si riferisce. Per
esempio

    ^s(.*)s

significa parti con una s poi cerca 0 o qualsiasi carattere fino a che
trovi un’altra s. Questo matcha

    sitting at starbucks
    ^^^^^^^^^^^^^^^^^^^^            # non si ferma alla prima s di starbucks
    setting up mysql and rails
    ^^^^^^^^^^^^^^^^^^^^^^^^^^

La greediness di \* può esser disattivata con ? (che dice al primo di
divenire *lazy*), come in

    ^s(.*?)s

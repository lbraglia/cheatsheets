# Tikz

## Setup
Includere nel preambolo
```latex
\usepackage{tikz}
\usetikzlibrary{arrows,snakes,backgrounds}
```
Per includere un immagine utilizzare `tikzpicture`
```latex
\begin{figure}
  \centering
  \begin{tikzpicture}
     %comandi tikz qui
  \end{tikzpicture}
  \caption{Immagine di  tikz} 
  \label{fig:tikztest}
\end{figure}
```
Tikz può essere usato anche piu comodamente (es in linea al testo) mediante
```latex 
\tikz[options]{commands}
```
(che altro non fa che porre ; al termine del programma e inscatolarlo in un tikzpicture

## Concetti base
Un **path** è una serie di linee e curve. Un path può essere disegnato, riempito, ombreggiato o clippato (??), e ogni combinazione dei quattro precedenti.
- *Drawing* (also known as stroking) can be thought of as taking a pen of a certain thickness and moving it along the path, thereby drawing on the canvas.
- *Filling* means that the interior of the path is filled with a uniform color. Obviously, filling makes sense only for closed paths and a path is automatically closed prior to filling, if necessary.Given a path as in
```latex 
\path (0,0) rectangle (2ex,1ex);
```
you can draw it by adding the draw option as in

```latex 
\path[draw] (0,0) rectangle (2ex,1ex)
```
Il comando `\draw` è una abbreviazione di `\path[draw]`.

- *Ombreggiatura* e *clipping* lasciamoli stare per ora

Un **nodo** è un path dotato di nome al quale è possibile riferirsi in seguito:
- Ad esempio creiamo un nodo con una scritta Hello, piazzato in 0,0 e indicizzato come x e un cerchio piazzato in 3,1 indicizzato con y è che contiene una formula
```latex
\path 
  (0,0) node (x) {Hello} 
  (3,5) node[circle,draw](y) {$\sin^2 x +\cos^2 x=1 )$};
```
In seguito li colleghiamo mediante una freccia

```latex 
\draw[->,blue] (x) -- (y);
```
**Coordinate**
- Nel caso piu semplice le coordinate nel grafico possono essere specificate mediante dimensioni di $\TeX$, separate da virgole e posti entro parentesi del tipo `(x,y)`.
- Se non si fornisce una unità come in `(2,1)`, si specifica un punto nel sistema di coordinate di pgf, *di default i centimetri*. Alcune dimensioni tex rilevanti:
```
pt: point (72.27 points = 1 inch)
in: inch
cm: centimeter (2.54 centimeters = 1 inch)
mm: millimeter (10 millimeters = 1 centimeter)
```
- Specificando tre numeri come in (1,1,1) si fa un punto nel sistema di coordinate xyz.
- Si può anche specificare un punto in *coordinate polari*, utilizzando i due punti invece di virgola. Ad esempio `(30:1cm)`  means "1cm in a 30 degrees direction".
- Si può porre come *prefisso alle coordinate* (x,y):
	- il ++ per renderle relative rispetto all'ultima coordinata specificata (considerata come ancora). Ad esempio `++(1cm,0pt)` significa "1cm a destra della precedente posizione".  In seguito questa nuova posizione sarà considerata come "ancora" per i punti a venire. Ad esempio `(1,0) ++ (1,0) ++ (0,1)` specifica le coodinate (1,0), poi (2,0), and (2,1).
	- Se invece poniamo solamente un +, non verrà aggiornata l'"ancora" che rimane l'ultima valida/specificata.  Ad esempio `(1,0) + (1,0) +(0,1)` specifica le coordinate (1,0), poi (2,0), e (1,1).

## Comandi utili
### Griglia
Per disegnare una griglia da 0,0 a 2,3:
```latex 
\draw[step=1, style=help lines] (0,0) grid (2,3);
```
`step=1` è il default e si sarebbe potuto omettere, ma può essere utile per specificare dei tick differenti (es a 0.5) style specifica uno stile (in questo caso predefinito utile per le griglie di background).\
Alternativamente utilizzare `grid` che ho così definito

```latex 
\newcommand{\grid}[4]{
  \draw[style=help lines] (#1,#3) grid (#2,#4);
}
```
### Piano cartesiano
Utilizzare `\cartesiano`, così definito
```latex
\newcommand{\cartesiano}[4]{
  \draw[->] (#1 -.2 ,0) -- (#2 + .2,0);
  \draw[->] (0,#3 -.2) -- (0,#4 +.2);
  \node [right] at (#2 + .2 ,0) {$x$};
  \node [above] at (0,#4 +.2) {$y$};
}
```
### Aggiungere i ticks ad un cartesiano
Utilizzare `ticks` che ho così definito
```latex
\newcommand{\ticks}[4]{
  \foreach \x in {#1, ...,#2} \draw (\x,0)-- ++(0,2pt);
  \foreach \y in {#3, ...,#4} \draw (-1pt,\y)-- ++(+2pt,0);
}
```
### Disegnare una funzione
```latex 
    \draw [domain=0:2, samples=100] plot (\x, {\x^(3/2)});
```
Una cosa che può essere utile se la funzione ci sembra un poco spigolosa è aumentare il numero di punti che vengono valutati\
mediante samples (di default a 25)

```latex
\draw[domain=-5:5, samples=100, red] plot (\x,{sin(\x r) + 1});
```
### Funzioni già disponibili
Non è necessario definire tutte le funzioni; alcune disponibili sono riportate sotto
```latex 
factorial(\x) 
sqrt(\x)
pow(\x,y)
exp(\x)
ln(\x)
log10(\x)
log2(\x)
abs(\x),
mod(\x,y) (x modulo y)
round(\x) 
floor(\x) , 
ceil(\x)
sin(\x) (sin(x), it assumes that x is in degrees; if x is expressed in radians use sin(\x r)),
cos(\x) (cos(x), it assumes that x is in degrees; if x is expressed in radians use cos(\x r)), 
tan(\x) (tan(x), it assumes that x is in degrees; if x is expressed in radians use tan(\x r)),
min(\x,y,), max(\x,y)
rnd (senza argomenti) stampa un numero casuale tra 0 e 1.
```
### Costanti matematiche
```latex
e which is equal to 2.718281828
pi, which is equal to 3.141592654
```
### Combinazione di funzioni per crearne di nuove
Chiaramente le funzioni di base possono esser combinate per generare funzioni più complesse, ad esempio
```latex
\draw [domain=0:2*pi] plot (\x, {(sin(\x r)* ln(\x+1))/2});
\draw [domain=pi:2*pi] plot (\x, {cos(\x r)*exp(\x/exp(2*pi))});
```
### Plot di funzione con nome o definizione a destra
```latex
\draw[color=red] plot (\x,\x) node[right] {$f(x) =x$};
\draw[color=blue] plot (\x,{sin(\x r)}) node[right] {$f(x) = \sin x$};
\draw[color=orange] plot (\x,{0.05*exp(\x)}) node[right] {$f(x) = \frac{1}{20} \mathrm e^x$};
```
### Porre scritte e formule matematiche
Per porre scritte si usa node
```latex
\node at (1,1) {yes};
\node [above] at (1,1) {nord};
\node [below] at (1,1) {sud};
\node [left] at (1,1) {ovest};
\node [right] at (1,1) {est};
```
La prima di sopra pone "yes" centrato su 1,1; le altre quattro con i punti cardinali sono poste sopra, sotto, a sinistra e a destra, snza mai toccare il punto 1,1.

Possiamo usare anche:
```latex
\node [above right] at (.5,.75) {nord est};
\node [below right, red] at (.5,.75) {sud est};
\node [below left, purple] at (.5,.75) {sud ovest};
\node [above left, green] at (.5,.75) {nord ovest};
```
E' possibile scrivere formule matematiche usando $$ come al solito

```latex
\node at (.5,.75) {$f(x) = \sqrt{x^2}$};
```latex
Per andare a capo in un testo si usa `\\`, quando lo si fa però bisogna specificare l'allineamento (se no non compila) del testo\
mediante align (left, right, center).

```latex
\node[align=left, below] at (1.5,-.5){Test\\ allineato \\a sinistra};
```
### Forme geometriche
Ad esempio per una spezzata, un rettangolo che parte da 0,0 e va a 2,2 e la circonferenza trigonometrica si usa
```latex
\draw (0,0) --(1,2) -- (2,3) -- (1,0); %spezzata
\draw (0,0) rectangle (2,2);           %rettangolo
\draw (0,0) circle [radius=1];         %cerchio
```
### Formattazione spezzate (tipo tratteggio, dimensione, colore etc)
**Tipo di tratteggio**\
Disponibili: solid (default), dotted, densely dotted, loosely dotted,\
dashed, densely dashed, loosely dashed

```latex
\draw [dashed] (0, 0.5) -- (2,0.5);
\draw [dotted] (0,0) -- (2,0);
```
**Spessore delle linee**\
Disponibili ultra thin, very thin, thin, semithick, thick, very thick, ultra thick

```latex
\draw [ultra thick] (0,1) -- (2,1);
\draw [thick] (0,0.5) -- (2,0.5);
\draw [thin] (0,0) -- (2,0);
```
Per spessori personalizzati invece (es la prima specifica larghezza di 12 punti, la seconda di 0.2 cm):

```latex
\draw [line width=12] (0,0) -- (2,0);
\draw [line width=0.2cm] (4,.75) -- (5,.25);
```
**Colore** \
Disponibili: red, green, blue, cyan, magenta, yellow, black, gray,\
darkgray, lightgray, brown, lime, olive, orange, pink, purple, teal,\
violet e white.

``` latex
\draw [gray] (0,1) -- (2,1);
\draw [red] (0, 0.5) -- (2,0.5);
\draw [blue] (0,0) -- (2,0);
```
Si possono definire colori custom (cfr manuale)

**Termine della linea**
```latex
\draw [->] (0,0) -- (2,0);
\draw [<-] (0, -0.5) -- (2,-0.5);
\draw [|->] (0,-1) -- (2,-1);
\draw [<->] (0,2) -- (0,0) -- (3,0);
```
Nell'ultimo caso, se si fa una spezzata che passa per diversi punti, l'inizio e la fine solamente sono coslati dalle particolarità tra parentesi quadre; comode ad esempio per disegnare gli assi.

**Angoli arrotondati**
```latex
\draw [rounded corners] (0,2) -- (0,0) -- (3,0);
```
### Aree e riempimento
Quando un "path" è chiuso lo si può colorare all'interno mediante `fill=colore`:
- se il colore del bordo non è specificato, continua ad esser nero;
- se si specifica solo fill senza specificare il colore del riempimento, questo sarà preso dal colore del bordo;
- se una figura viene sovrapposta ad un'altra ed entrambe sono con riempimento, ne uscirà sopra la figura specificata per ultima

```latex
\draw [fill] (0,0) rectangle (1,1);
\draw [draw=black, fill=red] (2,0) rectangle (3,1);
\draw [blue, fill=blue] (4,0) -- (5,1) -- (4.75,0.15) -- (4,0);
\draw [fill] (7,0.5) circle [radius=0.1];
```
Se si vuole creare un riempimento trasparente, bisogna specificare il livello di trasparenza (1 minima, 0 massima)
```latex
\draw [fill=gray, fill opacity=.3] (8,3.5) ellipse (1.5 and 2);
```


## Misc
### Cicli foreach
- Per effettuare un ciclo si usa
```latex
\foreach \nomevar in {lista valori} {comandi che usano \nomevar}
```
Se si forniscono due numeri prima del `...`, foreach usa la loro differenza per definire lo stepping. Ad esempio un modo per creare dei tick da uno a 10 su una linea:

```latex
\foreach \x in {1,2,...,10}
\draw[xshift=\x cm] (0pt,-1pt) -- (0pt,1pt);
```
- I foreach possono esser incastonati, ad esempio come segue:
```latex
\foreach \x in {1,2,...,5}
\foreach \y in {1,...,5}
{
   \draw (\x,\y) node {\x,\y};
}		
```
- Se si vuole looppare su due/tre variabili contemporaneamente si deve adottare una sintassi del tipo: 
```latex 
foreach \x / \y in {1/2 , a/b} {"\x\ and \y "} 
``` 
che stampa "1 and 2 a and b". il secondo `\` dopo `\x` serve per avere lo spazio ...

- Per plottare 3  punti centrati in diverse coordinate e aventi differenti diametri, ad esempio:
```latex
\foreach \x / \y / \diameter in {0 / 0 / 2mm, 1 / 1 / 3mm, 2 / 0 / 1mm}
\draw (\x,\y) circle (\diameter);
```
### Figure multiple
- Un esempio di figura multipla con tikz. Si usa sempre subfloat come fatto per figure/tabelle, ponendo il codice al posto di includegraphics
```latex
\begin{figure}
\centering
\subfloat[][Segmenti consecutivi. \label{fig:segcons}]
{
\begin{tikzpicture}[scale=1]
  \draw[red,-] (-1,1) -- (0,0) -- (2,0);
  \draw [fill] (-1,1) circle [radius=1pt];
  \draw [fill] (0,0) circle [radius=1pt];
  \draw [fill] (2,0) circle [radius=1pt];
  \node [below] at (-1,1) {A};
  \node [below] at (0,0) {B};
  \node [below] at (2,0) {C};

\end{tikzpicture}
} \qquad\qquad
\subfloat[][Segmenti adiacenti. \label{fig:segadiac}]
{
\begin{tikzpicture}[scale=1]
  \draw[red,-] (-1,0) -- (0,0) -- (2,0);
  \draw [fill] (-1,0) circle [radius=1pt];
  \draw [fill] (0,0) circle [radius=1pt];
  \draw [fill] (2,0) circle [radius=1pt];
  \node [below] at (-1,0) {A};
  \node [below] at (0,0) {B};
  \node [below] at (2,0) {C};

\end{tikzpicture}
}
\end{figure}
```
### Stretching di figura
- Se desideriamo stretchare una figura dobbiamo utilizzare `scale` (proporzionale) oppure`xscale` e `yscale` come opzione all'environment `tikzpicture`. Ad esempio il prossimo codice mostra un segmento di lunghezza 1 che viene stretchato verticalmente fino a sembrare un segmento che arriva in 1,2, invece che in 1,1
```latex
\begin{tikzpicture}[xscale=1,yscale=2]
\draw[help lines] (0,0) grid (0,0);
\draw (0,0) -- (1,1)	
\end{tikzpicture}
```
### Creazione di stili
- è possibile specificare propri stili mediante
```latex
\tikzstyle{rock lines}=[red,very thin]

\begin{tikzpicture}
\draw[style=rock lines] (2,0) grid +(2,2);
\end{tikzpicture}

```
il nuovo stile inizia a funzionare a partire dal grafico successivo (non i precedenti)

- Se il += viene dato nella definizione di stile, l'opzione è aggiunta a partire da uno stile (che viene modificato a partire da tal momento)
```latex
\tikzstyle{help lines}+=[dashed]
```
### Tipi di linee (pacchetto snakes)
- Non vi sono solamente linee dritte ma si possono utilizzare anche\
linee particolari (es snakes)

```latex
\draw[snake=zigzag] (0,0) --(1,2); # andamento a zigzag
\draw[snake=brace] (0,0) --(1,2); # parentesi graffa
\draw[snake=triangles] (0,0) --(1,2); # triangolini
```
In generale le opzioni di una determinata linea vengono specificate tra parentesi graffe PRIMA della prima tonda (che specifica il punto di partenza); se ve ne sono piu per un medesimo tratto, vanno separate da virgola. Vediamo nel seguito le opzioni piu comuni

### Plotting di archi
- Per disegnare degli archi la sintassi è qualcosa di simile
```latex
\draw (3mm,0mm) arc (0:30:3mm);
```
Si specifica un punto di partenza dell'arco, seguito da arc, seguito ancora da una tripletta separata da due punti tra tonde Le prime due componenti della tripletta sono angoli, l'ultima componente è un raggio. Ad esempio (10:80:10pt) significa arco da 10 gradi a 80 gradi di raggio di 10 punti

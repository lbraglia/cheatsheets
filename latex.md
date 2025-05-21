# LaTeX


## Matematica
- Singole equazioni vanno impostate nell'environment `equation` o
  `equation*` (il primo stampa anche il numero dell'equazione, ed è
  possibile farvi riferimento mediante una label).
- Per piu' righe di matematica e colonne allineabili utilizzare
  `align` o `align*`, con la seguente sintassi:
  ``` latex
  \begin{align*}
    y &= asd  \\ 
      &= foo
  \end{align*}
  ```
- Se una linea e prosieguo (es una somma di termini che sfocia in più
  di una linea) di un'altra potrebbe esser utile `\qquad {}` per
  indentare.
- Se si desidera che solo una linea abbia la numerazione, sopprimere
  le numerazioni in tutte le altre linee ponendo `\nonumber` prima di
  `\\`.
  ``` latex
  \begin{align}
    f(x) &= x^4 + 7x^3 + 2x^2 \nonumber \\
         & \qquad {} + 10x + 12
  \end{align}
  ```

### Definire comandi e alias
```latex
\newcommand{\vettore}[1]{\overrightarrow{#1}}
\let\vec\vettore
```

### Operatori "custom"
Non tutti gli operatori dell'analisi sono disponibili (ad esempio Re
per l'estrazione della parte reale di un complesso). Per far capire a
latex che è un operatore (il che lo fa stampare NON in corsivo,
bisogna adoperare \operatorname, ad esempio:
``` latex
\operatorname{Re} z = a
```

### Testo sopra/sotto parti di formula
Si realizzano rispettivamente mediante
``` latex
\overbrace{frammento_formula}^\text{contenuto}
\underbrace{frammento_formula}_\text{contenuto}
```

### Creare box nelle equazioni
Per un box che contenga solo la formula (e non il numero si può
utilizzare `boxed`, ad esempio
``` latex
\begin{equation}
\boxed{x^2+y^2 = z^2}
\end{equation}
```


### Frecce

``` latex
\rightarrow           \Rightarrow
\leftarrow            \Leftarrow
\leftrightarrow       \Leftrightarrow
\longrightarrow       \Longrightarrow
\longleftarrow        \Longleftarrow
\longleftrightarrow   \Longleftrightarrow
```

### Numeri esplicativi
Usare `explained`

```latex 
\begin{equation}
  asd = foo \explained{\iff}{1} bar = baz
\end{equation}
dove $(1)$ è dovuto al fatto che
```

**Template per esercizi**
```latex
\begin{exercise}[]
  \id{} \page{} \source{} \topic{}
  \begin{question}
  \end{question}
  \begin{hint}
  \end{hint}
  \begin{solution}
  \end{solution}
\end{exercise}
```

## Formattazione e cose di base

### Note a margine varie o evidenziazione di scritto
```latex
\newcommand{\colored}[2]{{\color{#1} #2}} 
\newcommand{\todo}[1]{{ \marginpar{\color{red}\textbf{TODO}: #1} }}
\newcommand{\nb}[1]{{ \marginpar{\color{blue}\textbf{NB}: #1} }}
\newcommand{\fixme}[2][fixme]{{ \colored{red}{#2} } \todo{#1}}
```

### Link ipertestuali
``` latex
\href{url}{testo}
```

### Includere file verbatim
Utilizzare il pacchetto `verbatim` nell'intestazione
``` latex
\verbatiminput{nome_file}
```

### Citazione
Si possono utilizzare gli environment `quote` o `quotation`:
quest'ultima indenta le colonne ed è meglio per citazioni lunghe
```latex
\begin{quote}
\end{quote}
\begin{quotation}
\end{quotation}
```

### Cross-reference nel documento
Per creare una referenza a section subsection, figure table o teorema\
utilizzare
``` latex
\label{nomepersonalizzato}
```
Per utilizzarlo: 
- `\pageref{nomepersonalizzato}` restituisce la pagina della label
- `\ref{nome}` restituisce il numero della label (es numero tabella,
  teorema ecc)

## Tabelle e figure

### Indicazioni generali
Si usano rispettivamente l'ambiente `tabular` e il comando `\includegraphics` all'interno degli ambienti `table` e `figure` che sarà piazzata da latex al meglio nel documento, accompagnata da didascalia. Si possono anche dare direttive sul piazzamento come segue
``` latex
\begin{table}[ht] %la sequenza di possibili posizionamenti è seguita
\begin{figure}[b]
```
e le opzioni disponibili sono le seguenti

| lettera  | significato  |
|:---------|:---------|
| h        | qui (here), se possibile					|
| t        | in cima (top) alla pagina				|	
| b        | in fondo alla pagina						|
| p        | in una pagina di soli oggetti mobili		|
| !        | forza ma meglio di no (usare tabular allora)|



### Tabelle
Si pone un tabular dentro a table: le opzioni di tabular sono

| lettera  | significato  |
|:---------|:---------|
| l  |  left-justified column |
| c | centered column |
| r | right-justified column|
| p{'width'} | column with text vertically aligned at the top|
| m{'width'} | column with text vertically aligned in the middle (array package)|
| b{'width'}| column with text vertically aligned at the bottom (array package)|

Tabella **minimale** (copia e incolla)
```latex
\begin{table}
\centering
\begin{tabular}{ll} 
  \hline
  & \\
  \hline
  & \\
  &  \\
  \hline
\end{tabular}
\caption{} 
\label{tab:}
\end{table}
```
Tabella **più elaborata**
```latex
\begin{table}
\centering
\begin{tabular}{lcccc} 
  % Nelle qui si puo' utilizzare uno o + "|" per specificare le
  % linee di separazione verticali
  \hline
  & & & & & \\
  \hline                  
  
  % \hline serve per la linea orizzontale completa
  % \cline{da_colonna-a_colonna} serve a specificare la linea
  % orizzontale non completa da dove a dove deve andare
  % Per un contenuto che occupa più di una linea utilizzare
  % multicolumn:
  % 
  % \multicolumn{numero_colonne}{allineamento}{scritta}
  & & & & & \\
  & & & & & \\
  \hline    
\end{tabular}
\caption{Caption della tabella} 
\label{tab:asd}
\end{table}
```
Per **celle che vanno a capo** utilizzare il custom
```latex
\specialcell{riga1 \\ riga2 \\ riga3}
```

Per **colonne che wrappano testo automaticamente** usare p{larghezza colonna} come qui: 
la prima larga 1 inch e wrappa, l'ultima 1.5 inches e wrappa
```latex 
\begin{tabular}{m{1in}clllllm{1.5in}}
```

Per **tabelle lunghe** che si estendono su piu pagine guardare
`longtable`.

Per **tabelle larghe**, per ruotare di 90 gradi è utile il pacchetto
`rotating` che definisce l'ambiente `sidewaystable`, da usare nel modo
seguente:

``` latex
\begin{sidewaystable}Template per esercizi
\caption{}
\label{}
\centering
\begin{tabular}
  ...
\end{tabular}
\end{sidewaystable}
```


### Figure
Step per l'inclusione:
- avere la figura in pdf
- decommentare l'uso del pacchetto graphicx 
```latex 
\usepackage[pdftex]{color,graphicx}
```
- utilizzare il comando `includegraphics`
```latex
\begin{figure}
  \centering
  \includegraphics[scale=0.4]{path/file/pdf}
  \caption{Caption della figura.}
  \label{fig:latvar}
\end{figure}
```
La sintassi di `includegraphics` è
``` latex
\includegraphics[key=value, . . . ]{path_file}
```
con:

- `path_file` NON deve contenere estensione .pdf
- possono esser key le seguenti

| key  | significato  |
|:--|:--|
|width    | scale graphic to the specified width   |
|height   | scale graphic to the specified height  |
|angle    | rotate graphic counterclockwise        |
|scale    | scale graphic                          |

- Per **ruotare** la figura utilizzare il pacchetto rotating e
  l'environment `sidewaysfigure`, similmente a quanto illustrato con
  le tabelle/sidewaystable`.


### Altri tips/tricks per figure e tabelle

#### Figure/tabelle multiple/affiancate
Per affiancare piu figure o tabelle si usa il pacchetto `subfig` (che richiede la presenza del pacchetto `caption`, per la personalizzazione delle caption) mediante il comando `subfloat`\
Un esempio di figure multiple in un box $2 \times 2$:
``` latex
\begin{figure}
\centering

\subfloat[][\emph{Mano con sfera riflettente}.]{\includegraphics[width=.45\textwidth]{fig/sfera}} 
\subfloat[][\emph{Belvedere}.]{\includegraphics[width=.45\textwidth]{fig/belvedere}} 
\\
\subfloat[][\emph{Cascata}.]{\includegraphics[width=.45\textwidth]{fig/cascata}} 
\subfloat[][\emph{Salita e discesa}.]{\includegraphics[width=.45\textwidth]{fig/salita_discesa}}

\caption{Alcune litografie di M.~Escher.}
\label{fig:subfig}
\end{figure}
```
nel primo argomento facoltativo di `subfloat`, se usato, si mette la didascalia breve da mandare nel relativo indice (`listoffigures` o `listoftables`);\
nel secondo ci va la didascalia che comparirà effettivamente sulla pagina;\
per riferirsi a un sottooggetto in particolare da altre parti del documento, `label` va dato dentro il secondo argomento facoltativo immediatamente dopo la sottodidascalia.
#### Caption avente citazione
Utile sia in tabelle (per citare la fonte dell'immagine o dei numeri), è impostabile seguendo il modello
``` latex
\caption[roba dell'indice]{roba che va nella caption}
```
Ad esempio

``` latex
\caption[Reddito, aspirazioni e felicità.]{Reddito e felicità. Fonte: \cite{Easterlin2001}}
```
####  Tabelle/figure avvolte nel testo
In alcune circostanze può essere desiderabile "avvolgere" un oggetto con del testo, magari anche solo per movimentare la pagina. Per farlo serve il pacchetto wrapfig\
Il pacchetto definisce l'ambiente wrapfloat nel quale mettere l'oggetto con i comandi consueti

Un esempio
``` latex

\begin{wrapfloat}{figure}{I}{0pt}
\includegraphics[width=0.5\textwidth]{Relativo}
\caption{Esempio di figura "avvolta" da un testo.}
\end{wrapfloat}
```
La sintassi
``` latex
\begin{wrapfloat}{ oggetto }{ collocazione }{ larghezza }
```
tre argomenti obbligatori:
- **oggetto** indica il tipo di oggetto da includere (figure o table, da non confondere con gli ambienti omonimi);
- **collocazione**, che dice a dove mettere l’oggetto sulla pagina, accetta una sola delle otto opzioni spcificate in seguito, in maiuscolo o in minuscolo a seconda che si voglia mettere l’oggetto “esattamente qui nel testo” o si voglia creare un oggetto mobile, rispettivamente. Le preferenze di collocazione sono specificabili mediante

| Opzione | Descrizione                        |
|---------|------------------------------------|
| r,R     | Sul lato destro del testo (right)  |
| l,L     | Sul lato sinistro del testo (left) |
| i,I     | Sul margine interno (inner)        |
| o,O     | Sul margine esterno (outer)        |

- **larghezza** specifica la larghezza dell’oggetto che, se nulla (0pt), equivale  all’opzione assegnata a \includegraphics .


## Citazioni/bibliografia
Usare il pacchetto `biblatex` e il tool `biber`
```latex
\usepackage{biblatex}                     % numerica semplice
% \usepackage[style=alphabetic]{biblatex}    % alfabetica
% \usepackage[style=authoryear]{biblatex}    % autore e anno

\addbibresource{file.bib}

\begin{document}

% comandi citazione
\cite{foo}           % citazione numerica
\parencite{bar}      % citations in parentheses (or square brackets)
\footcite{baz}       % citazione in a footnote

% trick per aggiungere prenote (eg see) e postnote (qualcosa aggiunta dopo la
% citazione e virgola)
\cite[see][page 12]{latexcompanion}


\printbibliography 
\end{document}
```

dopo la sequenza è 
```bash
pdflatex file
biber file
pdflatex file
pdflatex file
```


## beamer (slides)
Qui tutorial https://latex-beamer.com/tutorials/.
Intestazione minimale
```latex
\documentclass[10pt,handout,notes=hide]{beamer}
\usepackage[T1]{fontenc}
\usepackage[english, italian]{babel}
\usepackage[utf8]{inputenc}
\usepackage{mypkg}
\usepackage{hyperref}
\usepackage[style=authoryear]{biblatex}
\addbibresource{biblio.bib}
\usetheme{Copenhagen}
\setbeamercovered{transparent} 
% -----------------------------------------------------------------------
\title[Small official title]{Long official title}
\subtitle{Subtitle}
\author{Luca Braglia} 
\date{}
% -----------------------------------------------------------------------
\begin{document}
\setbeamertemplate{navigation symbols}{}%remove navigation symbols
\frame{ \titlepage }

% ========================================================================
<<include = FALSE>>=

library(knitr)
opts_chunk$set("engine" = "R", fig.align = "center", tidy = TRUE, echo=FALSE)

@

\end{document}
```
Sezione
```latex
% -----------------------------------------------------------------------
\part{Titolo Parte}
\frame{\partpage}
% -----------------------------------------------------------------------
```
Template di una slide
```latex
\begin{frame}[options]{Frame Title}{Frame subtitle}
  Contenuto
\end{frame}
```
Template minimale di slide
```latex
\begin{frame}[allowframebreaks]{Titolo}
  content
\end{frame}
```
Creare blocchi
```latex
\begin{block}{Intestazione}
  contenuto
\end{block}
```
Creare degli stop nella presentazioni
```latex
\pause
```
Inclusione immagini (meglio vedi sopra)
```latex
% \begin{center}
%   \includegraphics[scale = 0.35]{img/immagine}
% \end{center}
```
Per includere altri documenti knitr
```latex
\Sexpr{knitr::knit_child("common_include/slide_da_includere.Rnw")}
```
Per l'aggiunta di *note del relatore*:
```latex
\documentclass[10pt]{beamer}
\setbeameroption{show notes on second screen=right}
```
Per la visualizzazione di presentazione e note torna comodo `pympress`
```bash
pympress slides.pdf # apt install pympress
```
Stampa bibliografia alla fine
```latex
\begin{frame}[allowframebreaks]{Bibliografia}
  \printbibliography
\end{frame}
```
Aggiunta di struttura
```latex
% slide di TOC
\begin{frame}{Outline}
    \tableofcontents
\end{frame}
% e poi sezioni normalmente
\section{Problem statement}
\section{Existing results}
    \subsection{Method 1}
    \subsection{Method 2}
    \subsection{Method 3}
\section{Comparative study}
\section*{References}
```

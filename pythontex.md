Disponibile in Debian nel pacchetto `texlive-extra-utils`\
Utilizzo tipico a seguire
```bash
pdflatex file.tex  # qui pythontex estrae il codice py in un file temporaneo
pythontex file.tex  # qui esegue il codice e salva gli output
pdflatex file.tex  # qui si mette tutto assieme
```
<br>

## cheatsheet
**Environment**:
- A disposizione:
	- `pycode` esegue il codice presente ma non lo stampa a video. Stampa solo ciò che è stampato esplicitamente mediante print, che deve essere codice $\LaTeX$ valido. Tornano in questo caso comodo \
	 le stringhe raw di Python he permettono di non porre la doppia backslash per averne una;

	- `pyblock` esegue il codice e lo stampa a video. Il codice stampato con print non è automaticamente incluso ma si usano le macro `\printpythontex` dove si vuole che avvenga la stampa
	- `rcode`, `rblock`: cosa equivalente, per `R`, ma da abilitare mediante
		```latex
		\usepackage[usefamily=R]{pythontex}
		```
	- *Secondari* (non usare se non strettamente necessari):`pyverbatim` (`rverbatim`)per il codice prettyprintato ma non eseguito; `pyconsole` per la simulazione di console con prettyprintato il codice e anche l'output

- È meglio:
	- *lasciare sempre una linea bianca all’inizio e alla fine* di un environment, non stare a ridosso del begin end per esigenze di interprete.
	- *evitare di mischiare codice che deve essere eseguito sequenzialmente in environment* di tipo diverso: non è possibile definire in pyconsole e usare in pycode o viceversa. È invece possibile definire in pycode e usare in pyblock (e viceversa)

<br>

**Comandi**
- `\py` usato per eseguire codice (anche statement di print volendo) e stampare il risultato finale, convertendo in stringa se necessario. Serve tipicamente per richiamare dati/risultati. Se dentro py si usa chiama una funzione verrà convertito il valore di return (quindi se non restituisce verrà stampato None). Il quello che ritorna deve essere valido codice Latex,\
che verrà stampato paro paro;

- `\pyc` (con c per code) è usato eseguire ma non visualizzare (equivalente a pycode, se si vuole stampare usare print)
- `\R``\Rb`  equivalenti degli environment `rcode` ed `rblock` da abilitare sempre mediante `usefamily=R`
<br>

**Inclusione di tabelle**
- Usare la funzione `lb.io.latex_table` che stampa una tabella (un pd.DataFrame o un oggetto inheritante avente il metodo `to_latex`)

<br>

**Inclusione di immagini** :
- L'idea è creare/salvare l'immagine in un `pycode` (non visualizzato) e poi inserirla in latex normalmente mediante `\includegraphics` che potrà essere stampato con `print` (oppure incluso a mano sotto al codice python, in quello latex).
- `lb.io.fig_dump` velocizza l'esportazione su file e l'inclusione con `\includegraphics`.
	- In un environment di `pycode` (codice non stampato, per report) basta questo che salva la figura e stampa il codice latex per includerla
	```python 
	# matplot stuff
	fig, ax = plt.subplots()
	x = np.linspace(0, 10, 100)
	ax.plot(x, np.sin(x), label = 'sin(x)')
	ax.plot(x, np.cos(x), label = 'cos(x)')
	ax.legend()
	
	import pylbmisc as lb
	lb.io.fig_dump(fig, label = 'first_plot')
	```
	- in un environment `pyblock` (codice stampato, per didattica) aggiungere appena al termine del chunk python il seguente comando per l'inclusione effettiva della figura nel report pdf
	```latex
	\printpythontex
	```
<br>

- **Definizione di funzioni python per uso in LaTeX**: alcune idee
	- per una funzione che stampa (es utile per formattazione dove si vuole controllo) la usiamo entro `pyc`: 
	```python
	def tabellina(n):
	    print(r"\begin{table} \centering \begin{tabular}{cc} \hline")
	    for i in range(1, 10 + 1):
	    print(i, "&", n*i, r"\\")
	    print(r"\hline \end{tabular}")
	    print(r"\caption{Tabellina del %d.}" % n)
	    print(r"\label{tab:tabellina_del_%d}" % n)
	    print(r"\end{table}")
	```
	e la chiamiamo con `\pyc{tabellina(7)}`

	- se in `pycode` o `pyblock` definiamo
	```python 
	def pow(x, y):
	    return x ** y
	```
	e in seguito in LATEX definiamo il suo utilizzo entro `\py`

	```latex 
	\newcommand{\pow}[2]{\py{pow(#1, #2)}}
	```
	poi, sempre in latex si potrà usare `\pow{2}{3}`

	<br>

	<br>

<br>


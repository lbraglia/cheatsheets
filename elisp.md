# elisp

## Resources

- https://www.gnu.org/software/emacs/manual/html_mono/elisp.html
- https://github.com/chrisdone-archive/elisp-guide/blob/master/README.md


## Testing
In un buffer `.el`

|-----------------------------|---------------------------------|
| `C-x C-e  (eval-last-sexp)` | valuta l'espressione precedente |
| `M-x eval-buffer`           | esegue l'intero buffer          |
| `M-x eval-region`           | esegue la zona evidenziata      |
|-----------------------------|---------------------------------|


## Sintassi

La sintassi è composta di liste (tra parentesi) simboli/variabili e valori

```elisp

;; Questa è una lista che effettua una somma 1+1 
(+ 1 1)

;; definizione di funzione è una lista
(defun greet (name)
  (message "Hello %s!" name))

;; chiamata di funzione idem
(greet "Luca")

;; definizione di variabile è una lista
(defvar var-name valore
  "Documentazione variabile.")
```
La notazione è prefissa: funzioni è operatori sono posti come primo elemento
della lista.


## Tipi di dati
È tipo il python: i valori hanno un tipo (non le variabili che possono essere
di qualsiasi tipo e variare in corso d'opera)

I tipi provengono dal lisp (Strings, Numbers, Symbols, Cons cells, Arrays and
Vectors ...) e da emacs (Buffers, Windows, Frames, Threads,Keymaps)

I Simboli/variabili sono contenitori. Si puà creare un proprio namespace
mediante /: ad esempio `lb/mia-variabile`.

```elisp
42    ;;costante
"Hi"  ;;costante

'(1 2 3);; simple list
(list 1 2 3) ;; another way to create list
[1, 2, 3] ;; a vector
```

Per valutare il tipo di qualcosa usare `type-of`
```elisp
(type-of 42)
(type-of "hello")
```

## Valutazione
Le regole di valutazione cambiano a seconda di cosa si sta valutando: alcune
cose sono self-evaluating (ritornano il loro valore) come costanti. 

Quando simboli/variabili vengon valutati restituiscono il valore associato

Vi sono due namespace: uno per variabili uno per funzioni (lisp2) (questo rende
possibile avere una funzione e una variabile con lo stesso nome)

La valutazione avviene nel global environment per cui può essere utile
utilizzare namespace per evitare clash

``` elisp
(setq lb/mio-nickname "lucailgarb")
(greet lb/mio-nickname)
(setq lb/mio-nickname "paglia")
```


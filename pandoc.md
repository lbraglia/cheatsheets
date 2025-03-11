# pandoc

## da markdown (Rmd) a LaTex
```
pandoc input.Rmd -f gfm -t latex -o output.tex
```

## conversione da LaTeX a markdown per Github
```
pandoc input.tex -f latex -t gfm -o output.md
```

## lista formati input disponibili
```
pandoc --list-input-formats
```

## list formati output
```
pandoc --list-output-formats
```

# emacs

### Help

| Keystrokes | Action                                                    |
|------------|-----------------------------------------------------------|
| `C-h C-h`  | Help for help system                                      |
| `C-h k`    | Describe command from keystrokes                          |
| `C-h f`    | Describe command from function name                       |
| `C-h m`    | List keybinding for current modes                         |
| `C-h v`    | Describe variable                                         |
| `C-h b`    | Describe bindings for current buffer (in ordered fashion) |
| `C-h ?`    | help suggestions                                          |
| `C-x 1`    | to close `*Help*` buffer                                  |

### Files/Buffers

| Keystrokes | Action                                     |
|------------|--------------------------------------------|
| `C-x C-f`  | Create buffer/Open file                    |
| `C-x C-s`  | Save current buffer to file                |
| `C-x s`    | Save all buffers connected to a file       |
| `C-x C-w`  | Save to file named as                      |
| `C-x i`    | Insert                                     |
| `C-x C-b`  | list available buffers                     |
| `C-x b`    | move to a given buffer or create a new one |
| `C-x ->`   | move to next buffer in the list            |
| `C-x <-`   | move to previous buffer in the) list       |
| `C-x k`    | kill a buffer (remove from the list)       |
| `C-x C-q`  | set/unset a buffer as read-only            |

### Managing windows

| Keystrokes | Action                                                 |
|------------|--------------------------------------------------------|
| `C-x 2`    | split windows horizontally                             |
| `C-x 3`    | split windows vertically                               |
| `C-x o`    | go to another other window                             |
| `C-x 0`    | close the current window                               |
| `C-x 1`    | close all but the current window                       |
| `C-x ^`    | expand vertically (one line, eg use `C-u` before)      |
| `C-x {`    | expand horizontally (one line, eg use `C-u` before)    |
| `C-x -`    | shrink windows if larger than buffer (thus not needed) |
| `C-x +`    | back to windows of equal size (vertically)             |

### Moving

| Keystrokes | Action                                                       |
|------------|--------------------------------------------------------------|
| `C-p `     | previous line                                                |
| `C-n `     | next line                                                    |
| `C-a `     | line beginning                                               |
| `C-e `     | end of line                                                  |
| `C-f `     | forward a character                                          |
| `C-b `     | backward a character                                         |
| `M-f `     | forward a word                                               |
| `M-b `     | backward a word                                              |
| `M-a `     | beginning of sentence                                        |
| `M-e `     | end of sentence                                              |
| `M-{ `     | beginning of paragraph (text delimited by white space)       |
| `M-} `     | end of paragraph (text delimited by white space)             |
| `C-q C-l`  | insert a page break                                          |
| `C-x [`    | previous page                                                |
| `C-x ]`    | next page                                                    |
| `C-v`      | next screen                                                  |
| `M-v`      | previous screen                                              |
| `M-< `     | beginning of buffer                                          |
| `M-> `     | end of buffer                                                |
| `M-g M-g`  | go to line                                                   |
| `C-l`      | (repeated) center display as desired                         |
| `C-M-l`    | porre la cosa corrente (es funzione) nello schermo al meglio |


### Select/mark region

| Keystrokes         | Action                                                     |
|--------------------|------------------------------------------------------------|
| `C-space`          | start selecting by line (modo + generale) poi muoversi     |
| `C-x space`        | start selecting by column (modo + generale) poi muoversi   |
| `S-M-f`            | (Shift + movimento) evidenzia muovendosi (avanti parola)   |
| `S-M-b`            | (Shift + movimento) evidenzia muovendosi (indietro parola) |
| `S-C-n`            | (Shift + movimento) evidenzia muovendosi (avanti riga)     |
| `S-C-n`            | (Shift + movimento) evidenzia muovendosi (indietro riga)   |
| `M-@`              | seleziona prossima parola (a ripetizione) senza muoversi   |
| `C-M-@`            | idem non ho capito diff                                    |
| `M-h`              | mark the whole paragraph                                   |
| `C-M-h`            | mark the whole defun (elisp)                               |
| `C-x C-p`          | mark the current page                                      |
| `C-x h`            | mark the whole buffer                                      |
| `C-x C-x`          | move to other end of marked region                         |
| `M-x -region[TAB]` | to see all the commands usable for regions                 |


### Bookmarks

| Keystrokes            | Action                  |
|-----------------------|-------------------------|
| `C-x r l`             | display bookmarks list  |
| `C-x r m`             | set a bookmark          |
| `C-x r b`             | jump to a bookmark      |
| `M-x bookmark-delete` | delete a saved bookmark |
| `M-x bookmark-rename` | rename a saved bookmark |


### Editing

| Keystrokes | Action                                                              |
|------------|---------------------------------------------------------------------|
| `C-d`      | Delete one char forward                                             |
| `M-d`      | Cut one word forward                                                |
| `M-DEL`    | Cut one word backward                                               |
| `C-k `     | Cut to the end of line                                              |
| `C-w `     | Cut selected region                                                 |
| `M-w`      | Copy selected region                                                |
| `C-y`      | Paste last cut things                                               |
| `M-y`      | after a `C-y` goes through the ring of kill to choose what to paste |
| `C-x u`    | Undo                                                                |

### Search

| Keystrokes                 | Action                                     |
|----------------------------|--------------------------------------------|
| `C-s`                      | Incremental search forward, type           |
| `C-r`                      | Incremental search backward, type          |
| `C-s C-w`                  | Incremental search forward, following word |
| `M-x word-search-forward`  | Exact search forward                       |
| `M-x word-search-backward` | Exact search backward                      |
| `C-M-s`                    | incremental regexp search forward          |
| `C-M-r`                    | incremental reg-ex search backward         |
| `C-g`                      | Interrupt search, go where search began    |

### Replace

| Keystrokes           | Action                          |
|----------------------|---------------------------------|
| `M-x replace-string` | Replace string without querying |
| `M-x query-replace`  | Replace string querying         |
| `M-%`                | Query replace                   |
| `C-M-%`              | Regexp query replace            |

### Abbreviations

| Keystrokes            | Action                                                 |
|-----------------------|--------------------------------------------------------|
| `C-x aig`             | add a global abbreviation (with last word as abbrev)   |
| `C-x ail`             | add abbreviation for a mode (with last word as abbrev) |
| `M-x unexpand-abbrev` | undo last word abbreviation                            |

### Wrapping/Indenting/commenting text

| Keystrokes        | Action                               |
|-------------------|--------------------------------------|
| `M-q `            | wrap paragraph                       |
| `M-x fill-region` | wrap paragraphs from selected region |
| `C-M-\`           | indent lines from selected region    |
| `M-;`             | comment line or selected region      |


### Repeating a command

| Keystrokes                   | Action                           |
|------------------------------|----------------------------------|
| `M-n CMD_KEYSTROKES`         | repeat n times `CMD_KEYSTROKES`  |
| `C-u CMD_KEYSTROKES`         | repeat 4 times `CMD_KEYSTROKES`  |
| `C-u C-u CMD_KEYSTROKES`     | repeat 16 times `CMD_KEYSTROKES` |
| `C-u C-u C-u CMD_KEYSTROKES` | repeat 64 times `CMD_KEYSTROKES` |
| ...                          | ...                              |

### Spell checking

| Keystrokes                     | Action                               |
|--------------------------------|--------------------------------------|
| `M-x ispell-change-dictionary` | set spelling dictionary              |
| `M-$`                          | ispell check a single word           |
| `M-x ispell-region`            | check selected region                |
| `M-x ispell-buffer`            | check current buffer                 |
| `M-x flyspell-mode`            | use flyspell for spelling on the fly |
| `C-g`                          | Stop spell checking                  |


## Interesting modes

### Useful modes/commands

| Keystrokes     | Action                 |
|----------------|------------------------|
| `M-x cd`       | change local directory |
| `M-x mkdir`    | create directory       |
| `M-x man`      | manpages mode          |
| `M-x shell`    | shell                  |
| `M-x calendar` | view calendar          |

### Shell commands

| Keystrokes | Action                                                 |
|------------|--------------------------------------------------------|
| `M-!`      | execute shell command                                  |
| `C-u M-!`  | execute shell command and put output in current buffer |
| `M-\|`     | execute shell command on marked region                 |

### Directory editor mode (Dired)

| Keystrokes  | Action                                                 |
|-------------|--------------------------------------------------------|
| `C-x d`     | attiva Dired mode                                      |
| `^`         | parent directory                                       |
| `>`         | prossima directory                                     |
| `<`         | directory precedente                                   |
| `+`         | crea directory                                         |
| `T`         | crea file (touch)                                      |
| `C`         | copia file                                             |
| `R`         | rinomina/muovi                                         |
| `S`         | fai soft link                                          |
| `W`         | open file with external application                    |
| `Z`         | compress/uncompress (gzip)                             |
| `Enter`     | edit selected file/enter directory                     |
| `v`         | view (read only) selected file                         |
| `D`         | marka per eliminazione                                 |
| `x`         | delete marked files                                    |
| `u`         | unmarka un file                                        |
| `U`         | unmarka tutti i marked files                           |
| `g`         | aggiorna listato                                       |
| `s`         | sort                                                   |
| `m`         | mark a file (poi usare `D` per eliminarlo)             |
| `%m`        | mark files via regexp on the name                      |
| `%g`        | mark files via regexp on the content (similar to grep) |
| `! command` | run command on a file                                  |
| `q`         | quit                                                   |


### Shell mode

| Keystrokes   | Action                       |
|--------------|------------------------------|
| `M-x shell`  | shell mode                   |
| `C-c C-z`    | equal to `C-z` in pure shell |
| `C-c C-d`    | as above with `C-d`          |
| `C-c C-c`    | as above with `C-c`          |
| `M-p`        | history, previous command    |
| `M-n`        | history, next command        |


### Python mode

| Keystrokes     | Action                                             |
|----------------|----------------------------------------------------|
| `C-c C-p`      | start interpreter from python code                 |
| `C-c C-z`      | muoviti nella shell python                         |
| `C-h a python` | vedi qualsiasi comando associato a python          |
| `C-c <`        | indenta a sinistra                                 |
| `C-c >`        | indenta a destra                                   |
| `M Tab`        | autocomplete                                       |
| `C-c C-d`      | describe at point (roba builtin)                   |
| `C-c C-f`      | documentazione ad un punto                         |
| `C-c C-l`      | evaluate a file (source) nel sottoprocesso         |
| `C-c C-c`      | evaluate a buffer                                  |
| `C-c C-r`      | evaluate a selected region                         |
| `C-c C-e`      | evaluate a statement                               |
| `C-c C-s`      | evaluate a command                                 |
| `C-c C-j`      | spostati il cursore in definizioni varie (imenu)   |
| `C-c C-v`      | check code                                         |
| `M-x compile`  | specificando `mypy file.py` controlla il typecheck |


### Projectile

| Keystrokes  | Action                           |
|-------------|----------------------------------|
| `C-c p p`   | switch project                   |
| `C-c p f`   | seach file                       |
| `C-c p s g` | greppa nel progetto teoricamente |

### Magit

| Keystrokes  | Action                           |
|-------------|----------------------------------|
| `C-x g`     | status                           |

### org-mode

| Keystrokes  | Action                                              |
|-------------|-----------------------------------------------------|
| `TAB`       | collassa                                            |
| `M + enter` | new section/ aggiungi elemento elenco puntato/lista |
| `M + su`    | sposta su una sezione                               |
| `C-c C-l`   | inserire link                                       |
| `C-c C-o`   | aprire link                                         |
|             |                                                     |


### Compile

Start with something like `emacs *.[ch] Makefile`; do the makefile. Then

| Keystrokes     | Action                            |
|----------------|-----------------------------------|
| `M-x compile`  | compile (`make -k` by default)    |
| `C-x backtick` | buffer set to next compile error  |
| `M-n`          | next error                        |
| `M-p`          | previous error                    |
| `C-c C-c`      | go to current error with a buffer |
| `space`        | scroll down                       |
| `del`          | scroll up                         |

### etags

| Keystrokes             | Action                                                              |
|------------------------|---------------------------------------------------------------------|
| `etags *.[ch]`         | from command line, builds/update tag table (`TAGS` file by default) |
| `M-x visit-tags-table` | tell emacs to use a tag table                                       |
| `M-.`                  | find tag/visit definition in this window                            |
| `C-x 4 .`              | find tag/visit in other window                                      |



###

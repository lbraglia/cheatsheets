# R - Python


## 01 Numpy

| Topic                 | R   | Python                              | Note                                  |
|-----------------------|-----|-------------------------------------|---------------------------------------|
| **Vectorized/ufuncs** |     | `f = np.frompyfunc(f_worker, 1, 1)` | ufunc da funzione 1->1 (es un mapper) |
|                       |     | `f = np.frompyfunc(f_worker, 2, 1)` | ufunc da funzione 2->1 (es operatore) |

## 02 Pandas

| Topic                  | R                   | Python                              | Note                                    |
|------------------------|---------------------|-------------------------------------|-----------------------------------------|
| **Testing/coercion**   | `is.integer(x)`     | ` pd.api.types.is_integer_dtype(x)` |                                         |
|                        | `a = as.integer(x)` | ` a = x.astype(int)`                |                                         |
|                        |                     |                                     |                                         |
| **Missingness**        | `is.na(x)`          | ` x.isna()`                         |                                         |
|                        | `!is.na(x)`         | ` x.notna()`                        |                                         |
|                        | `x[!is.na(x)]`      | ` x.dropna()`                       |                                         |
|                        | `x[is.na(x)]<- -9`  | ` x.fillna(9)`                      |                                         |
|                        |                     |                                     |                                         |
| **Duplicated/unique**  | `duplicated(x)`     | ` x.duplicated()`                   |                                         |
|                        | `unique(x)`         | ` x.unique() # np.dnarray`          |                                         |
|                        | `unique(x)`         | ` x.drop_duplicates() # pd.Series`  |                                         |
|                        |                     |                                     |                                         |
| **Applying functions** | `exp(x) + 1`        | ` np.exp(x) + 1 # np ufuncs`        |                                         |
|                        | `f(x)`              | `f(x)`                              | applicazione f vettorizzata/ufunc       |
|                        |                     | `x.map(f)`                          | applicazione f per singolo elemento     |
|                        |                     | `x.map(d)`                          | applicazione dict per recoding completo |
|                        |                     | `x.replace(d)`                      | applicazione dict per recoding parziale |


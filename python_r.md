# R - Python


## 01 Numpy

| R   | Python                              | Note                                  |
|-----|-------------------------------------|---------------------------------------|
| `.` | `f = np.frompyfunc(f_worker, 1, 1)` | ufunc da funzione 1->1 (es un mapper) |
| `.` | `f = np.frompyfunc(f_worker, 2, 1)` | ufunc da funzione 2->1 (es operatore) |

## 02 Pandas

| R                   | Python                              | Note                                    |
|---------------------|-------------------------------------|-----------------------------------------|
| `is.integer(x)`     | ` pd.api.types.is_integer_dtype(x)` | nan                                     |
| `a = as.integer(x)` | ` a = x.astype(int)`                | nan                                     |
| `is.na(x)`          | ` x.isna()`                         | nan                                     |
| `!is.na(x)`         | ` x.notna()`                        | nan                                     |
| `x[!is.na(x)]`      | ` x.dropna()`                       | nan                                     |
| `x[is.na(x)]<- -9`  | ` x.fillna(9)`                      | nan                                     |
| `duplicated(x)`     | ` x.duplicated()`                   | nan                                     |
| `unique(x)`         | ` x.unique() # np.dnarray`          | nan                                     |
| `unique(x)`         | ` x.drop_duplicates() # pd.Series`  | nan                                     |
| `exp(x) + 1`        | ` np.exp(x) + 1 # np ufuncs`        | nan                                     |
| `f(x)`              | `f(x)`                              | applicazione f vettorizzata/ufunc       |
| `nan`               | `x.map(f)`                          | applicazione f per singolo elemento     |
| `nan`               | `x.map(d)`                          | applicazione dict per recoding completo |
| `nan`               | `x.replace(d)`                      | applicazione dict per recoding parziale |


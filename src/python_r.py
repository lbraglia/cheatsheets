import pandas as pd
from pathlib import Path
import pylbmisc as lb

tab_dir = Path("python_r_data")
dfs = lb.io.data_import(list(sorted(tab_dir.iterdir())), csv_kwargs = {"sep":"\t"})


def make_code(x):
    x = str(x)
    if x!= "":
        rval = "`" + x + "`"
    else:
        rval = x
    return rval

def make_bold(x):
    x = str(x)
    if x!= "":
        rval = "**" + x + "**"
    else:
        rval = x
    return rval

md = ["# R - Python", "\n\n\n"]
for nm, df in dfs.items():
    title = nm.replace("_", " ").title()
    md.append("## {}\n\n".format(title))
    # replace NA with "" and markup for columns
    df = df.fillna("")
    df["Topic"] = df["Topic"].map(make_bold)
    df["R"] = df["R"].map(make_code)
    df["Python"] = df["Python"].map(make_code)
    md.append(df.to_markdown(index=False, tablefmt="github"))
    md.append("\n\n")

    
outfile = Path("../python_r.md")
with outfile.resolve().open(mode="w") as f:
    f.writelines(md)

# TODO: syntax hightlight
# https://gist.github.com/MarcoEidinger/c0f0583f19baca0a8f33bcded644be41

# Master GitHub markdown tables with code blocks
# - Use HTML tags to define the table to get the best layout result
# - Use either backticks (```) or the HTML pre element with attribute lang
# - Keep a blank line before and after a code block for correct
#   formatting and syntax highlighting


## Example: nice looking table to show HTTP Responses

# <table>
# <tr>
# <td> Status </td> <td> Response </td>
# </tr>
# <tr>
# <td> 200 </td>
# <td>
    
# ```json
# {
#   "id": 10,
#   "username": "marcoeidinger",
#   "created_at": "2021-02-097T20:45:26.433Z",
#   "updated_at": "2015-02-10T19:27:16.540Z"
# }
# ```

# </td>
# </tr>
# <tr>
# <td> 400 </td>
# <td>
    
# **Error**, what the hell is going on?!?
    
# </td>
# </tr>
# <tr>
# <td> 500 </td>
# <td>
# Internal Server Error    
# </td>
# </tr>
# </table>


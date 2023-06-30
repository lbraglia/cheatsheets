import pandas as pd
from pathlib import Path
import pylbmisc as lb

infile = Path("python_r_data.xlsx")
dfs = lb.io.data_import(infile)

def add_code_markup(x, lang = ''):
    return "```" + x.astype(str) + "```"

md = ["# R - Python", "\n\n\n"]
for nm, df in dfs.items():
    title = nm.replace("python_r_", "").replace("_", " ").title()
    md.append("## {}\n\n".format(title))
    # add code for content to R and Python
    df["R"] = add_code_markup(df["R"])
    df["Python"] = add_code_markup(df["Python"])
    md.append(df.to_markdown(index=False, tablefmt="github"))
    md.append("\n\n")

    
outfile = Path("../python_r.md")
with outfile.resolve().open(mode="w") as f:
    f.writelines(md)

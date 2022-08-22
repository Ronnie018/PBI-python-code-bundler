import re

newPath = "newPath"

def formatLine(line):
  if "read_excel" in line:
    return line.replace('excel.xlsx', newPath)
  return line.replace("df.", "")

with open("./bundle.py", "w", encoding="utf-8") as bundle:
  
  file1 = open("./assets/dataFuncs.py", "r", encoding="utf-8")
  file2 = open("./index.py", "r", encoding="utf-8")
  
  bundleText = ""
  
  for line in file1.readlines():
    if len(line) < 3 and not(")" in line or "]" in line or "}" in line):
      continue
    
    if (
      "if" in line
      or "elif" in line
      or "else" in line
    ):
      bundleText += "\n"
    
    if "def " in line:
      bundleText += "\n"
    bundleText += line
    if (")" in line or "]" in line or "}" in line) and len(line) < 5:
      bundleText += "\n"

  for line in file2.readlines():
    importVr = re.compile(r"import")
    
    line = formatLine(line)
    
    if "import" in line:
      continue
    elif "table.to_excel" in line:
      continue
    elif len(line) < 3 and not(")" in line or "]" in line or "}" in line):
      continue
    if (
      "if" in line
      or "elif" in line
      or "else" in line
    ):
      bundleText += "\n"
    if "def " in line:
      bundleText += "\n"
    bundleText += line
    if (
         ")" in line
      or "]" in line
      or "}" in line
    ) and len(line) < 5:
      bundleText += "\n"
  
  bundle.writelines(bundleText)
  
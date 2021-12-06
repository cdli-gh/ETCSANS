import os,sys,re,traceback

def help():
    sys.stderr.write("""synopsis: conll2tei.py [-h|-?|-help] [-] [FILE1..n]
    -h    print this message
    -     read CDLI-CoNLL from stdin
    FILEi read CDLI-CoNLL from file
Read CDLI-CoNLL files from stdin or args, write one TEI/XML file to stdout.
If no arguments or - are provided, read from stdin.\n""")
    sys.stderr.flush()

files=sys.argv[1:]
if len(files)==0:
    files=["-h","-"]


header="""<?xml version="1.0"?>
<TEI>
  <teiHeader>
    <revisionDesc>
      <change who="conll2tei.py" when="">Converted from CDLI-CoNLL</change>
    </revisionDesc>
  </teiHeader>
  <teiCorpus>"""

footer="""  </teiCorpus>
</TEI>
"""

output=False

for file in files:
    input=None
    if os.path.exists(file):
        sys.stderr.write("reading from \""+file+"\"\n")
        input=open(file,"rt", errors="ignore")
    elif re.match(r"^[\-]+$",file):
        sys.stderr.write("reading from stdin\n")
        input=sys.stdin
    elif re.match(r"^[\-]+(?|h|help)$",file):
        help()
    else:
        sys.stderr.write("could not open file \""+file+"\"\n")
        sys.exit(1)
    sys.stderr.flush()

    if not output:
        print(header)
        output=True

    print(f"""    <TEI>
      <teiHeader>
        <notesStmt>
          <note n=orgfile>{file}</note>
        </notesStmt>
      <teiHeader>
      <text>""")
    s=0
    tok=0
    for line in input:
        line=line.strip()
        if not line.startswith("#"):
            if line=="" and tok!=0:
                print("        </s>")
                tok=0
                s+=1
            if "\t" in line:
                fields=line.split("\t")
                if len(fields)>=7:
                    if tok==0:
                        s+=1
                        tok=fields[0]
                        print(f"""        <s id="s-{s}">""")
                    row={
                        "id": "w-"+fields[0],
                        "lemma": fields[2],
                        "xpos": fields[4],
                        "head": "w-"+fields[5],
                        "deprel": fields[6]
                    }
                    print("          <tok "+" ".join([key+"=\""+val+"\"" for key,val in row.items()])+">"+fields[1]+"</tok>")
    if tok!=0:
        print("        </s>")

    print("""      </text>
    </TEI>""")

    if os.path.exists(file):
        input.close()

if output:
    print(footer)

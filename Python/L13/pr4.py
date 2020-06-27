import requests
paper_url="http://www.mum.digitaluniversity.ac/WebFiles/1S01331.pdf"
res=requests.get(paper_url)
print(res)
with open("paper.pdf","wb") as f:
    f.write(res.content)
    print("pdf downloaded")
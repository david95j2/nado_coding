site = "https://naver.com"
site = site.replace("https://","")
site = site[:site.index(".")]
site = site[:3]+str(len(site))+str(site.count("e")) + "!"
print(site)

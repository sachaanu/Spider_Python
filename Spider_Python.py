from pandas import *
import re
import urllib.request                                        ################importing libraries

def utkarsh_sachaan_Spider(mainURL,depth):                   #########defining main function
    v=0
    new_list=[]
    links_final=[]
    links=[]
    temp=[]
    depth=int(depth)
    try:
        
        with urllib.request.urlopen(mainURL) as url:          ###reading every line on the website and storing as string
            theSite=str(url.read())
            
    except Exeption:
        pass
    
    links=re.findall('''<a href="(.+?)"''',theSite,re.DOTALL) #creating main list links which has all links on first page or url
   
    while v<depth:                                            ###############introducing depth
        for j in links:                                       ###############iterating each element from the main list
            
            try:
                with urllib.request.urlopen(j) as url2:       ###############for each element in links opening and reading
                    tempSite=str(url2.read())
                    
            except Exception:                                 ###############introducing exeption to remove invalid links
                pass
            
        
            links_temp = re.findall('''<a href="(.+?)"''',tempSite,re.DOTALL)
            for element in links_temp:
                if element not in new_list:                  ################removing duplicates from links_temp
                    new_list.append(element)
            
        
        for g in new_list:                                   ################ensuring only unique elements gets added to the final list
            if g not in links:
                links.append(g)

    
    
    
        v=v+1
        
    for h in links:
            if h not in links_final:                       ##############appending final list
                links_final.append(h)
    print(len(links_final))
    return(links_final)



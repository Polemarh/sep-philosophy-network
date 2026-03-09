import parse_article 
import parse_content

table = parse_content.parse_content()
print(table[0:-15])

# for i in table[0:15]:
#     text = parse_article.parse_article(i["url"])
#     print(text) 
    
    
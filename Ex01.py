import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
pag = requests.get(URL)

# print(pag.text)

soup=BeautifulSoup(pag.content,"html.parser") #.content para melhor "tradução" do conteúdo de html e html.parser é o analisador de html
resultado=soup.find(id="ResultsContainer") #Procurar a parte que tem todos os anúncios de emprego

#print(resultado.prettify())

elementos_trabalho=resultado.find_all("div",class_="card-content") #Retornar todo o HTML para todas as listas de empregos exibidas naquela página

#Filtro por emprego/titulo:
trabalhos_title=resultado.find_all("h2", string=lambda text: "python" in text.lower()) #Verficar todos os que estiverem com h2 e procurar a palavra-chave python e converter em minusculo (Filtrador)
trabalhos_title_elementos=[h2_elemento.parent.parent.parent for h2_elemento in trabalhos_title] #Agora ele está passando por cima dos <div class="card-content"> em vez de apenas os <h2> elementos do título

#Filtro por company:
company_trabalhos=resultado.find_all("h3", string=lambda text: "davis" in text.lower())
company_trabalhos_elementos=[h3_elemento.parent.parent.parent for h3_elemento in company_trabalhos]

#Filto por localização:
location_trabalhos=resultado.find_all("p", string=lambda text: text and "williamsburgh" in text.lower())
location_trabalhos_elementos=[p_elemento.parent.parent for p_elemento in location_trabalhos]


for elementos_trabalho in trabalhos_title_elementos:
    titulo_trabalho = elementos_trabalho.find("h2", class_="title")
    compania_trabalho = elementos_trabalho.find("h3", class_="company")
    local_trabalho = elementos_trabalho.find("p", class_="location")
    link_url = elementos_trabalho.find_all("a") [1] ["href"]  # Colocando a posição para poder pegar apenas o segundo link desejado

    print(titulo_trabalho.text.strip())
    print(compania_trabalho.text.strip())
    print(local_trabalho.text.strip())
    print('Inscrição: {}'.format(link_url))
    print()

    #links=elementos_trabalho.find_all("a")
    #for link in links:
    #print(link.text.strip()) Ele pegava apenas as palavras "Learn" e "Apply" inves dos links dele, pelo fato de ser text
    #print(elementos_trabalho,end="\n"*2)
    #print(len(trabalhos_pyhton)) Quantidade de postagens que ele achou com a palvra-chave
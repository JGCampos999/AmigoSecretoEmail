from random import randint
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def tentaSorteio(boo1):
    for i in range(len(lNomes)):
        if (lNomes[i] in lNomes2):
            lNomes2.remove(lNomes[i])
            boo = True
        else:
            boo = False
        if (len(lNomes2) == i+1):
            l = 0
        else:
            l = randint(0, (len(lNomes2)-1))
        fT.append(lNomes2[l])
        lNomes2.remove(lNomes2[l])
        if boo:
            lNomes2.append(lNomes[i])
    boo1 = True
    return boo1

nomes = 'Teste 1, Teste2'
emails = 'Email 1, Email 2'
lNomes = nomes.split(', ')
lNomes2 = nomes.split(', ')
lEmail = emails.split(', ')
fT = []
boo1 = False

while (not boo1):
    try:
        boo1 = tentaSorteio(boo1)
    except:
        fT = []
        lNomes2 = nomes.split(', ')
        
for i in range (len(lNomes)):
    message = Mail(
        from_email='amigoSecreto@gmail.com',
        to_emails=str(lEmail[i]),
        subject='Amigo Secreto',
        html_content=lNomes[i]+' você tirou: <strong>'+fT[i]+'</strong>')
    sg = SendGridAPIClient('API SENDGRID')
    response = sg.send(message)
print('Sorteio realizado com sucesso')

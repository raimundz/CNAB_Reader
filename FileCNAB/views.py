from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from FileCNAB.models import FileCNAB
from django.forms.models import model_to_dict


def upload(request):
  if request.method == 'GET':

        return render(request,'upload.html')
  uploaded_file = request.FILES['document']
  if request.method == 'POST':
    fs= FileSystemStorage()
    fs.save(uploaded_file.name, uploaded_file)
  
  with open(f'media/{uploaded_file.name}', 'r')as file:
      
      for value in file:
        data = {}
        if(value[0]=='1'):
          data['tipo'] = 'Debito'
          data['natureza'] = 'Entrada'
        elif(value[0]=='2'):
          data['tipo'] = 'Boleto'
          data['natureza'] = 'Saida'
        elif(value[0]=='3'):
          data['tipo'] = 'Financiamento'
          data['natureza'] = 'Saida' 
        elif(value[0]=='4'):
          data['tipo'] = 'Credito'
          data['natureza'] = 'Entrada' 
        elif(value[0]=='5'):
          data['tipo'] = 'Recebimento Emprestimo'
          data['natureza'] = 'Entrada'
        elif(value[0]=='6'):
          data['tipo'] = 'Vendas'
          data['natureza'] = 'Entrada'
        elif(value[0]=='7'):
          data['tipo'] = 'Recebimento TED'
          data['natureza'] = 'Entrada'
        elif(value[0]=='8'):
          data['tipo'] = 'Recebimento DOC'
          data['natureza'] = 'Entrada'
        elif(value[0]=='9'):
          data['tipo'] = 'Aluguel'
          data['natureza'] = 'Saida'
        
        data['data'] = value[1:9]
        data['valor'] = value[9:19]
        data['CPF'] = value[19:30]
        data['cartao'] = value[30:42]
        data['hora'] = value[42:48]
        data['dono'] = value[48:62]
        data['loja'] = value[62:81]
        
        operation = FileCNAB.objects.create(**data)

  return render(request,'upload.html')

  

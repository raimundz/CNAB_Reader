from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload(request):
  uploaded_file = request.FILES['document']
  if request.method == 'POST':
    fs= FileSystemStorage()
    fs.save(uploaded_file.name, uploaded_file)

  with open(f'media/{uploaded_file.name}', 'r')as file:

      for value in file:
        print(value[1])

  return render(request,'upload.html')

  #REVISAR SOBRE METODOS DE STRING PARA SETAR TODOS OS ATRIBUTOS DO MEU OBJETO E FAZER MINHA REQUISIÇÃO

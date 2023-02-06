from django.shortcuts import render

def upload(request):
  if request.method == 'POST':
    uploaded_file = request.FILES['document']
    print(uploaded_file)
  return render(request,'upload.html')

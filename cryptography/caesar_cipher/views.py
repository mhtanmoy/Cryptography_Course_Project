from django.shortcuts import render
from .models import ccDB

# Create your views here.

def home(request):
    msg = ""
    if request.POST:
        
        plain = request.POST.get("plain")
        key = request.POST.get("key")
        key = int(key)
        result = ""
   
        for i in range(len(plain)):
            Iplain = plain[i]
            
            
            if (Iplain.isupper()):
                result = chr((ord(Iplain) + key-65) % 26 + 65) + result
            
            else:
                result = chr((ord(Iplain) + key - 97) % 26 + 97) + result
        print(result)
        ccdb = ccDB.objects.create(
            cipher = result,
            key=key
        )
        return render(request,'caesar_cipher/home.html', {'plain':plain,'key':key})
        
    else:
        plain = " "
        key = " "       
        return render(request,'caesar_cipher/home.html', {'plain':plain,'key':key})

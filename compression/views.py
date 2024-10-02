from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import inputFileForm
import os
from django.http import HttpResponse
from.models import fileInput
from django.http import FileResponse
import mimetypes
from .Algorithms import compression

def homePage(request):
    form = inputFileForm()
    # Using Post allows processing data 
    if request.method == "POST":
        # Gathers data user inputted 
        form = inputFileForm(request.POST, request.FILES)
        # Checks wether the data is ok 
        if form.is_valid():
            # saves the form in this case saves the file 
            newFile = form.save()
            # retrives the last section of the address eg text.txt
            filename = os.path.basename(newFile.file.name)
            #checks That the file is a .txt file 
            if filename[-4:].lower() != ".txt":
                #deletes file
                os.remove('compression/Algorithms/'+filename)
            else:
                # redirects to new page 
                return HttpResponseRedirect("sucess/"+filename)
        else:
            form = inputFileForm()
    # retruns back to same page 
    return render(request, "homepage.html",{"form": form})

# fucntion that retreives the sizes of compressed files 
def getSizes(filename):
    # start of path to where files are stored 
    folder_path = 'compression/Algorithms/'  # Replace with the actual path to your folder

    # gathers the sizes 
    OriginalSize = os.path.getsize(os.path.join(folder_path, filename))
    rleFileSize = os.path.getsize(os.path.join(folder_path,"CompressedRLE.dat"))
    lyndonFileSize =os.path.getsize(os.path.join(folder_path,"CompressedLyndonFactorisation.dat"))
    burrowsFileSize = os.path.getsize(os.path.join(folder_path,"CompressedBurrows.dat"))
    finalCompressedFileSize = os.path.getsize(os.path.join(folder_path,"CompressedFile.dat"))
    # adds sizes to list
    sizes = [OriginalSize,rleFileSize,lyndonFileSize,burrowsFileSize,finalCompressedFileSize]
    #deletes original copy
    os.remove('compression/Algorithms/'+filename)
    return sizes

   

    
    

# sends user to the sucess page 
def successPage(request,filename):
    # performs multiple compression techniques
    compression.compressVariations(filename)
    # gets the sizes of those techniqes
    sizes = getSizes(filename)
    
    # sends user to sucess page
    return render(request,"compressionComplete.html",{"sizes":sizes})




# allows user to download file
def download(request):
    # opens file
    fl = open('compression/Algorithms/CompressedFile.dat', 'rb')
    
    # gets MIME type based on file extension
    mime_type, _ = mimetypes.guess_type('Algorithms/CompressedFile.dat')
    
    # create an HTTP response with the file content
    response = HttpResponse(fl, content_type=mime_type)
    
    # set the  filename for the browser's download prompt
    response['Content-Disposition'] = "attachment; filename=%s" % "CompressedFile.dat"
    
    
    return response
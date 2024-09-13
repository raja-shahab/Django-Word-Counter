from django.shortcuts import redirect, render

def counter(request):

    if request.method == 'POST':
        text = request.POST['texttocount']

        if text != '':
            word = len(text.split())
            letter = len(text)

            context = {
                'text' : text,
                'word' : word,
                'letter' : letter
            }

            return render(request, 'home.html',context )

    else:
        return render(request, 'home.html')

    return render(request, 'home.html')
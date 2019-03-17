from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'wordcount/home.html')

def about(request):
    return render(request,'wordcount/about.html')

def count(request):
    #넘어온 데이터를 이용하기 위함 fulltext(textarea이름)라는 이름으로 넘어왔다
    full_text = request.GET['fulltext'] 
    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    return render(request,'wordcount/count.html',{'fulltext':full_text, 'total':len(word_list), 'dictionary':word_dictionary.items()})

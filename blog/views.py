from django.shortcuts import render

def blog_view(requests):
    return render(requests, 'blog/blog-home.html')

def blog_single(requests):
    context = {'title':'shiraz uni is closed', 'content':'shiraz city is open but shiraz univrsity is closed unfortunetly'}
    return render(requests, 'blog/blog-single.html',context)
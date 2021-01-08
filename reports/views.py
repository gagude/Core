from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.response import Response
context = {}

#Create Yout ViewS Here
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.get_queryset().order_by('article_id')
    serializer_class = ArticleSerializer
    serializer = ArticleSerializer
    # paginator = Paginator(queryset,25)
    

    

    
    # def list(self, request):
    #      print('List')
    #      obj = Article.objects.get_queryset().order_by('article_id')
    #      page = self.paginate_queryset(obj)
    #      serializer_context = {'request': request}
    #      serializer = self.serializer_class(
    #          page, context=serializer_context, many=True
    #      )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return HttpResponse(serializer.data)   
        #     return self.get_paginated_response(serializer.data)

    # def get_queryset(self):
    #     page = self.paginate_queryset(self.queryset)
    #     serializer = self.get_serializer(page, many=True)
    #     return Response(serializer.data)

def index(request):
    context['reports'] = Article.objects.get_queryset().order_by('article_id')
    
    return render(request, "reports/index.html",context)

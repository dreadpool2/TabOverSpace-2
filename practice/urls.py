from django.urls import path
from . import views

app_name="practice"

urlpatterns = [

    path('', views.index, name='index'),
    path('data_structures', views.data_structures, name='data_structures'),
    path('python', views.python, name='python'),
    path('java', views.java, name='java'),
    path('algorithms/constructive_algorithms', views.constructive_algorithms, name='constructive_algorithms'),
    path('algorithms/dynamic_programming', views.dynamic_programming, name='dynamic_programming'),
    path('algorithms/graph_theory', views.graph_theory, name='graph_theory'),
    path('algorithms/greedy', views.greedy, name='greedy'),
    path('algorithms/implementation', views.implementation, name='implementation'),
    path('algorithms/np_complete', views.np_complete, name='np_complete'),
    path('algorithms/recursion', views.recursion, name='recursion'),
    path('algorithms/search', views.search, name='search'),
    path('algorithms/sorting', views.sorting, name='sorting'),
    path('algorithms/strings', views.strings, name='strings'),
    path('algorithms/warmup', views.warmup, name='warmup'),
    path('c/classes', views.classes, name='classes'),
    path('c/debugging', views.debugging, name='debugging'),
    path('c/inheritance', views.inheritance, name='inheritance'),
    path('c/introduction', views.introduction, name='introduction'),
    path('c/stl', views.stl, name='stl'),
    path('c/strings', views.strings_cpp, name='strings_cpp'),

]

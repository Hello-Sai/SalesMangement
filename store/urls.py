from django.urls import path

from store.views import AnalysisView, ProductUpdateView, ProductView, SalesView

urlpatterns =[

    path('products/sale',SalesView.as_view()),

    path('products/create',ProductView.as_view()),
    path('products/update/<name>',ProductUpdateView.as_view()),
    path('analysis',AnalysisView.as_view())
]
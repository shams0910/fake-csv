from django.urls import path
from schemas import views

app_name = 'schemas'

urlpatterns = [
    path('schema-list/', views.SchemaListView.as_view(), name='schema-list'),
    path('schema-create/', views.SchemaCreateView.as_view(), name='schema-create'),
    path('schema-edit/<int:id>/',
         views.SchemaEditView.as_view(), name='schema-edit'),
    path('schema-delete/<int:id>/',
         views.SchemaDeleteView.as_view(), name='schema-delete'),
    path('schema-datasets/<int:id>/',
         views.SchemaDatasetsView.as_view(), name='schema-datasets'),
    path('schema-generate-dataset/',
         views.GenerateDataSetView.as_view(), name='generate-dataset')
]

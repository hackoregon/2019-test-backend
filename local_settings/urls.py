from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

api_title = 'Hack Oregon Test 2019 API'

schema_view = get_swagger_view(title=api_title)


urlpatterns = [
    url(r'^test/schema/', schema_view),
    url(r'^test/tester/', include('hackoregon_test.tester.urls')),
    url(r'^test/docs/', include_docs_urls(title=api_title)),
]

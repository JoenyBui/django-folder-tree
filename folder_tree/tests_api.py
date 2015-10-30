from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from django.contrib.auth.models import User

from .models import TreeFolder
from .viewsets import FolderViewSet

__author__ = 'jbui'


class TestFolderTreeAPI(APITestCase):

    def test_create_folder(self):
        u1 = User.objects.get_or_create(username='olivia', password='password')
        # url = reverse('/folder/')

        factory = APIRequestFactory()

        request = factory.get('/folder/')
        force_authenticate(request, user=u1)
        #
        data = {'name': "new folder"}

        view = FolderViewSet.as_view()
        response = view(request)

        print(response)
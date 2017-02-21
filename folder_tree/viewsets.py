from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import TreeProfile, TreeFolder, GeneralFile, ImageFile, ProjectFolder
from .serializers import GeneralFileSerializer, ImageFileSerializer, FolderSerializer, ProjectSerializer

__author__ = 'jbui'


class TreeFullView(APIView):
    """
    Return the tree full view.

    """

    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, format=None):
        """
        Get the JSON structure of the folder view.

        :param request:
        :param format:
        :return:
        """
        user = request.user
        profile = TreeProfile.objects.get(user=user)

        return Response(profile.get_children())


class JsTreeView(APIView):
    """
    Javascript Tree View

    """
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        """
        Return the javascript tree view for the model.

        :param request:
        :return:
        """
        profile = TreeProfile.objects.get(user=request.user)

        return Response(profile.get_jstree())


class FolderViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Folder View Set

    """
    queryset = TreeFolder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'name', 'user')
    search_fields = ('id', 'name', 'user')
    ordering_fields = ('created', 'modified')
    paginate_by = 25

    def get_queryset(self):
        return TreeFolder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectFolderViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Project Folder Viewset

    """
    queryset = ProjectFolder.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'name', 'user')
    search_fields = ('id', 'name', 'user')
    ordering_fields = ('created', 'modified')
    paginate_by = 25

    def get_queryset(self):
        return ProjectFolder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GeneralFileViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    General File Viewset

    """
    # queryset = GeneralFile.objects.all()
    serializer_class = GeneralFileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'name', 'user', 'file_type')
    search_fields = ('id', 'name', 'user')
    ordering_fields = ('created', 'modified')
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)

    def get_queryset(self):
        return GeneralFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageFileViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Image file viewset.

    """
    # queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'name', 'user', 'file_type')
    search_fields = ('id', 'name', 'user')
    ordering_fields = ('created', 'modified')
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)

    def get_queryset(self):
        return ImageFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

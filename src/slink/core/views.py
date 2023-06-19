from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from slink.core.models import LinkModel
from slink.core.serializers import LinkModelSerializer


class LinkGenericViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = LinkModel.objects
    serializer_class = LinkModelSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

        # Redirect :)
        from django.http.response import HttpResponseRedirect
        return HttpResponseRedirect(redirect_to=self.get_object().url)

from rest_framework import serializers

from slink.core.models import LinkModel


class LinkModelSerializer(serializers.HyperlinkedModelSerializer):
    short = serializers.HyperlinkedIdentityField(view_name="core:link-detail")

    class Meta:
        model = LinkModel
        fields = ('url', 'short')
        read_only_fields = ('short',)

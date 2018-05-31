from rest_framework import serializers
from gtfs.models import GTFSForm

class FormSerializer(serializers.ModelSerializer):
	class Meta:
		model = GTFSForm
		fields = [
			'url',
			'name',
			'osm_tag',
			'gtfs_tag',
			'timestamp',
			'frequency'
		]
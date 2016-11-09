from rest_framework import fields
from rest_framework.serializers import Serializer


class PersonsListSerializer(Serializer):
    name = fields.CharField(required=True)
    last_name = fields.CharField(required=True)
    phone_number = fields.CharField(required=True)
    timestamp = fields.DateTimeField(required=True)
    address = fields.CharField(required=True)
    review = fields.SerializerMethodField()

    def get_review(self, obj):
        inst = obj.reviews.order_by('timestamp').last()
        if inst is not None:
            review = {
                'text': inst.text,
                'author': '{} {}'.format(inst.author.name, inst.author.last_name),
                'rating': inst.rating,
                'timestamp': inst.timestamp.isoformat(),
                'rewies_count': obj.reviews.count(),
            }
        else:
            review = {
                'text': 'There are no reviews yet',
                'rewies_count': 0,
            }
        return review

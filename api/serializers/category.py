from rest_framework import serializers
from api.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "company", "name", "parent_category", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, data):
        if 'parent_category' in data and data['parent_category'] is not None:
            if 'company' in data and data['parent_category'].company != data['company']:
                raise serializers.ValidationError("Parent category must belong to the same company")
        return data
from rest_framework import serializers

from .models import Element, Handbook, Version


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'code', 'value', 'handbook']


class HandbookSerializer(serializers.HyperlinkedModelSerializer):
    version = serializers.PrimaryKeyRelatedField(queryset=Version.objects.all(), source='version.title')

    class Meta:
        model = Handbook
        fields = ['id', 'title', 'mini_title', 'description', 'start_date', 'version', 'element']

    def create(self, validated_data):  # метод для сохранения объекта справочника
        instance = Handbook.objects.create(title=validated_data['title'], mini_title=validated_data['mini_title'],
                                           description=validated_data['description'],
                                           start_date=validated_data['start_date'],
                                           version=validated_data['version']['title'])
        instance.element.set(validated_data['element'])  # присвоение элементов

        return instance

    def update(self, instance, validated_data):  # метод для обновления объекта справочника
        for key, value in validated_data.items():  # цикл для обновления данных объекта справочника

            if key == 'version':  # для версии справочника нужно брать объект по ключу title
                setattr(instance, key, value['title'])

            elif not key == 'element':  # элементы справочника нужно обновлять с помощью set()
                setattr(instance, key, value)

        instance.save(update_fields=['title', 'mini_title', 'description', 'start_date', 'version'])
        instance.element.set(validated_data['element'])

        return instance

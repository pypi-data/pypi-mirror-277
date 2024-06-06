from io import BytesIO

from PIL import Image as PillowImage
from django.core.files import File as DjangoFile
from django.db import models, transaction

from ..models.file import File


class Image(File):
    original = models.ImageField(upload_to='media/images/originals', null=True, verbose_name='original size')
    thumbnail = models.ImageField(upload_to='media/images/thumbnails', null=True, verbose_name='thumbnail size')
    compact = models.ImageField(upload_to='media/images/compacts', null=True, verbose_name='compact size')

    def post_initialize(self):
        self._set_thumbnail()
        self._set_compact()

    def resize_image(self, resize_percent: int):
        image = PillowImage.open(self.original.file).convert('RGB')
        image_io = BytesIO()
        new_size = (
            int(image.width - image.width * (resize_percent / 100)),
            int(image.height - image.height * (resize_percent / 100)))
        resized_image = image.resize(new_size)
        resized_image.save(image_io, format=self.original.file.image.format, quality=100, optimize=True)
        django_image = DjangoFile(image_io, name=self.original.file.name)
        return django_image

    def _set_thumbnail(self):
        self.thumbnail = self.resize_image(resize_percent=60)

    def _set_compact(self):
        self.compact = self.resize_image(resize_percent=80)

    def delete_files(self):
        self.original.delete()
        self.thumbnail.delete()
        self.compact.delete()

    def delete(self, using=None, keep_parents=False):
        with transaction.atomic():
            self.delete_files()
            super(Image, self).delete(using=using, keep_parents=keep_parents)

    class Meta:
        ordering = ('-created_at',)

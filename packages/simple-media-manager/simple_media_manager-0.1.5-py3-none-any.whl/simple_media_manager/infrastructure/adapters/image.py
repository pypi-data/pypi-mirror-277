from collections.abc import Iterator

from simple_media_manager.domain.repository.image import ImageReadRepository, ImageWriteRepository
from simple_media_manager.infrastructure.models import Image


class DjangoImageWriteRepository(ImageWriteRepository):

    def save(self, file: bytes, name: str = '') -> Image:
        return Image.objects.create(file=file, name=name)

    def bulk_save(self, files: list) -> Iterator[Image]:
        new_images = []
        for data in files:
            new_image = Image(original=data.get('image'), name=data.get('name'))
            new_image.post_initialize()
            new_images.append(new_image)
        return Image.objects.bulk_create(new_images)

    def delete(self, id: int):
        Image.objects.get(id=id).delete()


class DjangoImageReadRepository(ImageReadRepository):
    def all(self) -> Iterator[Image]:
        return Image.objects.all()

    def get(self, pk: int) -> Image:
        return Image.objects.get(pk=pk)

    def find(self, name: str) -> Iterator[Image]:
        return Image.objects.filter(name__icontains=name)

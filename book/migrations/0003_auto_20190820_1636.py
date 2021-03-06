 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_describe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='upload_time',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='anonymous', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='describe',
            field=models.TextField(default='DataFlair Django tutorials'),
        ),
    ]

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('exam', '0002_remove_stadium_status_and_more'),
    ]

    # CustomUser is created in 0001, before models that reference it.
    operations = []

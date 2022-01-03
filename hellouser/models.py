from django.db import models


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    first_name = models.TextField()  # This field type is a guess.
    last_name = models.TextField(db_collation='C')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'User'
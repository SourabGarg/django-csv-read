from django.db import models
from django.core.validators import FileExtensionValidator

ext_validator = FileExtensionValidator(['csv'])


class CSVUpload(models.Model):
    csv = models.FileField(upload_to='uploaded_csv/', validators=[ext_validator])

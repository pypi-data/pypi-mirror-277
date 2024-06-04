import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_pdf_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".pdf"]
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            _("Unsupported file extension. Only PDF files are accepted.")
        )


def validate_pks_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".p12"]
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            _("Unsupported file extension. Only p12 files are accepted.")
        )

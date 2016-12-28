from base import *
USE_LESS = True
LESSC_BIN = os.path.join(BASE_DIR, 'node_modules', '.bin', 'lessc')
COMPRESS_PRECOMPILERS = (
    ('text/less', '%s {infile}'%LESSC_BIN),
)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

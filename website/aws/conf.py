import datetime
from decouple import config, Csv

AWS_USERNAME = config('AWS_USERNAME')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'website.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'website.aws.utils.StaticRootS3BotoStorage'

AWS_STORAGE_BUCKET_NAME = 'projects-samples'
S3DIRECT_REGION = 'eu-central-1'

S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

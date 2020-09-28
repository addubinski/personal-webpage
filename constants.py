from collections import namedtuple

SOFTWARE = 'SOFTWARE'
DATA = 'DATA'
OTHER = 'OTHER'
RECAPTCHA = 'RECAPTCHA'

# DB Primary Keys
PK_MY_PICTURE = 'top'

# DB Common Fields
ORDER = 'order'
PROJECT = 'project'
VIEWS = 'views'
IMAGE = 'image'
ALT = 'alt'
PROJECT_TITLE = 'project__title'

# HTTP
POST = 'POST'
GET = 'GET'
PLAIN_TEXT_CONTENT = 'text/plain'

# Recaptcha
RECAPTCHA_FORM_NAME = 'g-recaptcha-response'
RECAPTCHA_VERIFY_ENDPOINT = 'https://www.google.com/recaptcha/api/siteverify'
RECAPTCHA_SUCCESS = 'success'
RECAPTCHA_MESSAGE = 'recaptcha_message'
CONTACT_SUCCESS_MESSAGE = 'Message received! I will get back to you as soon as possible.'
RECAPTCHA_VERIFY_FAILED_MESSAGE = 'Recaptcha Failed. You might be a robot...'

# Resume
ResumeItem = namedtuple('ResumeItem', ['info', 'details'])

# Homepage Template Fields
EXPERIENCES = 'experiences'
EDUCATIONS = 'educations'
CERTS_AND_AWARDS = 'certs_and_awards'
PROJECTS = 'projects'
MY_PICTURE = 'my_picture'
MY_PICTURE_ALT = 'my_picture_alt'
SECRET = 'secret'
RESPONSE = 'response'
ERRORS = 'errors'
FORM = 'form'

# Projects Template Fields
SEARCH = 'search'

# Redirect Targets
PROJECT_HOME = 'projects_home'

# Query Params
QUERY_DESTINATION = 'dest'



from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponse
from .forms import ContactForm
from collections import defaultdict
from constants import SOFTWARE, DATA, OTHER, PK_MY_PICTURE, ORDER, PROJECT_TITLE, ALT, IMAGE, GET, POST,\
    RECAPTCHA_FORM_NAME, RECAPTCHA_VERIFY_ENDPOINT, SECRET, RESPONSE, RECAPTCHA_SUCCESS, \
    RECAPTCHA_VERIFY_FAILED_MESSAGE, CONTACT_SUCCESS_MESSAGE, ResumeItem, EXPERIENCES, EDUCATIONS, CERTS_AND_AWARDS,\
    PROJECTS, MY_PICTURE_ALT, MY_PICTURE, FORM, RECAPTCHA_MESSAGE, PLAIN_TEXT_CONTENT
from .models import Skills, Pictures, RecentProjects, Experience, Education, ExperienceDetails, EducationDetails,\
    CertsAndAwards
from requests import post
from os import environ
from constants import RECAPTCHA


@require_http_methods([GET, POST])
def homepage(request):
    skills = Skills.objects.order_by(ORDER).all()
    projects = RecentProjects.objects.order_by(ORDER).only(PROJECT_TITLE, ALT, IMAGE)[:3]
    experiences = Experience.objects.order_by(ORDER).all()
    educations = Education.objects.order_by(ORDER).all()
    experience_details = [ExperienceDetails.objects.filter(exp_id=experience.exp_id) for experience in experiences]
    education_details = [EducationDetails.objects.filter(edu_id=education.edu_id) for education in educations]
    certs_and_awards = CertsAndAwards.objects.order_by(ORDER).all()

    software_categories = defaultdict(list)
    data_categories = defaultdict(list)
    other_categories = list()
    categories = dict([
        (SOFTWARE, lambda software_skill: software_categories[software_skill.sub_category].append(software_skill)),
        (DATA, lambda data_skill: data_categories[data_skill.sub_category].append(data_skill)),
        (OTHER, lambda other_skill: other_categories.append(other_skill))])
    for skill in skills:
        categories[skill.category](skill)
    my_picture = get_object_or_404(Pictures, pk=PK_MY_PICTURE)

    recaptcha_message = ''
    form = None

    if request.method == POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get(RECAPTCHA_FORM_NAME)
            recaptcha_validation = post(RECAPTCHA_VERIFY_ENDPOINT, data={
                SECRET: environ[RECAPTCHA],
                RESPONSE: recaptcha_response})
            result = recaptcha_validation.json()
            if result[RECAPTCHA_SUCCESS]:
                form.save()
                form = None
                recaptcha_message = CONTACT_SUCCESS_MESSAGE
            else:
                recaptcha_message = RECAPTCHA_VERIFY_FAILED_MESSAGE
    return render(request, 'homepage/base.html', {
        SOFTWARE: software_categories,
        DATA: data_categories,
        OTHER: other_categories,
        EXPERIENCES: [ResumeItem(experience, experience_detail)
                      for experience, experience_detail in zip(experiences, experience_details)],
        EDUCATIONS: [
            ResumeItem(education, education_detail)
            for education, education_detail in zip(educations, education_details)],
        CERTS_AND_AWARDS: certs_and_awards,
        PROJECTS: projects,
        MY_PICTURE: my_picture.url,
        MY_PICTURE_ALT: my_picture.alt,
        FORM: form,
        RECAPTCHA_MESSAGE: recaptcha_message
    })


def show_404(request, exception):
    print(exception)
    return render(request, 'global/404.html')


def show_500(request):
    return render(request, 'global/500.html')


@require_GET
def robots_txt(request):
    lines = [
        'User-Agent: *',
        'Disallow: /404/',
        'Disallow: /500/',
        'Disallow: /admin/'
    ]
    return HttpResponse('\n'.join(lines), content_type=PLAIN_TEXT_CONTENT)

from django.contrib import admin
from .models import Skills, Education, EducationDetails,\
    Experience, ExperienceDetails, CertsAndAwards, CertsAndAwardsDetails, Pictures, RecentProjects, Contact

admin.site.register([Skills, Education, EducationDetails,
                     Experience, ExperienceDetails, CertsAndAwardsDetails, CertsAndAwards, Pictures, RecentProjects,
                     Contact])


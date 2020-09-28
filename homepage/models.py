from django.db import models


class Details(models.Model):
    detail_id = models.AutoField(primary_key=True)


class Pictures(models.Model):

    class Meta:
        db_table = 'pictures'
        verbose_name = 'picture'
        verbose_name_plural = 'pictures'

    picture_id = models.CharField(primary_key=True, max_length=50, unique=True)
    url = models.ImageField(upload_to='primary')
    alt = models.CharField(max_length=100)

    def __str__(self):
        return f'id: {self.picture_id}, alt: {self.alt}'


class Skills(models.Model):

    class Meta:
        db_table = 'skills'
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    class Category(models.TextChoices):
        SOFTWARE = 'SOFTWARE'
        DATA = 'DATA'
        OTHER = 'OTHER'

    skill_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    info = models.TextField(max_length=750, null=True, blank=True)
    category = models.CharField(choices=Category.choices, max_length=8)
    sub_category = models.CharField(max_length=255)
    order = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name}, {self.category}, {self.sub_category}, order: {self.order}'


class Education(models.Model):

    class Meta:
        db_table = 'education'
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    edu_id = models.AutoField(primary_key=True)
    from_date = models.DateField()
    to_date = models.DateField()
    name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    info = models.TextField(max_length=750, null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    order = models.SmallIntegerField()

    def __str__(self):
        return f'id: {self.edu_id}, {self.name}, {self.major}, order: {self.order}'


class EducationDetails(Details):

    class Meta:
        db_table = 'education_details'
        verbose_name = 'Education Detail'
        verbose_name_plural = 'Education Details'

    info = models.TextField(max_length=750)
    edu = models.ForeignKey(to='Education', on_delete=models.CASCADE)

    def __str__(self):
        return f'detail id: {self.detail_id}, edu id: {self.edu_id}'


class Experience(models.Model):

    class Meta:
        db_table = 'experience'
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    exp_id = models.AutoField(primary_key=True)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    info = models.TextField(max_length=750, blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return f'id: {self.exp_id}, {self.name}, {self.title}, order: {self.order}'


class ExperienceDetails(Details):

    class Meta:
        db_table = 'experience_details'
        verbose_name = 'Experience Detail'
        verbose_name_plural = 'Experience Details'

    info = models.TextField(max_length=750)
    exp = models.ForeignKey(to='Experience', on_delete=models.CASCADE)

    def __str__(self):
        return f'detail id: {self.detail_id}, exp id: {self.exp_id}'


class CertsAndAwards(models.Model):

    class Meta:
        db_table = 'certs_and_awards'
        verbose_name = 'Cert or Award'
        verbose_name_plural = 'Certs and Awards'

    ca_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    award_date = models.DateField()
    issuer = models.CharField(max_length=255)
    order = models.SmallIntegerField()

    def __str__(self):
        return f'id: {self.ca_id}, {self.title}, order: {self.order}'


class CertsAndAwardsDetails(Details):

    class Meta:
        db_table = 'cert_and_awards_details'
        verbose_name = 'Certs and Awards Detail'
        verbose_name_plural = 'Certs and Awards Details'

    info = models.TextField(max_length=750)
    ca = models.ForeignKey(to='CertsAndAwards', on_delete=models.CASCADE)

    def __str__(self):
        return f'detail id: {self.detail_id}, exp id: {self.ca_id}'


class RecentProjects(models.Model):

    class Meta:
        db_table = 'recent_projects'
        verbose_name = 'Recent Project'
        verbose_name_plural = 'Recent Project'

    recent_project_id = models.AutoField(primary_key=True)
    destination = models.URLField()
    image = models.ImageField(upload_to='recent_projects')
    alt = models.CharField(max_length=255)
    order = models.SmallIntegerField()
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)

    def __str__(self):
        return f'proj id: {self.recent_project_id}, {self.destination}, for project: {self.project}'


class Contact(models.Model):

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'id: {self.id}, {self.name}'

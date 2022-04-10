from django.db import models

# Create your models here.
JOB_TYPES = [
    ('HR', 'HR'),
    ('C++', 'C++'),
    ('Sales', 'Sales')
]
GENDERS = [
    ('女', '女'),
    ('男', '男')
]


class Resume(models.Model):
    job = models.CharField(blank=False, max_length=30, choices=JOB_TYPES, verbose_name='职位名称')
    company = models.CharField(blank=True, max_length=50, verbose_name='公司名称')
    active = models.CharField(blank=True, max_length=50, verbose_name='活跃度')
    id = models.CharField(primary_key=True, blank=False, max_length=50, verbose_name='id')
    datetime = models.DateTimeField(auto_now_add=True)
    person_info = models.CharField(blank=True, max_length=512, verbose_name='个人信息')
    education_info = models.CharField(blank=True, max_length=512, verbose_name='教育信息')
    work_info = models.CharField(blank=True, max_length=512, verbose_name='工作信息')
    resume_pdf_info = models.CharField(blank=True, max_length=1024, verbose_name='pdf简历文件名')
    resume_url = models.TextField(blank=True, max_length=1024, verbose_name='简历网站链接')
    gender = models.CharField(blank=True, max_length=10, choices=GENDERS, verbose_name='性别')
    age = models.SmallIntegerField(blank=True, verbose_name='年龄')
    pdf_file_abstract_path = models.TextField(blank=True, max_length=1024, verbose_name='pdf简历相对路径')
    pdf_file_abstract_path_hyperlink = models.TextField(blank=True, max_length=1024, verbose_name='pdf简历相对路径超级链接')
    resume_url_hyperlink = models.TextField(blank=True, max_length=1024, verbose_name='简历网站链接超级链接')
    resume_source = models.CharField(blank=True, max_length=20, verbose_name='简历渠道')
    pdf = models.BinaryField(verbose_name='PDF简历')

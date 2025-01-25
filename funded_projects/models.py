from datetime import date
from sqlite3 import Date
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class FundedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='funded_project', null=True, blank=True)
    title = models.CharField(max_length=200)
    funding_agency = models.CharField(max_length=100)
    project_grant = models.IntegerField(help_text="Grant amount in Rs")
    letter_no = models.CharField(max_length=50)
    submission_date = models.DateField()
    cd_pi = models.CharField(max_length=200)
    project_duration_years = models.IntegerField()
    project_duration_months = models.IntegerField()

    def __str__(self):
        return self.title

class FundedProjectSanctioned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='funded_project_sanctioned', null=True, blank=True)
    title = models.CharField(max_length=200)
    funding_agency = models.CharField(max_length=100)
    project_grant = models.IntegerField(help_text="Grant amount in Rs")
    letter_no = models.CharField(max_length=50)
    submission_date = models.DateField()
    cd_pi = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    proof = models.FileField(upload_to='images/project_proofs/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class ConsultancyProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultancy_projects', null=True, blank=True)
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    amount_sanctioned = models.IntegerField(help_text="Amount sanctioned in Rs")
    letter_amount = models.IntegerField(help_text="Letter amount in Rs")
    date_of_sanction = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    proof = models.FileField(upload_to='images/consultancy_proofs/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class SeedMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seed_money_projects', null=True, blank=True)
    faculty_id = models.IntegerField()
    faculty_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    amount_credited = models.IntegerField(help_text="Amount credited in Rs")
    letter_no = models.IntegerField()
    date_of_sanction = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    proof = models.FileField(upload_to='images/seedmoney_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.faculty_name} - {self.title}"
    
class Patent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patents', null=True, blank=True)
    co_inventors = models.TextField(help_text="Enter names of co-inventors (students and faculty)")
    title = models.CharField(max_length=200)
    filing_date = models.DateField()
    status = models.CharField(max_length=100)
    proof = models.FileField(upload_to='images/patent_proofs/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Startup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='startups', null=True, blank=True)
    team_members = models.TextField(help_text="Enter names of team members (students and faculty)")
    startup_name = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.startup_name

class ScopusWosPublication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scopus_wos_publications', null=True, blank=True)
    authors = models.TextField(help_text="Enter names of authors and co-authors")
    title = models.CharField(max_length=300)
    journal_name = models.CharField(max_length=200)
    volume = models.IntegerField(null=True, blank=True)
    issue = models.IntegerField(null=True, blank=True)
    pages = models.CharField(max_length=50, null=True, blank=True)
    publication_date = models.DateField()
    indexed_in = models.CharField(max_length=50, choices=[('Scopus', 'Scopus'), ('WoS', 'Web of Science')])
    if_value = models.CharField(max_length=10, help_text="Impact Factor value")
    collaborator = models.CharField(max_length=300, help_text="Academic/Industry with name and designation")
    full_paper_link = models.URLField()

    def __str__(self):
        return self.title
    
class BookChapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_chapters', null=True, blank=True)
    author_name = models.CharField(max_length=200)
    chapter_title = models.CharField(max_length=300)
    book_title = models.CharField(max_length=300)
    publisher_name = models.CharField(max_length=200)
    chapter_number = models.IntegerField()
    page_number = models.CharField(max_length=50)  # Using CharField for flexibility (e.g., "123-145")
    publication_year = models.IntegerField()
    # collaborators = models.TextField(help_text="Academic/Industry with name and designation")
    # full_paper_link = models.URLField()

    def __str__(self):
        return f"{self.author_name} - {self.chapter_title}"
    
class ConferenceProceeding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conference_proceedings', null=True, blank=True)
    authors = models.TextField(help_text="Enter names of authors")
    title = models.CharField(max_length=300)
    conference_name = models.CharField(max_length=300)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    # isbn_issn = models.CharField(max_length=20, help_text="ISBN or ISSN number")
    collaborators = models.TextField(help_text="Academic/Industry with name and designation")
    proof = models.FileField(upload_to='images/conference_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.authors} - {self.title}"
    
class GuestLecture(models.Model):
    EVENT_TYPES = [
        ('Internal', 'Internal Event'),
        ('External', 'External Event'),
    ]
    
    LECTURE_TYPES = [
        ('FDP', 'FDP'),
        ('Webinar', 'Webinar'),
        ('Other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest_lectures', null=True, blank=True)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES, default="Internal")
    title = models.CharField(max_length=300, default="")
    topic = models.CharField(max_length=300, default="")
    lecture_type = models.CharField(max_length=10, choices=LECTURE_TYPES, default="Other")
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    venue = models.CharField(max_length=300, default="")
    city = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    participants_count = models.PositiveIntegerField(default=0)
    report_certificate = models.FileField(upload_to='guest_lecture_reports/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.topic}"
    
class FacultyEventParticipation(models.Model):
    EVENT_TYPES = [
        ('FDP', 'FDP'),
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
        ('Conference', 'Conference'),
    ]
    MODE_CHOICES = [
        ('Offline', 'Offline'),
        ('Online', 'Online'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faculty_event_participations', null=True, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='FDP')
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='Offline')
    program_title = models.CharField(max_length=300, default='')
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    sponsoring_agency = models.CharField(max_length=300, default='')
    report_certificate = models.FileField(upload_to='faculty_event_reports/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.program_title}"
    
class FacultyEventParticipationOffCampus(models.Model):
    EVENT_TYPES = (
        ('FDP', 'FDP'),
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
        ('Conference', 'Conference'),
    )
    MODE_CHOICES = (
        ('Offline', 'Offline'),
        ('Online', 'Online'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faculty_event_participations_off_campus', null=True, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='FDP')
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='Offline')
    program_title = models.CharField(max_length=300, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    sponsoring_agency = models.CharField(max_length=300, blank=True)
    host_institution = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    report_certificate = models.FileField(upload_to='event_certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.program_title} at {self.host_institution}"
    
class ProgramOrganized(models.Model):
    EVENT_TYPES = (
        ('FDP', 'FDP'),
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
        ('Conference', 'Conference'),
    )
    MODE_CHOICES = (
        ('Offline', 'Offline'),
        ('Online', 'Online'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='programs_organized', null=True, blank=True)
    faculty_name = models.CharField(max_length=200, blank=True, help_text="Name of the faculty")
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='FDP')
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='Offline')
    program_title = models.CharField(max_length=300, blank=True, help_text="Title of the program")
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    venue = models.CharField(max_length=300, blank=True, help_text="Enter the Venue")
    resource_person = models.CharField(max_length=200, blank=True, help_text="Name of the resource person")
    sponsorships = models.CharField(max_length=300, blank=True, help_text="Sponsorships if any")
    delegates_count = models.PositiveIntegerField(default=0, help_text="Number of delegate participants")
    report_certificate = models.FileField(upload_to='images/program_certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.faculty_name} - {self.program_title}"
    
class IncomeGeneratedProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='income_generated_programs', null=True, blank=True)
    program_name = models.CharField(max_length=200, help_text="Name of the program")
    event_title = models.CharField(max_length=300, help_text="Title of the event")
    event_level = models.CharField(max_length=50, choices=[('National', 'National'), ('International', 'International')], help_text="National or International")
    start_date = models.DateField(help_text="Start date of the event",null=True, blank=True)
    end_date = models.DateField(help_text="End date of the event",null=True, blank=True)
    resource_person_designation = models.CharField(max_length=300, help_text="Resource person & Designation")
    delegates_count = models.IntegerField(help_text="Number of delegates participated")
    income_generated = models.DecimalField(max_digits=10, decimal_places=2, help_text="Income generated (Rs)")

    def __str__(self):
        return f"{self.program_name} - {self.event_title}"
    
class AlumniInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alumni_interactions', null=True, blank=True)
    alumni_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    event_title = models.CharField(max_length=300)
    event_date = models.DateField()
    student_participants = models.PositiveIntegerField()
    report_link = models.FileField(upload_to='images/alumini/', null=True, blank=True)

    def __str__(self):
        return f"{self.alumni_name} - {self.event_title}"
    
class FacultyMoocCourse(models.Model):
    PLATFORM_CHOICES = [
        ('NPTEL', 'NPTEL'),
        ('Coursera', 'Coursera'),
        ('edX', 'edX'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mooc_courses', null=True, blank=True)
    # faculty_name = models.CharField(max_length=200)
    # designation = models.CharField(max_length=200)
    virtual_platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    course_title = models.CharField(max_length=300)
    duration_weeks = models.PositiveIntegerField()
    report_certificate = models.FileField(upload_to='images/faculty_mooc/', null=True, blank=True)

    def __str__(self):
        return f"{self.faculty_name} - {self.course_title}"

    class Meta:
        unique_together = ['user', 'course_title', 'virtual_platform']

class PlacementHigherStudiesEntrepreneurship(models.Model):
    CATEGORY_CHOICES = [
        ('Placement', 'Placement'),
        ('Higher Studies', 'Higher Studies'),
        ('Entrepreneurship', 'Entrepreneurship'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='placement_higher_studies_entrepreneurship', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Placement', null=True, blank=True)
    resource_person = models.CharField(max_length=200)
    resource_person_designation = models.CharField(max_length=300, help_text="Designation/Organization details", null=True, blank=True)
    resource_person_company = models.CharField(max_length=300, help_text="Company details", null=True, blank=True)
    program_title = models.CharField(max_length=300, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    student_participants = models.PositiveIntegerField()
    report_certificate = models.FileField(upload_to='images/faculty_mooc/', null=True, blank=True)

    def __str__(self):
        return f"{self.resource_person} - {self.program_title}"
    
class CommunitySpiritualActivity(models.Model):
    ACTIVITY_CHOICES = [
        ('community', 'Community'),
        ('spiritual', 'Spiritual'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_spiritual_activities', null=True, blank=True)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, null=True, blank=True)
    # faculty_name = models.CharField(max_length=200, null=True, blank=True)
    # faculty_designation = models.CharField(max_length=200, null=True, blank=True)
    program_name = models.CharField(max_length=300, null=True, blank=True)
    place = models.CharField(max_length=300, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    beneficiaries_count = models.PositiveIntegerField(null=True, blank=True)
    proof = models.FileField(upload_to='community_spiritual_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.faculty_name} - {self.program_name}"

    class Meta:
        verbose_name_plural = "Community & Spiritual Activities"

class CompanyVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_visits', null=True, blank=True)
    # faculty_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    purpose = models.TextField()
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    possible_outcome = models.TextField()
    report_link = models.FileField(upload_to='community_spiritual_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.faculty_name} - {self.company_name} - {self.visit_date}"

    class Meta:
        verbose_name_plural = "Company Visits by Faculty Members"

class InternationalInternship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='international_internships', null=True, blank=True)
    reg_no = models.CharField(max_length=50)
    student_name = models.CharField(max_length=200)
    mentor_name = models.CharField(max_length=200)
    host_institution = models.CharField(max_length=300)
    city_country = models.CharField(max_length=200)
    period_duration = models.CharField(max_length=200)
    proof = models.FileField(upload_to='images/conference_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.host_institution}"

    class Meta:
        verbose_name_plural = "International Internships (IAESTE)"

class StudentSeedMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_seed_money', null=True, blank=True)
    student_name = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=200)
    project_title = models.CharField(max_length=300)
    amount_sanctioned = models.DecimalField(max_digits=10, decimal_places=2)
    letter_no_and_date = models.CharField(max_length=200)
    period = models.CharField(max_length=200)
    proof = models.FileField(upload_to='images/conference_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.project_title}"

    class Meta:
        verbose_name_plural = "Seed Money for Students"

class ProductDevelopedByStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_products', null=True, blank=True)
    reg_no = models.CharField(max_length=50, help_text="Registration number of the student")
    student_name = models.CharField(max_length=200, help_text="Name of the student")
    product_name = models.CharField(max_length=300, help_text="Name of the prototype/product")
    area_of_application = models.CharField(max_length=200, help_text="Area of application for the product")
    brief_description = models.TextField(help_text="Brief description of the product")
    proof = models.FileField(upload_to='images/conference_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.product_name}"

    class Meta:
        verbose_name_plural = "Products Developed by Students"

class StudentStartup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_startups', null=True, blank=True)
    student_details = models.CharField(max_length=300, help_text="Name of student(s) and registration number(s)")
    startup_title = models.CharField(max_length=200, help_text="Title of the startup")
    investors = models.CharField(max_length=300, help_text="Names of investors")
    registration_info = models.DateField()
    proof = models.FileField(upload_to='images/conference_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.startup_title} by {self.student_details}"

    class Meta:
        verbose_name_plural = "Student Startups"


class CompetitiveExamSuccess(models.Model):
    EXAM_CHOICES = [
        ('NET', 'NET'),
        ('SLET', 'SLET'),
        ('GATE', 'GATE'),
        ('GMAT', 'GMAT'),
        ('CAT', 'CAT'),
        ('GRE', 'GRE'),
        ('JAM', 'JAM'),
        ('IELTS', 'IELTS'),
        ('TOEFL', 'TOEFL'),
        ('CIVIL_SERVICES', 'Civil Services'),
        ('STATE_GOVT', 'State Government Exams'),
        ('OTHER', 'Other')
    ]

    YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Fifth Year'),
        ('OTHER', 'Other')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='competitive_exam_successes')
    reg_no = models.CharField(max_length=50, help_text="Registration number / Roll number of examination")
    student_name = models.CharField(max_length=200, help_text="Name of selected/qualified student")
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, help_text="Year of study", null=True, blank=True)
    roll_no = models.CharField(max_length=50, help_text="Student's roll number", null=True, blank=True)
    exam_type = models.CharField(max_length=20, choices=EXAM_CHOICES)
    other_exam = models.CharField(max_length=100, blank=True, null=True, help_text="Specify if 'Other' is selected")
    proof = models.FileField(upload_to='competitive_exam_proofs/', help_text="Upload proof or documentation",blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.get_exam_type_display()} - {self.get_year_display()}"

    class Meta:
        verbose_name_plural = "Competitive Exam Successes"

class StudentEventParticipation(models.Model):
    ACTIVITY_CHOICES = [
        ('HACKATHON', 'Hackathon'),
        ('COMPETITION', 'Competition'),
        ('ONLINE_COURSE', 'Online Course'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_participations', null=True, blank=True)
    reg_no = models.CharField(max_length=50, help_text="Registration number of the student")
    student_name = models.CharField(max_length=200, help_text="Name of the student")
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    host_institute = models.CharField(max_length=200, help_text="Host institute")
    city = models.CharField(max_length=100, help_text="City of the event", null=True, blank=True)
    country = models.CharField(max_length=100, help_text="Country of the event", null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    award = models.CharField(max_length=200, blank=True, null=True, help_text="Award received, if any")
    proof = models.FileField(upload_to='event_participation_proofs/', help_text="Upload proof or documentation", null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.get_activity_display()} at {self.host_institute}"

    class Meta:
        verbose_name_plural = "Student Event Participations"

class StudentCoCurricularParticipation(models.Model):
    ACTIVITY_CHOICES = [
        ('NCC', 'NCC'),
        ('NSS', 'NSS'),
        ('NON_TECH', 'Non-Technical Event'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='co_curricular_participations', null=True, blank=True)
    reg_no = models.CharField(max_length=50, help_text="Registration number of the student")
    student_name = models.CharField(max_length=200, help_text="Name of the student")
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    host_institute = models.CharField(max_length=200, help_text="Host institute", default="Unknown")
    city = models.CharField(max_length=100, help_text="City of the event", null=True, blank=True)
    country = models.CharField(max_length=100, help_text="Country of the event", null=True, blank=True)
    award = models.CharField(max_length=200, blank=True, null=True, help_text="Award received, if any")
    proof = models.FileField(upload_to='co_curricular_proofs/', help_text="Upload proof or documentation", null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.get_activity_display()} at {self.host_institute}"

    class Meta:
        verbose_name_plural = "Student Co-Curricular Participations"

class StudentSportsParticipation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sports_participations', null=True, blank=True)
    reg_no = models.CharField(max_length=50, help_text="Registration number of the student")
    student_name = models.CharField(max_length=200, help_text="Name of the student")
    sports_event = models.CharField(max_length=200, help_text="Name of the sports event")
    organizing_institution = models.CharField(max_length=200, help_text="Organizing institution", null=True, blank=True)
    city = models.CharField(max_length=100, help_text="City of the event", null=True, blank=True)
    country = models.CharField(max_length=100, help_text="Country of the event", null="True", blank="True")
    award = models.CharField(max_length=200, blank=True, null=True, help_text="Award received, if any")
    proof = models.FileField(upload_to='sports_proofs/', help_text="Upload proof or documentation", null=True, blank=True)
    date_from = models.DateField(help_text="Start date of the event", default=timezone.now)
    date_to = models.DateField(help_text="End date of the event", default=timezone.now)

    def __str__(self):
        return f"{self.student_name} - {self.sports_event} at {self.organizing_institution}"

    class Meta:
        verbose_name_plural = "Student Sports Participations"

class NCCParticipation(models.Model):
    PARTICIPATION_CHOICES = [
        ('CAMP', 'Camp'),
        ('PARADE', 'Parade'),
        ('EVENT', 'Event'),
        ('EXAM', 'Exam'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ncc_participations', null=True, blank=True)
    cadet_name = models.CharField(max_length=200, help_text="Name of the cadet")
    rank = models.CharField(max_length=100, help_text="Rank of the cadet")
    participation_type = models.CharField(max_length=10, choices=PARTICIPATION_CHOICES, help_text="Type of participation")
    award = models.CharField(max_length=200, blank=True, null=True, help_text="Award received, if any")
    proof = models.FileField(upload_to='ncc_proofs/', help_text="Upload proof or documentation", null=True, blank=True)
    date_from = models.DateField(default=date.today, help_text="Start date of participation")
    date_to = models.DateField(default=date.today, help_text="End date of participation")

    def __str__(self):
        return f"{self.cadet_name} - {self.rank} - {self.get_participation_type_display()}"

    class Meta:
        verbose_name_plural = "NCC Participations"

class IndustrialVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='industrial_visits', null=True, blank=True)
    place_of_visit = models.CharField(max_length=300, help_text="Place of industrial visit")
    date_from = models.DateField(help_text="Start date of the visit", default=timezone.now)
    date_to = models.DateField(help_text="End date of the visit", null=True, blank=True)
    number_of_students = models.PositiveIntegerField(help_text="Number of students who participated")
    faculty_members = models.TextField(help_text="Names of faculty members who participated", default="To be updated")
    outcome = models.TextField(help_text="Outcome of the industrial visit")
    proof = models.FileField(upload_to='industrial_visit_proofs/', help_text="Upload proof or documentation", null=True, blank=True)

    def __str__(self):
        return f"Industrial Visit to {self.place_of_visit} from {self.date_from} to {self.date_to}"

    class Meta:
        verbose_name_plural = "Industrial Visits"
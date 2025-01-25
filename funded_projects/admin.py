from django.contrib import admin

from funded_projects.serializers import ScopusWosPublication
from .models import AlumniInteraction, BookChapter, CommunitySpiritualActivity, CompanyVisit, CompetitiveExamSuccess, FacultyEventParticipation, FacultyEventParticipationOffCampus, FacultyMoocCourse, FundedProject, FundedProjectSanctioned, ConsultancyProject, GuestLecture, IncomeGeneratedProgram, IndustrialVisit, InternationalInternship, NCCParticipation, Patent, PlacementHigherStudiesEntrepreneurship, ProgramOrganized, SeedMoney, Startup, StudentCoCurricularParticipation, StudentEventParticipation, StudentSeedMoney, StudentSportsParticipation, StudentStartup

@admin.register(FundedProject)
class FundedProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'funding_agency', 'project_grant', 'submission_date')
    search_fields = ('title', 'funding_agency', 'user__username')
    list_filter = ('submission_date', 'user')

@admin.register(FundedProjectSanctioned)
class FundedProjectSanctionedAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'funding_agency', 'project_grant', 'submission_date')
    search_fields = ('title', 'funding_agency', 'user__username')
    list_filter = ('submission_date', 'user')

@admin.register(ConsultancyProject)
class ConsultancyProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'client', 'amount_sanctioned', 'date_of_sanction', 'start_date', 'end_date')
    search_fields = ('title', 'client', 'user__username')
    list_filter = ('date_of_sanction', 'start_date', 'end_date', 'user')
    readonly_fields = ('proof',)  # Make the proof field read-only in the admin

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('proof',)
        return self.readonly_fields
    
@admin.register(SeedMoney)
class SeedMoneyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'user', 'title', 'amount_credited', 'date_of_sanction', 'start_date', 'end_date')
    search_fields = ('faculty_name', 'title', 'user__username')
    list_filter = ('date_of_sanction', 'start_date', 'end_date', 'user')
    readonly_fields = ('proof',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('proof',)
        return self.readonly_fields
    
@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'filing_date', 'status')
    search_fields = ('title', 'co_inventors', 'user__username')
    list_filter = ('filing_date', 'status', 'user')
    readonly_fields = ('proof',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('proof',)
        return self.readonly_fields
    
@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('startup_name', 'user', 'status')
    search_fields = ('startup_name', 'team_members', 'user__username')
    list_filter = ('status', 'user')

@admin.register(ScopusWosPublication)
class ScopusWosPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'journal_name', 'publication_date', 'indexed_in', 'if_value', 'collaborator')
    search_fields = ('title', 'journal_name', 'collaborator')
    list_filter = ('indexed_in', 'publication_date')

@admin.register(BookChapter)
class BookChapterAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'user', 'chapter_title', 'book_title', 'publication_year')
    search_fields = ('author_name', 'chapter_title', 'book_title', 'user__username')
    list_filter = ('publication_year', 'user')

from .models import ConferenceProceeding

@admin.register(ConferenceProceeding)
class ConferenceProceedingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'conference_name', 'date')
    search_fields = ('authors', 'title', 'conference_name', 'user__username')
    list_filter = ('date', 'user')

@admin.register(GuestLecture)
class GuestLectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'event_type', 'lecture_type', 'date_from', 'date_to', 'venue', 'city', 'country', 'participants_count')
    list_filter = ('event_type', 'lecture_type', 'date_from', 'country')
    search_fields = ('title', 'topic', 'venue', 'city', 'country')

@admin.register(FacultyEventParticipation)
class FacultyEventParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'program_title', 'date_from', 'date_to', 'sponsoring_agency')
    list_filter = ('event_type', 'mode')
    search_fields = ('user__username', 'program_title', 'sponsoring_agency')

@admin.register(FacultyEventParticipationOffCampus)
class FacultyEventParticipationOffCampusAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'program_title', 'date_from', 'date_to', 'host_institution')
    list_filter = ('event_type', 'mode', 'country')
    search_fields = ('user__username', 'program_title', 'host_institution')

@admin.register(ProgramOrganized)
class ProgramOrganizedAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'event_type', 'program_title', 'date_from', 'date_to', 'venue')
    list_filter = ('event_type', 'mode')
    search_fields = ('faculty_name', 'program_title', 'resource_person')

@admin.register(IncomeGeneratedProgram)
class IncomeGeneratedProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'event_title', 'start_date', 'end_date', 'event_level', 'income_generated')
    list_filter = ('event_level', 'start_date', 'end_date')
    search_fields = ('program_name', 'event_title', 'resource_person_designation')

@admin.register(AlumniInteraction)
class AlumniInteractionAdmin(admin.ModelAdmin):
    list_display = ('alumni_name', 'user', 'event_title', 'event_date', 'student_participants')
    search_fields = ('alumni_name', 'event_title', 'user__username')
    list_filter = ('event_date', 'user')

@admin.register(FacultyMoocCourse)
class FacultyMoocCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'virtual_platform', 'course_title', 'duration_weeks')
    list_filter = ('virtual_platform',)
    search_fields = ('user__username', 'course_title')
    ordering = ('-duration_weeks', 'course_title')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('user', 'virtual_platform', 'course_title')
        return ()

@admin.register(PlacementHigherStudiesEntrepreneurship)
class PlacementHigherStudiesEntrepreneurshipAdmin(admin.ModelAdmin):
    list_display = ('category', 'resource_person', 'resource_person_designation', 'resource_person_company', 'program_title', 'date_from', 'date_to', 'student_participants')
    list_filter = ('category', 'date_from', 'date_to', 'resource_person_company')
    search_fields = ('resource_person', 'program_title', 'resource_person_company')
    date_hierarchy = 'date_from'

@admin.register(CommunitySpiritualActivity)
class CommunitySpiritualActivityAdmin(admin.ModelAdmin):
    list_display = ( 'activity_type', 'program_name', 'place', 'date_from', 'date_to', 'beneficiaries_count')
    list_filter = ('activity_type', 'date_from', 'date_to')
    search_fields = ('faculty_name', 'program_name', 'place')

@admin.register(CompanyVisit)
class CompanyVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'purpose', 'date_from', 'date_to', 'possible_outcome')
    list_filter = ('date_from', 'date_to')
    search_fields = ('user__username', 'company_name', 'purpose')
    readonly_fields = ('user',)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return self.readonly_fields
        return self.readonly_fields + ('date_from', 'date_to')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(InternationalInternship)
class InternationalInternshipAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'student_name', 'user', 'host_institution', 'city_country', 'period_duration')
    search_fields = ('reg_no', 'student_name', 'mentor_name', 'host_institution', 'user__username')
    list_filter = ('city_country', 'user')

@admin.register(StudentSeedMoney)
class StudentSeedMoneyAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'reg_no', 'project_title', 'amount_sanctioned', 'letter_no_and_date', 'period')
    search_fields = ('student_name', 'reg_no', 'project_title')
    list_filter = ('period',)
    readonly_fields = ('user',)

    def has_delete_permission(self, request, obj=None):
        # Disable delete permission for the admin
        return False

    def has_add_permission(self, request):
        # Disable add permission for the admin
        return False

    def save_model(self, request, obj, form, change):
        # Set the user field to the current user before saving the object
        obj.user = request.user
        super().save_model(request, obj, form, change)

from django.contrib import admin
from .models import ProductDevelopedByStudent

@admin.register(ProductDevelopedByStudent)
class ProductDevelopedByStudentAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'student_name', 'product_name', 'area_of_application')
    search_fields = ('reg_no', 'student_name', 'product_name')
    list_filter = ('area_of_application',)

@admin.register(StudentStartup)
class StudentStartupAdmin(admin.ModelAdmin):
    list_display = ('startup_title', 'student_details', 'registration_info')
    search_fields = ('startup_title', 'student_details', 'investors')
    list_filter = ('registration_info',)

@admin.register(CompetitiveExamSuccess)
class CompetitiveExamSuccessAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'reg_no', 'year', 'roll_no', 'exam_type')
    list_filter = ('exam_type', 'year')
    search_fields = ('student_name', 'reg_no', 'roll_no')
    
@admin.register(StudentEventParticipation)
class StudentEventParticipationAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'reg_no', 'activity', 'host_institute', 'city', 'country', 'date_from', 'date_to', 'award')
    list_filter = ('activity', 'country', 'date_from')
    search_fields = ('student_name', 'reg_no', 'host_institute', 'city', 'country')
    date_hierarchy = 'date_from'
    
    fieldsets = (
        (None, {
            'fields': ('user', 'reg_no', 'student_name', 'activity')
        }),
        ('Event Details', {
            'fields': ('host_institute', 'city', 'country', 'date_from', 'date_to')
        }),
        ('Outcomes', {
            'fields': ('award', 'proof')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('reg_no', 'student_name')
        return ()

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(StudentCoCurricularParticipation)
class StudentCoCurricularParticipationAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'reg_no', 'activity', 'host_institute', 'city', 'country', 'award')
    list_filter = ('activity', 'country')
    search_fields = ('student_name', 'reg_no', 'host_institute', 'city', 'country')
    
    fieldsets = (
        (None, {
            'fields': ('user', 'reg_no', 'student_name', 'activity')
        }),
        ('Event Details', {
            'fields': ('host_institute', 'city', 'country')
        }),
        ('Outcomes', {
            'fields': ('award', 'proof')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('reg_no', 'student_name')
        return ()

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(StudentSportsParticipation)
class StudentSportsParticipationAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'reg_no', 'sports_event', 'organizing_institution', 'city', 'country', 'date_from', 'date_to')
    search_fields = ('student_name', 'reg_no', 'sports_event', 'organizing_institution')
    list_filter = ('country', 'date_from', 'date_to')

@admin.register(NCCParticipation)
class NCCParticipationAdmin(admin.ModelAdmin):
    list_display = ('cadet_name', 'rank', 'participation_type', 'award', 'date_from', 'date_to')
    list_filter = ('participation_type', 'rank')
    search_fields = ('cadet_name', 'rank', 'award')
    ordering = ('-date_from',)  # Orders by date_from in descending order
    date_hierarchy = 'date_from'  # Allows filtering by date in the admin interface

    # To customize the form layout
    fieldsets = (
        (None, {
            'fields': ('cadet_name', 'rank', 'participation_type', 'award', 'proof', 'date_from', 'date_to')
        }),
    )
    # Exclude proof field from the add form if you don't want to handle file uploads here
    # exclude = ('proof',)

    # Make sure to add readonly fields if you do not want them to be editable
    readonly_fields = ('proof',)

    def save_model(self, request, obj, form, change):
        # If you need custom save logic
        super().save_model(request, obj, form, change)

@admin.register(IndustrialVisit)
class IndustrialVisitAdmin(admin.ModelAdmin):
    list_display = ('place_of_visit', 'date_from', 'date_to', 'number_of_students')
    list_filter = ('date_from', 'date_to')
    search_fields = ('place_of_visit', 'faculty_members', 'outcome')
    date_hierarchy = 'date_from'
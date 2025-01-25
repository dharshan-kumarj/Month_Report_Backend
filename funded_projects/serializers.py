from rest_framework import serializers
from .models import AlumniInteraction, BookChapter, CommunitySpiritualActivity, CompanyVisit, CompetitiveExamSuccess, ConferenceProceeding, ConsultancyProject, FacultyEventParticipation, FacultyEventParticipationOffCampus, FacultyMoocCourse, FundedProject, FundedProjectSanctioned, GuestLecture, IncomeGeneratedProgram, IndustrialVisit, InternationalInternship, NCCParticipation, Patent, PlacementHigherStudiesEntrepreneurship, ProductDevelopedByStudent, ProgramOrganized, SeedMoney, Startup, ScopusWosPublication, StudentCoCurricularParticipation, StudentEventParticipation, StudentSeedMoney, StudentSportsParticipation, StudentStartup
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FundedProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = FundedProject
        fields = '__all__'

class FundedProjectSanctionedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = FundedProjectSanctioned
        fields = '__all__'
        read_only_fields = ('user',) 

class ConsultancyProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ConsultancyProject
        fields = '__all__'

class SeedMoneySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = SeedMoney
        fields = '__all__'
        read_only_fields = ('user',)

class PatentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Patent
        fields = '__all__'
        read_only_fields = ('user',)

class StartupSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Startup
        fields = '__all__'
        read_only_fields = ('user',)

class ScopusWosPublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ScopusWosPublication
        fields = '__all__'
        read_only_fields = ('user',)

class BookChapterSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BookChapter
        fields = '__all__'
        read_only_fields = ('user',)

class ConferenceProceedingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ConferenceProceeding
        fields = '__all__'
        read_only_fields = ('user',)

class GuestLectureSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = GuestLecture
        fields = '__all__'
        read_only_fields = ('user',)

class FacultyEventParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = FacultyEventParticipation
        fields = '__all__'
        read_only_fields = ('user',)

class FacultyEventParticipationOffCampusSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = FacultyEventParticipationOffCampus
        fields = '__all__'
        read_only_fields = ('user',)

class ProgramOrganizedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ProgramOrganized
        fields = '__all__'
        read_only_fields = ('user',)

class IncomeGeneratedProgramSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = IncomeGeneratedProgram
        fields = '__all__'
        read_only_fields = ('user',)

class AlumniInteractionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AlumniInteraction
        fields = '__all__'
        read_only_fields = ('user',)

class FacultyMoocCourseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = FacultyMoocCourse
        fields = '__all__'
        read_only_fields = ('user',)

class PlacementHigherStudiesEntrepreneurshipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = PlacementHigherStudiesEntrepreneurship
        fields = '__all__'
        read_only_fields = ('user',)

class CommunitySpiritualActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = CommunitySpiritualActivity
        fields = '__all__'
        read_only_fields = ('user',)

class CompanyVisitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = CompanyVisit
        fields = '__all__'
        read_only_fields = ('user',)

class InternationalInternshipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = InternationalInternship
        fields = '__all__'
        read_only_fields = ('user',)

class StudentSeedMoneySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StudentSeedMoney
        fields = '__all__'
        read_only_fields = ('user',)

class ProductDevelopedByStudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ProductDevelopedByStudent
        fields = '__all__'
        read_only_fields = ('user',)

class StudentStartupSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StudentStartup
        fields = '__all__'
        read_only_fields = ('user',)

class CompetitiveExamSuccessSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = CompetitiveExamSuccess
        fields = '__all__'
        read_only_fields = ('user',)

class StudentEventParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StudentEventParticipation
        fields = '__all__'

class StudentCoCurricularParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StudentCoCurricularParticipation
        fields = '__all__'

class StudentSportsParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StudentSportsParticipation
        fields = '__all__'

class NCCParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = NCCParticipation
        fields = '__all__'

class IndustrialVisitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = IndustrialVisit
        fields = '__all__'
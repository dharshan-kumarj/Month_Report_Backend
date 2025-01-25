from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import AlumniInteraction, BookChapter, CommunitySpiritualActivity, CompanyVisit, CompetitiveExamSuccess, ConferenceProceeding, ConsultancyProject, FacultyEventParticipation, FacultyEventParticipationOffCampus, FacultyMoocCourse, FundedProject, FundedProjectSanctioned, GuestLecture, IncomeGeneratedProgram, IndustrialVisit, InternationalInternship, NCCParticipation, Patent, PlacementHigherStudiesEntrepreneurship, ProductDevelopedByStudent, ProgramOrganized, ScopusWosPublication, SeedMoney, Startup, StudentCoCurricularParticipation, StudentEventParticipation, StudentSeedMoney, StudentSportsParticipation, StudentStartup
from .serializers import AlumniInteractionSerializer, BookChapterSerializer, CommunitySpiritualActivitySerializer, CompanyVisitSerializer, CompetitiveExamSuccessSerializer, ConferenceProceedingSerializer, ConsultancyProjectSerializer, FacultyEventParticipationOffCampusSerializer, FacultyEventParticipationSerializer, FacultyMoocCourseSerializer, FundedProjectSerializer, FundedProjectSanctionedSerializer, GuestLectureSerializer, IncomeGeneratedProgramSerializer, IndustrialVisitSerializer, InternationalInternshipSerializer, NCCParticipationSerializer, PatentSerializer, PlacementHigherStudiesEntrepreneurshipSerializer, ProductDevelopedByStudentSerializer, ProgramOrganizedSerializer, ScopusWosPublicationSerializer, SeedMoneySerializer, StartupSerializer, StudentCoCurricularParticipationSerializer, StudentEventParticipationSerializer, StudentSeedMoneySerializer, StudentSportsParticipationSerializer, StudentStartupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class FundedProjectViewSet(viewsets.ModelViewSet):
    queryset = FundedProject.objects.all()
    serializer_class = FundedProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FundedProjectViewSet(viewsets.ModelViewSet):
    queryset = FundedProject.objects.all()
    serializer_class = FundedProjectSerializer

class FundedProjectSanctionedViewSet(viewsets.ModelViewSet):
    queryset = FundedProjectSanctioned.objects.all()
    serializer_class = FundedProjectSanctionedSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ConsultancyProjectViewSet(viewsets.ModelViewSet):
    queryset = ConsultancyProject.objects.all()
    serializer_class = ConsultancyProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SeedMoneyViewSet(viewsets.ModelViewSet):
    queryset = SeedMoney.objects.all()
    serializer_class = SeedMoneySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatentViewSet(viewsets.ModelViewSet):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
def project_list(request):
    projects = FundedProject.objects.all()
    return render(request, 'funded_projects/project_list.html', {'projects': projects})


class ScopusWosPublicationViewSet(viewsets.ModelViewSet):
    queryset = ScopusWosPublication.objects.all()
    serializer_class = ScopusWosPublicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookChapterViewSet(viewsets.ModelViewSet):
    queryset = BookChapter.objects.all()
    serializer_class = BookChapterSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ConferenceProceedingViewSet(viewsets.ModelViewSet):
    queryset = ConferenceProceeding.objects.all()
    serializer_class = ConferenceProceedingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GuestLectureViewSet(viewsets.ModelViewSet):
    queryset = GuestLecture.objects.all()
    serializer_class = GuestLectureSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FacultyEventParticipationViewSet(viewsets.ModelViewSet):
    queryset = FacultyEventParticipation.objects.all()
    serializer_class = FacultyEventParticipationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FacultyEventParticipationOffCampusViewSet(viewsets.ModelViewSet):
    queryset = FacultyEventParticipationOffCampus.objects.all()
    serializer_class = FacultyEventParticipationOffCampusSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProgramOrganizedViewSet(viewsets.ModelViewSet):
    queryset = ProgramOrganized.objects.all()
    serializer_class = ProgramOrganizedSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IncomeGeneratedProgramViewSet(viewsets.ModelViewSet):
    queryset = IncomeGeneratedProgram.objects.all()
    serializer_class = IncomeGeneratedProgramSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlumniInteractionViewSet(viewsets.ModelViewSet):
    queryset = AlumniInteraction.objects.all()
    serializer_class = AlumniInteractionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FacultyMoocCourseViewSet(viewsets.ModelViewSet):
    queryset = FacultyMoocCourse.objects.all()
    serializer_class = FacultyMoocCourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlacementHigherStudiesEntrepreneurshipViewSet(viewsets.ModelViewSet):
    queryset = PlacementHigherStudiesEntrepreneurship.objects.all()
    serializer_class = PlacementHigherStudiesEntrepreneurshipSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommunitySpiritualActivityViewSet(viewsets.ModelViewSet):
    queryset = CommunitySpiritualActivity.objects.all()
    serializer_class = CommunitySpiritualActivitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompanyVisitViewSet(viewsets.ModelViewSet):
    queryset = CompanyVisit.objects.all()
    serializer_class = CompanyVisitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InternationalInternshipViewSet(viewsets.ModelViewSet):
    queryset = InternationalInternship.objects.all()
    serializer_class = InternationalInternshipSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentSeedMoneyViewSet(viewsets.ModelViewSet):
    queryset = StudentSeedMoney.objects.all()
    serializer_class = StudentSeedMoneySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductDevelopedByStudentViewSet(viewsets.ModelViewSet):
    queryset = ProductDevelopedByStudent.objects.all()
    serializer_class = ProductDevelopedByStudentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentStartupViewSet(viewsets.ModelViewSet):
    queryset = StudentStartup.objects.all()
    serializer_class = StudentStartupSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompetitiveExamSuccessViewSet(viewsets.ModelViewSet):
    queryset = CompetitiveExamSuccess.objects.all()
    serializer_class = CompetitiveExamSuccessSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentEventParticipationViewSet(viewsets.ModelViewSet):
    queryset = StudentEventParticipation.objects.all()
    serializer_class = StudentEventParticipationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentCoCurricularParticipationViewSet(viewsets.ModelViewSet):
    queryset = StudentCoCurricularParticipation.objects.all()
    serializer_class = StudentCoCurricularParticipationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentSportsParticipationViewSet(viewsets.ModelViewSet):
    queryset = StudentSportsParticipation.objects.all()
    serializer_class = StudentSportsParticipationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NCCParticipationViewSet(viewsets.ModelViewSet):
    queryset = NCCParticipation.objects.all()
    serializer_class = NCCParticipationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IndustrialVisitViewSet(viewsets.ModelViewSet):
    queryset = IndustrialVisit.objects.all()
    serializer_class = IndustrialVisitSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
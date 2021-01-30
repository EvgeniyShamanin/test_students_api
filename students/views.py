from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Student
from .serializers import StudentSerializer


# Create your views here.


class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"students": serializer.data})

    def post(self, request):
        student = request.data.get('student')
        # Create an article from the above data
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response({"success": "Студент '{}' created successfully".format(student_saved)})

    def put(self, request, pk):
        saved_student = get_object_or_404(Student.objects.all(), pk=pk)
        data = request.data.get('student')
        serializer = StudentSerializer(instance=saved_student, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response({
            "success": "Студент '{}' updated successfully".format(student_saved)
        })

    def delete(self, request, pk):
        # Get object with this pk
        student = get_object_or_404(Student.objects.all(), pk=pk)
        student.delete()
        return Response({
            "message": "Студент with id `{}` has been deleted.".format(pk)
        }, status=204)


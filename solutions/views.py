from django.shortcuts import render

from solutions.models import Solution

# Create your views here.


def cc_python(request):
	question = Solution.objects.all()
	return render(request, 'solutions/cc-python.html', {'questions': question})


from django.shortcuts import render

def exam_1(request):
    start = int(request.POST.get('start', 0))
    end = int(request.POST.get('end', 0))

    result = sum(range(start, end + 1 ))
    context = {'result': result}
    return render(request, 'exam/exam_1.html', context)
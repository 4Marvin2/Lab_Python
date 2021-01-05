from django.shortcuts import get_list_or_404, render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Exam, Group, Schedule


def index(request):
    group_list = Group.objects.all()
    exam_list = Exam.objects.all()
    context = {'group_list': group_list, 'exam_list': exam_list}
    return render(request, 'schedule/index.html', context)


def detail_student(request, group_id):
    group_list = Group.objects.all()
    for i in group_list:
        if i.id == group_id:
            group = i
    schedule_list = get_list_or_404(Schedule, group=group_id)
    for i in range(len(schedule_list) - 1):
        for j in range(len(schedule_list) - i - 1):
            if schedule_list[j].lesson_time > schedule_list[j + 1].lesson_time:
                schedule_list[j], schedule_list[j + 1] = schedule_list[j + 1], schedule_list[j]
    exam_list = []
    for i in schedule_list:
        exam_list.append(i.lesson)
    return render(request, 'schedule/detail_student.html', {'group': group,
                                                            'schedule_list': schedule_list,
                                                            'exam_list': exam_list})


def detail_lecturer(request, name):
    exam_list = Exam.objects.all()
    for i in exam_list:
        if i.lecturer == name:
            exam = i
    schedule_list = get_list_or_404(Schedule, lesson=exam)
    for i in range(len(schedule_list) - 1):
        for j in range(len(schedule_list) - i - 1):
            if schedule_list[j].lesson_time > schedule_list[j + 1].lesson_time:
                schedule_list[j], schedule_list[j + 1] = schedule_list[j + 1], schedule_list[j]
    group_list = []
    for i in schedule_list:
        group_list.append(i.group)
    schedule_data_list = []
    count = 1
    exam_count = [1]
    for schedule in schedule_list:
        current_date_str = str(schedule.lesson_time)
        current_date = current_date_str.split(' ')
        if len(schedule_data_list) != 0:
            if current_date[0] == schedule_data_list[-1]:
                exam_count[-1] += 1
            else:
                exam_count.append(count)
                count = 1
                schedule_data_list.append(current_date[0])
        else:
            schedule_data_list.append(current_date[0])
    if request.method == "POST":
        exam.name = request.POST.get("exam_name")
        exam.save()
        name_group_change = request.POST.get("group_name")
        for group in group_list:
            if group.name == name_group_change:
                group_change = group
                break
        for schedule in schedule_list:
            if schedule.group == group_change:
                schedule.lesson_time = request.POST.get("lesson_time")
                schedule.save()
        return HttpResponseRedirect(f"/schedule/{name}")
    else:
        return render(request, 'schedule/detail_lecturer.html', {'group_list': group_list,
                                                                 'schedule_list': schedule_list,
                                                                 'exam': exam,
                                                                 'schedule_date_list': schedule_data_list,
                                                                 'exam_count': exam_count})

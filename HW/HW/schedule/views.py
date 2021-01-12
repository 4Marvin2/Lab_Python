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
    # for exam in exam_list:
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

    # формируем листы дат консультаций и экзаменов
    # а также формируем листы количества консультаций и экзаменов в датологическом порядке
    schedule_exam_data_list = []
    schedule_cons_data_list = []
    count_ex = 1
    count_cons = 1
    cons_count = [1]
    exam_count = [1]
    for schedule in schedule_list:
        current_exam_date_str = str(schedule.lesson_time)
        current_cons_date_str = str(schedule.consultation_time)
        current_exam_date = current_exam_date_str.split(' ')
        current_cons_date = current_cons_date_str.split(' ')
        if len(schedule_exam_data_list) != 0:
            if current_exam_date[0] == schedule_exam_data_list[-1]:
                exam_count[-1] += 1
            else:
                exam_count.append(count_ex)
                count_ex = 1
                schedule_exam_data_list.append(current_exam_date[0])
        else:
            schedule_exam_data_list.append(current_exam_date[0])
        if len(schedule_cons_data_list) != 0:
            if current_cons_date[0] == schedule_cons_data_list[-1]:
                cons_count[-1] += 1
            else:
                cons_count.append(count_cons)
                count_cons = 1
                schedule_cons_data_list.append(current_cons_date[0])
        else:
            schedule_cons_data_list.append(current_cons_date[0])

    # создаем полный лист дат для графика
    schedule_data_list = []
    i = j = 0
    while (i < len(schedule_exam_data_list)) and (j < len(schedule_cons_data_list)):
        if schedule_exam_data_list[i] < schedule_cons_data_list[j]:
            schedule_data_list.append(schedule_exam_data_list[i])
            i += 1
        else:
            schedule_data_list.append(schedule_cons_data_list[j])
            j += 1
    while i < len(schedule_exam_data_list):
        schedule_data_list.append(schedule_exam_data_list[i])
        i += 1
    while j < len(schedule_cons_data_list):
        schedule_data_list.append(schedule_cons_data_list[j])
        j += 1

    # определяем кол-во консультаций и экзаменов в каждую из дат
    i = 0
    for i in range(len(schedule_data_list)):
        if schedule_data_list[i] not in schedule_exam_data_list:
            j = 0
            for date in schedule_exam_data_list:
                if schedule_data_list[i] < date:
                    schedule_exam_data_list.append('0')
                    k = len(schedule_exam_data_list) - 2
                    while k >= j:
                        schedule_exam_data_list[k + 1] = schedule_exam_data_list[k]
                        k -= 1
                    schedule_exam_data_list[j] = schedule_data_list[i]
                    break
                else:
                    j += 1
            exam_count.append(0)
            k = len(exam_count) - 2
            while k >= j:
                exam_count[k + 1] = exam_count[k]
                k -= 1
            exam_count[j] = 0
        i += 2
    i = 1
    for i in range(len(schedule_data_list)):
        if schedule_data_list[i] not in schedule_cons_data_list:
            j = 0
            for date in schedule_cons_data_list:
                if schedule_data_list[i] < date:
                    schedule_cons_data_list.append('0')
                    k = len(schedule_cons_data_list) - 2
                    while k >= j:
                        schedule_cons_data_list[k + 1] = schedule_cons_data_list[k]
                        k -= 1
                    schedule_cons_data_list[j] = schedule_data_list[i]
                    break
                else:
                    j += 1
            cons_count.append(0)
            k = len(cons_count) - 2
            while k >= j:
                cons_count[k + 1] = cons_count[k]
                k -= 1
            cons_count[j] = 0
        i += 2

    # убираем повторные даты
    i = 0
    schedule_data_list_no_repetitions = []
    for i in range(len(schedule_data_list) - 1):
        if schedule_data_list[i] != schedule_data_list[i + 1]:
            schedule_data_list_no_repetitions.append(schedule_data_list[i])
            if i == len(schedule_data_list) - 2:
                schedule_data_list_no_repetitions.append(schedule_data_list[i + 1])
            i += 1
            continue

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
                schedule.consultation_time = request.POST.get("consultation_time")
                schedule.save()
        return HttpResponseRedirect(f"/schedule/{name}")
    else:
        return render(request, 'schedule/detail_lecturer.html', {'group_list': group_list,
                                                                 'schedule_list': schedule_list,
                                                                 'exam': exam,
                                                                 'schedule_date_list': schedule_data_list_no_repetitions,
                                                                 'exam_count': exam_count,
                                                                 'cons_count': cons_count})

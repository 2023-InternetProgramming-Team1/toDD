from django.shortcuts import render

from datetime import datetime, timedelta

# Create your views here.
def login(request):
    return render(
        request,
        'join/login.html',
    )

def account(request):
    return render(
        request,
        'join/account.html',
    )

def mypage(request):
    today = datetime.now()
    current_weekday = today.weekday()

    # 현재 날짜에서 현재 요일을 기준으로 월요일을 계산
    monday_of_current_week = today - timedelta(days=current_weekday)

    # 각각의 날짜 변수에 값을 할당
    monday = monday_of_current_week.strftime('%m/%d')
    tuesday = (monday_of_current_week + timedelta(days=1)).strftime('%m/%d')
    wednesday = (monday_of_current_week + timedelta(days=2)).strftime('%m/%d')
    thursday = (monday_of_current_week + timedelta(days=3)).strftime('%m/%d')
    friday = (monday_of_current_week + timedelta(days=4)).strftime('%m/%d')
    saturday = (monday_of_current_week + timedelta(days=5)).strftime('%m/%d')
    sunday = (monday_of_current_week + timedelta(days=6)).strftime('%m/%d')

    # Django의 context에 결과를 저장
    context = {
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,
    }

    return render(
        request,
        'join/mypage.html',
        context
    )


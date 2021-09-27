
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# 진원님 코드 추가
def home(request):
    """
    pybo HOME 출력
    """
    return render(request, 'security_portal/home_ik.html')
# 진원님 코드 종료

def index(request):
    """
    security_portal 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'security_portal/question_list.html', context)

def detail(request, question_id):
    """
    security_portal 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'security_portal/question_detail.html', context)

def answer_create(request, question_id):
    """
    security_portal 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('security_portal:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'security_portal/question_detail.html', context)

def question_create(request):
    """
    security_portal 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('security_portal:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'security_portal/question_form.html', context)
from django.shortcuts import render, get_object_or_404

from .forms import AnswerForm
from .models import Question
from ..user_profile import models, forms


# Create your views here.
def question_view(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except models.Profile.DoesNotExist:
            form = forms.ProfileForm(initial={'nick_name': request.user.username})
            return render(request, 'profile/profile.html', {'form': form})

        context = {'completed':False}
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.data.get('answer')
                if answer and answer == profile.current_question.answer:
                    context['result'] = dict(title=answer,image=profile.current_question.image)
                    number = profile.current_question.number + 1
                    profile.marks = profile.marks + profile.current_question.marks
                    if number > len(Question.objects.all()):
                        profile.has_completed = True
                        profile.save()
                        context['completed'] = True
                        return render(request, 'game/result.html', context)
                    else:
                        profile.current_question = Question.objects.get(number=number)
                        profile.save()
                        return render(request, 'game/result.html', context)
                else:
                    context['result'] = dict(title=answer,image=profile.current_question.image)
                    return render(request, 'game/result.html', context)
            else:
                context['form'] = form
                return render(request, 'game/question.html', context)
        else:
            if profile.has_completed:
                return render(request, 'game/end.html')
            if profile.current_question is None:
                queryset = get_object_or_404(Question, number=1)
                profile.current_question = queryset
                profile.save()
            context['question'] = profile.current_question
            context['form'] = AnswerForm()
            return render(request, 'game/question.html', context)

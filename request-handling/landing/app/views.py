from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    ab_test_arg = request.GET.get('from-landing')
    counter_click[ab_test_arg] += 1
    print(counter_click)
    return render('index.html', None)


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test_arg = request.GET.get('ab_test_arg')
    counter_show[ab_test_arg] += 1
    print(counter_show)
    if ab_test_arg == 'original':
        return render('landing.html', None)
    elif ab_test_arg == 'test':
        return render('landing_alternate.html', None)
    else:
        return render('index.html', None)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        original_conversion = counter_click['original']/counter_show['original']
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        original_conversion = 0
    try:
        test_conversion = counter_click['test']/counter_show['test']
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        test_conversion = 0

    return render(None, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })

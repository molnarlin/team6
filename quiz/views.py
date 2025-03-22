from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz

def quiz_list(request):
    # Reset session data when starting a new quiz
    if 'quiz_progress' in request.session:
        del request.session['quiz_progress']
    if 'quiz_results' in request.session:
        del request.session['quiz_results']
    
    # Redirect to the first question
    quizzes = Quiz.objects.all().order_by('id')
    if quizzes:
        return redirect('quiz_question', quiz_id=quizzes.first().id)
    else:
        return render(request, 'no_quizzes.html')

def quiz_question(request, quiz_id):
    # Get the current quiz
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    # Initialize quiz progress in session if not present
    if 'quiz_progress' not in request.session:
        request.session['quiz_progress'] = []
    
    if 'quiz_results' not in request.session:
        request.session['quiz_results'] = []
    
    context = {
        'quiz': quiz,
        'question_number': len(request.session['quiz_progress']) + 1
    }
    
    return render(request, 'quiz_question.html', context)

def quiz_answer(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        selected_option = request.POST.get('answer')
        
        # Get the text of the selected option
        if selected_option == 'option1':
            selected_option_text = quiz.option1
        elif selected_option == 'option2':
            selected_option_text = quiz.option2
        elif selected_option == 'option3':
            selected_option_text = quiz.option3
        elif selected_option == 'option4':
            selected_option_text = quiz.option4
        else:
            selected_option_text = "No option selected"
        
        # Get the text of the correct option (handle both formats)
        if quiz.answer == 'option1':
            correct_option_text = quiz.option1
        elif quiz.answer == 'option2':
            correct_option_text = quiz.option2
        elif quiz.answer == 'option3':
            correct_option_text = quiz.option3
        elif quiz.answer == 'option4':
            correct_option_text = quiz.option4
        else:
            # If the answer is stored as the text instead of the option identifier
            correct_option_text = quiz.answer
        
        # Check if the answer is correct - handle both formats
        if quiz.answer in ['option1', 'option2', 'option3', 'option4']:
            # Standard format - compare option identifiers
            is_correct = selected_option == quiz.answer
        else:
            # Text-based format - compare the selected text with the stored answer
            is_correct = selected_option_text == quiz.answer
        
        # Store the result in session
        if 'quiz_progress' not in request.session:
            request.session['quiz_progress'] = []
        
        if 'quiz_results' not in request.session:
            request.session['quiz_results'] = []
        
        request.session['quiz_progress'].append(quiz.id)
        
        result = {
            'quiz_id': quiz.id,
            'question': quiz.question,
            'selected_option': selected_option,
            'selected_text': selected_option_text,
            'correct_text': correct_option_text,
            'is_correct': is_correct
        }
        
        request.session['quiz_results'].append(result)
        request.session.modified = True
        
        # Calculate current score
        current_score = sum(1 for result in request.session['quiz_results'] if result['is_correct'])
        
        # Find the next quiz that hasn't been answered yet
        next_quiz = Quiz.objects.exclude(id__in=request.session['quiz_progress']).order_by('id').first()
        
        if next_quiz:
            # Show feedback for current answer and link to next question
            context = {
                'quiz': quiz,
                'selected_option_text': selected_option_text,
                'correct_option_text': correct_option_text,
                'is_correct': is_correct,
                'next_quiz': next_quiz,
                'question_number': len(request.session['quiz_progress']),
                'current_score': current_score
            }
            
            return render(request, 'quiz_answer.html', context)
        else:
            # All questions have been answered, show final results
            return redirect('quiz_results')
    
    return redirect('quiz_question', quiz_id=quiz_id)

def quiz_results(request):
    # Get results from session
    if 'quiz_results' not in request.session:
        return redirect('quiz_list')
    
    results = request.session['quiz_results']
    
    # Count correct answers
    correct_count = sum(1 for result in results if result['is_correct'])
    total_questions = len(results)
    
    # Calculate percentage score
    percentage = round((correct_count / total_questions) * 100) if total_questions > 0 else 0
    
    context = {
        'results': results,
        'correct_count': correct_count,
        'total_questions': total_questions,
        'percentage': percentage
    }
    
    # Clear session data
    if 'quiz_progress' in request.session:
        del request.session['quiz_progress']
    if 'quiz_results' in request.session:
        del request.session['quiz_results']
    
    return render(request, 'quiz_results.html', context)

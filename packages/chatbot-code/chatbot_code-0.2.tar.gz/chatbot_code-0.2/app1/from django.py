from django.shortcuts import render,redirect,get_object_or_404
from .models import UploadedFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from .models import ChatSession,Feedback

from sklearn.metrics.pairwise import cosine_similarity,euclidean_distances

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import inflect
nltk.download('punkt')
nltk.download('wordnet')
import re
from sentence_transformers import SentenceTransformer
from .forms import QnAForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from django.utils.crypto import get_random_string
from django.utils import timezone
import uuid 
import openai
import fitz
# Download necessary NLTK data (if not already done)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']

        # Save the uploaded file to the database
        uploaded_file_obj = UploadedFile(file=uploaded_file)
        uploaded_file_obj.save()

        return redirect('chat')  # Redirect to the chat page after uploading the file

    return render(request, 'upload_file.html')



def clear_all_sessions(request):
    

    request.session.flush()
    return HttpResponse("All sessions have been cleared.")





class CustomLoginView(LoginView):
    template_name = "admin_login.html"  # Use your login template
    redirect_authenticated_user = (
        True  # Redirect logged-in users away from the login page
    )

    def get_success_url(self):
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            return reverse_lazy("dashboard")
        else:
            return reverse_lazy("unauthorised")

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)




@login_required(login_url='/admin_login/')
def dashboard_view(request):
    
    if not request.user.is_superuser:
        return redirect("unauthorised")
    
    all_entries = ChatSession.objects.all().order_by('-session_start_time')
    answers_by_user = {}
    
    for entry in all_entries:
        user_id = entry.user_identifier
        
        if user_id not in answers_by_user:
            answers_by_user[user_id] = {'answers': []}
        
        answers_by_user[user_id]['answers'].append(entry)
    
    context = {
        'answers_by_user': answers_by_user
    }
    
    return render(request, 'dashboard.html', context)


def qna_create(request):
    if request.method == 'POST':
        form = QnAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = QnAForm()  # Initialize the form for GET requests
    return render(request, 'qna_form.html', {'form': form})

def qna_update(request, pk):
    qna = get_object_or_404(ChatSession, pk=pk)
    if request.method == 'POST':
        form = QnAForm(request.POST, instance=qna)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = QnAForm(instance=qna)
    return render(request, 'qna_form.html', {'form': form, 'qna': qna}) 



def qna_delete(request, pk):
    qna = get_object_or_404(ChatSession, pk=pk)
    if request.method == 'POST':  # Corrected 'methos' to 'method'
        qna.delete()
        return redirect('dashboard')
    return render(request, 'qna_confirm_delete.html', {'qna': qna})

from django.contrib.auth.models import User

@login_required
def verify_question(request, session_id):
    session = get_object_or_404(ChatSession, session_id=session_id)
    user = request.user
    if user not in session.verified_by.all():
        session.verification_count += 1
        session.verified_by.add(user)
        session.save()
        return JsonResponse({'message': 'Verification successful'})
    else:
        return JsonResponse({'message': 'Already verified by this user'})





def extract_keywords(question):
    # Tokenize the question to get a list of words
    words = word_tokenize(question)

    # Remove stop words
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]

    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize the words to get their base form
    keywords = [lemmatizer.lemmatize(word) for word in filtered_words]
    print('keywords',keywords)

    return keywords

def find_relevant_text(document_text, keywords):
    paragraphs = document_text.split('\n\n')  # Splitting document into paragraphs
    relevant_paragraphs = []
    for paragraph in paragraphs:
        if any(keyword.lower() in paragraph.lower() for keyword in keywords):
            relevant_paragraphs.append(paragraph)
            # print(relevant_paragraphs)
    return " ".join(relevant_paragraphs)[:4097]  # Limiting to 69000 characters


@csrf_exempt
# views.py
 # Import the uuid module for generating unique identifiers

@csrf_exempt
# views.py
def chat(request):
    if request.method == 'POST':
        # Generate a unique user identifier if it doesn't exist in the session
        if 'user_identifier' not in request.session:
            user_identifier = f"ch-{uuid.uuid4().hex[:2]}"  # Combine prefix 'ch-' with a random unique identifier
            request.session['user_identifier'] = user_identifier
        else:
            user_identifier = request.session['user_identifier']

        # Retrieve session_start_time from the session or generate a new one
        session_start_time = request.session.get('session_start_time')
        if not session_start_time:
            session_start_time = timezone.now()
            request.session['session_start_time'] = session_start_time.strftime("%Y-%m-%d %H:%M:%S")

        # Generate a unique session ID for each chat session
        # session_id = get_random_string(4)
        session_id = f"{user_identifier}.{uuid.uuid4().hex[:2]}"

        question = request.POST.get('question', '')
        if not question:
            return HttpResponseBadRequest('Missing or empty "question" parameter in the request.')

        existing_answer = get_answer_from_database(question)
        if existing_answer:
            return JsonResponse({'answer': existing_answer, 'source': 'database'})

        dir_path = os.path.dirname(os.path.realpath(__file__))
        document_path = os.path.join(dir_path, 'innohealth.pdf')
        
        with fitz.open(document_path) as doc:
            document_text = " ".join(page.get_text() for page in doc)

        keywords = extract_keywords(question)
        relevant_text = find_relevant_text(document_text, keywords)

        openai.api_key = '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'
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Keep the answer as concise as possible. If you don't know the answer, just say i dont know dont try to make up an answer. Respond in common words so that usage of tokens is reduced ."},
                    {"role": "user", "content": relevant_text},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[-1].message['content'].strip()
            print(answer)
        except Exception as e:
            return JsonResponse({'error': str(e)})

        save_to_database(question, answer, user_identifier, session_id, session_start_time)
        return JsonResponse({'answer': answer, 'source': 'llm'})
    else:
        return render(request, 'chat.html', {'error': 'Invalid request method.'})





def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    p = inflect.engine()

    def convert_number_to_words(token):
        if token.isdigit():
            return p.number_to_words(token)
        else:
            return token

    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(convert_number_to_words(token.lower())) for token in tokens]
    # print('lemmatized_tokens',lemmatized_tokens)
    return ' '.join(lemmatized_tokens)



def extract_session_number(question):
    # Extracting session number from the question
    match = re.search(r'session\s*(\d+)', question, re.IGNORECASE)
    # print('match',match)
    return int(match.group(1)) if match else None

def get_answer_from_database(question):
    try:
        all_entries = ChatSession.objects.all()
        
        if not all_entries:
            return None  # No questions in the database, return None
        
        current_question_session_number = extract_session_number(question)
        processed_current_question = preprocess_text(question)
        # print('processed_current_questions',processed_current_question)

        # Filter entries by session number if present
        relevant_entries = [entry for entry in all_entries if extract_session_number(entry.question) == current_question_session_number]
        # print('relevant_entries',relevant_entries)

        if not relevant_entries:
            return None  # No relevant entries found for the specific session

        processed_questions = [preprocess_text(entry.question) for entry in relevant_entries]
        processed_questions.append(processed_current_question)  # Adding the current question for similarity comparison
        # print('processed_questions',processed_questions)

        # Use SentenceTransformer for creating embeddings
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        question_embeddings = model.encode(processed_questions, convert_to_tensor=True)

        # Convert embeddings to NumPy arrays for similarity calculation
        question_embeddings_np = [embedding.cpu().detach().numpy() for embedding in question_embeddings]

        # Calculate cosine similarities
        similarities = cosine_similarity([question_embeddings_np[-1]], question_embeddings_np[:-1])
        # print('similarities',similarities)

        # Find the most similar question
        most_similar_index = similarities.argmax()
        most_similar_answer = relevant_entries[most_similar_index].answer

        # Adjust similarity threshold based on context
        similarity_threshold = 0.8 if 'session' in processed_current_question else 0.8

        if similarities[0][most_similar_index] >= similarity_threshold:
            retrieved_entry = relevant_entries[most_similar_index]
            retrieved_entry.retrieval_count += 1
            retrieved_entry.save() 
            return most_similar_answer
        else:
            return None

    except ChatSession.DoesNotExist:
        return None




# def save_to_database(question, answer, user_identifier, session_id):
#     ChatSession.objects.create(question=question, answer=answer, user_identifier=user_identifier, session_id=session_id)
    

# views.py
from datetime import datetime



def save_to_database(question, answer, user_identifier, session_id, session_start_time):
    current_time = datetime.now()
    ChatSession.objects.create(
        session_id=session_id,
        session_start_time=session_start_time,
        question=question,
        question_asked_time=current_time,
        answer=answer,
        user_identifier=user_identifier
    )


import json
@csrf_exempt
def submit_feedback(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))  # Ensure decoding of the body
            question = data.get('question')
            answer = data.get('answer')
            feedback = data.get('feedback')
            
            # Convert feedback to boolean
            if feedback.lower() == "positive":
                feedback_bool = True
            else:
                feedback_bool = False

            print('question :',question)
            print('answer :',answer)
            print('feedback : ',feedback)
            Feedback.objects.create(question=question, answer=answer, feedback=feedback_bool)
            
            # Save the feedback to the database here
            
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)














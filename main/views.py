from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

#view to render the index page
from django.shortcuts import render

from django.shortcuts import render
from .models import UserResponse
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from .models import UserResponse

from django.shortcuts import render, redirect
from .models import UserResponse
import requests


def index(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        previous_question = request.POST.get('previous_question')
        session_id = request.session.session_key

        # Save the response
        UserResponse.objects.create(session_id=session_id, question=previous_question, response=user_input)

        # Example logic to determine the next question
        if previous_question == "Describe your project":
            question = "What type of website should it be - Static, Dynamic or E-Commerce?"
        elif previous_question == "What type of website should it be - Static, Dynamic or E-Commerce?":
            question = "Who is your target audience?"
        elif previous_question == "Who is your target audience?":
            question = "What features do you want in your website?"
        else:
            # Render the thank you page and then redirect to the proposal generation view
            return render(request, 'main/thank_you.html')

        context = {'question': question, 'previous_question': question}
        return render(request, 'main/question.html', context)

    context = {'question': "Describe your project", 'previous_question': "Describe your project"}
    return render(request, 'main/index.html', context)

#View to generate proposal using Gemini API

from django.shortcuts import render
from .models import UserResponse
from .gemini_api import generate_proposal_with_gemini
from .docx_generator import generate_docx

def generate_proposal(request):
    session_id = request.session.session_key
    responses = UserResponse.objects.filter(session_id=session_id)

    # Construct the prompt for Gemini API based on the collected responses
    prompt = "Generate a website development proposal based on the following details:\n\n"
    for response in responses:
        prompt += f"{response.question}\n{response.response}\n\n"

    # Add a closing statement to guide the API
    prompt += "Please provide a detailed proposal including the project description, target audience, type of website, and desired features."

    # Generate the proposal using Gemini API
    proposal = generate_proposal_with_gemini(prompt)

    context = {'proposal': proposal}
    return render(request, 'main/proposal.html', context)

def download_proposal(request):
    session_id = request.session.session_key
    responses = UserResponse.objects.filter(session_id=session_id)

    # Construct the prompt for Gemini API based on the collected responses
    prompt = "Generate a website development proposal based on the following details:\n\n"
    for response in responses:
        prompt += f"{response.question}\n{response.response}\n\n"

    # Add a closing statement to guide the API
    prompt += "Please provide a detailed proposal including the project description, target audience, type of website, and desired features."

    # Generate the proposal using Gemini API
    proposal = generate_proposal_with_gemini(prompt)

    # Generate the Word document
    return generate_docx(proposal)



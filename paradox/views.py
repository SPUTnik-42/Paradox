from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import User, question, hint, log, team_member, user_detail
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

"""when you want to prohibit every participitant from accessing this part of the website just apply the staff member 
decorator to each view , this will force out every user but still give access to the staff"""

"""when you want to close registrations apply the staff decorators on the view function so that only staff can access it """

def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            user_data = User.objects.get(username=username)
            request.session['user_id'] = user_data.pk
            request.session['user_lvl'] = user_data.details.level
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    if request.session.get('user_id'):
        del request.session['user_id']
        del request.session['user_lvl']
    else: 
        pass
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        team_name = request.POST["teamName"]
        school = request.POST["school"]
       
        username_p1 = request.POST["username-p1"]
        email_p1 = request.POST["email-p1"]
        class_p1 = request.POST["class-p1"]
       
        username_p2 = request.POST["username-p2"]
        email_p2 = request.POST["email-p2"]
        class_p2 = request.POST["class-p2"]
    
        username_p3 = request.POST["username-p3"]
        email_p3 = request.POST["email-p3"]
        class_p3 = request.POST["class-p3"]
        

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        if school == "The Mother's International School":
            school = "INTRA"
        # Attempt to create new user
        try:
            
            user1 = User.objects.create_user(username_p1, email_p1, password)
            user1.save()
            user2 = User.objects.create_user(username_p2, email_p2, password)
            user2.save()
            user3 = User.objects.create_user(username_p3, email_p3, password)
            user3.save()
            team = team_member(teamName=team_name, alpha=user1, beta=user2, gamma=user3)
            team.save()
            user1_details = user_detail(user=user1, user_class = class_p1,isschool= school, team_members=team)
            user1_details.save()
            user2_details = user_detail(user=user2, user_class = class_p2,isschool= school, team_members=team)
            user2_details.save()
            user3_details = user_detail(user=user3, user_class = class_p3,isschool= school, team_members=team)
            user3_details.save()
            
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "register.html")

@login_required(login_url='/login')
def user_profile(request):
    userID = request.session.get('user_id')
    user_data = User.objects.get(pk=userID)
    
    return render(request, "user_profile.html", {
        "user_data": user_data        
    })

@login_required(login_url='/login')
def question_page(request):
    user_lvl = request.session.get('user_lvl')
    
    question_data = question.objects.get(pk=user_lvl)
    userID = request.session.get('user_id')
    user_data = User.objects.get(pk=userID)
    if user_data.details.disqualified == 0:
        if request.method == "POST":
            answer = question_data.answer
            alt_answer = question_data.alt_answer
            user_ans = request.POST["answer"]
            log_qs = log(username=user_data.username, action=user_ans, category="answer",level = user_data.details.level)
            log_qs.save()

            if user_ans == answer or user_ans == alt_answer:
                team = user_data.details.team_members
                team.level += 1
                team.save()
                team.alpha.details.level += 1
                team.alpha.details.save()
                if team.beta.details.level >= 0 :
                    team.beta.details.level += 1
                    team.beta.details.save()
                if team.gamma.details.level >= 0 :
                    team.gamma.details.level += 1
                    team.gamma.details.save()
                
                print(user_data.details.level)
                request.session['user_lvl'] += 1
                print(request.session.get('user_lvl'))
                return HttpResponseRedirect(reverse("question-page"))
    else:
        return render(request, "question.html", {
            "message": "you have been disqualified",
            "disqualify": 1
        })

    return render(request, "question.html", {
        "question_data": question_data
    })

@login_required(login_url='/login')
def hint_page(request):
    user_lvl = request.session.get('user_lvl')
    try:
        hint_data = hint.objects.get(pk=user_lvl)
        return render(request, "hint.html", {
            "hint_data": hint_data
        })
    except hint.DoesNotExist :
        return render(request, "hint.html")

def leaderboard_page(request):

    user_teams = team_member.objects.order_by("-level").all()

    return render(request,"leaderboard.html", {
        "user_teams" : user_teams
    })

@staff_member_required(login_url="/")
def log_page(request):
    log_data = log.objects.order_by("time").all()

    return render(request, "log.html", {
        "log_data": log_data
    })
@staff_member_required(login_url="/")
def disqualification_page(request):
    
    user_teams = team_member.objects.order_by("level").all()

    return render(request,"disqualify.html", {
        "user_teams" : user_teams
    })

@staff_member_required(login_url="/")
def disqualify(request, user_id):
    user_data = User.objects.get(pk=user_id)
    team = user_data.details.team_members
    team.alpha.details.disqualified = 1
    team.beta.details.disqualified = 1
    team.gamma.details.disqualified = 1

    team.gamma.details.save()
    team.beta.details.save()
    team.alpha.details.save()

    return HttpResponseRedirect(reverse("disqualification-page"))

@staff_member_required(login_url="/")
def un_disqualify(request, user_id):
    user_data = User.objects.get(pk=user_id)
    team = user_data.details.team_members
    team.alpha.details.disqualified = 0
    team.beta.details.disqualified = 0
    team.gamma.details.disqualified = 0

    team.gamma.details.save()
    team.beta.details.save()
    team.alpha.details.save()

    return HttpResponseRedirect(reverse("disqualification-page"))
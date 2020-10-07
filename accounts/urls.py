from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('',views.indexView,name="home"), # We are creating urls for apps
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login_url"),
    path('dashboard1/', views.dashboardView1, name="dashboard1"),
    path('dashboard1/external/', views.external, name="external"),
    path('dashboard/', views.dashboardView, name="examportal"),
    path('examportal/', views.examportalView, name="examportal"),
    path('examportal/exampage/', views.exampageView, name="exampage"),
    path('examportal/exampage/finalpage/', views.multifaceexecute, name="finalpage"),
    path('examportal/exampage/examfinish/', views.cheatindexView, name="examfinish"),

    path('examportal/exampage/finalpage/examfinish/', views.indexView, name="examfinish"),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'),name="logout"),
]



"""
path('output/',views.output,name="script"), can be used

path('examportal/exampage/examfinish/finalpage/', views.cheatindexView, name="examfinish"),
"""

"""
index.html value

<!--


<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Student Exam Portal{% endblock %}</title>
</head>
<body>
  <main>
    {% block content %}
    {% endblock %}
  </main>
</body>
</html>


"""

"""
<!--
login.html value


{% extends 'index.html' %}
{% block title %}
    Home
{% endblock %}
{% block content %}
{% if user.is_authenticated %}
    <div style="text-align:center">
        Hi {{ user.username }}! Welocme to Exam Portal
    </div>
        <p>
            <a href="{% url 'logout' %}">logout</a>
        </p>
{% else %}
  <p>You are not logged in</p>
     <a href="{% url 'login_url' %}">login</a>
{% endif %}
{% endblock %}


-->

"""

"""
dashboard.html value

<!--

{% extends 'index.html' %}
{% block title %}
    Login
{% endblock %}
{% block content %}
    <div style="text-align:center">
        <h2>Login</h2>
    </div>

    <div style="text-align:center">
        <form method="post" id="form_login">
            {% csrf_token %}
                {{ form.as_p }}
            <button type="submit">Login</button>
        </form>
    </div>
{% endblock %}
->
"""


"""
Original login.html

{%extends 'index.html' %}
{% load crispy_forms_tags %}
{%block content%}
    <h1> Exam Portal Login  </h1>
    <form method="POST">
        {%csrf_token%}
        {{ form|crispy}}
        <button> Login </button>
    </form>
{%endblock%}

"""
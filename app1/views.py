from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Job, Application


def home(request):
    user_id = request.session.get("user_id")
    all_jobs = Job.objects.all()

    context = {"jobs": all_jobs, "jobs_count": all_jobs.count()}

    if user_id:
        context["user_id"] = user_id

    return render(request, "index.html", context)


def signup(request):
    if request.method == "POST":

        # errors = User.objects.validate(request.POST)

        # There is some errors
        # if len(errors) > 0:
        #     for error in errors.values():
        #         messages.error(request, error)
        #     return redirect("app1:registration")

        # بنستخرج المدخلات من الفورم
        email_form = request.POST["email"]
        password_form = request.POST["password"]
        confirm_password_form = request.POST["password2"]

        if password_form == confirm_password_form:
            hash_password = bcrypt.hashpw(
                password_form.encode(), bcrypt.gensalt()
            ).decode()

            new_user = User.objects.create(
                email=email_form,
                password=hash_password,
            )

            request.session["user_id"] = new_user.id

            return redirect("app1:home")

        # if password didn't match
        else:
            messages.error(request, "Password not match.")
            return redirect("app1:login_page")


def login_page(request):
    user_id = request.session.get("user_id")
    if user_id:
        return redirect("app1:home")

    context = {"login_page": True}
    return render(request, "login.html", context)


def login(request):
    if request.method == "POST":
        email_form = request.POST["email"]
        password_form = request.POST["password"]

        users = User.objects.filter(email=email_form)

        if len(users) == 0:
            messages.error(request, "Email doesn't exist.")
            return redirect("app1:registration")

        if bcrypt.checkpw(password_form.encode(), users.first().password.encode()):
            request.session["user_id"] = users[0].id

            return redirect("app1:home")
        # if password is wrong
        else:
            messages.error(request, "Password not correct.")
            return redirect("app1:login_page")


def logout(request):
    request.session.flush()
    return redirect("app1:login_page")


def post_job_page(request):
    return render(request, "post-job.html")


def post_job(request):
    form_email = request.POST.get("email", "")
    form_title = request.POST.get("title", "")
    form_location = request.POST.get("location", "")
    form_type = request.POST.get("type", "")
    form_job_description = request.POST.get("job-description", "")
    form_company_name = request.POST.get("company_name", "")
    form_company_description = request.POST.get("company-description", "")
    form_logo = request.FILES.get("logo", "")

    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    Job.objects.create(
        user=user,
        email=form_email,
        title=form_title,
        location=form_location,
        type=form_type,
        description=form_job_description,
        company_name=form_company_name,
        company_description=form_company_description,
        logo=form_logo,
    )

    return redirect("app1:home")


def job_details(request, pk):
    job = Job.objects.get(id=pk)

    user_id = request.session.get("user_id")
    current_user = User.objects.get(id=user_id)

    application = Application.objects.filter(job=job, user=current_user)
    print(len(application))

    applied = False

    if len(application) > 0:
        applied = True

    context = {"job": job, "applied": applied}
    return render(request, "job-single.html", context)


def apply_page(request, pk):
    job = Job.objects.get(id=pk)

    context = {"job": job}
    return render(request, "apply.html", context)


def apply(request, pk):
    form_email = request.POST.get("email", "")
    form_first_name = request.POST.get("first_name", "")
    form_lastname = request.POST.get("last_name", "")
    form_cover_letter = request.POST.get("cover_letter", "")
    form_cv = request.FILES.get("cv")

    print(form_cv)

    applied_job = Job.objects.get(id=pk)

    user_id = request.session.get("user_id")
    user_applied = User.objects.get(id=user_id)

    Application.objects.create(
        email=form_email,
        first_name=form_first_name,
        last_name=form_lastname,
        cover_letter=form_cover_letter,
        cv=form_cv,
        job=applied_job,
        user=user_applied,
    )

    return redirect("app1:home")


def list_jobs(request):
    all_jobs = Job.objects.all()

    context = {"jobs": all_jobs, "jobs_count": all_jobs.count()}
    return render(request, "job-listings.html", context)


def delete_application(request, pk):
    job = Job.objects.get(id=pk)

    user_id = request.session.get("user_id")
    current_user = User.objects.get(id=user_id)

    application = Application.objects.filter(job=job, user=current_user)

    application.delete()

    print("deleted")

    return redirect("app1:home")


def posted_jobs(request):

    user_id = request.session.get("user_id")
    current_user = User.objects.get(id=user_id)

    posted_jobs = Job.objects.filter(user=current_user)

    context = {"jobs": posted_jobs, "jobs_count": posted_jobs.count()}

    return render(request, "posted_jobs.html", context)


def applied_jobs(request):

    user_id = request.session.get("user_id")
    current_user = User.objects.get(id=user_id)

    applications = Application.objects.filter(user=current_user)

    # Extract the jobs from these applications
    applied_jobs = Job.objects.filter(application__in=applications)

    context = {"jobs": applied_jobs, "jobs_count": applied_jobs.count()}
    return render(request, "applied_jobs.html", context)


def edit_job_page(request, pk):

    job = Job.objects.get(id=pk)

    context = {"job": job}
    return render(request, "edit_job.html", context)


def edit_job(request, pk):
    job = Job.objects.get(id=pk)

    form_email = request.POST.get("email", "")
    form_title = request.POST.get("title", "")
    form_location = request.POST.get("location", "")
    form_type = request.POST.get("type", "")
    form_job_description = request.POST.get("job-description", "")
    form_company_name = request.POST.get("company_name", "")
    form_company_description = request.POST.get("company-description", "")
    form_logo = request.FILES.get("logo", "")
    
    
    


def delete_job(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect("app1:posted_jobs")

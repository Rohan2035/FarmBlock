from django.shortcuts import redirect, render, HttpResponse
from .models import BlogPost as bp
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Contact as c
import random as rn


# Class that handles posts
class PostFunc():

    def index(request):
        a = []

        for i in range(1, 7):
            a.append(bp.objects.get(post_id = i))

        all_post = list(bp.objects.all())
        items = rn.sample(all_post, 6)

        context = {'post' : items}

        return render(request, 'index.html', context)


    def content(request, slug):

        # Fetching the Post
        post = bp.objects.get(slug = slug)

        # Suggestions
        all_post = list(bp.objects.all())
        items = rn.sample(all_post, 3)

        context = {'post' : post, 'post1' : items}
        return render(request, 'content.html', context)


    def category(request, Category):
        post = bp.objects.filter(Category=Category)
        context = {"cat" : post}
        return render(request, 'cat.html', context)
    

    def search(request):

        query = request.GET['query']
        print(query)

        query = " ".join(query.split())

        if(len(query) == 0):
            return HttpResponse("Search unsucessful please fill the search box")

        elif(len(query) > 1000):
            return HttpResponse("You have filled a long character please enter a smaller keyword")

        else:
            post = bp.objects.filter(Name__icontains=query)
            context = {'post': post}

        return render(request, 'search.html', context)


    def addContent(request):

        if request.user.is_authenticated:
            return render(request, 'addContent.html')

        else:
            return HttpResponse("Error 404 Not found")


    def validate(request):

        if request.method == 'POST':

            name = request.POST['name']
            category = request.POST['cat']
            post = request.POST['post']
            d = request.POST['date']
            
            img = request.FILES["photo"]


            # Few basic checks
            slug = str(name).lower()
            slug = "".join(slug.split())

            name = name.lower()

            category = category.lower()
            category = "".join(category.split())

            a = request.user
            a = str(a)

            # Use this checks while deployment
            if(len(name) > 3 and len(category) > 3 and len(post) > 50):
                pass


            final = bp(Name=name, Category=category, content=post, slug=slug, img1=img, date=d, author = a)
            
            final.save()  
            messages.success(request, "Post Sucessfully added") 
            return redirect("Index")

        else:

            return HttpResponse("Error 404 not found")


    def DisplayAll(request):
        post = bp.objects.all()
        context = {"post" : post}
        return render(request, "DisplayAll.html", context)


    def contact(request):
        return render(request, "Contact.html")


    def validateContact(request):

        if request.method == 'POST':
            name = request.POST['name']
            s = request.POST['sug']

            if(len(name) < 2 and len(s) < 2):
                return HttpResponse("Invalid")

            f = c(user_name = name, Suggestions = s)
            f.save()  
            messages.success(request, "Message Sucessfully Sent")
            
            return redirect("Index")

        else:
            return HttpResponse("Error not found")



    # Remove This
    def test(request):
        posts = list(bp.objects.all())
        items = rn.sample(posts, 6)

        print(items[3].author)

        return HttpResponse("Test")        




# Class that handles user login
class utility():

    def handleSignup(request):
        
        if request.method == 'POST':

            name = request.POST['name']
            mail = request.POST['email']
            password = request.POST['password']
            confirmPassword = request.POST['confirmPassword']

            #Basic Checks
            check = User.objects.filter(email = mail).exists() 
            if (check):
                messages.warning(request, 'account already exists')

            elif (password != confirmPassword):
                messages.warning(request, "Passwords don't match")

            elif (len(password) < 5):
                messages.warning(request, 'Your passsword is too short')

            else:       
                #Create User
                myuser = User.objects.create_user(name, mail, password)
                myuser.save()
                messages.success(request, f'Welcome to FarmBlock {name}') 

            
            return redirect('Index')

        else:
            return HttpResponse("404 Error no resource found")


    def handleLogin(request):
        
        if request.method == 'POST':
            
            mail = request.POST['loginEmail']
            passw = request.POST['loginPassword']
            check = User.objects.filter(email = mail).exists()

            if(check):

                name = User.objects.get(email=mail).username
                us = authenticate(username = name, password = passw)

                if us is not None:
                    login(request, us)
                    messages.success(request, "Login Sucessful")
                    return redirect("Index")

                else:
                    messages.warning(request, "Please enter valid credentials")
                    return redirect ("Index")


            else:
                messages.warning(request, "Please enter valid credentials")
                return redirect ("Index")


        else:
            return HttpResponse("Error 404")
                

    def handleLogout(request):
        logout(request)
        messages.success(request, "Sucessfully logged out")
        return redirect("Index")


# Class to see all the posts entered by the user
class userUtility():

    def userPost(request):
        
        name = request.user

        if (bp.objects.filter(author = name).exists()):
            post = bp.objects.filter(author = name)
            
            context = {'post' : post}
            return render(request, 'userposts.html', context)

        else:
            return HttpResponse("<h1 align='center'>No posted added</h1>")


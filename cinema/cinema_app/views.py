from django.shortcuts import render, get_object_or_404, redirect
from .models import Director, Actor, Genre, Movie, User, Session, Ticket
from .forms import TicketForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                return redirect('session_list')
    else:
        form = UserCreationForm()
        
    
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_log = authenticate(request, username=username, password=password)
        
        if user_log is not None:
            login(request, user_log)  
            return redirect('session_list')  
        else:
            error_message = "Неверное имя пользователя или пароль."
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')   
 
@csrf_exempt            
def logout_view(request):
    logout(request)
    return redirect('session_list')

def sessions_list(request):
    list_of_sessions = Session.objects.all()
    return render(request, 'session_list.html', {'sessions': list_of_sessions})

def session_detail(request, ses_id):
    session = get_object_or_404(Session, id=ses_id)
    film = session.movie.all()
    director = film.director.all()
    actors = film.actors.all()
    genres = film.genres.all()
    

    return render(request, 'session_detail.html',
                   {'session': session, 'film': film, 'director': director, 'actors': actors, 'genres': genres, 
                   })

def film_detail(request, film_id):
    film = get_object_or_404(Movie, id=film_id)
    film_name = film.name
    director_film = film.director
    actors_film = film.actors.all()
    actor_names = [actor.name for actor in actors_film]
    actor_id = [actor.id for actor in actors_film]
    genre_film = film.genres.all()
    genre_names = [genre.genre_name for genre in genre_film]
    description_film = film.description
    available_sessions = Session.objects.filter(movies = film)
    image = film.image

    return render(request, 'film_detail.html', {'film': film, 'film_name': film_name, 'director_film': director_film, 'all_actors': actors_film,
                                                'genre_film': genre_names, 'description_film': description_film, 'available_sessions': available_sessions, 'actor_id': actor_id,
                                                'image': image})


def purchase_ticket(request, ses_id):
    session = get_object_or_404(Session, id = ses_id)
    film = get_object_or_404(Movie, id = session.movies.id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user 
            ticket.session = session
            ticket.ticket_total = 1
            ticket.ticket_price = 100.0

            if session.ticket_total > 0:
                session.ticket_sold += 1
                session.ticket_total -= 1
                ticket.ticket_sold = 1  # Устанавливаем значение для ticket_sold
                ticket.save()
                session.save()
            
            
            return redirect('session_list')
    else:
        form = TicketForm()

    return render(request, 'purchase_ticket.html', {
        'form': form,
        'ticket_price': 100.0,
        'available_tickets': session.ticket_total
    })

def page_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    your_tickets = Ticket.objects.filter(user=user)
    return render(request, 'user_page.html', {'your_tickets': your_tickets })

def actor_info(request, id):
    actor = get_object_or_404(Actor, id=id)

    actor_name = actor.name
    actor_age = actor.age
    actor_sex = actor.sex
    actor_image = actor.image
    return render(request, 'actor_info.html', {'actor_name' : actor_name, 'actor_age' : actor_age, 'actor_sex' : actor_sex, 'actor_image' : actor_image})


#new code and new code        
                                                
                               

        







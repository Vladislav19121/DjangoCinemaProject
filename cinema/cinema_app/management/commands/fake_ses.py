from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import random
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.files.base import ContentFile

from io import BytesIO

from cinema_app.models import Session, Movie, Genre, Actor, Director, Ticket

genres_for_film = [
    "Фантастика",
    "Фэнтези",
    "Детектив",
    "Романтика",
    "Ужасы",
    "Научная фантастика",
    "Приключения",
    "Исторический роман",
    "Комедия",
    "Триллер"
                ]

movies_fl = {
    'Голодные игры' : {'name': 'Голодные игры', 'image': 'entire_games.jpg'},
    'Железный человек': {'name': 'Железный человек', 'image': 'iron_man.jpg'},
    'Человек паук': {'name': 'Человек паук', 'image': 'spider_man.jpg'},
}

actors_fl = {
    "Роберт Дауни-младший": {"name": "Роберт Дауни-младший", "sex": "мужской", "age": 58, 'image': "robert_downey_jr.jpg",},
    "Мерил Стрип": {"name": "Мерил Стрип", "sex": "женский", "age": 74, 'image': "meryl_streep.jpg", },
    "Джулия Робертс": {"name": "Джулия Робертс", "sex": "женский", "age": 56, 'image': "julia_roberts.jpg", },
    "Том Хэнкс": {"name": "Том Хэнкс", "sex": "мужской", "age": 67, 'image': "tom_hanks.jpg", },
    "Натали Портман": {"name": "Натали Портман", "sex": "женский", "age": 42, 'image': "natalie_portman.jpg", },
    "Бенедикт Камбербэтч": {"name": "Бенедикт Камбербэтч", "sex": "мужской", "age": 47, 'image': "benedict_cumberbatch.jpg", },
    "Сандра Буллок": {"name": "Сандра Буллок", "sex": "женский", "age": 59, 'image': "sandra_bullock.jpg", },
}


directors_fl = {
    "Стивен Спилберг": {"name": "Стивен Спилберг", "age": 76, "sex": "мужской", 'image': "steven_spielberg.jpg"},
    "Кристофер Нолан": {"name": "Кристофер Нолан", "age": 53, "sex": "мужской", 'image': "christopher_nolan.jpg"},
    "Квентин Тарантино": {"name": "Квентин Тарантино", "age": 60, "sex": "мужской", 'image': "quentin_tarantino.jpg"},
    "Андрей Тарковский": {"name": "Андрей Тарковский", "age": 82, "sex": "мужской", 'image': "andrei_tarkovsky.jpg"},  # Умер в 1986
    "Мартин Скорсезе": {"name": "Мартин Скорсезе", "age": 81, "sex": "мужской", 'image': "martin_scorsese.jpg"},
    "Грета Гервиг": {"name": "Грета Гервиг", "age": 40, "sex": "женский", 'image': "greta_gerwig.jpg"},
    "Кэтрин Бигелоу": {"name": "Кэтрин Бигелоу", "age": 71, "sex": "женский", 'image': "kathryn_bigelow.jpg"},
    "Джордж Лукас": {"name": "Джордж Лукас", "age": 79, "sex": "мужской", 'image': "george_lucas.jpg"},
    "Фрэнсис Форд Коппола": {"name": "Фрэнсис Форд Коппола", "age": 84, "sex": "мужской", 'image': "francis_ford_coppola.jpg"},
    "Ридли Скотт": {"name": "Ридли Скотт", "age": 86, "sex": "мужской", 'image': "ridley_scott.jpg"}}

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        # def get_random_image():
        #     response = requests.get('https://picsum.photos/200/300')  # Случайное изображение
        #     return ContentFile(response.content)

        for _ in range(3):
            User.objects.create_user(username=faker.user_name(),
                                     email=faker.email(),
                                     password='qwe1asd2zxc3')
            
            users = list(User.objects.all())

        movies = Movie.objects.all()

        

    #Создаем сессию и связываем ее с текущим фильмом
                

        for _ in range(10):
            Genre.objects.create(genre_name = random.choice(genres_for_film),
                                 pg_rating = random.randint(1, 18))
            
        actor_names = list(actors_fl.keys())
        selected_actors = random.sample(actor_names, k=7)
        for actor_name in selected_actors:
            actor_info = actors_fl[actor_name]
    
            actor = Actor.objects.create(
            name=actor_info['name'],
            age=actor_info['age'],
            sex=actor_info['sex'],
            oscar_count=random.randint(1, 3),
            image=f'/media/images/{actor_info["image"]}'  # Исправлено: используйте двойные кавычки для ключа 'image'
        )   
            
            # actor.image.save(f'{actor.name}.jpg', get_random_image())
            
            actor = list(Actor.objects.all())
        
        for _ in range(10):
            director_name = random.choice(list(directors_fl.keys()))
            director_info = directors_fl[director_name]

            directors = []
            for director_name in directors_fl.values():
                    director = Director.objects.create(
                    name=director_name['name'],
                    age=director_name['age'],
                    sex=director_name['sex'],
                    film_count=random.randint(1, 15),
                    # image=f'/images/{directors_fl["image"]}',
            )
                
                    # director.image.save(f'{director.name}.jpg', get_random_image())
            directors.append(director)

        
        
        created_movies = set()
        while len(created_movies) < 3:
            movie_name = random.choice(list(movies_fl.keys()))
            if movie_name not in created_movies:
                created_movies.add(movie_name)
                movie_info = movies_fl[movie_name]      
                movie_director = random.choice(directors)
                movie = Movie.objects.create(name = movie_info['name'],
                                            director = movie_director,
                                            description = faker.paragraph(nb_sentences=15),
                                            release_data = faker.date(),
                                            image = f'/media/images/{movie_info['image']}' 
                                            )
            
            
            selected_actors = random.sample(list(Actor.objects.all()), k=random.randint(1, 4))
            movie.actors.set(selected_actors)  
            selected_genres = random.sample(list(Genre.objects.all()), k = random.randint(1, 3))
            movie.genres.set(selected_genres)
            if len(selected_actors) != len(set(selected_actors)):
                print("Ошибка: найдены дубликаты актеров!")
            
        movies = list(Movie.objects.all())

            #Создаем сессии для каждого фильма
        for movie in movies:
            time_start_naive = faker.date_time_this_year()
            time_start = timezone.make_aware(time_start_naive)

            session = Session.objects.create(
            time_start=time_start,
            time_end=time_start + timedelta(hours=random.randint(1, 5)),
            ticket_total=random.randint(1, 100),
            ticket_sold=random.randint(1, 100),
            movies=movie  # Связываем сессии с фильмом через ForeignKey
                    )

        sessions = Session.objects.all()
        for session in sessions:
            print(session)

            
        for _ in range(1000):
            session = random.choice(Session.objects.all())
            user = random.choice(User.objects.all())
            ticket_price = round(random.uniform(10.0, 100.0), 2) 
            ticket_total = random.randint(1, 100) 
            ticket_sold=random.randint(1, 100)

            Ticket.objects.create(
                            session=session,
                            user=user,
                            ticket_price=ticket_price,
                            ticket_total = ticket_total,
                            ticket_sold = ticket_sold
                            
                                )
            

        self.stdout.write(self.style.SUCCESS('Seeded data successfully'))    
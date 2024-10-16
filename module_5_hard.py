import time


class User:

    def __str__(self):
        return self.nickname

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other

    def __ne__(self, other):
        return self.nickname != other

    def __contains__(self, other):
        return __eq__(self, other)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __ne__(self, other):
        return self.title != other.title

    def __contains__(self, other):
        return __eq__(self, other)


class UrTube:
    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user: User
        self.current_user = 0

    def add_one_video(self, new_video: Video):

        if new_video in self.videos:
            print(f'видео уже есть')
        else:
            self.videos.append(new_video)

    def add(self, *new_video: Video):
        for i in new_video:
            self.add_one_video(i)

    def log_in(self, nickname, password: str):

        if nickname in self.users:
            user1 = self.users[self.users.index(nickname)]
            if user1.password != hash(password):
                print('Неверный пароль')
            else:
                self.current_user = user1
        else:
            print('Неверный логин')

    def log_out(self):
        self.users.remove(self.current_user)
        self.current_user = None

    def get_videos(self, search_video: str):

        new_list1: list = []

        for i in self.videos:
            a_title = i.title.lower()
            b_title = search_video.lower()
            if a_title.count(b_title):
                new_list1.append(i.title)

        return new_list1

    def watch_video(self, search_video: str):

        if self.current_user == 0:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        waching = False
        for i in self.videos:
            if search_video == i.title:
                waching = True
                waching_video = i
                break
        if waching:
            if self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return

            sec = 1
            while sec <= waching_video.duration:
                print(sec, end=' ')
                time.sleep(1)
                sec += 1
            print('Конец видео')
        else:
            print('Такое видео отсутствует')

    def register(self, nickname, password, age):

        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

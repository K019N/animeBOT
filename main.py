import requests
import bs4
from art import tprint
from termcolor import cprint 
import datetime 


CUR_YEAR = datetime.datetime.now().year

TYPES = {
    'фильм': 'movie',
    'сериал': 'tv',
}

GENRES = {
    'вампиры': 'vampire',
    'гарем': 'harem',
}



def get_all_key_from_dict(dictionary):
    result = ''
    for i, value in enumerate(dictionary):
        if i == len(dictionary) - 1:
            result += f'"{value}"'
        else:
            result += f'"{value}" или '
    return result



def searching():
    cprint(
        f'Напиши в консоль что хочешь посмотреть {get_all_key_from_dict(TYPES)}.\n'
        'p.s тут только аниме',
        'black', 'on_white')
    film_or_tv = input().lower()
    while True:
        if film_or_tv in TYPES:
            film_or_tv = TYPES[film_or_tv]
            break
        cprint(f'Напиши в консоль, что хочешь посмотреть {get_all_key_from_dict(TYPES)}.',
               'black', 'on_white')
        film_or_tv = input().lower()
    cprint(
        'Поскольку мой создатель ленив вариации жанров не так велики..прости.\n'
        f'Напиши в консоль какой жанр тебе ближе {get_all_key_from_dict(GENRES)}.',
        'black', 'on_white')
    genre = input().lower()

    while True:
        if genre in GENRES:
            genre = GENRES[genre]
            break
        cprint(f'Напиши в консоль какой жанр тебе ближе {get_all_key_from_dict(GENRES)}.',
               'black', 'on_white')
        genre = input().lower()
    cprint(
        'Хм..интересный выбор, у тебя необычные вкусы. Хочешь выбрать время выхода шедевра анимации?\n'
        f'Напиши в консоли "нет" если хочешь оставить стандартный промежуток времени от 1959 до {CUR_YEAR},\n'
        'либо напиши новый промежуток в формате "2010 2022"',
        'black', 'on_white')
    year_from = 1959
    year_to = CUR_YEAR

    while True:
        year_range = input()
        if year_range.lower() == "нет":
            break
        if year_range:

            try:
                year_range = list(map(int, year_range.split()))
                if (year_range[0] in range(1959, CUR_YEAR)) and (year_range[1] in range(year_range[0], CUR_YEAR)):
                    break
            except:
                pass
            cprint(
                f'Напиши в консоли "нет" если хочешь оставить стандартный промежуток времени от 1959 до {CUR_YEAR},\n'
                f'либо напиши новый промежуток в формате "2010 2022"',
                'black', 'on_white')
    year_from = year_range[0]
    year_to = year_range[1]

    web = requests.get(
        f'https://animego.org/anime/filter/year-from-{year_from}-to-{year_to}/genres-is-{genre}/type-is-{film_or_tv}/apply?sort=rating&direction=desc&page=1')
    soup = bs4.BeautifulSoup(web.text, 'lxml')
    all_block = soup.find_all(class_="col-12")
    link_list = []
    for block in all_block:
        try:
            link = block.find('a')['href']
            link_list.append(link)
        except:
            pass
    return link_list

def output(link_list):
    if len(link_list) > 3:
        for link in link_list[:3]:
            print(link)
        cprint(
            'Показать остальные варианты?\n'
            'Напишите в консоли "да" или "нет".',
            'black', 'on_white')
        show = input().lower()
        while True:
            if show == 'да':
                for link in link_list[3:]:
                    print(link)
                break
            if show == 'нет':
                break
            show = input().lower()
    elif len(link_list) >= 1:
        for link in link_list:
            print(link)
    else:
        print('Пустота... ничего нет... все пропало\n')


def main():
    tprint('anime   super   bot')
    cprint(
        'Привет! Я бот - мастер прокрастинации, помогу тебе подобрать, что посмотреть сегодня вечером!\n'
        'Почти, "Netflix and chill" если бы я не был пайтон кодом(((.\nПоехали?\n'
        'Чтобы начать напиши в консоли "да"',
        'black', 'on_white')
    inp = input().lower()
    trolling_count = 0
    while True:
        trolling_count += 1
        if inp == 'да':
            break
        if trolling_count > 10:
            cprint(
                'Прошу.. не издевайся, любовь моя, ну зачем тебе это\n',
                'black', 'on_white')
        cprint(
            'Чтобы начать напиши в консоли "да"',
            'black', 'on_white')
        inp = input().lower()

    cycle = True
    while cycle:
        link_list = searching()
        output(link_list)
        cprint(
            'Искать по другим критериям?\n'
            'Напишите в консоли "да" или "нет".',
            'black', 'on_white')
        repeat = input().lower()
        while True:
            if repeat == 'да':
                break
            if repeat == 'нет':
                cycle = False
                cprint(
                    'Не судите строго..Я-я умоляю (Ла-ла-ла-ла-ла)'
                    'green', 'on_white')
                break
            repeat = input().lower()

    input("\nPress enter to exit;")


if __name__ == "__main__":
    main()

# https://requests.readthedocs.io/en/latest/
# https://beautiful-soup-4.readthedocs.io/en/latest/
# https://art-python.readthedocs.io/en/latest/
# https://pypi.org/project/termcolor/'

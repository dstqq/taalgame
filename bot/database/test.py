import json
# from database import mycursor, mydb
import mysql.connector
# from bot.misc import TgKeys
from main import *

class Word:
    def __init__(self, ru, ned, type, article):
        self.ru = ru
        self.ned = ned
        self.type = type
        self.article = article
    
    @classmethod
    def get_type():
        return {'noun': 'существительное', 'verb': 'глагол', 'adjective': 'прилагательное', 
        'adverb': 'наречие', 'pronoun':'местоимение', 'preposition':'предлог', 
        'conjunction':"соединение", 'interjection':"междометие", 'article':"артикль", 
        'numeral':"числительное"}
        # return ['существительное', 'глагол', 'прилагательное', 'наречие', 'местоимение', "предлог", "соединение", "междометие", "артикль?", "числительное"]


def check_for_table(table_name: str):
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        if table_name in x:
            return True
    return False


def create_sql_table(table_name: str):
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        if table_name in x:
            sql = f"DROP TABLE {table_name}"
            mycursor.execute(sql)
            print(f"DELETING TABLE {table_name.upper()}")
    if table_name == 'word_base':
        mycursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, rus VARCHAR(50), ned VARCHAR(50), type ENUM('noun', 'verb', 'adjective', 'adverb', 'pronoun', 'preposition', 'conjunction', 'interjection', 'article', 'numeral'), article ENUM('het', 'de', ''), lesson INT, difficulty INT)")
    elif table_name == 'settings':
        mycursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, field VARCHAR(50), value VARCHAR(50))")
    elif table_name == 'users':
        mycursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, user_id VARCHAR(50), user_name VARCHAR(50), user_in_game VARCHAR(50), user_last_game VARCHAR(50))")
    print(f"TABLE {table_name.upper()} CREATED SUCCESSFULLY")


def insert_setting_table(table_name: str):
    sql = f"INSERT INTO {table_name} (field, value) VALUES (%s, %s)"
    val = [
        ('GOD', '386760687'),
        ('TASHA', '5190092132'),
        ('Quiz quantity', '6'),
        ('Game quantity', '0'),
    ]
    mycursor.executemany(sql, val)
    mydb.commit()


def test():
    mycursor.execute("SELECT value FROM settings WHERE field = 'Quiz quantity'")
    myresult = mycursor.fetchall()
    print(myresult[0][0])


def insert_in_table(table_name):
    sql = f"INSERT INTO {table_name} (rus, ned, type, article, lesson, difficulty) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [
            ("жить(существовать)", "leven", 'verb', "", 1, 1),
            ('знать', 'weten', 'verb', '', 1, 1),
            ('верить', 'geloven', 'verb', '', 1, 1),
            ('между', 'tussen', "preposition", '', 1, 1),
            ('взрослый', 'volwassen', 'noun', 'de', 1, 2),
            ('использовать', 'gebruiken', 'verb', '', 1, 2),
            ('жить(в каком-то месте)', 'wonen', 'verb', '', 1, 1),
            ('спряжение(глаголов)', 'vervoeging', 'verb', '', 1, 3),
            ('корень', 'stam', 'noun', 'de', 1, 1),
            ('без', 'zonder', 'preposition', '', 1, 1),
            ('плакать', 'huilen', 'verb', '', 1, 1),
            ('лежать', 'liggen', 'verb', '', 1, 1),
            ('рисовать', 'tekenen', 'verb', '', 1, 1),
            ('гореть', 'branden', 'verb', '', 1, 1),
            ('лгать', 'liegen', 'verb', '', 1, 1),
            ('какой', 'welk/e', 'preposition', '', 1, 1),
            ('никогда', 'nooit', 'adverb', '', 1, 1),
            ('исключение', 'uitzondering', 'noun', 'de', 1, 2),
            ('одинаковые(the same)', 'dezelfde', 'adjective', '', 1, 1),
            ('that', 'die', 'pronoun', '', 1, 1),
            ('позади, сзади', 'achter', 'adverb', '', 1, 1),
            ('уходить', 'weggaan', 'verb', '', 1, 1),
            ('любым/each', 'elk', 'adjective', '', 1, 1),
            ('которым', 'waarmee', 'pronoun', '', 1, 1),
            ('получать', 'krijgen', 'verb', '', 1, 1),
            ('источник', 'bron', 'noun', 'de', 1, 1),
            ('подходит, приближается', 'komt eraan', 'verb', '', 1, 1),

            ('бежать', 'hardlopen', 'verb', '', 2, 1),
            ('тяжёлый', 'zwaar', 'adjective', '', 2, 1),
            ('закрыт', 'dicht', 'adjective', '', 2, 1),
            ('шкаф', 'kast', 'noun', 'de', 2, 1),
            ('обычно, в основном', 'meestal', 'adverb', '', 2, 2),
            ('железо', 'ijzer', 'noun', 'het', 2, 1),
            ('ломать', 'breken', 'verb', '', 2, 1),
            ('строить', 'timmeren', 'verb', '', 2, 1),
            ('красить', 'verven', 'verb', '', 2, 1),
            ('беседа', 'gesprek', 'noun', 'het', 2, 2),
            ('комната', 'kamer', 'noun', 'de', 2, 1),
            ('оплата', 'betaling', 'noun', 'de', 2, 2),
            ('деньги', 'geld', 'noun', 'het', 2, 1),
            ('цель', 'doel', 'noun', 'het', 2, 1),
            ('пол', 'floer', 'noun', 'de', 2, 1),
            ('сироп', 'stroop', 'noun', 'de', 2, 1),
            ('газета', 'krant', 'noun', 'de', 2, 1),
            ('ящик', 'doos', 'noun', 'de', 2, 1),
            ('количество', 'bedrag', 'noun', 'het', 2, 2),
            ('хватать', 'pakken', 'verb', '', 2, 2),
            ('чистить, натирать', 'poetsen', 'verb', '', 2, 2),

            ('аллея', 'laan', 'noun', 'de', 3, 1),
            ('рыба', 'vis', 'noun', 'de', 3, 1),
            ('воздух', 'lucht', 'noun', 'de', 3, 1),
            ('указывать', 'wijzen', 'verb', '', 3, 1),
            ('звезда', 'ster', 'noun', 'de', 3, 1),
            ('дверь', 'deur', 'noun', 'de', 3, 1),
            ('облако', 'wolk', 'noun', 'de', 3, 1),
            ('церковь', 'kerk', 'noun', 'de', 3, 1),
            ('коробка', 'doos', 'noun', 'de', 3, 1),
            ('сиять, светить(to shine)', 'schijnen', 'verb', '', 3, 2),
            ('после', 'na', 'adverb', '', 3, 1),
            ('волна', 'golf', 'noun', 'de', 3, 1),
            ('будильник', 'wekker', 'noun', 'de', 3, 1),
            ('часы', 'horloge', 'noun', 'het', 3, 3),
            ('очки', 'bril', 'noun', 'de', 3, 1),
            ('рукав', 'mouw', 'noun', 'de', 3, 1),
            ('куртка', 'jas', 'noun', 'de', 3, 1),
            ('платье', 'rok', 'noun', 'de', 3, 1),
            ('кепка', 'pet', 'noun', 'de', 3, 1),
            ('палка', 'stok', 'noun', 'de', 3, 1),
            ('но', 'maar', 'conjunction', '', 3, 1),
            ('сумка', 'tas', 'noun', 'de', 3, 1),
            ('ограда, забор', 'hek', 'noun', 'het', 3, 1),
            ('ножка(стола)', 'poot', 'noun', 'de', 3, 1),

            ("лицо", "gezicht", 'noun', "het", 4, 2),
            ('волосы', 'haar', 'noun', 'het', 4, 1),
            ('голова', 'hoofd', 'noun', 'het', 4, 1),
            ('бровь', 'wenkbrauw', 'noun', 'de', 4, 3),
            ('ресницы', 'wimpers', 'noun', 'de', 4, 3),
            ('нос', 'neus', 'noun', 'de', 4, 1),
            ('ухо', 'oor', 'noun', 'het', 4, 1),
            ('язык', 'tong', 'noun', 'de', 4, 1),
            ('губа', 'lip', 'noun', 'de', 4, 1),
            ('подбородок', 'kin', 'noun', 'de', 4, 1),
            ('шея(горло)', 'hals', 'noun', 'de', 4, 1),
            ('шея(сзади)', 'nek', 'noun', 'de', 4, 1),
            ('рот', 'mond', 'noun', 'de', 4, 1),
            ('щека', 'pupil', 'noun', 'de', 4, 1),
            ('пробовать на вкус', 'proeven', 'verb', '', 4, 2),
            ('глаз', 'oog', 'noun', 'het', 4, 1),
            ('лоб', 'voorhoofd', 'noun', 'het', 4, 1),
            ('затылок', 'achterhoohd', 'noun', '', 4, 1),
            ('страшный', 'eng', 'adjective', '', 4, 1),
            ('ноздря', 'neusgat', 'noun', 'het', 4, 2),
            ('челюсть', 'kaak', 'noun', 'de', 4, 1),
            ('грудь', 'borsten', 'noun', 'de', 4, 2),

            ("уставший", "moe", 'adjective', "", 5, 1),
            ('злой', 'boos', 'adjective', '', 5, 1),
            ('дружелюбный', 'aardig', 'adjective', '', 5, 1),
            ('больной', 'ziek', 'adjective', '', 5, 1),
            ('sad', 'verdrietig', 'adjective', '', 5, 2),
            ('все(all)', 'allemaal', 'pronoun', '', 5, 1),
            ('окно', 'raam', 'noun', 'het', 5, 1),
            ('часто', 'vaak', 'adverb', '', 5, 1),
            ('раз', 'maal', 'noun', '', 5, 1),
            ('красивый', 'mooi', 'adjective', '', 5, 1),
            ('милый(характер)', 'lief', 'adjective', '', 5, 1),
            ('дорогой', 'duur', 'adjective', '', 5, 1),
            ('симпатичный', 'knap', 'adjective', '', 5, 1),
            ('носок', 'sok', 'noun', 'de', 5, 1),
            ('грзяный', 'vuil', 'adjective', '', 5, 1),
            ('высокий', 'hoog', 'adjective', '', 5, 1),
            ('камень', 'steen', 'noun', 'de', 5, 1),
            ('холодный', 'koud', 'adjective', '', 5, 1),
            ('всё(everything)', 'alles', 'pronoun', '', 5, 1),

            ('брат', 'broer', 'noun', 'de', 6, 1),
            ('сестра', 'zus', 'noun', 'de', 6, 1),
            ('тётя', 'tante', 'noun', 'de', 6, 1),
            ('дядя', 'oom', 'noun', 'de', 6, 1),
            ('звонить', 'bellen', 'verb', '', 6, 1),    
            ('считать(кол-во)', 'tellen', 'verb', '', 6, 1),
            ('висеть', 'hangen', 'verb', '', 6, 1),
            ('зависеть', 'afhangen', 'verb', '', 6, 1),
            ('живот', 'buik', 'noun', 'de', 6, 1),
            ('спина', 'rug', 'noun', 'de', 6, 1),
            ('нога', 'been', 'noun', 'het', 6, 1),
            ('коричневый', 'bruin', 'adjective', '', 6, 1),
            ('зеленый', 'groen', 'adjective', '', 6, 1),
            ('красный', 'rood', 'adjective', '', 6, 1),  
            ('желтый', 'geel', 'adjective', '', 6, 1),
            ('синий', 'blauw', 'adjective', '', 6, 1),
            ('голубой', 'lichtblauw', 'adjective', '', 6, 1),
            ('оранжевый', 'oranje', 'adjective', '', 6, 1),
            ('фиолетовый', 'paars', 'adjective', '', 6, 1),
            ('серый', 'grijs', 'adjective', '', 6, 1),
            ('черный', 'zwart', 'adjective', '', 6, 1),
            ('белый', 'wit', 'adjective', '', 6, 1),
            ('малиновый', 'karmozijn', 'adjective', '', 6, 2),
            ('бирюзовый', 'turquoise', 'adjective', '', 6, 3),   

            ('шляпа', 'hoed', 'noun', 'de', 7, 1),
            ('винтовка', 'geweer', 'noun', 'het', 7, 2),
            ('оружие', 'wapen', 'noun', 'het', 7, 1),
            ('война', 'oorlog', 'noun', 'de', 7, 1),
            ('порог', 'drempel', 'noun', 'de', 7, 1),
            ('доска', 'plank', 'noun', 'de', 7, 1),
            ('клавиатура', 'toeotsenbord', 'noun', 'het', 7, 1),
            ('конечно(естественно)', 'natuurlijk', 'adverb', '', 7, 1),
            ('бутылка', 'fles', 'noun', 'de', 7, 1),
            ('полный', 'vol', 'adjective', '', 7, 1),
            ('большой', 'groot', 'adjective', '', 7, 1),
            ('животное', 'dier', 'noun', 'het', 7, 1),
            ('сильный', 'strek', 'adjective', '', 7, 1),
            ('опасный', 'hevaarlijk', 'adjective', '', 7, 2),

            ('день', 'dag', 'noun', 'de', 0, 1),
            ('много', 'veel', 'adverb', '', 0, 1),
            ('больше', 'meer', 'adverb', '', 0, 1),
            ('озеро', 'meer', 'noun', 'het', 0, 1),
            ('меньше', 'minder', 'adverb', '', 0, 1),
            ('свободный', 'vrij', 'adjective', '', 0, 1),
            
    ]
    mycursor.executemany(sql, val)
    mydb.commit()


def opdracht_create():
    ru = ["спряжение(глаголов)|корень|без|плакать|лежать|рисовать|гореть|лгать|какой|никогда|исключение|одинаковые|that|позади, сзади|уходить|each|которым|получать|источники".title()]
    ned = ["Vervoeging|de stam|zonder|huilen|liggen|tekenen|branden|liegen|welkl/e|nooit|uitzondering|dezelfde|die|achter|weggaan|elk|waarmee|Krijgen|bronnen".title()]
    ru.append("аллея|рыбы|воздух|указывать|звезда|дверь|облако|церковь|коробка|светить|после|волна|будильник|часы|очки|рукав|куртка|юбка|кепка|палка|но|сумка|забор, ограда|лапа, ножка стола".title())
    ned.append("de laan|de vissen|de lucht|wijzen|de ster|de deur|de wolk|de kerk|de doos|schijnen|na|de golf|de wekker|het horloge|de bril|de mouw|de jas|de rok|de pet|de stok|maar|de tas|het hek|de poot".title())
    ru.append('знать|верить|между|взрослые|использовать|подходит, приближается|бежать|тяжелый|закрыт|outside|шкаф|используется(пассивный залог)|обычно, в основном|железо|ломать|строить|красить'.title())
    ned.append("weten|geloven|tussen|volwassenen|gebruiken|komt eraan|hardlopen|zwaar|dicht|de kast|wordt gebruikt|meestal|ijzer|breken|timmeren|verven".title())
    ru.append("лицо|волос|голова|брови|ресницы|нос|ухо|язык|губа|подбородок|горло|шея|рот|щека|глаз|лоб|затылок|страшный".title())
    ned.append("het gezicht|het haar|het hoofd|de wenkbrauw|de wimpers|de neus|het oor|de tong|de lip|de kin|de hals|de nek|de mond|de pupil|het oog|het voorhoofd|het achterhooft|eng".title())
    ru.append("злой|уставший|дружелюбный|больной|грустный|все(all)|окно|часто|раз|красивая|милый(характер)|дорогой|симпатичный|носок|грязный|высокий|камень|холодный|всё(everything)".title())
    ned.append("boos|moe|aardig|ziek|verdrietig|allemaal|het raam|vaak|maal|mooi|lief|duur|knap|de sok|vuil|hoog|de steen|koud|alles".title())
    ru.append("брат|сестра|тётя|дядя|жить(место)|жить(существовать)|звонить|считать(кол-во)|висеть|зависеть|живот|спина|нога|коричневый|зелёный|красный|жёлтый|голубой|синий|оранжевый|фиолетовый|серый|чёрный|белый|малиновый|бирюзовый|грудь".title())
    ned.append("de broer|de zus|de tante|de oom|wonen|leven|bellen|tellen|hangen|afhangen|de buik|de rug|het been|bruin|groen|rood|geel|blauw|lichtblauw|oranje|paars|grijs|zwart|wit|karmozijn|turquoise|de borsten".title())
    for i in range(len(ru)):
        list_ru = ru[i].split('|')
        list_ned = ned[i].split('|')
        ru_ned = dict(zip(list_ru, list_ned))
        with open(f'opdrachten\opdracht{i+1}.json', 'w', encoding="utf-8") as file:
            json.dump(ru_ned, file)

if __name__ == "__main__":
    # opdracht_create()
    # create_sql_table('word_base')
    # create_sql_table('settings')
    # create_sql_table('users')
    # insert_setting_table('settings')
    # insert_in_table("word_base")
    # print(check_for_table("settings"))
    drop_table('quiz_0')
    # test()
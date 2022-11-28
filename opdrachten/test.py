import json
# from bot.database import mycursor, mydb


class Word:
    def __init__(self, ru, ned, type, article):
        self.ru = ru
        self.ned = ned
        self.type = type
        self.article = article
    
    @classmethod
    def get_type():
        return ['noun', 'veb', 'adjective', 'adverb', 'pronoun', 'preposition', 'conjunction', 'interjection', 'article', 'numeral']


# def create_sql_table(table_name):
#     mycursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, rus VARCHAR(50), ned VARCHAR(50), type ENUM('noun', 'veb', 'adjective', 'adverb', 'pronoun', 'preposition', 'conjunction', 'interjection', 'article', 'numeral'), article ENUM('het', 'de', ''))")


# def insert_in_table(table_name):
#     sql = f"INSERT INTO {table_name} (ru, ned, type, article) VALUES (%s, %s, %s, %s)"
#     val = [("лицо", "gezicht", 'noun', "het"),
#             ("уставший", "moe", 'adjective', ""),
#             ("жить(существовать)", "leven", 'verb', ""),
#     ]
#     mycursor.executemany(sql, val)
#     mydb.commit()


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
    opdracht_create()
    # create_sql_table('word_base')
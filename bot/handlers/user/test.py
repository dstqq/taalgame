a = [(1, 'жить(существовать)', 'leven', 'verb', '', 1, 1), (2, 'знать', 'weten', 'verb', '', 1, 1), (3, 'верить', 'geloven', 'verb', '', 1, 1), (4, 'между', 'tussen', 'preposition', '', 1, 1), (5, 'взрослый', 'volwassen', 'noun', 'de', 1, 2), (6, 'использовать', 'gebruiken', 'verb', '', 1, 2), (7, 'жить(в каком-то месте)', 'wonen', 'verb', '', 1, 1), (8, 'спряжение(глаголов)', 'vervoeging', 'verb', '', 1, 3), (9, 'корень', 'stam', 'noun', 'de', 1, 1), (10, 'без', 'zonder', 'preposition', '', 1, 1), (11, 'плакать', 'huilen', 'verb', '', 1, 1), (12, 'лежать', 'liggen', 'verb', '', 1, 1), (13, 'рисовать', 'tekenen', 'verb', '', 1, 1), (14, 'гореть', 'branden', 'verb', '', 1, 1), (15, 'лгать', 'liegen', 'verb', '', 1, 1), (16, 'какой', 'welk/e', 'preposition', '', 1, 1), (17, 'никогда', 'nooit', 'adverb', '', 1, 1), (18, 'исключение', 'uitzondering', 'noun', 'de', 1, 2), (19, 'одинаковые(the same)', 'dezelfde', 'adjective', '', 1, 1), (20, 'that', 'die', 'pronoun', '', 1, 1), (21, 'позади, сзади', 'achter', 'adverb', '', 1, 1), (22, 'уходить', 'weggaan', 'verb', '', 1, 1), (23, 'любым/each', 'elk', 'adjective', '', 1, 1), (24, 'которым', 'waarmee', 'pronoun', '', 1, 1), (25, 'получать', 'krijgen', 'verb', '', 1, 1), (26, 'источник', 'bron', 'noun', 'de', 1, 1), (27, 'подходит, приближается', 'komt eraan', 'verb', '', 1, 1)]
# for i in a:
#     print(i)  # tuple
len_a = len(a)
# (number, rus, ned, article, res ENUM('right', 'wrong', 'none'))
# mycursor.execute(f"CREATE TABLE quiz_{num} (number INT, rus VARCHAR(50), ned VARCHAR(50), article ENUM('het', 'de', ''), res ENUM('right', 'wrong', 'none'))")
# sql = f"INSERT INTO {table_name} (number, rus, ned, article, res) VALUES (%s, %s, %s, %s, %s)"
# val = []
# start = 1
# for i in a:
#     val.append([start, i[1], i[2], i[4], 'none'])
#     start += 1

# mycursor.executemany(sql, val)
# mydb.commit()
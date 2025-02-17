from bingo_card import BingoCard
from bingo_data import BingoData
import pymysql.cursors


class User:

    def __init__(self, id, nickname, win, lose, profile_img):
        self.id = id
        self.nickname = nickname
        self.bingo_card = None
        self.record = {'win': win, 'lose': lose}
        self.profile_img = profile_img
        self.game_match_num = 0
        self.connection = pymysql.connect(host=BingoData.MYSQL_HOST,
                             user=BingoData.MYSQL_USER,
                             password=BingoData.MYSQL_PW,
                             db=BingoData.MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def get_nickname(self):
        return self.nickname

    def get_record(self):
        return self.record

    def get_bingo_card(self):
        return self.bingo_card.get_card()

    def get_id(self):
        return self.id

    def get_profile_img(self):
        return self.profile_img

    def get_game_match_num(self):
        return self.game_match_num

    def set_game_match_num(self, game_match_num):
        print("game match num:", game_match_num)
        self.game_match_num = game_match_num

    def win(self):
        self.record['win'] += 1
        self.update_win_in_db()

    def update_win_in_db(self):
         with self.connection.cursor() as cursor:
            # Increase the win count in the database for the user_id
            sql_query = "UPDATE user SET win = win + 1 WHERE user_id = %s"
            values = (self.id,)
            cursor.execute(sql_query, values)
            self.connection.commit()

    def lose(self):
        self.record['lose'] += 1
        self.update_lose_in_db()

    def update_lose_in_db(self):
        with self.connection.cursor() as cursor:
            # Increase the lose count in the database for the user_id
            sql_query = "UPDATE user SET lose = lose + 1 WHERE user_id = %s"
            values = (self.id,)
            cursor.execute(sql_query, values)
            self.connection.commit()

    def generate_bingo_card(self):
        self.bingo_card = BingoCard()

    def check_number(self, number):
        return self.bingo_card.check_number(number)

    def check_bingo(self):
        return self.bingo_card.check_bingo()


class User:
    def __init__(self, num):
        self.name = self.input_user_name(num)

    @staticmethod
    def input_user_name(num):
        print(f"{num}人目のユーザーの名前を入力")
        return input()


class App:
    def __init__(self, first_user, second_user):
        self.user1 = first_user
        self.user2 = second_user
        self.num = self.input_num()
        self.table = self.create_table()

    def create_table(self):
        table = [[" " for _ in range(self.num)] for _ in range(self.num)]
        return table

    @staticmethod
    def input_num():
        print("何列でプレイしますか？")
        return int(input())

    @staticmethod
    def check(check_list):
        if all([check == " " for check in check_list]):
            return False
        elif all([check == check_list[0] for check in check_list[1:]]):
            return True
        else:
            return False

    def check_table(self, user):
        for i in range(self.num):
            vertical = []
            for i_in in self.table:
                vertical.append(i_in[i])

            beside = self.table[i]

            diagonal1 = []
            diagonal2 = []

            for i_in in range(self.num):
                i_reverse = self.num - 1 - i_in
                diagonal1.append(self.table[i_in][i_in])
                diagonal2.append(self.table[i_in][i_reverse])

            if self.check(vertical) or self.check(beside) or self.check(diagonal1) or self.check(diagonal2):
                print(f"{user.name}の勝利")
                return True
            else:
                continue

        print("続く")
        return False

    def input_point(self):
        while True:
            print("左から何行目に配置しますか？")
            pos_x = int(input())
            pos_x -= 1
            print("上から何列目に配置しますか？")
            pos_y = int(input())
            pos_y -= 1
            pos = [pos_x, pos_y]
            if pos_x < 0 or pos_x > self.num - 1 or pos_y < 0 or pos_y > self.num - 1:
                print("その座標は存在しません")
                continue
            elif self.table[pos_y][pos_x] != " ":
                print("その座標はすでに取得されています")
                continue
            else:
                return pos

    def push_list(self, where, user):
        if user == self.user1:
            self.table[where[1]][where[0]] = "o"
        else:
            self.table[where[1]][where[0]] = "x"

    def create_txt(self, where):
        if where[1] == 0:
            txt = f"""|   {self.table[where[0]][where[1]]}   |"""
        else:
            txt = f"""   {self.table[where[0]][where[1]]}   |"""
        return txt

    def play_content(self, user):
        print("""--------------------------------------------
""")
        sample_txt = "--------" * self.num
        txt = ""
        txt += f"""
{sample_txt}
"""
        for i in range(self.num):
            for i_in in range(self.num):
                l = [i, i_in]
                l_txt = self.create_txt(l)
                txt += l_txt
            txt += f"""
{sample_txt}
"""
        print(txt)
        print(f"{user.name}さんのターン")
        pos = self.input_point()
        self.push_list(pos, user)

    def play(self):
        while True:
            if all([" " not in x for x in self.table]):
                print("引き分け")
                break
            self.play_content(self.user1)
            user_check = self.check_table(self.user1)
            if user_check:
                break

            if all([" " not in x for x in self.table]):
                print("引き分け")
                break
            self.play_content(self.user2)
            user_check = self.check_table(self.user2)
            if user_check:
                break

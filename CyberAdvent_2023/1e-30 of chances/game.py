from requests import get
from hashlib import sha256
URL = 'http://challenges.wsi.edu.pl:5010/'


def create_game() -> str:
    return get(f'{URL}/create').content.decode()


def get_answers(game_id: str) -> list[str]:
    answer_table = []
    for index in range(30):
        for guess in range(1, 11):
            response = get(f'{URL}/check?id={game_id}&guess={guess}&index={index}').content
            if int(response) == 1:
                answer_table.append(str(guess))
                break
    return answer_table


def get_flag(game_id: str, checksum: str) -> str:
    return get(f'{URL}/flag?id={game_id}&checksum={checksum}').content.decode()


if __name__ == '__main__':
    gameID = create_game()
    answer_tab = get_answers(gameID)
    c_sum = sha256(''.join(answer_tab).encode()).hexdigest()
    print(get_flag(gameID, c_sum))

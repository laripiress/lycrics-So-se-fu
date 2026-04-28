import time
import sys
import os
import threading

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

HIGHLIGHT_COLOR = "\033[38;5;196m"   # VERMELHO
MAIN_COLOR = "\033[38;5;15m"        # branco
COR_INATIVA = "\033[38;5;239m"

CURSOR_POS = lambda row, col: f"\033[{row};{col}H"
CLEAR_SCREEN = "\033[H\033[J"

TEXT_WIDTH = 60
TEXT_HEIGHT = 15

terminal_width = 80
terminal_height = 24

screen_lock = threading.Lock()


def tamanho_terminal():
    global terminal_width, terminal_height
    try:
        w, h = os.get_terminal_size()
        terminal_width = max(80, w)
        terminal_height = max(20, h)
    except:
        pass


# ✅ CORRIGIDA
def split_wrap(text, max_width):
    lines = []
    for part in text.split("\n"):
        words = part.split(" ")
        current = ""

        for word in words:
            if len(current) + len(word) + (1 if current else 0) <= max_width:
                current += (" " if current else "") + word
            else:
                lines.append(current)
                current = word

        if current:
            lines.append(current)

    return lines


def display_content(current_index, lyrics_data, content_info):
    start_col = 2
    start_row = 1
    current_row = 0

    with screen_lock:
        sys.stdout.write(CLEAR_SCREEN)

        # título
        for line in split_wrap(content_info["title_lines"][0], TEXT_WIDTH):
            sys.stdout.write(CURSOR_POS(start_row + current_row, start_col))
            sys.stdout.write(f"{BOLD}{line}{RESET}")
            current_row += 1

        # artista
        for line in split_wrap(content_info["artist_lines"][0], TEXT_WIDTH):
            sys.stdout.write(CURSOR_POS(start_row + current_row, start_col))
            sys.stdout.write(f"{DIM}{line}{RESET}")
            current_row += 2

        # letras
        for i in range(current_index, current_index + (TEXT_HEIGHT - current_row)):
            if 0 <= i < len(lyrics_data):
                data = lyrics_data[i]
                wrapped = split_wrap(data["original"], TEXT_WIDTH)

                for part in wrapped:
                    if i == current_index:
                        color = BOLD + (
                            HIGHLIGHT_COLOR if data.get("highlight") else MAIN_COLOR
                        )
                    else:
                        color = COR_INATIVA

                    sys.stdout.write(CURSOR_POS(start_row + current_row, start_col))
                    sys.stdout.write(f"{color}{part}{RESET}")
                    current_row += 1

        sys.stdout.flush()


def start_lyrics_animation():
    tamanho_terminal()

    start_time = time.monotonic()
    current_index = 0

    while time.monotonic() - start_time < 40:
        elapsed = time.monotonic() - start_time

        while (
            current_index < len(LYRICS_DATA)
            and elapsed >= LYRICS_DATA[current_index]["time"]
        ):
            current_index += 1

        display_index = max(0, current_index - 1)

        display_content(display_index, LYRICS_DATA, CONTENT_INFO)

        time.sleep(0.1)

    print("\nFim da música!")


CONTENT_INFO = {
    "title_lines": ["Só Se Fu..."],
    "artist_lines": ["Jean Tassy (part. Yago Oproprio)"],
}

LYRICS_DATA = [
    {"time": 0.0, "original": "Só tenho o seu telefone"},
    {"time": 2.0, "original": "Como que eu\nposso te encontrar"},
    {"time": 5.0, "original": "Sempre ela me prioriza"},
    {"time": 6.0, "original": "O primeiro da fila"},
    {"time": 7.0, "original": "O melhor que ela já provou"},
    {"time": 9.0, "original": "É proibido de dia"},
    {"time": 10.0, "original": "Calada da noite ela\nvolta pro meu cobertor"},
    {"time": 13.0, "original": "E eu só se fu", "highlight": True},
    {"time": 14.0, "original": "Mas so lame"},
    {"time": 15.0, "original": "Você não sabe o\nque passa aqui dentro"},
    {"time": 15.0, "original": "Você não sabe o\nque passa aqui dentro"},
    {"time": 17.0, "original": "Decidiu pagar pra ver"},
    {"time": 19.0, "original": "Cansei, não quero mais"},
    {"time": 20.0, "original": "Talvez"},
    
    {"time": 21.0, "original": "Vou ficar distante"},
    {"time": 22.0, "original": "Você não quer nem\nsaber como é eu tô"},
    {"time": 25.0, "original": "Sabe que eu\nnão moro perto"},
    {"time": 27.0, "original": "Mas cê sabe\nde onde eu sou"},
    {"time": 30.0, "original": "Então tá bom"},

    {"time": 32.0, "original": "Pode me acompanhar"},
    {"time": 34.0, "original": "Quando quiser"},
    {"time": 36.0, "original": "Me chama no WhatsApp"},
    
    {"time": 37.0, "original": "Se eu não sei\nnem dizer seu nome"},
    {"time": 38.0, "original": "Nem seu sobrenome"},   
]

if __name__ == "__main__":
    start_lyrics_animation()
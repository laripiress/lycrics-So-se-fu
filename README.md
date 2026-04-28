# lycrics-So-se-fu...
# 🎶 Terminal Lyrics Player — “Só Se Fu...”

Um projetinho em Python que exibe letras de música sincronizadas diretamente no terminal.

A ideia é simular sentimentos usando estruturas de programação:
loops infinitos, funções que não funcionam e condições que nunca são satisfeitas (igual a vida).

---

## Sobre o projeto

Este script reproduz a letra da música **“Só Se Fu...”** de forma sincronizada com o tempo, destacando a linha atual enquanto as demais aparecem suavizadas.

Tudo isso acontece no **terminal**, usando códigos ANSI para cores e posicionamento do cursor.

---

## Funcionalidades

* Sincronização de letras com tempo (tipo karaokê)
* Destaque da linha atual
* Quebra automática de linhas longas
* Renderização dinâmica no terminal
* Atualização em tempo real

---

## Tecnologias utilizadas

* Python 3
* ANSI Escape Codes (cores e cursor)
* Manipulação de tempo (`time`)
* Controle de terminal (`os`, `sys`)
* Threads (`threading`)

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/laripiress/lycrics-So-se-fu
```

### 2. Acesse a pasta

```bash
cd lycrics-So-se-fu
```

### 3. Execute o script

```bash
python lyrics.py
```

---

## Requisitos

* Python 3 instalado
* Terminal compatível com ANSI (recomendado):

  * Windows Terminal
  * PowerShell
  * Terminal do VS Code

---

## Personalização

Você pode alterar as cores no início do código:

```python
HIGHLIGHT_COLOR = "\033[38;5;196m"  # vermelho
MAIN_COLOR = "\033[38;5;15m"        # branco
COR_INATIVA = "\033[38;5;239m"      # cinza
```

---

## Estrutura da letra

As letras são definidas assim:

```python
LYRICS_DATA = [
    {"time": 0.0, "original": "Linha da música"},
    {"time": 2.0, "original": "Próxima linha"},
]
```

* `time` → tempo em segundos
* `original` → texto da linha
* `highlight` (opcional) → destaque especial

---

## Ideias para melhorias

* Destaque palavra por palavra
* Integração com áudio real
* Animações mais suaves
* Suporte para múltiplas músicas

---

Este projeto é apenas para fins de estudo, humor e criatividade, inspirado na trend de programadores recriando músicas em código.

Não substitui terapia.
Mas compila risadas (às vezes).

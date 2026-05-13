import turtle
# --- Настройки экрана ---
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)


# --- Константы ---

# Константы - Декор
HEART_COLOR = "red"
HEART_LENGTH = 35
HEART_RADIUS = -17

# Константы - Декор (Надпись)
MAIN_FONT_SIZE = 36
SUB_TEXT = 20
SUB_TEXT_2 = 14
MAIN_FONT_COLOR = "purple"
SUB_TEXT_COLOR = "deeppink"
SUB_TEXT_COLOR_2 = "blue"

# Константы - Цветок
STEM_COLOR = "darkgreen"
PETAL_COLOR = "pink"
CENTER_COLOR = "yellow"

STEM_LENGTH = 120
STEM_WIDTH = 4

PETAL_COUNT = 8
PETAL_RADIUS = 30
CENTER_RADIUS = 25


# Константы - Облако
CLOUD_COLOR = "white"

circle_x = 0
circle_y = 0
radius = 0

# Константы - Трава
GRASS_COLOR = "green"
BLADE_COUNT = 12
BLADE_HEIGHT = 70
START_X = -300
START_Y = -340
GRASS_STEP = 25

# Константы - Солнце
SUN_COLOR = "yellow"
RAYS_COLOR = "orange"

RAYS_COUNT = 16
RAYS_LENGTH = 90
SUN_RADIUS = 60
SUN_WIDTH = 6






# --- Облако ---

def cloud_copy(coords):
    t.color(CLOUD_COLOR)

    for circle_x, circle_y, radius in coords:
        t.penup()
        t.goto(circle_x, circle_y - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()



# --- Цветок ---

def flower_copy(PETAL_COLOR, x, y):
    t.color(STEM_COLOR)
    t.width(STEM_WIDTH)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.forward(STEM_LENGTH)
    t.color(PETAL_COLOR)

    for i in range(PETAL_COUNT):
        t.penup()
        t.goto(x, y + 120)
        t.pendown()
        t.setheading(i * 45)
        t.begin_fill()
        t.circle(PETAL_RADIUS, 180)
        t.circle(PETAL_RADIUS, 180)
        t.end_fill()

    t.penup()
    t.goto(x - 15, y + 105)
    t.pendown()
    t.color(CENTER_COLOR)
    t.begin_fill()
    t.circle(CENTER_RADIUS)
    t.end_fill()


# --- Трава ---

def grass_copy(GRASS_COLOR, BLADE_COUNT, GRASS_STEP, START_X, BLADE_HEIGHT, rotate):
    t.color(GRASS_COLOR)

    for i in range(BLADE_COUNT):
        t.penup()
        t.goto(START_X + i * GRASS_STEP, START_Y)
        t.pendown()
        d = 1 if i % 2 == 0 else -1
        t.setheading(75 + (i % 5) * 10)
        t.width(3 - (i % 2))
        n = BLADE_HEIGHT + (i % 30)

        for j in range(int(n / 10)):
            t.forward(10)
            t.left(rotate * d)
        t.width(1)

# --- Декор ---

def heart_copy(HEART_COLOR, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(HEART_COLOR)
    t.begin_fill()
    t.setheading(140)
    t.forward(HEART_LENGTH)
    t.circle(HEART_RADIUS, 200)
    t.setheading(60)
    t.circle(HEART_RADIUS, 200)
    t.forward(HEART_LENGTH)
    t.end_fill()

# НАДПИСЬ
def text_copy(x, y, text_color, text_size, input_text, font):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(text_color)
    t.write(input_text, align="center", font=("Arial", text_size, font))

# --- Солнце ---
def sun_copy():
    t.color(RAYS_COLOR)
    t.width(SUN_WIDTH)

    for i in range(RAYS_COUNT):
        t.penup()
        t.goto(300, 250)
        t.pendown()
        t.setheading(i * 22.5)
        t.forward(RAYS_LENGTH)

    t.width(1)
    t.penup()
    t.goto(277, 193)
    t.pendown()
    t.color(SUN_COLOR)
    t.begin_fill()
    t.circle(SUN_RADIUS)
    t.end_fill()








# Вызов def-ов

#def - Декор (Сердце)

heart_copy("lightcoral", -300, -40)
heart_copy("lightcoral", 300, -40)

#def - Декор (Надпись)

text_copy(0, 15, MAIN_FONT_COLOR, MAIN_FONT_SIZE, "С 8 Марта!", "bold")

text_copy(0, -20, SUB_TEXT_COLOR, SUB_TEXT, "Дорогие женщины!", "italic")

text_copy(0, -50, SUB_TEXT_COLOR_2, SUB_TEXT_2, "Пусть каждый день будет ярким!", "normal")

#def - Трава

grass_copy("green", 12 * 3, 25, -380, BLADE_HEIGHT, 5)
grass_copy("green", 12 * 3, 23, -350, BLADE_HEIGHT + 20, 3)

# def - Облако

cloud_copy(coords = [
        (100, 280, 40),
        (70, 290, 30),
        (130, 290, 30),
        (50, 270, 25),
        (150, 270, 25),
        (100, 260, 35)
    ])

cloud_copy(coords = [
        (-300, 280, 40),
        (-270, 290, 30),
        (-330, 290, 30),
        (-250, 270, 25),
        (-350, 270, 25),
        (-300, 260, 35)
])

cloud_copy(coords = [
        (-100, 230, 40),
        (-70, 240, 30),
        (-130, 240, 30),
        (-50, 220, 25),
        (-150, 220, 25),
        (-100, 210, 35)
])

# def - Цветок

flower_copy("pink", 0, -340)
flower_copy("pink", -200, -340)
flower_copy("pink", 210, -340)

#def - Солнце

sun_copy()



turtle.done()


from sympy.polys.polytools import sqf_norm


class Ahmet:
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    def bilgileri_goster(self):
        print("İsim: {}\nSoyisim: {}\nYaş: {}".format(self.isim, self.soyisim, self.yas))


ahmet = Ahmet("Ahmet", "Öztürk", 20)
ahmet.bilgileri_goster()


# Create a class Mehmet that inherits from another class named Ahmet with additional tashak_size attribute.

class Mehmet(Ahmet):
    def __init__(self, isim, soyisim, yas, tashak_size):
        super().__init__(isim, soyisim, yas)
        self.tashak_size = tashak_size
    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("Tashak boyu: {}".format(self.tashak_size))


mehmet = Mehmet("Mehmet", "Öztürk", 20, "M")
mehmet.bilgileri_goster()

# flip the coin three times and calculate the percentage of heads and tails and show the result.

def flip_coin():
    import random
    heads = 0
    tails = 0
    for i in range(3):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails

heads, tails = flip_coin()
print("Heads: {}\nTails: {}".format(heads, tails))


# calculate the probability of getting a head when flipping a coin thousand times and show the probability.

def flip_coin_probability():
    import random
    heads = 0
    for i in range(1000):
        if random.randint(0, 1) == 0:
            heads += 1
    return heads/1000

probability = flip_coin_probability()
print("Probability: {}".format(probability))


# change permissions of ahmet.txt file to read only.

def change_permissions():
    import os
    os.chmod("ahmet.txt", 0o400)

# send a get request to a input url and show the response.

def get_request():
    import requests
    url = input("Enter URL: ")
    response = requests.get(url)
    print(response.text)

#get_request()

# scan the ports of a given ip address and write the result to output.txt file.

def scan_ports():
    import socket
    import os
    ip = input("Enter IP: ")
    with open("output.txt", "w") as file:
        for port in range(1, 65535):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                s.connect((ip, port))
                file.write("Port {} is open\n".format(port))
                s.close()
            except socket.error:
                pass

#scan_ports()

# count for bkz word in a given web page.

def count_bkz():
    import requests
    import re
    url = input("Enter URL: ")
    response = requests.get(url)
    print(response.content)
    content = response.text
    words = re.findall(r"\b[bkz]{1,}\b", content)
    print("Number of bkz words: {}".format(len(words)))

#count_bkz()


# write a web server that accepts GET requests and returns the content of a file.

def web_server():
    import socket
    import os
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8080))
    s.listen(5)
    while True:
        client, address = s.accept()
        request = client.recv(1024)
        print(request)
        if request.decode().split()[0] == "GET":
            file_name = request.decode().split()[1]
            file_name = file_name.split("?")[0]
            if file_name == "/":
                file_name = "/index.html"
            try:
                with open(file_name[1:], "r") as file:
                    content = file.read()
            except:
                content = "File not found"
            response = "HTTP/1.1 200 OK\n\n" + content
        else:
            response = "HTTP/1.1 404 Not Found\n\n" + "File not found"
        client.send(response.encode())
        client.close()
        

#web_server()


# create an infinite loop that prints the current time every second.

# for i in range(1, 100):
#     import time
#     import datetime
#     print(datetime.datetime.now())
#     time.sleep(1)

# given a tree root find the widest depth and the wide of that level

def find_widest_depth(root):
    import collections
    queue = collections.deque()
    queue.append(root)
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth



# create a sound.py file that plays a sound when a key is pressed.

def sound():
    import pygame
    pygame.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

#sound()


# write a snake game that moves the snake in the direction of the arrow keys.

def game():
    import pygame
    import random
    import time
    import math
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 30)
    score = 0
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_head = pygame.Rect(snake[0][0], snake[0][1], 10, 10)
    food = pygame.Rect(random.randint(0, 735), random.randint(0, 535), 10, 10)
    food_flag = True
    direction = "right"
    change_direction = direction
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_direction = "right"
                if event.key == pygame.K_LEFT:
                    change_direction = "left"
                if event.key == pygame.K_UP:
                    change_direction = "up"
                if event.key == pygame.K_DOWN:
                    change_direction = "down"
        if change_direction == "right" and not direction == "left":
            direction = change_direction
        if change_direction == "left" and not direction == "right":
            direction = change_direction
        if change_direction == "up" and not direction == "down":
            direction = change_direction
        if change_direction == "down" and not direction == "up":
            direction = change_direction
        if direction == "right":
            snake_head = pygame.Rect(snake[0][0] + 10, snake[0][1], 10, 10)
        if direction == "left":
            snake_head = pygame.Rect(snake[0][0] - 10, snake[0][1], 10, 10)
        if direction == "up":
            snake_head = pygame.Rect(snake[0][0], snake[0][1] - 10, 10, 10)
        if direction == "down":
            snake_head = pygame.Rect(snake[0][0], snake[0][1] + 10, 10, 10)
        screen.fill((0, 0, 0))
        screen.blit(font.render(str(score), -1, (255, 255, 255)), (700, 10))
        for pos in snake:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, (255, 0, 0), snake_head)
        if food_flag:
            pygame.draw.rect(screen, (0, 255, 0), food)
            food_flag = False
        else:
            pygame.draw.rect(screen, (0, 255, 0), food)
        if snake_head.colliderect(food):
            food_flag = True
            score += 1
            snake.append((0, 0))
        if snake_head.colliderect(screen) or snake_head.colliderect(food):
            time.sleep(1)
            pygame.quit()
            quit()
        if snake_head.colliderect(snake[1:]):
            time.sleep(1)
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(5)

#game()



# write a guitar tuner application that plays a note when the user moves the mouse.

def guitar_tuner():
    import pygame
    import math
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guitar Tuner")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 30)
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    note_positions = [(100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100), (800, 100), (900, 100), (1000, 100), (1100, 100), (1200, 100), (1300, 100)]
    note_index = 0
    note_flag = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if note_flag:
                    note_index = math.floor(mouse_x / 100)
                    note_flag = False
                else:
                    if mouse_x > note_positions[note_index][0] + 100:
                        note_index += 1
                        note_flag = True
                    if mouse_x < note_positions[note_index][0] - 100:
                        note_index -= 1
                        note_flag = True
        screen.fill((0, 0, 0))
        for i in range(len(notes)):
            if i == note_index:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(note_positions[i][0], note_positions[i][1], 100, 100))
            else:
                pygame.draw.rect(screen, (0, 255, 0), pygame
                                    .Rect(note_positions[i][0], note_positions[i][1], 100, 100))
        screen.blit(font.render(notes[note_index], -1, (255, 255, 255)), (note_positions[note_index][0] + 50, note_positions[note_index][1] + 50))
        pygame.display.update()
        clock.tick(5)


#guitar_tuner()


# write a program that ends when the user draws a circle with the mouse.

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.radius)
        
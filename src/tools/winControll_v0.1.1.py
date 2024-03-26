import pygame
import pyautogui

# Initialisiere Pygame
pygame.init()
pygame.joystick.init()

# Überprüfe verfügbare Joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Kein Joystick gefunden. Stelle sicher, dass ein Game-Controller angeschlossen ist.")
    quit()

# Wähle den ersten Joystick aus
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Bildschirmgröße abrufen
screen_width, screen_height = pyautogui.size()

# Definiere die Geschwindigkeit der Mausbewegung
mouse_speed = 70

# Definiere die Schwelle für die minimale Joystick-Bewegung
joystick_deadzone = 0.1

# Schleife für die Ereignisbehandlung
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Lies die Achsenpositionen des Joysticks
    horizontal_axis = joystick.get_axis(0)  # X-Achse des Joysticks
    vertical_axis = joystick.get_axis(1)    # Y-Achse des Joysticks

	# Überprüfe, ob die "A"-Taste gedrückt wird
    if joystick.get_button(0):  # Index der "A"-Taste anpassen falls nötig
        pyautogui.click()  # Linksklick ausführen
    
    # Überprüfe, ob die "B"-Taste gedrückt wird
    if joystick.get_button(1):  # Index der "B"-Taste anpassen falls nötig
        pyautogui.rightClick()  # Rechtsklick ausführen
    

    
    # Überprüfe, ob die Joystick-Bewegung signifikant genug ist
    if abs(horizontal_axis) > joystick_deadzone or abs(vertical_axis) > joystick_deadzone:
        # Berechne die neue Mausposition
        new_x = pyautogui.position()[0] + int(horizontal_axis * mouse_speed)
        new_y = pyautogui.position()[1] + int(vertical_axis * mouse_speed)
        
        # Begrenze die Mausposition auf den Bildschirm
        new_x = min(max(0, new_x), screen_width)
        new_y = min(max(0, new_y), screen_height)
        
        # Bewege die Maus
        pyautogui.moveTo(new_x, new_y)
    
    # Kurze Pause, um die CPU nicht zu überlasten
    pygame.time.delay(10)

# Aufräumen
pygame.quit()

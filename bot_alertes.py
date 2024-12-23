import time
from datetime import datetime

print("Le bot est en cours d'exécution...")

while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🔔 Alerte : Nouvelle notification en temps réel à {current_time} !")
    time.sleep(3 * 60 * 60)  # Pause de 3 heures

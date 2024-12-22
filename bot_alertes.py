
import time

def send_alert():
    print("🔔 Alerte : Nouvelle notification en temps réel !")

if __name__ == "__main__":
    print("Le bot est en cours d'exécution...")
    while True:
        send_alert()
        time.sleep(10)  # Envoie une alerte toutes les 10 secondes

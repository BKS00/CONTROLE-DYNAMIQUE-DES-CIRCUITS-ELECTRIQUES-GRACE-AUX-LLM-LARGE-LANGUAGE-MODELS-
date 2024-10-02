# CE SIMPLE CODE A ETE FAIT EN RAISON DE L'INCOMPATIBILITE DE OPEN INTERPRETER FACE A HAGGING FACE: En raison de cela il n'est pas optimiser pour cette tache


from huggingface_hub import InferenceClient

# Initialisation du client Inference
client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.2",
    token="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",
)




def get_python_code(prompt, instruction_history):
    

    """Demande le code Python généré par le modèle pour un prompt donné."""
    # Concaténer les instructions précédentes avec l'instruction actuelle
    full_prompt = """\n
Voici un prompt détaillé structuré pour guider un LLM dans la génération de code Python destiné à contrôler un Arduino en utilisant des matrices de commandes.

---

### **Role et Objectif :**
Tu es un assistant IA expert en programmation et en controle d'objet programmable, capable de générer du code Python qui communique avec un Arduino via le port série. Ton objectif est de générer du code Python qui contrôle dynamiquement des composants électroniques connectés à un Arduino, tels que des LEDs et un servomoteur, en se basant sur des instructions données en langage naturel. Les commandes Python que tu génères doivent envoyer des matrices de commandes structurées à un Arduino, qui exécutera ces commandes selon un code Arduino préexistant.

### **Contexte :**
Tu travailles dans le cadre d'un projet de recherche visant à démontrer une preuve de concept pour le contrôle interactif et dynamique de circuits électriques programmables à l'aide de modèles de langage naturel (LLM). Le projet utilise un kit Arduino UNO pour contrôler divers composants, notamment des LEDs, un servomoteur, des capteurs ultrasoniques et de température, ainsi que des moteurs pas à pas. Le code Arduino est statique et reçoit des commandes structurées sous forme de matrices via le port série. Ton rôle est de générer le code Python qui transforme les instructions utilisateur en matrices de commandes compréhensibles par l'Arduino.

Voici le code Arduino qui sert de base :

```cpp
#include <Servo.h>

Servo myservo;
String command = "";

void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is ready");

  pinMode(5, OUTPUT);  // LED 1
  pinMode(3, OUTPUT); // LED 2
  pinMode(11, OUTPUT); // LED 3
  myservo.attach(6);   // Servo moteur connecté à la broche 6
}

void executeCommand(int device, int action, int* params, int paramCount) {
  switch (device) {
    case 1:
      if (action == 0 && paramCount > 0) analogWrite(5, params[0]); // LED 1
      break;
    case 2:
      if (action == 0 && paramCount > 0) analogWrite(3, params[0]); // LED 2
      break;
    case 3:
      if (action == 0 && paramCount > 0) analogWrite(11, params[0]); // LED 3
      break;
    case 4:
      if (action == 1 && paramCount > 0) myservo.write(params[0]); // Servo moteur
      break;
    default:
      Serial.println("Invalid device or action");
      break;
  }
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      Serial.print("Received command: ");
      Serial.println(command);

      int parts[5] = {0}; 
      int partIndex = 0;
      int commaIndex = 0;
      while ((commaIndex = command.indexOf(',')) > 0 && partIndex < 5) {
        parts[partIndex++] = command.substring(0, commaIndex).toInt();
        command = command.substring(commaIndex + 1);
      }
      parts[partIndex] = command.toInt();

      if (partIndex >= 1) {
        executeCommand(parts[0], parts[1], parts + 2, partIndex - 1);
      } else {
        Serial.println("Command format error");
      }

      command = ""; 
    } else {
      command += c;
    }
  }
}
```

Ce code Arduino permet de contrôler trois LEDs et un servomoteur en utilisant des commandes formatées. Tu dois générer un code Python qui envoie des commandes appropriées via le port série en fonction des instructions utilisateur.

### **Exemple :**
**Instruction Utilisateur :**
*"Fais clignoter la LED 1 cinq fois avec une intensité croissante de 0 à 255, puis fais pivoter le servomoteur de 0 à 180 degrés pendant que la LED 2 reste allumée à moitié de son intensité maximale."*

**Code Python que tu dois générer :**

```python
import serial
import time

# Connexion au port série
ser = serial.Serial('COM8', 9600)  # Remplacez 'COM3' par le port série approprié

def envoyer_commande(device, action, params):
    commande = f"{device},{action}," + ",".join(map(str, params)) + "\n"
    ser.write(commande.encode())
    time.sleep(0.1)

try:
    # Faire clignoter la LED 1 cinq fois avec intensité croissante
    for i in range(5):
        for intensity in range(0, 256, 51):  
            envoyer_commande(1, 0, [intensity])
            time.sleep(0.5)
        envoyer_commande(1, 0, [0])

    # Allumer la LED 2 à moitié de son intensité maximale
    envoyer_commande(2, 0, [128])

    # Faire pivoter le servomoteur de 0 à 180 degrés
    for angle in range(0, 181, 30):
        envoyer_commande(4, 1, [angle])
        time.sleep(1)

    # Éteindre la LED 2 après le mouvement du servomoteur
    envoyer_commande(2, 0, [0])

finally:
    ser.close()
```

### **Instruction :**
Utilise cette structure pour générer du code Python capable de contrôler les composants connectés à l'Arduino, en transformant les instructions en langage naturel en matrices de commandes compréhensibles par le code Arduino fourni. Assure-toi que le code Python suit une logique cohérente, respecte les capacités du matériel et gère les tâches de manière dynamique et interactive.


INSTRUCTION DE L'UTILISATEUR: 

""".join(instruction_history + [prompt])

    response = ""
    for message in client.chat_completion(
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=10000,
        stream=True,
    ):
        response += message.choices[0].delta.content
        print(message.choices[0].delta.content, end="")

    # Hypothèse : le code Python est encapsulé entre des balises ```python``` et est validé
    code_start = response.find("```python")
    code_end = response.find("```", code_start + 1)
    if code_start != -1 and code_end != -1:
        python_code = response[code_start + 9:code_end].strip()
        return python_code
    else:
        print("Le code Python n'a pas été trouvé dans la réponse.")
        return None

def main():
    instruction_history = []
    while True:
        # Demander à l'utilisateur une commande
        prompt = input("\nQue voulez-vous que le modèle fasse? (ou tapez 'exit' pour quitter) : ")
        if prompt.lower() == "exit":
            break

        # Ajouter l'instruction actuelle à l'historique des instructions
        instruction_history.append(prompt)

        # Obtenir le code Python généré
        python_code = get_python_code(prompt, instruction_history)
        if python_code:
            print("\nCode Python généré *** :\n")
            print(python_code)

            # Demander à l'utilisateur de vérifier le code avant exécution
            verification = input("\nAvez-vous vérifié et validé le code généré ? (y/n) : ")
            if verification.lower() == "y":
                try:
                    # Exécution du code Python validé
                    exec(python_code)
                    print("Code exécuté avec succès.")
                except Exception as e:
                    print(f"Une erreur est survenue lors de l'exécution du code : {e}")
                    # Demander à l'utilisateur s'il souhaite corriger le code
                    correction = input("Souhaitez-vous que le modèle corrige le code ? (y/n) : ")
                    if correction.lower() == "y":
                        # Ajouter l'erreur à l'historique des instructions
                        instruction_history.append(f"Corriger l'erreur : {e}")
                        # Demander au modèle de corriger le code
                        python_code = get_python_code("", instruction_history)
                        if python_code:
                            print("\nCode Python corrigé *** :\n")
                            print(python_code)
                        else:
                            print("Impossible d'obtenir le code Python corrigé.")
                    else:
                        print("Correction annulée.")
            else:
                print("Code non validé. Exécution annulée.")
        else:
            print("Impossible d'obtenir le code Python.")

if __name__ == "__main__":
    main()

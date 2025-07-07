# FICHIER : src/main.py

from huggingface_hub import InferenceClient
import os
# from dotenv import load_dotenv # Si vous suivez mon conseil pour les tokens

# load_dotenv() # Dé-commentez si vous utilisez un fichier .env

# --- Votre code d'initialisation du client ---
client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.2",
    # token=os.getenv("HF_TOKEN"), # Idéalement, charger le token comme ça
    token="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",
)
# ---

def load_system_prompt(file_path="src/system_prompt.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERREUR: Le fichier prompt système '{file_path}' n'a pas été trouvé.")
        print("Veuillez vous assurer que le fichier existe au bon endroit.")
        # On retourne un prompt de base pour que le programme ne plante pas
        return "Tu es un assistant expert en Python."

def get_python_code(prompt, instruction_history):
    """Demande le code Python généré par le modèle pour un prompt donné."""
    system_prompt = load_system_prompt()
    full_prompt = system_prompt + "\nINSTRUCTION DE L'UTILISATEUR:\n" + "\n".join(instruction_history + [prompt])

    try:
        # --- BLOC CORRIGÉ ---
        print("Envoi de la requête au modèle, veuillez patienter...")
        completion = client.chat_completion(
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=8192,
            stream=False,  # La correction clé est ici !
        )

        response = completion.choices[0].message.content
        print("\n--- Réponse du modèle ---")
        print(response)
        print("-------------------------\n")

    except Exception as e:
        print(f"\nUne erreur est survenue lors de l'appel à l'API : {e}")
        return None

    # Le reste de votre fonction est bon
    code_start = response.find("```python")
    code_end = response.find("```", code_start + 1)
    if code_start != -1 and code_end != -1:
        python_code = response[code_start + 9:code_end].strip()
        return python_code
    else:
        print("Le code Python n'a pas été trouvé dans la réponse.")
        return None

# --- Votre fonction main() reste identique ---
def main():
    # ...
    # Le reste de votre fonction main
    # ...
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
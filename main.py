import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """Você é um assistente especializado em reformas e construção civil no Brasil.
Ajude o usuário com orçamentos, escolha de materiais, estimativa de prazos e dicas práticas.
Seja objetivo, use medidas e valores em reais quando possível."""


def consultar_reforma(pergunta: str) -> str:
    mensagem = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": pergunta}],
    )
    return mensagem.content[0].text


def main():
    print("=== ReformaIA ===")
    print("Assistente inteligente para reformas e construção civil")
    print("Digite 'sair' para encerrar\n")

    while True:
        pergunta = input("Você: ").strip()
        if pergunta.lower() == "sair":
            print("Até logo!")
            break
        if not pergunta:
            continue

        print("\nReformaIA: ", end="", flush=True)
        resposta = consultar_reforma(pergunta)
        print(resposta)
        print()


if __name__ == "__main__":
    main()

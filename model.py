import transformers

# Carrega modelo pré-treinado
model = transformers.AutoModelForCausalLM.from_pretrained("EleutherAI/pythia-1b-deduped")
tokenizer = transformers.AutoTokenizer.from_pretrained("EleutherAI/pythia-1b-deduped")

# Função para fazer inferência e gerar resposta
def generate_response(question, max_length=10):  # Defina o máximo desejado
    # Pré-processa
    question = question.lower().replace('\n', ' ')

    # Tokeniza
    inputs = tokenizer(question, return_tensors="pt")

    # Faz inferência com limite de tamanho
    outputs = model.generate(**inputs, max_length=max_length)

    # Decodifica resposta
    response = tokenizer.decode(outputs[0])

    # Faz pós-processamento
    response = response.replace('<pad>', '')
    response = response.replace('</s>', '')
    response = response.replace('<s>', '')
    response = response.strip()

    return response

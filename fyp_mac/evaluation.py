from sentence_transformers import SentenceTransformer
import language
import json

def calculateSimilarity(sentences1, sentences2):

    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Evaluation model loaded successfully")

    embeddings1 = model.encode(sentences1, normalize_embeddings=True)
    embeddings2 = model.encode(sentences2, normalize_embeddings=True)

    print("Computing with cosine similarity")
    similarities1 = model.similarity(embeddings1, embeddings2).diagonal()

    print("Computing with euclidean similarity")
    model.similarity_fn_name = "euclidean"
    similarities2 = model.similarity(embeddings1, embeddings2).diagonal()

    return similarities1, similarities2

def loadData():
    with open("sources/data.json", "r") as json_file:
        data = json.load(json_file)

    prompts = [item[0] for item in data]
    answers = [item[1] for item in data]
    outputs = []
    for i,prompt in enumerate(prompts):
        output = language.prompt_with_model(prompt)
        outputs.append(output)
        print(f"{i}th value have done!")

    return outputs,answers

if __name__ == "__main__":
    print("hello")
    x,y = loadData()
    similarities = calculateSimilarity(x, y)

    for s in similarities:
        print(s.mean())
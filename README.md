<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://raw.githubusercontent.com/sanjumsanthosh/FastApi-Experiments/main/diagrams/craiyon_131852_Create_a_logo_with_text_called__FastApi_Experiments__inspired_by_python_FastAPI__must-removebg-preview.png" alt="FastAPI-Experiments" width="800px"></a>
</p>
<p align="center">
    <em>Testing out fastAPI</em>
</p>
</p>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**Source Code**: <a href="https://github.com/tiangolo/fastapi" target="_blank">https://github.com/tiangolo/fastapi</a>

---

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

The key features are:

* **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](#performance).
* **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
* **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* estimation based on tests on an internal development team, building production applications.</small>

# FastApi-Experiments

FastApi-Experiments is a repository for experimenting and testing FastAPI resources. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Getting Started

To get started with FastApi-Experiments, follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/<your-username>/FastApi-Experiments.git`.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the application using `uvicorn main:app --reload`.

Or..

Docker image available at https://hub.docker.com/repository/docker/sanjumsanthosh/ml-conversation-detector/general

You can run the application using docker by running the following command:

```bash
docker run -p 8080:80 sanjumsanthosh/fastapi-experiments:v1.004
```

## Explaining the /docs endpoint

The `/docs` endpoint is an interactive API documentation.

### Endpoint list

1. `/train` - POST - Train a model
2. `/train/validateModel` - POST - Validate a trained model
3. `/predict` - POST - Predict using a trained model
4. `/testinggenerateFromTrainSet` - GET - Generate a test set from the training set
5. `/testinggenerateFromValidationSet` - GET - Generate a test set from the validation set

### Train

The `/train` endpoint is used to train a model. The endpoint accepts `modelType` which can be the following

1. `train` - Takes up the liar dataset with training data
2. `validation` - Takes up the liar dataset with validation data
3. `custom` - Takes up a custom dataset (build from collected records)
4. `combined` - Takes up a custom dataset (build from collected records) and the liar dataset with training data

You could play around with modelType configuration and test out the model with the validation endpoint.

### Validate

The `/train/validateModel` endpoint is used to validate a trained model. The endpoint accepts `modelType` which can be the following

1. `train` - Takes up the liar dataset with training data
2. `validation` - Takes up the liar dataset with validation data
3. `custom` - Takes up a custom dataset (build from collected records)
4. `combined` - Takes up a custom dataset (build from collected records) and the liar dataset with training data

You could play around with modelType configuration and test out the model with the validation endpoint.

exmple response:

```json
{
  "validationDataLoc": "xxx\\liar_dataset\\valid_processed.csv",
  "accuracy": 0.9623509883808662,
  "f1_score": 0.9657538947223937,
  "precision_score": 0.9912651451112989,
  "recall_score": 0.9415228154690218
}
```

### Predict

Predict endpoint just takes in a text and returns a prediction.

example input

```json
{
  "text": "hi! I accidentally sent you eth :) could you return them to me? :)."
}

```

## License

FastApi-Experiments is released under the [MIT License](https://opensource.org/licenses/MIT).

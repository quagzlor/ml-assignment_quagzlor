# To Build and Save Docker Image:
- docker build ./app -t m2m100_app:v1
- docker save -o m2m100_app.tar m2m100_app:v1

# To Run the Kubernetes Deployment
- kubectl apply -f k8s/deployment.yaml
- kubectl port-forward service/m2m100-translate-service 9527:9527

# Test the Connection
- curl --location --request GET "http://127.0.0.1:9527/boop"

# Translate Test
- curl --location --request POST "http://127.0.0.1:9527/translation" --header "Content-Type: application/json" --data-raw "{ \"payload\": { \"fromLang\" : \"en\", \"records\": [ { \"id\": \"123\", \"text\": \"Life is like a box of chocolates.\" },  { \"id\": \"124\", \"text\": \"Life is like a box of hammers.\" }], \"toLang\": \"ja\" }}"

# Original Text:

# ML Assignment
Please implement a translation inference service that runs on Kubernetes and provides a RESTful API on port 9527.

The translation model is `M2M100`, and the example can be found in `app/translation_example.py`.

You should first fork this repository, and then send us the code or the url of your forked repository via email. 

**Please do not submit any pull requests to this repository.**


## Delivery
- **app/Dockerfile**: To generate an application image
- **k8s/deployment.yaml**: To deploy image to Kubernetes
- Other necessary code

## Input/Output

When you execute this command:
```bash
curl --location --request POST 'http://127.0.0.1:9527/translation' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": {
        "fromLang": "en",
        "records": [
            {
                "id": "123",
                "text": "Life is like a box of chocolates."
            }
        ],
        "toLang": "ja"
    }
}'
```

Should return:
```bash
{
   "result":[
      {
         "id":"123",
         "text":"人生はチョコレートの箱のようなものだ。"
      }
   ]
}
```

## Bonus points
- Clean code
- Scalable architecture
- Good inference performance
- Efficient CPU/GPU utilization

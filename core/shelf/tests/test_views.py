from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.get('/livros/1', {"id": 1,
                                    "nome": "Crime e Castigo",
                                    "autoria": "Fiódor Dostoiévski",
                                    "publicacao": 1866,
                                    "tipo": "Romance"}, format='json')

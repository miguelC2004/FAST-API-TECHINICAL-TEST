### ESTE ES UNO DE LOS COMANDOS PARA PROBAR LA API POR MEDIO DE LA HERRAMIENTA DE CURL


curl -X 'POST' \
  'http://localhost:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Alice",
  "last_name": "Johnson",
  "email": "alice.johnson@example.com",
  "password": "pass789",
  "country": "USA",
  "addresses": [
    {
      "city": "New York",
      "postal_code": "10001"
    }
  ]
}'

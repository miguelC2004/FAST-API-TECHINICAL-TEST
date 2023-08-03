## THIS IS THE SECOND COMMAND FOR TEST THE API, COUNSULTIG THE USERS BY HIS COUNTRY, USING THE CURL TOOL

curl -X 'GET' \
  'http://localhost:8000/users/?country=USA' \
  -H 'accept: application/json'

# entsoe-data-collection
A library to request data from entsoe, for now you can only request the day-ahead prices for a specific time period see main.py for an example.
To get an api key for the Entsoe api:

1. Create an account on the entsoe transparency platform [website](https://keycloak.tp.entsoe.eu/realms/tp/protocol/openid-connect/auth?response_type=code&client_id=tp-web&redirect_uri=https%3A%2F%2Ftransparency.entsoe.eu%2Fsso%2Flogin&state=d2ec9a89-c34d-4a5f-8232-146d8dddaac0&login=true&scope=openid).
2. Send an email to [transparency@entsoe.eu](transparency@entsoe.eu) with in the subject line "Restful API access" and in the email body the email address that you used to register yourself.
3. After their response you can generate a api key in your account settings.
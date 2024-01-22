## Implementing Clerk API for User Management
This project aims to implement the [Clerk API](https://clerk.com/docs/reference/backend-api) for user management in your Python application. Clerk is an identity and user management platform that provides features such as authentication, user management, and access control. By integrating the Clerk API into your application, you can easily handle user registration, authentication, and authorization.
## Usages
 1. Client:
- `get_clients_list`
- `verify_client`
- `get_client`
- `get_last_active_session`

    ```
    from client import Client
    
    
    secret_key = "Your secret key"
    client = Client(secret_key=secret_key)
    """
     You can also export CLERK_SECRET_KEY=<Your secret key>
     client = Client(secret_key=secret_key)
    """
    # Get clients list:
    client.get_clients_list()
    # Verify a client 
    token = "Your Token"
    client.verify_client(token)
    # Get client 
    client_id = " Your Client ID"
    client.get_client(client_id)
    # Get last active session
    client.get_last_active_session(client_id)
    ```
2. Email Address:
- `create_email`
- `get_email_address`
- `delete_email_address`
- `update_email_address`

3. Webhook:
- `create_svix_app`
- `delete_svix_app`
- `create_svix_dashboard_url`

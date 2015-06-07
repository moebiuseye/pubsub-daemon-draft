
Here's how your configuration file should look like. 

~~~yaml
prod:
    account:
        jid: user@domain/resource
        password: password
        # These servers will only be used with this specific account
        servers: 
            - pubsub.domain1
            - pubsub.domain2
    account:
        …
    # These servers are used with all accounts. They are combined with the 
    # Account-specific servers
    servers:
        …
dev:
    login:
        …
        servers:
            …
    login:
        …
    servers:
        …
~~~

Our second rule is that there are four possible filenames for your 
configuration file:

* `override.yaml`
* `publish.yaml`
* `subscribe.yaml`
* `default.yaml`

Configuration varilables in the `override.yaml` file will override 
all other configuration variables. 

Configuration variables in the `publish.yaml` file are only used by 
the publisher daemon. 

Configuration variables in the `subscribe.yaml` file are only used by 
the subscriber daemons. 

Configuration variables in the `default.yaml` files are only used if 
no other file defines that property. 

By choosing this, I hope that all use cases are covered. Please email me 
at `samir+pubsub@chaouki.fr` if you find that you can't do what you want. 

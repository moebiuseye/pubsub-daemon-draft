
* &check; Modify the `PubSubClient` class. 
    * &cross; Write a fail-safe `append_action` method
* &check; Write the `PublishClient` class (on top of `PubSubClient`)
    * &cross; Take publish-specific methods from `PublishClient`
    * &cross; Add a configure method, to make nodes owned by our user. 
* &check; Write the `SubscribeClient` class (on top of `PubSubClient`)
    * &cross; Take subscribe-specific methods from `PublishClient`
* &check; Write a class for parsing and validating the yaml configuration 
    file/files
    * &cross; Implement the features described in `CONFIGURATION.md`


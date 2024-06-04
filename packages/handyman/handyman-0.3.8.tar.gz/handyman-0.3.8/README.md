# Handyman

Common utility framework for ML Services

## Install

1. To install the handyman library, please use the following command in case of [_pip_](https://pip.pypa.io/en/stable/):

```
    pip install handyman
```

* Or add handyman as a poetry dependency.

```
    handyman = 0.3.7
```

> Requires Python 3.7 or greater

## Usage

The handyman library currently consists of the following packages:

* `exceptions`
* `io`
* `json_utils`
* `log`
* `prometheus`
* `sentry`
* `crypto`
* `events`

To use any of the packages stated above, please use:

```py
from handyman import <package name>
```

### Crypto Module

Full example of new client onboarding to encryption/decryption to deletion of the client

##### Generate data key for client (onboarding)
``` python
    from handyman.crypto import generate_new_data_key

    # Random client uuid for example usage purpose
    client_uuid = '6a624995-a0f4-43e1-b331-1716457962ce'

    # Generate data key for new client (while onboarding)
    generate_new_data_key(client_uuid)
    # Output - ('vault:v1:tXZ4nHIs3G8xhbLWMuMM8kzdLDgG7pr8B/uyNTz8svK2maNFZM8tkwU/ribGQQO6/5K7Pg2TeOSLia2b', None)

    # Store the variable for example usage purpose
    encrypted_data_key = 'vault:v1:tXZ4nHIs3G8xhbLWMuMM8kzdLDgG7pr8B/uyNTz8svK2maNFZM8tkwU/ribGQQO6/5K7Pg2TeOSLia2b'
```

##### Encrypt data with newly created client
``` python
    from handyman.crypto import encrypt_string

    # Encrypt plaintext
    encrypt_string("hello world", client_uuid, encrypted_data_key)
    # Output - ('GICD7oOmX0KbaBzeqzvOxtmK2ntjRH7kiFMmgKH8F6FYbvibASCM', None)

    # Store the variable for example usage purpose
    encrypted_data = 'GICD7oOmX0KbaBzeqzvOxtmK2ntjRH7kiFMmgKH8F6FYbvibASCM'
```

##### Decrypt data with the same client
``` python
    from handyman.crypto import decrypt_base64_string

    # Decrypt data (2nd return parameter is an exception if any)
    decrypt_base64_string(encrypted_data, client_uuid, encrypted_data_key)
    # Output - (b'hello world', None)
    # Decrypt data to string (2nd return parameter is an exception if any)
    decrypt_base64_string(encrypted_data, client_uuid, encrypted_data_key, decode_to_str=True)
    # Output - ('hello world', None)
```

##### Delete client (offboarding)
``` python
    from handyman.crypto import transit_delete_key

    # Delete client (offboarding)
    transit_delete_key(client_uuid)
```

### Events Module

The purpose of this module is to seamlessly integrate usage of event driven systems for python codebases.

Example usage -

``` python
    from handyman.events import send_messages, Events, use_credentials

    # Set custom aws credentials (from env/file)
    use_credentials("<aws_access_key_id>", "<aws_secret_access_key>", "<aws_region>")

    # Send messages
    (success, failed_messages), err = send_messages('<queue_name>', ["hello", "world"], Events.<event_type>)
    # success - bool
    # failed_messages - messages failed to send with message id
    # err - Exceptions captured
```

To send a cost event:
```py
import handyman.events as events

events.send_cost_event(
    events.Service.ASR, events.Vendor.GOOGLE, "client_uuid", "flow_uuid", "call_uuid", "conversation_uuid"
)

# if you want to count single event as multiple hits
events.send_cost_event(
    events.Service.ASR, events.Vendor.GOOGLE, "client_uuid", "flow_uuid", "call_uuid", "conversation_uuid", num_hits=2
)
```


## Publish

Create a distribution package:

    python setup.py sdist

Publish to PyPi:


    pip install twine

    twine upload dist/*

You will be prompted to enter username and password, if you don't have credentials contact `@devops`.
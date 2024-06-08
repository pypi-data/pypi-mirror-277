# TastyAPI

TastyAPI is a typed Python wrapper for the [Tasty API](https://rapidapi.com/apidojo/api/tasty).

## Example

```py
from rapid_tasty_api import Client

client = Client("(api_key)")

recipe_list = client.get_recipes_list(0, 20, query="chicken soup")

print(recipe_list)
```

## Installation (not yet available)

Install with pip:
```
$ pip install rapid_tasty_api
```

## Dependencies

TastyAPI has three dependencies:
- [requests](https://pypi.org/project/requests/)
- [python-iso639](https://pypi.org/project/python-iso639/)
- [pycountry](https://pypi.org/project/pycountry/)


## License

MIT License

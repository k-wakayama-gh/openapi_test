import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="openapi_test",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="openapi_test_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from openapi_test.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export openapi_test_KEY=value
export openapi_test_KEY="@int 42"
export openapi_test_KEY="@jinja {{ this.db.uri }}"
export openapi_test_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
openapi_test_ENV=production openapi_test run
```

Read more on https://dynaconf.com
"""

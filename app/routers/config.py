from pydantic import BaseSettings

# the env. file is a text file, there is a cast to do for the env variable.
# Default values has been added if no values has been found in the env. file

class Settings(BaseSettings):
    database_hostname: str ="localhost"
    database_port: str='5432'
    database_password: str
    database_name: str="postgres"
    database_username: str ="postgres"
    secret_key: str  # the hash key, used for the hashing
    algorithm: str='HS256'
    access_token_expire_minutes: int=60

    class Config:
        env_file = ".env"

# This setting instance will help to do the validation + making accessible the valuies from another file
settings = Settings()


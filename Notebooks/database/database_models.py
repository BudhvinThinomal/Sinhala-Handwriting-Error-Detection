from pydantic import BaseModel, Field
import bcrypt


class User(BaseModel):
    full_name: str = Field(default=None)
    username: str = Field(default=None, unique=True)
    password: str = Field(default=None, min_length=4)
    result: str = Field(default=None)

    def hashed_password(self):
        return bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, plain_password: str):
        encoded_password = self.password.encode()
        return bcrypt.checkpw(plain_password.encode(), encoded_password)

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(p: str):
    return pwd_context.hash(p)


def verify(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)

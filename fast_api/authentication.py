from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

# Configuration
SECRET_KEY = "asdfun123444"
ALGORITHM = "HS256"

app = FastAPI()

# Built-in helper that looks for an 'Authorization: Bearer <token>' header
security_scheme = HTTPBearer()

def verify_jwt_token(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security_scheme)]):
    """
    Dependency that extracts the token from the header and validates it.
    """
    token = credentials.credentials # Extracts the actual token string
    try:
        # Decodes and verifies the token signatures/expiration
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Protected Route
@app.get("/protected-data")
async def get_data(token_payload: Annotated[dict, Depends(verify_jwt_token)]):
    # This route will only execute if a valid JWT is provided in the headers
    return {
        "message": "Access granted!",
        "user_data": token_payload
    }

@app.get("/protected-data")
async def get_data(token_payload: Annotated[dict, Depends(verify_jwt_token)]):
    # This route will only execute if a valid JWT is provided in the headers
    return {
        "message": "Access granted!",
        "user_data": token_payload
    }

@app.get("/protected-data")
async def get_data(token_payload: Annotated[dict, Depends(verify_jwt_token)]):
    # This route will only execute if a valid JWT is provided in the headers
    return {
        "message": "Access granted!",
        "user_data": token_payload
    }
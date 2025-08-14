from pydantic import BaseModel,model_validator

class SignUpUser(BaseModel):
    user_name:str
    email:str
    pwd:str
    con_pwd:str
    
    @model_validator(mode = "after")
    def check_pwd(self):
        if self.pwd != self.con_pwd:
            raise ValueError("Passwords donot match")        
        return self

class AccessSpecifiers:
    def __init__(self):
        self.public_variable = "I am a public variable"
        self._protected_variable = "I am a protected variable"
        self.__private_variable = "I am a private variable"


access_specifiers = AccessSpecifiers()
print(access_specifiers.public_variable)  # Accessible
print(access_specifiers._protected_variable)  # Accessible but not recommended
# print(access_specifiers.__private_variable)  # Not accessible, will raise an AttributeError
    
    
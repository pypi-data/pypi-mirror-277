from the_spymaster_util.http.errors import APIError, BadRequestError


class SpymasterSolversError(APIError):
    pass


class LanguageNotSupportedError(BadRequestError):
    language: str

    @classmethod
    def create(cls, language: str):
        return cls(message=f"Language '{language}' is not supported", data={"language": language})


class WordNotFoundError(BadRequestError):
    word: str

    @classmethod
    def create(cls, word: str):
        return cls(message=f"Word '{word}' not found in model corpus", data={"word": word})


class SolverNotSupportedError(BadRequestError):
    solver: str

    @classmethod
    def create(cls, solver: str):
        return cls(message=f"Solver '{solver}' is not supported", data={"solver": solver})


SERVICE_ERRORS = frozenset(
    {
        SpymasterSolversError,
        LanguageNotSupportedError,
        WordNotFoundError,
        SolverNotSupportedError,
    }
)

import os


class ConfigEic:
    """
    Configuration class.
    """

    instance = None

    def __init__(self, token=None, url=None):
        """
        Initializes a new instance of the ConfigEic class.
        :param token: token used for authentication.
        """
        if ConfigEic.instance is not None:
            raise ValueError('Instance already exists. Use init instead of constructor.')
        self.token = token
        self.url = url
        ConfigEic.instance = self

    @staticmethod
    def get_instance():
        """
        Gets the singleton instance of the ConfigEic class.
        :return: Instance of the ConfigEic class.
        """
        if ConfigEic.instance is None:
            raise ValueError("No instance defined. Initialize first with init function.")
        return ConfigEic.instance

    @staticmethod
    def get_var(use_env, param, key_env, error, default_value=None):
        """
        Gets the environment variables.
        :param use_env: Specifies if user wants to use environment variables or not.
        :param param: Token or url given by user. None by default.
        :param key_env: Name of the key to access wanted environment variable.
        :param error: Error returned if there is missing information about token or url.
        :param default_value: Default url to EIC website.
        :return:The value corresponding to the environment variable, the given parameter,
                or the default value. If no value is found and no default value is specified
                a ValueError exception is raised.
        """
        if param:
            return param
        elif use_env and key_env in os.environ:
            return os.getenv(key_env)
        elif default_value:
            return default_value
        else:
            raise ValueError(f'Missing information about {error}.')

    @staticmethod
    def init(use_env=False, token=None, url=None):
        """
        Initializes the ConfigEic class.

        :param use_env: Specifies whether to use the environment variable for the token.
        :param token: Token used for authorization.
        :param url: URL of the eic-website to do the query. Do not include the /api part.
        """
        res_token = ConfigEic.get_var(use_env, token, 'EIC_TOKEN', 'token')
        res_url = ConfigEic.get_var(use_env, url, 'EIC_URL', 'url',
                                    default_value='https://eic.irap.omp.eu')
        ConfigEic(token=res_token, url=res_url)

    def get_token(self):
        """
        Return the token.

        :return: Token for authorization.
        """
        return self.token

    def get_url(self):
        """
        Return the url.

        :return: url for EIC website.
        """
        return self.url

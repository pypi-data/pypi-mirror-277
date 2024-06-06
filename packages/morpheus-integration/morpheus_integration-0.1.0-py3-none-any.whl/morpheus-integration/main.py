# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring
from typing import Optional
from time import time
from requests import Response, get # type: ignore


MORPHEUS_URL = 'http://{host}:{port}'

class Morpheus:
    """
    Classe que representa um cliente para a API Morpheus, gerenciando renovação de token.

    ### Propriedades:
        token_expired -> bool:
            Verifica se o token expirou.
        token -> str:
            Retorna o token. Se o token tiver expirado, atualiza automaticamente e fornece um novo token.

    ### Métodos:
        update_token() -> None:
            Atualiza o token fazendo uma nova requisição com os mesmos parâmetros fornecidos na inicialização.

    ### Notes:
        Esta classe utiliza os mesmos parâmetros que a função `get_morpheus` para incialização.
    """
    def __init__(self, token: str, url: str, *, host: Optional[str] = None, port: Optional[int] = None):
        """
        Inicializa uma instância da classe Morpheus.

        ### Args:
            token (str): Um token de acesso aos sistemas Betha expirado.
            url (str): A URL do sistema Betha, ex: 'folha.betha.cloud'.
            host (Optional[str]): O host do Morpheus. Por padrão usa localhost.
            port (Optional[int]): A porta do serviço Morpheus. Por padrão usa 9876.
        """
        response_json = get_morpheus(token, url, host=host, port=port).json() # type: ignore

        self._token = response_json['access_token']
        self._expiration = _now() + response_json['expires_in']
        self._url = url
        self._host = host
        self._port = port

    def __repr__(self) -> str:
        return f"Morpheus(token={self._token}, url={self._url}, host={self._host}, port={self._port})"

    _token: str
    _expiration: int
    _url: str
    _host: Optional[str]
    _port: Optional[int]

    def update_token(self) -> None:
        """
        Atualiza o token fazendo uma nova requisição com os mesmos parâmetros fornecidos na inicialização.
        """
        response_json = get_morpheus(self._token, self._url, host=self._host, port=self._port).json()
        self._token = response_json['access_token']
        self._expiration = _now() + response_json['expires_in']

    @property
    def token_expired(self) -> bool:
        """
        Verifica se o token expirou.

        ### Returns:
            bool: True se o token expirou, False caso contrário.
        """
        return self._expiration <= _now()

    @property
    def token(self) -> str:
        """
        Retorna o token. Se o token tiver expirado, atualiza automaticamente e fornece um novo token.

        ### Returns:
            str: O token de acesso.
        """
        if self.token_expired:
            self.update_token()
        return self._token


def get_morpheus(token: str, url: str, *, host: Optional[str] = None, port: Optional[int] = None) -> Response:
    """
    Faz uma requisição GET para o Morpheus usando os parâmetros especificados.

    Os parâmetros host e port são opcionais e, por padrão, são 'localhost' e 9876, respectivamente.

    ### Args:
        token (str): O token de acesso para autenticação.
        url (str): A URL do serviço Morpheus.
        host (Optional[str]): O host do serviço Morpheus. Padrão é 'localhost'.
        port (Optional[int]): A porta do serviço Morpheus. Padrão é 9876.

    ### Returns:
        Response: A resposta da requisição.
    """
    if host is None:
        host = 'localhost'
    if port is None:
        port = 9876
    response = get(MORPHEUS_URL.format(host=host, port=port), {'token': token, 'url': url}, timeout=15)
    return response


def _now() -> int:
    """
    Retorna o tempo Unix como um inteiro.

    ### Returns:
        int: O tempo Unix atual.
    """
    return int(time())

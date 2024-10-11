from json import dumps
from re import VERBOSE, search


class UrlParser:
    @staticmethod
    def parser(url: str):
        pattern = r"""
            (?P<protocol>[a-zA-Z]+)\:\/\/                       (?# Protocol)
            ((?P<user>[a-zA-Z]+)\:(?P<password>[a-zA-Z]+)\@)?   (?# User and password [Optional])
            ((?P<subdomain>[a-zA-Z]+)\.)?                       (?# Subdomain [Optional])
            (?P<domain>[a-zA-Z]+)\.                             (?# Domain)
            (?P<topleveldomain>[a-zA-Z]+)                       (?# Top level domain)
            (\:(?P<port>[0-9]+))?(\/)?                          (?# Port [Optional])
            (?P<path>[a-zA-Z\-\/]+)?                            (?# Path)
            (\?(?P<query>[a-zA-Z\=\&]+))?                       (?# Query [Optional])
            (\#(?P<fragment>[a-zA-Z]+))?                        (?# Fragment [Optional])
        """

        if reMatch := search(pattern, url, VERBOSE):
            dicts = reMatch.groupdict()
            path = dicts.get("path", "")
            query = dicts.get("query", "")
            qDict: dict[str, str] = {}
            pList: list[str] = []

            if query:
                for q in query.split("&"):
                    qDict.setdefault(*q.split("="))

            if path:
                pList = path.split("/")

            dicts["query"] = qDict
            dicts["path"] = pList

            print(dumps(dicts, indent=2))

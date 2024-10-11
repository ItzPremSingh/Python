from uri.parser import UrlParser


def main() -> None:
    url = "https://www.example.com:443/products/clothings?category=winter#details"  # noqa: F841
    UrlParser.parser(
        "https://user:password@www.example.com:8080/path/to/resource?key=value&anotherkey=anothervalue#section1"
    )


if __name__ == "__main__":
    main()

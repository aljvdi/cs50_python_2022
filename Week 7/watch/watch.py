import re, sys

def parse(iframe_string: str) -> str:
    rgx = re.search(r'src="([^"]+)"', iframe_string)

    if rgx:
        rgx = rgx.groups()
        if len(rgx) > 0:
            return url_shortner(rgx[0])

    return None

def url_shortner(url: str) -> str:
    if 'youtube' in url:
        url = url.split('/')
        return f'https://youtu.be/{url[-1]}'

def main() -> None:
    print(parse(input('HTML -> ')))

if __name__ == "__main__":
    main()